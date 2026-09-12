"""
Runs every question in questions.json through the answer pipeline and scores
the result automatically against the expected state. This is a pure
state-match score (ANSWERED / NOT_FOUND / CONTRADICTION) -- exactly the kind
of thing a script can check without a human reading prose.

Usage:
    export GROQ_API_KEY=your_key_here
    python eval/run_eval.py                 # run everything, print + save results
    python eval/run_eval.py --bucket unanswerable   # run just the 25 hard ones
    python eval/run_eval.py --save eval/results.json --md eval/results.md
"""
import os
import sys
import json
import argparse
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from answer import answer_question  # noqa: E402

QUESTIONS_PATH = os.path.join(os.path.dirname(__file__), "questions.json")


def load_questions(include_buckets=None, exclude_buckets=None):
    with open(QUESTIONS_PATH, encoding="utf-8") as f:
        data = json.load(f)
    if include_buckets:
        data = {b: data[b] for b in include_buckets if b in data}
    if exclude_buckets:
        data = {b: qs for b, qs in data.items() if b not in exclude_buckets}
    return data


def run(include_buckets=None, exclude_buckets=None, sleep_between=1.0):
    data = load_questions(include_buckets, exclude_buckets)
    all_results = []

    for bucket_name, questions in data.items():
        print(f"\n=== Bucket: {bucket_name} ({len(questions)} questions) ===")
        for q in questions:
            qid = q["id"]
            question_text = q["question"]
            expected = q["expected_state"]
            try:
                result = answer_question(question_text)
                actual = result.get("state", "PARSE_ERROR")
            except Exception as e:
                result = {"state": "ERROR", "answer": str(e), "citations": [], "reasoning": str(e)}
                actual = "ERROR"

            correct = (actual == expected)
            status = "PASS" if correct else "FAIL"
            print(f"[{status}] {qid} | expected={expected:13s} actual={actual:13s} | {question_text[:70]}")

            all_results.append({
                "id": qid,
                "bucket": bucket_name,
                "question": question_text,
                "expected_state": expected,
                "actual_state": actual,
                "correct": correct,
                "answer": result.get("answer", ""),
                "citations": result.get("citations", []),
                "reasoning": result.get("reasoning", ""),
            })
            time.sleep(sleep_between)  # be polite to the API / avoid rate limits

    return all_results


def summarize(results):
    total = len(results)
    correct = sum(1 for r in results if r["correct"])
    print(f"\n{'='*60}")
    print(f"OVERALL: {correct}/{total} correct")

    by_bucket = {}
    for r in results:
        by_bucket.setdefault(r["bucket"], {"correct": 0, "total": 0})
        by_bucket[r["bucket"]]["total"] += 1
        by_bucket[r["bucket"]]["correct"] += int(r["correct"])

    for bucket, stats in by_bucket.items():
        print(f"  {bucket:15s}: {stats['correct']}/{stats['total']}")

    # confusion matrix
    states = ["ANSWERED", "NOT_FOUND", "CONTRADICTION"]
    print(f"\nConfusion matrix (rows=expected, cols=actual):")
    header = "                 " + "  ".join(f"{s:13s}" for s in states)
    print(header)
    for exp in states:
        row = [r for r in results if r["expected_state"] == exp]
        counts = [sum(1 for r in row if r["actual_state"] == act) for act in states]
        print(f"  {exp:15s} " + "  ".join(f"{c:13d}" for c in counts))

    return {"total": total, "correct": correct, "by_bucket": by_bucket}


def write_markdown_report(results, summary, path):
    lines = ["# Evaluation Results\n"]
    lines.append(f"**Overall: {summary['correct']}/{summary['total']} correct**\n")
    for bucket, stats in summary["by_bucket"].items():
        lines.append(f"- {bucket}: {stats['correct']}/{stats['total']}")
    lines.append("\n## Detail\n")
    lines.append("| ID | Bucket | Expected | Actual | Result | Question |")
    lines.append("|---|---|---|---|---|---|")
    for r in results:
        mark = "✅" if r["correct"] else "❌"
        q_short = r["question"][:80].replace("|", "/")
        lines.append(f"| {r['id']} | {r['bucket']} | {r['expected_state']} | {r['actual_state']} | {mark} | {q_short} |")

    lines.append("\n## Full answers and citations\n")
    for r in results:
        lines.append(f"### {r['id']} — {r['question']}")
        lines.append(f"- Expected: `{r['expected_state']}` | Actual: `{r['actual_state']}` | {'PASS' if r['correct'] else 'FAIL'}")
        lines.append(f"- Answer: {r['answer']}")
        if r["citations"]:
            cite_str = "; ".join(f"{c.get('source_file')} / {c.get('section')} (`{c.get('chunk_id')}`)" for c in r["citations"])
            lines.append(f"- Citations: {cite_str}")
        lines.append(f"- Reasoning: {r['reasoning']}")
        lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"\nMarkdown report written to {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bucket", nargs="+", choices=["answerable", "contradiction", "unanswerable"], default=None,
                         help="Run only these buckets (space-separated). Default: all.")
    parser.add_argument("--skip", nargs="+", choices=["answerable", "contradiction", "unanswerable"], default=None,
                         help="Skip these buckets (space-separated). Useful once a bucket is consistently passing "
                              "and you want to save API calls / avoid rate limits while iterating on the rest, "
                              "e.g. --skip answerable")
    parser.add_argument("--save", default="eval/results.json")
    parser.add_argument("--md", default="eval/results.md")
    parser.add_argument("--sleep", type=float, default=1.0, help="Seconds to wait between API calls (raise if hitting rate limits)")
    args = parser.parse_args()

    results = run(include_buckets=args.bucket, exclude_buckets=args.skip, sleep_between=args.sleep)
    summary = summarize(results)

    with open(args.save, "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "results": results}, f, indent=2)
    print(f"JSON results written to {args.save}")

    write_markdown_report(results, summary, args.md)