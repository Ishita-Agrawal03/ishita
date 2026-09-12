

````markdown
# RuleLens — The Rulebook That Argues With Itself

A retrieval-augmented QA system over a university rulebook that does **more than generate an answer**.

For every question, RuleLens decides whether the corpus:

- ✅ **ANSWERED** — contains a direct answer
- 🚫 **NOT_FOUND** — does not explicitly cover the requested scenario
- ⚠️ **CONTRADICTION** — contains conflicting rules for the same question

Every answer is grounded in retrieved passages and includes traceable
`chunk_id / source_file / section` citations.

---

## Why RuleLens?

Real regulatory documents are often amended over time. Different sections can
contain conflicting values or rules, while other seemingly plausible scenarios
may simply not be covered.

A normal RAG system can be tempted to:

> retrieve something vaguely related → generate a confident answer

RuleLens instead asks:

> **Does the retrieved corpus actually support an answer?**

The project deliberately contains three planted contradictions and 25 hard
unanswerable questions to test whether the system can distinguish:

**knowledge from the corpus** vs. **reasonable-sounding inference** vs.
**internal conflict**.

The goal is not to maximize the number of questions answered. The goal is to
find the line between **too little ignorance and too much caution**.

---

## Architecture

```text
                         ┌─────────────────────┐
                         │   Rulebook Corpus   │
                         │ Markdown + PDF      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     ingest.py       │
                         │ chunk + embed       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │       Chroma        │
                         │ persistent, local   │
                         │    vector store     │
                         └──────────┬──────────┘
                                    │
                              retrieve top-k
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      answer.py      │
                         │ retrieval sanity    │
                         │       check         │
                         │         +           │
                         │  Qwen2.5 14B local  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                 ┌──────────────────────────────────┐
                 │       Three-state decision        │
                 │                                  │
                 │ ANSWERED / NOT_FOUND /           │
                 │ CONTRADICTION                    │
                 └───────────────┬──────────────────┘
                                 │
                                 ▼
                         citations + answer
                                 │
                                 ▼
                         ┌─────────────────────┐
                         │    Streamlit UI     │
                         └─────────────────────┘
````

### Core components

* **Chunking** (`src/ingest.py`)
  Splits the corpus by document headings and numbered sub-clauses so that
  retrieved chunks correspond to coherent rules rather than arbitrary
  character windows.

* **Embeddings**
  `sentence-transformers/all-MiniLM-L6-v2` runs locally.

* **Vector store**
  Chroma is persisted to `data/vectorstore/`.

* **LLM**
  `qwen2.5:14b-instruct` runs locally through Ollama.

* **Retrieval sanity check**
  If the best retrieval distance is above
  `RETRIEVAL_DISTANCE_CEILING = 1.75`, RuleLens returns `NOT_FOUND` without
  calling the LLM.

* **Three-state classification**
  The LLM receives the retrieved passages and follows an explicit decision
  procedure:

  1. Identify passages that directly answer the question.
  2. If one consistent direct answer exists → `ANSWERED`.
  3. If multiple direct passages give different values/rules for the same
     quantity → `CONTRADICTION`.
  4. If no retrieved passage directly answers the question → `NOT_FOUND`.
  5. The system avoids silently extending a rule from one section to another
     when the corpus does not explicitly establish that connection.

---

## Repository Structure

```text
ishita/
│
├── app.py                         Streamlit demo UI
├── README.md
├── requirements.txt
├── contradictions.md              Answer key for the 3 planted contradictions
│
├── corpus/
│   ├── regulations.md             Main academic regulations
│   ├── fee_deadlines.md           Fee/deadline table
│   ├── student_society_constitution.md
│   └── hostel_policy.pdf          PDF rulebook document
│
├── src/
│   ├── ingest.py                  Chunk, embed, and store corpus
│   ├── retrieve.py                Query Chroma vector store
│   └── answer.py                  Three-state classification + Ollama call
│
├── eval/
│   ├── questions.json             Evaluation questions
│   ├── run_eval.py                Automated evaluation script
│   ├── results.json               Raw evaluation results
│   └── results.md                 Human-readable evaluation report
│
├── data/
│   └── vectorstore/               Persistent Chroma database
│
└── build/
    └── ...                        Supporting build/generated artifacts
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ishita-Agrawal03/ishita.git
cd ishita
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Install Ollama from:

