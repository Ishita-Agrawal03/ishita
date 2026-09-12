"""
Streamlit demo: ask a question, see the answer, the state badge
(ANSWERED / NOT_FOUND / CONTRADICTION), and the exact citations behind it.

Run:
    ollama serve                        # if not already running
    ollama pull qwen2.5:14b-instruct    # one-time, if not already pulled
    streamlit run src/app.py
"""
import os
import sys
import json
import streamlit as st

sys.path.insert(0, os.path.dirname(__file__))
from answer import answer_question  # noqa: E402

st.set_page_config(page_title="Rulebook Oracle", page_icon="📘", layout="centered")

STATE_STYLE = {
    "ANSWERED": ("✅ Answered", "#1a7f37", "#e6f4ea"),
    "NOT_FOUND": ("🚫 Not covered by the rulebook", "#8a6d00", "#fff8e1"),
    "CONTRADICTION": ("⚠️ Contradiction found", "#b3261e", "#fdecea"),
}

with st.sidebar:
    st.subheader("Evaluation score")
    results_path = os.path.join(os.path.dirname(__file__), "..", "eval", "results.json")
    try:
        with open(results_path, encoding="utf-8") as f:
            eval_data = json.load(f)
        summary = eval_data["summary"]
        st.metric("Overall", f"{summary['correct']}/{summary['total']}")
        for bucket, stats in summary["by_bucket"].items():
            st.caption(f"{bucket}: {stats['correct']}/{stats['total']}")
        st.caption("From the last `eval/run_eval.py` run — see eval/results.md for full detail.")
    except Exception:
        st.caption("Run `python eval/run_eval.py` to generate a score for this panel.")

st.title("📘 The Rulebook That Argues With Itself")
st.caption(
    "Ask a question about the university's academic regulations, hostel handbook, "
    "fee schedule, or student society constitution. Every answer is grounded in the "
    "actual documents — nothing here comes from the model's general knowledge."
)

if "history" not in st.session_state:
    st.session_state.history = []

example_cols = st.columns(3)
examples = [
    "What attendance percentage is needed for exams?",
    "What time is hostel curfew?",
    "What happens if I miss an exam for a family wedding?",
]
clicked_example = None
for col, ex in zip(example_cols, examples):
    if col.button(ex, use_container_width=True):
        clicked_example = ex

question = st.chat_input("Ask a question about the rulebook...")
question = question or clicked_example

if question:
    st.session_state.history.append({"role": "user", "content": question})
    with st.spinner("Retrieving passages and checking for conflicts..."):
        try:
            result = answer_question(question)
        except Exception as e:
            result = {"state": "ERROR", "answer": f"Something went wrong: {e}", "citations": [], "reasoning": ""}
    st.session_state.history.append({"role": "assistant", "content": result})

for turn in st.session_state.history:
    if turn["role"] == "user":
        with st.chat_message("user"):
            st.write(turn["content"])
    else:
        result = turn["content"]
        with st.chat_message("assistant"):
            state = result.get("state", "ERROR")
            if state in STATE_STYLE:
                label, fg, bg = STATE_STYLE[state]
                st.markdown(
                    f"<span style='background-color:{bg};color:{fg};padding:3px 10px;"
                    f"border-radius:12px;font-weight:600;font-size:0.85em'>{label}</span>",
                    unsafe_allow_html=True,
                )
            st.write(result.get("answer", ""))

            citations = result.get("citations", [])
            if citations:
                with st.expander(f"📎 {len(citations)} citation(s) — click to verify"):
                    for c in citations:
                        st.markdown(
                            f"**{c.get('source_file', '?')}** — *{c.get('section', '?')}* "
                            f"(`{c.get('chunk_id', '?')}`)"
                        )
            elif state == "NOT_FOUND":
                st.caption("No passage in the rulebook covers this scenario.")

st.divider()
st.caption(
    "Built for evaluation purposes: every claim is traceable to a chunk_id / source_file / "
    "section triple. See contradictions.md and eval/results.md in the repo for the scored test set."
)
