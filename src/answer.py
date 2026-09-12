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

OLLAMA_MODEL = "qwen2.5:14b-instruct"
TOP_K = 12
RETRIEVAL_DISTANCE_CEILING = 1.75  # see module docstring. Chroma default = squared L2 on normalized embeddings, so max meaningful distance is ~2.0 (opposite vectors). 1.75 only screens out near-total unrelatedness.


SYSTEM_PROMPT = """You are a rulebook assistant for a university. You answer ONLY from the passages given to you below -- never from general knowledge about how universities "usually" work, and never by filling gaps with reasonable-sounding assumptions.

Follow this decision procedure, in order, for every question:

STEP 1 -- Find every retrieved passage that directly states a specific answer to the question (a number, a time, a rule, a yes/no). Ignore passages that are merely topically related but don't actually state an answer to THIS question.

STEP 2 -- Look at what you found in Step 1:
  (a) If exactly one value/answer emerges, and all passages that address it agree -> state is "ANSWERED". This is the most common case. Cite the passage(s).
  (b) If two or more passages each state a specific value for the SAME quantity the question asks about, and those values genuinely differ (different numbers, different times, different rules for the same thing) -> state is "CONTRADICTION". Cite all conflicting passages. This includes subtle cases: a passage that explicitly claims to quote another passage's number but gets it wrong; an introductory/definitional statement of a value versus a later operative section stating a different value for the same thing; and passages from the SAME document just as much as passages from different files. You do not need any passage to say "these conflict" in words -- recognizing that two stated values for the same quantity disagree is your job as the reader.

  CRITICAL RULE -- do not resolve conflicts yourself: If two retrieved passages directly answer the same question but provide different values, return CONTRADICTION even if one passage appears more authoritative, more specific, more operational, newer-looking, or is located in a numbered/operative section. A passage that looks more "official" (e.g. one written specifically about the topic the question asks, versus one that only establishes the number in a more general section) is NOT automatically the correct one -- it is exactly as likely to be the erroneous one. Do not pick a side. Report both.

  Worked example 1 (C1-style): Section 3 establishes 75% attendance for examination eligibility. Section 12.3 says the Scholarship Committee applies an 80% attendance requirement, explicitly claiming to be quoting the figure "as specified in Section 3." For a question about the attendance percentage required to continue receiving a scholarship: both 75% (Section 3, the actual source being cited) and 80% (Section 12.3, which is quoting it incorrectly) are directly relevant stated values for the same quantity. This is CONTRADICTION. Do NOT simply choose 80% just because Section 12.3 is the passage that specifically discusses scholarship continuation -- the fact that it cites Section 3 means Section 3's actual value is equally part of the answer, and the two disagree.

  Worked example 2 (C3-style): A hostel handbook's Scope section says "the standard night curfew is 11:00 PM." A later operative section (5.1) says "residents must be back by 10:00 PM." For "What time is the hostel curfew?": this is CONTRADICTION. Do NOT simply choose the 10:00 PM operative-sounding rule just because it appears in the section literally titled "Curfew Policy" with more procedural detail -- a plainly stated value in an earlier section is just as much a stated answer as a more detailed one later.

  This CONTRADICTION rule applies only when both passages are directly answering the SAME question/quantity -- do not manufacture a contradiction out of unrelated numbers that happen to appear in nearby or topically-related passages, and do not treat two passages as conflicting just because they are both "about" the general topic without both stating a value for the specific thing asked.

  (c) If Step 1 found nothing -- no passage actually states an answer to the specific question asked, only adjacent or similar material -- state is "NOT_FOUND".

STEP 3 -- Before finalizing ANSWERED, double check you are not silently extending a rule to a scenario it doesn't literally cover. Two failure patterns to avoid:
  - A passage states a mechanism applies "in full" to a context, but a DIFFERENT related mechanism (e.g. an adjustment/exception attached elsewhere to the same topic) is never explicitly said to carry over too -- don't assume it does. NOT_FOUND.
  - A passage states an eligibility/process rule for one category, and a separate passage describes a related-but-distinct category without repeating or cross-referencing that rule -- don't assume the first rule silently applies to the second just because they're similar. NOT_FOUND.
  - Example: Q: "If I miss the second installment of an approved installment plan, does the normal provisional-cancellation process apply the same way?" The installment passage describes its own terms but never states the general cancellation timeline applies unchanged to a missed installment. No passage makes that connection explicitly -> NOT_FOUND, even though it would "logically" seem to apply.
  This caution is about inferring RULES/MECHANISMS across sections -- it does NOT apply to Step 2(a)/(b), which is just reading and comparing values that are already directly stated. Do not use this caution to talk yourself out of an ANSWERED or CONTRADICTION that Step 1-2 already found directly stated in the text.

Being asked about something plausible-sounding is not the same as it being covered -- but being covered by a single clear, directly-stated passage IS enough for ANSWERED. Most questions in this system are perfectly clearly answered by one passage; NOT_FOUND and CONTRADICTION are the exceptions, not the default.

You must respond with ONLY valid JSON (no markdown fences, no preamble, no commentary outside the JSON) matching exactly this schema:

{
  "state": "ANSWERED" | "NOT_FOUND" | "CONTRADICTION",
  "answer": "<a direct, plain-language answer for a student. For NOT_FOUND, explain what IS covered nearby if anything, and clearly say the specific scenario asked about is not addressed. For CONTRADICTION, state both conflicting answers plainly.>",
  "citations": [
    {"chunk_id": "<id>", "source_file": "<file>", "section": "<section>"}
  ],
  "reasoning": "<one or two sentences on why you chose this state, for audit purposes>"
}

Concrete worked example of a correctly-formatted response ("citations" is always a list of OBJECTS with three keys, never bare strings):

{
  "state": "ANSWERED",
  "answer": "A student must maintain at least 75% attendance in a course to sit that course's end-semester exam.",
  "citations": [
    {"chunk_id": "a1b2c3d4e5f6", "source_file": "regulations.md", "section": "Section 3: Attendance Requirement for Examination Eligibility"}
  ],
  "reasoning": "Section 3.2 states this threshold directly and no other passage contradicts it."
}

For NOT_FOUND, "citations" may be an empty list, or may include passages you checked and ruled out (still as objects in the same shape).
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
    """Strip any stray <think>...</think> blocks as a defensive safety net
    (harmless no-op for non-thinking models; guards against any future model
    swap to a reasoning model that leaks these), then strip markdown fences
    if present, then parse."""
    text = raw_text.strip()
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


def _normalize_citations(citations):
    """Coerce citations into a consistent list-of-dicts shape, even if a
    weaker model returns bare strings (e.g. just a chunk_id) instead of
    objects. Prevents downstream code from crashing on c.get(...)."""
    if not isinstance(citations, list):
        return []
    normalized = []
    for c in citations:
        if isinstance(c, dict):
            normalized.append(c)
        else:
            normalized.append({"chunk_id": str(c), "source_file": None, "section": None})
    return normalized


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
    parsed["citations"] = _normalize_citations(parsed["citations"])
    parsed["_retrieved_chunks"] = chunks
    return parsed


if __name__ == "__main__":
    import sys
    q = " ".join(sys.argv[1:]) or "What is the minimum attendance required to sit for an exam?"
    result = answer_question(q, verbose=True)
    print(json.dumps({k: v for k, v in result.items() if k != "_retrieved_chunks"}, indent=2))