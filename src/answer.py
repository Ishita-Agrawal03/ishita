"""
The core of the system: given a question, retrieve passages, then ask the
LLM to classify the question into exactly one of three states and answer
accordingly, grounded ONLY in the retrieved passages.

=========================================================================
THE ONE CONFIG VALUE THIS PROJECT IS ABOUT: RETRIEVAL_DISTANCE_CEILING
=========================================================================
Before even calling the LLM, we check the best (lowest) distance among the
retrieved chunks. If nothing retrieved is even topically close to the
question, we skip the LLM call entirely and return NOT_FOUND directly --
there is no point asking a model to "be careful" about a question that
isn't in the corpus's neighborhood at all (e.g. "What's the capital of
France?").

If this ceiling is set too LOW (strict): borderline-but-real questions get
killed before the LLM even sees them, and you fail easy questions that are
genuinely answerable but phrased unusually.

If set too HIGH (loose): every question reaches the LLM, including ones
with zero relevant passages, and you are relying entirely on prompt
discipline to avoid hallucinated answers -- which works most of the time,
but not all of the time.

We deliberately set this ceiling generously (see RETRIEVAL_DISTANCE_CEILING
below) so it only filters genuinely off-topic questions, and push almost
all of the "is this actually covered or just adjacent" judgment onto the
LLM with a strict grounding prompt instead of a numeric threshold. That
LLM-level strictness (not the distance ceiling) is the real lever that
determines whether the system over-answers or over-refuses; the ceiling is
just a cheap first pass. We tuned both together against our 25 hard
questions -- see eval/results.md for what happened at different settings.
=========================================================================
"""
import os
import json
import re
import time
import ollama

from retrieve import retrieve

OLLAMA_MODEL = "qwen3:4b"
TOP_K = 12
RETRIEVAL_DISTANCE_CEILING = 1.75  # see module docstring. Chroma default = squared L2 on normalized embeddings, so max meaningful distance is ~2.0 (opposite vectors). 1.75 only screens out near-total unrelatedness.


SYSTEM_PROMPT = """You are a rulebook assistant for a university. You answer ONLY from the passages given to you below -- never from general knowledge about how universities "usually" work, and never by filling gaps with reasonable-sounding assumptions.

You must classify every question into exactly one of three states:

1. "ANSWERED" -- one or more passages directly and unambiguously answer the question, and all relevant passages agree with each other.

2. "NOT_FOUND" -- the passages do not directly address the specific question asked. This is the correct state even when the passages cover an ADJACENT or SIMILAR situation but not the one actually asked about. For example: if the question asks about missing an exam due to a family wedding, and the passages only grant relief for medical reasons, that is NOT_FOUND -- do not extend a medical-only provision to a non-medical scenario, even if it seems like it "should" apply. Being asked about something plausible-sounding is not the same as it being covered. When in doubt about whether a passage truly covers the scenario as opposed to something merely similar, prefer NOT_FOUND.

3. "CONTRADICTION" -- two or more retrieved passages address the SAME question but give answers that cannot both be true (different numbers, different rules, incompatible procedures). Report both sides.

Rules for ANSWERED:
- Only use ANSWERED if you would be comfortable being quoted on it to a student who will act on your answer.
- You may combine multiple consistent passages into one answer.
- You may NOT extend a rule to a situation it does not literally cover, no matter how similar.

Rules for CONTRADICTION:
- Only use CONTRADICTION when the SAME question genuinely gets two incompatible answers from the corpus, not just two passages that are merely related.
- Do not manufacture a contradiction between a general rule and a narrower exception to it -- that is normal legal structure, not a contradiction. A real contradiction is when two passages claim to state the SAME threshold/number/rule and disagree.
- A contradiction can be subtle: one passage may state a number or rule directly, while a second passage explicitly claims to be quoting or referencing the first passage's number but states a DIFFERENT one (e.g. Passage A says "75%"; Passage B says "the 80% requirement specified in Section X" where Section X is actually Passage A). This is still a contradiction even though the two passages don't look symmetric -- one is a plain statement, the other is a misquote of it. Do not resolve it by assuming the plain statement is "obviously" correct; report both.
- If one retrieved passage is a meta/administrative note that says something like "two different figures exist for this, staff should use the current circular's number and flag the discrepancy" -- that note is CONFIRMING a contradiction exists, not resolving it. Do not treat such a note as authorizing you to pick one number as the answer. If the underlying conflicting values are visible anywhere in the retrieved passages (directly stated or referenced by the meta-note), classify as CONTRADICTION and report both underlying values, not the meta-note's procedural advice.
- If you strongly suspect a contradiction exists (e.g. a meta-note references two calculation methods) but the retrieved passages only contain ONE of the two actual conflicting values spelled out, still classify as CONTRADICTION if the meta-note itself names or clearly implies what the second value/method is, and cite both the meta-note and the passage with the value you do have.

Rules for NOT_FOUND:
- Do not refuse just because the answer requires connecting two consistent passages together -- that is still ANSWERED.
- Do not refuse just because the passage doesn't use the exact words in the question -- if the substance is clearly covered, that is ANSWERED.
- DO refuse (NOT_FOUND) if the question describes a scenario, exception, or circumstance the passages simply never mention, even if a similar-sounding scenario is covered.
- Do NOT silently carry a rule from one section into a neighboring section that never restates or explicitly extends it, even if it seems like it "probably" should apply. Two examples of this exact mistake to avoid:
  - A passage states a mechanism applies "in full" to a later context (e.g. "Summer Term attendance follows Section 3 in full"), but a DIFFERENT, separate mechanism (e.g. a medical-adjustment provision that modifies how Section 3 is computed) is never explicitly said to carry over too. Whether "follows Section 3 in full" also drags in an adjustment mechanism attached to Section 3 elsewhere is not stated -- that gap is NOT_FOUND, not an inference you should complete.
  - A passage states an eligibility rule for one category of role (e.g. "two completed semesters" for Council-wide offices), and a separate passage describes a related-but-distinct role (e.g. Class Representative) without repeating, cross-referencing, or excluding that rule. Do not assume the first rule silently applies to the second just because the roles are similar -- that is filling a gap, not reading a passage. This is NOT_FOUND.
  - When a specific provision (like an installment payment plan) modifies one variable (fee amounts/timing) but a related process (like provisional cancellation timelines) is described elsewhere for the general case, do not assume the general process transfers unchanged to the modified case unless a passage says so explicitly. This is NOT_FOUND.

You must respond with ONLY valid JSON (no markdown fences, no preamble, no commentary outside the JSON) matching exactly this schema:

{
  "state": "ANSWERED" | "NOT_FOUND" | "CONTRADICTION",
  "answer": "<a direct, plain-language answer for a student. For NOT_FOUND, explain what IS covered nearby if anything, and clearly say the specific scenario asked about is not addressed. For CONTRADICTION, state both conflicting answers plainly.>",
  "citations": [
    {"chunk_id": "<id>", "source_file": "<file>", "section": "<section>"}
  ],
  "reasoning": "<one or two sentences on why you chose this state, for audit purposes>"
}

For NOT_FOUND, "citations" may be an empty list, or may include passages you checked and ruled out as not actually covering the scenario (useful for showing your work).
For CONTRADICTION, "citations" must include the chunk_id/source_file/section for BOTH conflicting passages.
Never invent a chunk_id, source_file, or section that was not given to you below.
"""


