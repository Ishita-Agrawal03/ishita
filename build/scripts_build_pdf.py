"""One-off script: renders corpus/hostel_policy_source.md into corpus/hostel_policy.pdf"""
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

SRC = "corpus/hostel_policy_source.md"
OUT = "corpus/hostel_policy.pdf"

styles = getSampleStyleSheet()
h1 = ParagraphStyle("H1", parent=styles["Heading1"], spaceAfter=10, spaceBefore=14)
h2 = ParagraphStyle("H2", parent=styles["Heading2"], spaceAfter=6, spaceBefore=12)
body = ParagraphStyle("Body", parent=styles["Normal"], spaceAfter=8, leading=15)

def inline_md(text):
    # bold **text**
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    return text

story = []
with open(SRC, encoding="utf-8") as f:
    lines = f.read().split("\n")

buffer = []
def flush():
    if buffer:
        para = " ".join(buffer).strip()
        if para:
            story.append(Paragraph(inline_md(para), body))
        buffer.clear()

for line in lines:
    stripped = line.strip()
    if stripped.startswith("# "):
        flush()
        story.append(Paragraph(inline_md(stripped[2:]), h1))
    elif stripped.startswith("## "):
        flush()
        story.append(Paragraph(inline_md(stripped[3:]), h2))
    elif stripped == "":
        flush()
        story.append(Spacer(1, 4))
    else:
        buffer.append(stripped)
flush()

doc = SimpleDocTemplate(OUT, pagesize=letter,
                         leftMargin=0.9*inch, rightMargin=0.9*inch,
                         topMargin=0.8*inch, bottomMargin=0.8*inch,
                         title="Hostel Handbook 2025-26")
doc.build(story)
print("Built", OUT)
