# Planted Contradictions

This document records the three contradictions deliberately planted in the corpus, for evaluation purposes. Each is a genuine internal inconsistency a careful reader would find only by holding two passages side by side — the kind that exists in most real regulatory documents because they are amended piecemeal over years by different people.

---

## Contradiction 1 — Attendance threshold for examination eligibility

**File A:** `corpus/regulations.md`, Section 3.2 (Attendance Requirement for Examination Eligibility)
> "A student must maintain a minimum of **75% attendance** in a course to be eligible to sit for the End-Semester Examination in that course."

**File B:** `corpus/regulations.md`, Section 12.3 (Scholarship Continuation Review)
> "...applying the CGPA thresholds in Section 8 together with the attendance requirement of **80% as specified in Section 3**, to determine whether a recipient remains in good standing..."

**The conflict:** Section 12.3 explicitly claims to be quoting the number "specified in Section 3," but Section 3.2 specifies 75%, not 80%. This is a cross-reference error of the kind that accumulates when a document is amended in one place (the attendance floor was presumably lowered from 80% to 75% at some point) without updating a later section that references it by description rather than by direct link.

**Correct handling:** A question like *"What attendance percentage do I need to keep my scholarship?"* or *"What attendance is required for exams?"* should surface both numbers and flag them as contradictory, rather than confidently picking one. A question specifically about Section 3 alone can be answered as 75% since that is the actual text of Section 3; the contradiction only surfaces when the question implicates both passages (e.g., asking about the scholarship attendance rule, which is where the wrong number lives).

---

## Contradiction 2 — Late fee calculation method

**File A:** `corpus/regulations.md`, Section 9.2 (Fee Payment)
> "The late fee is a **flat charge of ₹500 per week or part thereof** of delay, applied uniformly regardless of the total fee amount outstanding, up to a maximum of four weeks..."

**File B:** `corpus/fee_deadlines.md`, "Late Payment Policy" section
> "Payments received after the due dates above are subject to a late fee calculated as **2% of the total outstanding fee amount for every week of delay**, compounding weekly, up to a maximum of six weeks..."

**The conflict:** Two different calculation methods (flat ₹500/week vs. 2% compounding/week) for the same event, from two documents that are meant to work together (the Regulations state the policy, the Fee Schedule is supposed to just fill in current amounts). They also disagree on the maximum duration before escalation (four weeks vs. six weeks). For any fee above ₹25,000 — i.e., every tuition fee in this corpus — the two methods produce materially different amounts owed.

**Correct handling:** A question like *"How much is the late fee if I pay two weeks late?"* cannot be answered with a single number; the system should surface both methods and note they conflict, rather than silently picking the one it retrieved first.

---

## Contradiction 3 — Hostel curfew time

**File:** `corpus/hostel_policy.pdf` (single document, internal self-contradiction)

**Passage A**, Section 1 (Scope):
> "The Institute's standard night curfew for all hostel residents, referenced throughout this document, is **11:00 PM**."

**Passage B**, Section 5.1 (Curfew and Night-Out Policy):
> "All resident students must be back within hostel premises by **10:00 PM** on all days of the week. The hostel gate is locked at 10:00 PM..."

**Passage C**, Section 5.3, consistent with Passage A:
> "A student holding a valid Night-Out Pass who returns to the hostel after **11:00 PM** must additionally inform the security desk..." — this implies 11:00 PM, not 10:00 PM, is the operative boundary time referenced elsewhere in the same section.

**The conflict:** The document states its own curfew is 11:00 PM in the scope section, then gives an operative rule of 10:00 PM in the section that actually governs curfew, while a neighboring clause in that same section (5.3) is written as if 11:00 PM were the reference point. This is a single-document self-contradiction, distinct from Contradictions 1 and 2, which span two files — included so the system is also tested on detecting conflicts within one source, not only across sources.

**Correct handling:** A question like *"What time is hostel curfew?"* should return both times (10:00 PM and 11:00 PM) and flag the conflict, citing both passages within the PDF, rather than picking whichever chunk the retriever ranks first.

---

## Why these three and not others

Each contradiction is representative of a different failure mode a retrieval system can miss:

1. **Contradiction 1** requires the system to notice that a passage's own claimed cross-reference doesn't match the referenced section — a case where naive retrieval would return only Section 12.3, sounding perfectly confident, unless the system also checks Section 3.
2. **Contradiction 2** spans two different files in two different formats (prose regulation vs. markdown table), testing whether retrieval surfaces both chunks together when a query touches a topic covered in more than one document.
3. **Contradiction 3** lives entirely inside one file (a PDF), testing detection of internal inconsistency rather than only cross-document inconsistency, and requires PDF text extraction to have preserved both passages correctly.

None of these are edge cases dreamed up to be tricky — they are the exact shape of contradiction a real registrar's office accumulates over years of amendments, which is the premise of this project.
