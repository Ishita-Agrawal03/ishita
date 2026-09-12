"""
Ingest the corpus into a persistent Chroma collection.

Chunking strategy:
  - Markdown files are split by heading (##, ###) so each chunk is a coherent
    clause/section, not an arbitrary character slice. This matters because the
    whole point of the system is precise citation: a chunk should be exactly
    "the passage a human would point to," not half of one.
  - The PDF is split by heading too (it has "## " style headings baked in from
    how it was authored), falling back to paragraph splits if no headings are
    found.
  - Every chunk gets metadata: source_file, section_title, chunk_id. This is
    what makes every answer traceable back to an exact passage.

Run:
    python src/ingest.py
"""
import os
import re
import hashlib
import chromadb
from chromadb.utils import embedding_functions
from pypdf import PdfReader

CORPUS_DIR = os.path.join(os.path.dirname(__file__), "..", "corpus")
DB_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "vectorstore")
COLLECTION_NAME = "rulebook"
EMBED_MODEL = "all-MiniLM-L6-v2"  # small, fast, good enough for this corpus size

MAX_CHUNK_WORDS = 220   # keep chunks tight so retrieval is precise
MIN_CHUNK_WORDS = 15    # merge tiny fragments (like a lone table row) upward


def read_pdf_text(path):
    reader = PdfReader(path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def split_markdown_by_heading(text):
    """
    Split on lines starting with '#' (markdown) OR on plain numbered heading
    lines like "5. Curfew and Night-Out Policy" (single number + period +
    short title) — the latter matters for PDF sources, where markdown '#'
    syntax doesn't survive text extraction but numbered section headings do.
    We deliberately do NOT match clause-numbering like "5.1 " or "12.3 "
    (two-level numbers), since those are body text, not section headings.
    Returns list of (heading_path, body_text).
    """
    lines = text.split("\n")
    chunks = []
    current_h1 = ""
    current_heading = ""
    buffer = []

    md_heading_re = re.compile(r"^#{1,3}\s+")
    plain_heading_re = re.compile(r"^(\d{1,2})\.\s+([A-Z][A-Za-z ,/&\-']{2,60})$")

    def flush():
        body = "\n".join(buffer).strip()
        if body:
            heading_path = current_h1 if current_h1 == current_heading else f"{current_h1} > {current_heading}"
            chunks.append((heading_path.strip(" >"), body))
        buffer.clear()

    for line in lines:
        stripped = line.rstrip()
        md_match = md_heading_re.match(stripped)
        plain_match = plain_heading_re.match(stripped.strip())
        if md_match:
            flush()
            heading_text = re.sub(r"^#{1,3}\s+", "", stripped).strip()
            level = len(re.match(r"^(#{1,3})", stripped).group(1))
            if level == 1:
                current_h1 = heading_text
                current_heading = heading_text
            else:
                current_heading = heading_text
            buffer.append(stripped)
        elif plain_match:
            flush()
            heading_text = stripped.strip()
            current_heading = heading_text
            if not current_h1:
                current_h1 = heading_text
            buffer.append(stripped)
        else:
            buffer.append(line)
    flush()
    return chunks


def subsplit_long_chunk(heading, body):
    """If a section is too long, split it further by numbered sub-clauses
    (e.g. '3.1', '3.2') or by paragraph, so no chunk blows past MAX_CHUNK_WORDS."""
    words = body.split()
    if len(words) <= MAX_CHUNK_WORDS:
        return [(heading, body)]

    # try splitting on numbered clause pattern like "\n3.1 " or "\n7.2 "
    parts = re.split(r"\n(?=\d+\.\d+\s)", body)
    if len(parts) > 1:
        return [(heading, p.strip()) for p in parts if p.strip()]

    # fallback: split into paragraph groups under the word budget
    paras = [p for p in body.split("\n\n") if p.strip()]
    out, buf, buf_words = [], [], 0
    for p in paras:
        pw = len(p.split())
        if buf_words + pw > MAX_CHUNK_WORDS and buf:
            out.append((heading, "\n\n".join(buf)))
            buf, buf_words = [], 0
        buf.append(p)
        buf_words += pw
    if buf:
        out.append((heading, "\n\n".join(buf)))
    return out


def merge_tiny_chunks(chunks):
    """Merge chunks under MIN_CHUNK_WORDS into the previous chunk so we don't
    end up with useless slivers (e.g. a lone '## Amendments' header with one line)."""
    merged = []
    for heading, body in chunks:
        if merged and len(body.split()) < MIN_CHUNK_WORDS:
            prev_heading, prev_body = merged[-1]
            merged[-1] = (prev_heading, prev_body + "\n" + body)
        else:
            merged.append((heading, body))
    return merged


def chunk_file(filepath):
    filename = os.path.basename(filepath)
    if filename.endswith(".pdf"):
        text = read_pdf_text(filepath)
    else:
        with open(filepath, encoding="utf-8") as f:
            text = f.read()

    raw_chunks = split_markdown_by_heading(text)
    if not raw_chunks:
        # no headings found at all -> treat whole doc as one chunk to subsplit
        raw_chunks = [("", text)]

    expanded = []
    for heading, body in raw_chunks:
        expanded.extend(subsplit_long_chunk(heading, body))
    expanded = merge_tiny_chunks(expanded)

    records = []
    for i, (heading, body) in enumerate(expanded):
        chunk_id = hashlib.sha1(f"{filename}-{i}-{heading}".encode()).hexdigest()[:12]
        records.append({
            "id": chunk_id,
            "text": body,
            "metadata": {
                "source_file": filename,
                "section": heading or "(untitled)",
                "chunk_index": i,
            },
        })
    return records


def main():
    os.makedirs(DB_DIR, exist_ok=True)
    client = chromadb.PersistentClient(path=DB_DIR)

    # drop any existing collection so re-running ingest is idempotent
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL)
    collection = client.create_collection(name=COLLECTION_NAME, embedding_function=embed_fn)

    all_records = []
    for fname in sorted(os.listdir(CORPUS_DIR)):
        fpath = os.path.join(CORPUS_DIR, fname)
        if not os.path.isfile(fpath):
            continue
        if not (fname.endswith(".md") or fname.endswith(".pdf")):
            continue
        records = chunk_file(fpath)
        print(f"{fname}: {len(records)} chunks")
        all_records.extend(records)

    collection.add(
        ids=[r["id"] for r in all_records],
        documents=[r["text"] for r in all_records],
        metadatas=[r["metadata"] for r in all_records],
    )

    print(f"\nTotal chunks ingested: {len(all_records)}")
    print(f"Vector store persisted at: {DB_DIR}")


if __name__ == "__main__":
    main()