[https://ollama.com/download](https://ollama.com/download)

Then pull the model:

```bash
ollama pull qwen2.5:14b-instruct
```

No API key is required.

The embeddings and LLM both run locally.

---

## Running RuleLens

### 1. Start Ollama

If Ollama is not already running as a background service:

```bash
ollama serve
```

### 2. Build the vector store

If the persistent vector store is missing or the corpus has changed:

```bash
python src/ingest.py
```

The ingestion process:

```text
corpus documents
      ↓
document-aware chunking
      ↓
MiniLM embeddings
      ↓
Chroma persistent vector store
```

### 3. Start the Streamlit application

From the repository root:

```bash
streamlit run app.py
```

The UI provides:

* question input
* generated answer
* `ANSWERED` / `NOT_FOUND` / `CONTRADICTION` state
* supporting citations
* source file and section information
* evaluation score from the latest evaluation run

---

## Command-Line Test

The answer pipeline can also be tested without Streamlit.

From the repository root:

```bash
python src/answer.py "What is the minimum attendance required for exams?"
```

This runs the same retrieval and local LLM pipeline used by the application.

---

## Evaluation

The evaluation set contains:

* **13 answerable questions**
* **3 contradiction questions**
* **25 hard unanswerable questions**

The 25 unanswerable questions are intentionally designed to be plausible
questions that the corpus genuinely does not answer.

Run the complete evaluation:

```bash
python eval/run_eval.py
```

Run only the contradiction tests:

```bash
python eval/run_eval.py --bucket contradiction
```

Run only the 25 hard unanswerable questions:

```bash
python eval/run_eval.py --bucket unanswerable
```

Skip a bucket:

```bash
python eval/run_eval.py --skip answerable
```

Add a delay between questions:

```bash
python eval/run_eval.py --sleep 1.0
```

The evaluator automatically:

* runs every question through the real answer pipeline
* compares the predicted state with `expected_state`
* prints PASS/FAIL for every question
* generates a confusion matrix
* writes `eval/results.json`
* writes `eval/results.md`

The score is based on **state classification**, not subjective judgement of
whether generated prose "sounds right".

---

## Evaluation Results

Most recent evaluation:

**35 / 41 correct — 85.4%**

| Bucket        |       Score |
| ------------- | ----------: |
| Answerable    |  **9 / 13** |
| Contradiction |   **3 / 3** |
| Unanswerable  | **23 / 25** |
| **Overall**   | **35 / 41** |

### What this means

The contradiction detector achieved:

**3 / 3**

This is important because a naive RAG system may retrieve two conflicting
passages and still confidently choose one.

The system also correctly rejected:

**23 / 25**

of the deliberately hard unanswerable questions.

The remaining failures are not hidden:

* **4 ANSWERED questions → NOT_FOUND**

  * A2, A4, A7, A8
  * The model was too conservative despite a direct answer being available.

* **2 NOT_FOUND questions → ANSWERED**

  * U5, U10
  * The model inferred a rule across a section boundary that the corpus did
    not explicitly establish.

These errors represent the central trade-off of the project: **when should a
system answer, and when should it admit that the corpus does not support the
answer?**

Full per-question results, answers, reasoning, and citations are available in:

```text
eval/results.md
```

---

## Example States

### 1. ANSWERED

**Question:**

```text
What is the minimum attendance percentage required to sit for the
end-semester examination?
```

Expected state:

```text
ANSWERED
```

The system retrieves the relevant attendance regulation and returns the
supported value with its citation.

---

### 2. NOT_FOUND

**Question:**

```text
If I'm approved for the two-installment tuition payment plan and then
miss the second installment, does the provisional cancellation process
in Section 9.3 apply the same way as it would to a normal missed payment?
```

Expected state:

```text
NOT_FOUND
```

The corpus discusses the relevant mechanisms separately but does not explicitly
establish that the provisional cancellation process applies to the
two-installment scenario.

RuleLens should not invent that connection.

---

### 3. CONTRADICTION

**Question:**

```text
What time is the hostel curfew?
```

Expected state:

```text
CONTRADICTION
```

The corpus contains conflicting curfew values.

RuleLens surfaces both passages rather than silently selecting one.

The exact locations of the three planted contradictions are documented in:

```text
contradictions.md
```

That file is intentionally outside `corpus/`, so it is **not ingested into the
vector store**.

---

## What Is Mocked / Simulated?

### Nothing in the core pipeline is mocked.

For every evaluation question, the system performs the actual pipeline:

```text
question
   ↓
MiniLM embedding
   ↓
Chroma retrieval
   ↓
retrieved corpus passages
   ↓
Qwen2.5 14B via Ollama
   ↓
state + answer + citations
```

There are:

* no hardcoded answers
* no fake retrieval results
* no simulated LLM responses
* no stubbed classification results

The embeddings, retrieval, and LLM call are real and run against the actual
corpus.

### What was considered but not implemented?

An earlier design considered a deterministic contradiction pre-check based on
regex/value extraction. The idea was to detect conflicting numeric values
before sending the question to the LLM.

It was **not implemented** because prompt-based contradiction detection was
sufficient to achieve:

**3 / 3 contradiction questions correct.**

A deterministic validation layer would be a natural future improvement if
additional reliability were required.

---

## Contradiction Design

The corpus contains three deliberately planted contradictions across the
rulebook.

The goal is to test whether the system:

1. retrieves both conflicting passages,
2. recognizes that they answer the same underlying question,
3. avoids choosing a passage merely because it appears more authoritative,
   specific, or operational,
4. returns `CONTRADICTION`,
5. cites the conflicting source passages.

The system is explicitly instructed not to resolve direct conflicts by silently
preferring one passage.

The answer key is stored separately in:

```text
contradictions.md
```

---

## Model Selection

Three model configurations were evaluated during development.

### 1. `llama-3.3-70b-versatile` via Groq

This performed well but encountered rate limits during evaluation on the free
tier. One evaluation also failed because of malformed JSON.

### 2. `qwen3:4b` via Ollama

This was fully local and free to run, but was not reliable enough for the
nuance required by this task.

It failed some easy answerable questions and also over-extended on unanswerable
questions.

### 3. `qwen2.5:14b-instruct` via Ollama

This is the model used for the reported evaluation results.

It provided:

* reliable JSON output
* stronger reasoning than the 4B local model
* fully local execution
* no API key
* no per-token API cost
* more stable behavior on the three-state classification task

---

## Design Decisions

### Why Chroma?

The project requires persistent local vector storage. Chroma provides a
simple persistent vector database without requiring an external service.

### Why MiniLM?

`all-MiniLM-L6-v2` provides lightweight local embeddings with minimal setup and
no API cost.

### Why top-12 retrieval?

The classifier needs enough surrounding context to detect cases where relevant
rules appear in different parts of the corpus, particularly contradictions.

### Why use an LLM for the three-state decision?

The distinction between:

```text
"the corpus does not answer this"
```

and

```text
"the corpus contains enough information to answer this"
```

is not always reducible to a simple similarity threshold.

Similarly, contradiction detection requires reasoning about whether two
passages provide different answers to the same underlying quantity or rule.

The retrieval distance threshold is therefore used only as an initial
relevance sanity check. The more nuanced classification is handled by the
local LLM.

---

## Known Limitations

* Retrieval uses `all-MiniLM-L6-v2`, which is not fine-tuned specifically for
  legal or regulatory text.

* Three-state classification depends partly on the LLM distinguishing
  **directly stated rules** from **reasonable inference**.

* The system is single-turn. Each question is evaluated independently.

* The Streamlit interface keeps visible question history, but each answer is
  still generated from the current question rather than relying on previous
  conversational context.

* Local-model results can vary somewhat depending on the Ollama version and
  model build, although `temperature=0` is used for more deterministic output.

* The current evaluation score is not intended to represent general
  benchmark performance. It measures performance on this project's specific
  corpus and evaluation set.

---

## Future Improvements

Potential extensions include:

* stronger domain-specific embedding models
* deterministic validation of extracted rule values
* hybrid keyword + vector retrieval
* better contradiction clustering
* document version/date awareness
* confidence calibration
* automated regression testing on every code change
* support for multi-turn rulebook conversations

---

## Project Goal

RuleLens is intentionally not optimized for:

> **"Answer every question."**

It is optimized for:

> **"Answer when the corpus supports the answer, refuse when it does not,
> and surface conflicts instead of hiding them."**

That distinction is the core of the project.

---

## License

This project is created as part of an academic/project evaluation submission.

```

**One final check before you commit:** your actual `app.py` is at the repository root, so this version now consistently uses `app.py` everywhere. The README also accurately documents the current **35/41** evaluation rather than hiding the failures.
```