def _build_user_prompt(question, chunks):
    passages_text = "\n\n".join(
        f"[chunk_id: {c['id']} | source_file: {c['source_file']} | section: {c['section']}]\n{c['text']}"
        for c in chunks
    )
    return f"""QUESTION: {question}

RETRIEVED PASSAGES:

{passages_text}

Respond with the JSON object only."""


def _extract_json(raw_text):
    """Strip <think>...</think> blocks (qwen3 is a 'thinking' model and may leak
    these even with think=False on some Ollama versions), then strip markdown
    fences if present, then parse."""
    text = raw_text.strip()
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


def answer_question(question, k=TOP_K, verbose=False):
    chunks = retrieve(question, k=k)

    if not chunks or min(c["distance"] for c in chunks) > RETRIEVAL_DISTANCE_CEILING:
        return {
            "state": "NOT_FOUND",
            "answer": "The rulebook does not contain any passages related to this question.",
            "citations": [],
            "reasoning": f"Best retrieval distance exceeded ceiling ({RETRIEVAL_DISTANCE_CEILING}); no LLM call made.",
            "_retrieved_chunks": chunks,
        }

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": _build_user_prompt(question, chunks)},
    ]

    raw = None
    last_err = None
    for attempt in range(3):
        try:
            response = ollama.chat(
                model=OLLAMA_MODEL,
                messages=messages,
                format="json",
                options={"temperature": 0, "num_predict": 1536},
                think=False,  # qwen3:4b is a thinking model -- turn off <think> blocks, they break JSON parsing
            )
            raw = response["message"]["content"]
            break
        except Exception as e:
            last_err = e
            # local model / connection hiccup (e.g. Ollama still loading the model) -- short retry
            if attempt < 2:
                print(f"  [ollama call failed ({e}), retrying in 3s...]")
                time.sleep(3)
                continue
            else:
                raise

    if raw is None:
        raise last_err

    if verbose:
        print("--- RAW MODEL OUTPUT ---")
        print(raw)
        print("------------------------")

    try:
        parsed = _extract_json(raw)
    except Exception as e:
        # Second chance: ask the model to just re-emit the same content as
        # strictly valid JSON -- catches cases where a stray unescaped quote
        # or leftover <think> fragment slipped through.
        try:
            repair_response = ollama.chat(
                model=OLLAMA_MODEL,
                messages=messages + [
                    {"role": "assistant", "content": raw},
                    {"role": "user", "content": "That was not valid JSON. Re-send your exact same answer, "
                                                 "but as strictly valid JSON matching the schema, with no "
                                                 "<think> tags and no text outside the JSON object. Escape any "
                                                 "double-quote characters inside string values properly."},
                ],
                format="json",
                options={"temperature": 0, "num_predict": 1536},
                think=False,
            )
            raw_repair = repair_response["message"]["content"]
            parsed = _extract_json(raw_repair)
        except Exception as e2:
            parsed = {
                "state": "NOT_FOUND",
                "answer": "Internal error: the model's response could not be parsed as valid JSON, even after a repair attempt. Treating as unanswered for safety.",
                "citations": [],
                "reasoning": f"JSON parse error: {e2}. Original raw output: {raw[:500]}",
            }

    parsed.setdefault("state", "NOT_FOUND")
    parsed.setdefault("answer", "")
    parsed.setdefault("citations", [])
    parsed.setdefault("reasoning", "")
    parsed["_retrieved_chunks"] = chunks
    return parsed


if __name__ == "__main__":
    import sys
    q = " ".join(sys.argv[1:]) or "What is the minimum attendance required to sit for an exam?"
    result = answer_question(q, verbose=True)
    print(json.dumps({k: v for k, v in result.items() if k != "_retrieved_chunks"}, indent=2))