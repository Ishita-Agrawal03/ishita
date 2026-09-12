# Evaluation Results

**Overall: 20/41 correct**

- answerable: 13/13
- contradiction: 2/3
- unanswerable: 5/25

## Detail

| ID | Bucket | Expected | Actual | Result | Question |
|---|---|---|---|---|---|
| A1 | answerable | ANSWERED | ANSWERED | ✅ | What is the minimum attendance percentage required to sit for the end-semester e |
| A2 | answerable | ANSWERED | ANSWERED | ✅ | What is the minimum CGPA a student must maintain to avoid being placed on Academ |
| A3 | answerable | ANSWERED | ANSWERED | ✅ | Within how many working days of result declaration can a student request revalua |
| A4 | answerable | ANSWERED | ANSWERED | ✅ | What is the tuition fee for a UG student in the Odd semester of 2025-26? |
| A5 | answerable | ANSWERED | ANSWERED | ✅ | Can a guest stay overnight in a student's hostel room? |
| A6 | answerable | ANSWERED | ANSWERED | ✅ | How many founding members are required to register a new student Society? |
| A7 | answerable | ANSWERED | ANSWERED | ✅ | Can a student report ragging anonymously? |
| A8 | answerable | ANSWERED | ANSWERED | ✅ | What CGPA must a Merit Scholarship recipient maintain to continue receiving it? |
| A9 | answerable | ANSWERED | ANSWERED | ✅ | If a student arrives late to an exam, after how many minutes will they not be al |
| A10 | answerable | ANSWERED | ANSWERED | ✅ | What is the maximum permitted duration of the B.Tech programme, including medica |
| A11 | answerable | ANSWERED | ANSWERED | ✅ | What happens to my exam eligibility if I miss classes because I had to attend my |
| A12 | answerable | ANSWERED | ANSWERED | ✅ | Can I get my attendance shortfall condoned if I was traveling internationally fo |
| A13 | answerable | ANSWERED | ANSWERED | ✅ | Does attending my sibling's graduation ceremony count toward the Medical Exempti |
| C1 | contradiction | CONTRADICTION | NOT_FOUND | ❌ | What attendance percentage does a student need to maintain to continue receiving |
| C2 | contradiction | CONTRADICTION | CONTRADICTION | ✅ | How much is the late fee if I pay my tuition fee one week late? |
| C3 | contradiction | CONTRADICTION | CONTRADICTION | ✅ | What time is the hostel curfew? |
| U4 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | If I represent my city (not the Institute) in a personal, non-Institute-affiliat |
| U5 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | Does the Medical Exemption's attendance denominator adjustment (Section 7.2) sti |
| U6 | unanswerable | NOT_FOUND | ANSWERED | ❌ | If a Merit Scholarship recipient's CGPA drops because they took a Medical Leave  |
| U7 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | Can a student challenge an Academic Integrity Committee's finding through the Gr |
| U8 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | If a student is expelled under Section 6.4 for a second academic integrity viola |
| U9 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | Does a Society event that runs past 9:00 PM on a Saturday need the same Dean app |
| U10 | unanswerable | NOT_FOUND | ANSWERED | ❌ | Can a first-year student, who hasn't completed two semesters yet, be elected as  |
| U11 | unanswerable | NOT_FOUND | ERROR | ❌ | If the Council Treasurer (an appointed, not elected, position) resigns mid-year, |
| U12 | unanswerable | NOT_FOUND | ERROR | ❌ | Is there a limit on how many different Societies a single student can hold an of |
| U13 | unanswerable | NOT_FOUND | ERROR | ❌ | If I take a Medical Leave of Absence for a semester, how is my CGPA-based schola |
| U14 | unanswerable | NOT_FOUND | ERROR | ❌ | Does the attendance policy have any different provisions for international stude |
| U15 | unanswerable | NOT_FOUND | ERROR | ❌ | Can a student on Academic Probation still hold a leadership position within a So |
| U16 | unanswerable | NOT_FOUND | ERROR | ❌ | Does the Institute provide extra time or accommodations during examinations for  |
| U17 | unanswerable | NOT_FOUND | ERROR | ❌ | Can a student doing a credit-bearing final-semester internship under Section 16. |
| U18 | unanswerable | NOT_FOUND | ERROR | ❌ | If a Warden refuses to grant a student a Night-Out Pass, can the student appeal  |
| U19 | unanswerable | NOT_FOUND | ERROR | ❌ | Are hostel residents permitted to keep pets in their rooms? |
| U20 | unanswerable | NOT_FOUND | ERROR | ❌ | What happens if a demand draft submitted for fee payment is dishonoured or bounc |
| U21 | unanswerable | NOT_FOUND | ERROR | ❌ | If a scholarship recipient graduates early under Section 14.3, is any remaining  |
| U22 | unanswerable | NOT_FOUND | ERROR | ❌ | Does a national-level esports achievement qualify a student for a Sports Scholar |
| U23 | unanswerable | NOT_FOUND | ERROR | ❌ | If I'm approved for the two-installment tuition payment plan and then miss the s |
| U24 | unanswerable | NOT_FOUND | ERROR | ❌ | Can a Society use part of its Student Activity Fund allocation to pay a stipend  |
| U25 | unanswerable | NOT_FOUND | ERROR | ❌ | If two Societies want to co-host a single event and split the funding request, h |
| U26 | unanswerable | NOT_FOUND | ERROR | ❌ | If a student qualifies for both a Merit Scholarship and a Sports Scholarship in  |
| U27 | unanswerable | NOT_FOUND | ERROR | ❌ | If a hostel resident switches from the "with mess" plan to the "without mess" pl |
| U28 | unanswerable | NOT_FOUND | ERROR | ❌ | If two candidates receive the exact same number of votes in a Council election,  |

## Full answers and citations

### A1 — What is the minimum attendance percentage required to sit for the end-semester exam, according to Section 3?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: Section 3 sets the minimum attendance at 75% of classes for a student to be eligible to sit for the End‑Semester Examination.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`7f84e49b1bf4`)
- Reasoning: The passage explicitly states a 75% attendance floor for exam eligibility, directly answering the question.

### A2 — What is the minimum CGPA a student must maintain to avoid being placed on Academic Probation?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: A student must maintain a CGPA of at least 5.0 to avoid being placed on Academic Probation.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 5: Minimum CGPA and Academic Probation (`648424e1de6f`); regulations.md / Institute of Applied Sciences and Technology > Appendix A: Definitions (`7b01c9aa83ea`)
- Reasoning: Section 5.1 and 5.2 explicitly state the 5.0 CGPA threshold for good standing and for avoiding probation, and no conflicting passages were found.

### A3 — Within how many working days of result declaration can a student request revaluation of an answer script?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: A student can request revaluation of an End‑Semester Examination answer script within seven working days of the result declaration.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 4: Internal Assessment and Grading (`21dd08400f0a`)
- Reasoning: Section 4.4 explicitly states the revaluation request must be made within seven working days of result declaration, providing a direct answer.

### A4 — What is the tuition fee for a UG student in the Odd semester of 2025-26?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: The tuition fee for an undergraduate (UG) student in the Odd semester of the 2025‑26 academic year is ₹1,25,000 per semester.
- Citations: fee_deadlines.md / Fee Schedule — Academic Year 2025–26 > Odd Semester (July–December 2025) (`1a65b79b837d`)
- Reasoning: The fee schedule table for the Odd semester explicitly lists the tuition fee for all UG students as ₹1,25,000, directly answering the question.

### A5 — Can a guest stay overnight in a student's hostel room?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: No. Overnight stays by guests are not permitted in student rooms under any circumstances; guests may only visit common areas during designated hours.
- Citations: hostel_policy.pdf / 1. Scope > 4. Guest Policy (`e9fbe82eaf40`)
- Reasoning: The Guest Policy explicitly states that overnight stays by guests are prohibited in student rooms, directly answering the question.

### A6 — How many founding members are required to register a new student Society?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: A new student Society must have at least fifteen founding members to be eligible for registration.
- Citations: student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 4: Recognition of Societies (`e6e84fd0a5c6`)
- Reasoning: Article 4.1 explicitly states the requirement of a list of at least fifteen founding members for a new Society seeking recognition.

### A7 — Can a student report ragging anonymously?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: Yes. A student may report ragging anonymously through the Institute's helpline, and any disclosed identity is protected as far as the law allows.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 17: Anti-Ragging and Student Conduct (`399dc4e07579`)
- Reasoning: Section 17.3 explicitly states that ragging reports can be made anonymously, directly answering the question.

### A8 — What CGPA must a Merit Scholarship recipient maintain to continue receiving it?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: A Merit Scholarship recipient must maintain a cumulative GPA of at least 8.0 to continue receiving the scholarship.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 8: Scholarships and Financial Aid (`802711830ef4`)
- Reasoning: Section 8.2 explicitly states the required CGPA for Merit Scholarship continuation, and no contradictory information is present.

### A9 — If a student arrives late to an exam, after how many minutes will they not be allowed to enter?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: A student who arrives more than 30 minutes after the start of an examination will not be permitted to enter the examination hall.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 10: Examination Conduct (`2db4b4308c88`)
- Reasoning: The passage explicitly states the 30‑minute threshold for late entry, directly answering the question with no conflicting information.

### A10 — What is the maximum permitted duration of the B.Tech programme, including medical leave?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: The maximum permitted duration of the B.Tech programme, including any Medical Leave of Absence, is fourteen semesters.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 14: Degree Requirements and Duration (`f62cbdd6b50d`)
- Reasoning: The passage explicitly states the maximum permitted duration, including medical leave, is fourteen semesters, with no conflicting information.

### A11 — What happens to my exam eligibility if I miss classes because I had to attend my sister's wedding out of town?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: Missing classes for your sister's wedding is considered a personal/family function, which is not covered by the attendance‑condonation provisions. Therefore you must still achieve at least 75% attendance; if you fall below that you will be awarded an “I” (Ineligible) grade for the End‑Semester Examination and will not be allowed to sit the exam.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`1c610bf397aa`); regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`4b7fb2c9120d`)
- Reasoning: The passages explicitly state that family functions/personal travel are not eligible for attendance condonation (3.5) and that falling below 75% attendance results in an "I" grade (3.3), directly answering the question.

### A12 — Can I get my attendance shortfall condoned if I was traveling internationally for personal reasons during the semester?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: No. The regulations state there is no provision for condoning attendance shortfalls that arise from personal travel (or similar private commitments) unless they fall under the specific exceptions listed in Section 3.4 or the Medical Exemption Clause. Personal international travel is therefore not eligible for attendance condonation.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`4b7fb2c9120d`); regulations.md / Institute of Applied Sciences and Technology > Section 7: Medical Exemption and Leave of Absence (`ddbfe13d9f01`)
- Reasoning: The passages explicitly say personal travel is not covered for condonation, providing a direct answer to the question.

### A13 — Does attending my sibling's graduation ceremony count toward the Medical Exemption Clause?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: No. Attending a sibling's graduation is a family function and is not covered by the Medical Exemption Clause. Such events are treated under Section 3.5 and do not qualify for attendance‑denominator adjustment.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`4b7fb2c9120d`); regulations.md / Institute of Applied Sciences and Technology > Section 7: Medical Exemption and Leave of Absence (`ddbfe13d9f01`)
- Reasoning: The passages explicitly state that family functions and personal travel are not covered by the Medical Exemption Clause and are governed by Section 3.5, which does not allow attendance adjustment.

### C1 — What attendance percentage does a student need to maintain to continue receiving their scholarship?
- Expected: `CONTRADICTION` | Actual: `NOT_FOUND` | FAIL
- Answer: Internal error: the model's response could not be parsed as valid JSON. Treating as unanswered for safety.
- Reasoning: JSON parse error: Unterminated string starting at: line 6 column 6 (char 619). Raw output: {
  "state": "CONTRADICTION",
  "answer": "One passage states that a student must maintain at least 75% attendance (Section 3.2) to be eligible for examinations, which is the attendance floor referenced for scholarship standing. Another passage says the Scholarship Committee applies an attendance re

### C2 — How much is the late fee if I pay my tuition fee one week late?
- Expected: `CONTRADICTION` | Actual: `CONTRADICTION` | PASS
- Answer: One source says the late fee is 2% of the total outstanding tuition fee for each week of delay (compounded weekly), while another source says the late fee is a flat charge of ₹500 per week (or part thereof). Both statements apply to a one‑week delay, but they conflict.
- Citations: fee_deadlines.md / Fee Schedule — Academic Year 2025–26 > Late Payment Policy (`91646c01c019`); regulations.md / Institute of Applied Sciences and Technology > Section 9: Fee Payment (`ffdf2c1521bd`)
- Reasoning: Two passages address the same question (late fee for a week) but give different calculation methods, creating a direct contradiction.

### C3 — What time is the hostel curfew?
- Expected: `CONTRADICTION` | Actual: `CONTRADICTION` | PASS
- Answer: One passage says the hostel curfew is 10:00 PM, while another passage says the standard hostel curfew is 11:00 PM.
- Citations: hostel_policy.pdf / 1. Scope > 5. Curfew and Night-Out Policy (`0df2d590f007`); hostel_policy.pdf / 1. Scope (`e4df0dc08fd2`)
- Reasoning: Two passages address the same question (hostel curfew time) but give different times (10:00 PM vs 11:00 PM), creating a direct contradiction.

### U4 — If I represent my city (not the Institute) in a personal, non-Institute-affiliated hackathon, can that count as grounds for attendance condonation?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The regulations only allow attendance condonation for Institute‑sanctioned activities (e.g., Institute sporting or cultural events, placement interviews, bereavement) as stated in Section 3.4, and explicitly state there is no provision for personal travel, family functions, or private commitments not covered by Section 3.4 (Section 3.5). A personal, non‑Institute‑affiliated hackathon representing your city does not fall under any of these listed categories, so the passages do not address it as grounds for condonation.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`db4b1eebaf7b`); regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`4b7fb2c9120d`)
- Reasoning: No passage directly covers attendance condonation for a personal, non‑Institute hackathon; the relevant sections only list Institute‑sanctioned events and exclude private commitments.

### U5 — Does the Medical Exemption's attendance denominator adjustment (Section 7.2) still apply if the medical absence happens during the Summer Term?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The regulations do not explicitly state whether the attendance denominator adjustment described in Section 7.2 applies to a medical absence that occurs during the Summer Term. Section 13.2 says Summer Term attendance follows Section 3 in full, and Section 7.2 describes the adjustment for a semester, but there is no direct provision linking the two for the Summer Term.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 7: Medical Exemption and Leave of Absence (`be8fcc04d012`); regulations.md / Institute of Applied Sciences and Technology > Section 13: Summer Term (`f0b3fccc4058`); regulations.md / Institute of Applied Sciences and Technology > Appendix B: Cross-Reference Notes for Administrative Staff (`fad757c23ee9`)
- Reasoning: No passage directly addresses the applicability of the Section 7.2 denominator adjustment to Summer Term situations; the relevant sections discuss each provision separately without linking them.

### U6 — If a Merit Scholarship recipient's CGPA drops because they took a Medical Leave of Absence semester, does the scholarship get paused rather than permanently lost?
- Expected: `NOT_FOUND` | Actual: `ANSWERED` | FAIL
- Answer: No. According to the regulations, a Merit Scholarship recipient must keep a CGPA of at least 8.0. If the CGPA falls below 8.0 in any semester, the scholarship is lost for the next semester, though the student may reapply once the CGPA rises again. There is no provision that the scholarship is merely paused because the drop was due to a medical leave of absence.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 8: Scholarships and Financial Aid (`802711830ef4`); regulations.md / Institute of Applied Sciences and Technology > Section 12: Committee Powers and Waivers (`12.3`)
- Reasoning: Section 8.2 explicitly states that a Merit Scholarship is lost if CGPA drops below 8.0, with no mention of a pause; thus the question is directly answered.

### U7 — Can a student challenge an Academic Integrity Committee's finding through the Grievance Redressal Committee (Section 11) instead of the procedural review in Section 6.5?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The regulations give a specific procedural review process for Academic Integrity Committee decisions in Section 6.5, and Section 11 on Grievance Redressal only covers certain academic grievances such as grading disputes beyond Section 4.4/4.5, harassment and discrimination. It does not provide a mechanism to challenge an Academic Integrity Committee finding through the Grievance Redressal Committee. Therefore, the scenario of using the GRC instead of the Section 6.5 procedural review is not addressed in the provided passages.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 6: Academic Integrity (`93821ee225e2`); regulations.md / Institute of Applied Sciences and Technology > Section 11: Grievance Redressal (`e0de5e77f3df`)
- Reasoning: No passage explicitly allows a student to use the Grievance Redressal Committee to challenge an Academic Integrity Committee finding; only Section 6.5 provides a review route, so the question is not covered.

### U8 — If a student is expelled under Section 6.4 for a second academic integrity violation, can they ever reapply for admission in a future year?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The regulations specify that a second proven instance of academic dishonesty results in expulsion (Section 6.4) and that there is no appeal provision beyond a procedural review (Section 6.5). However, none of the provided passages contain any rule or provision that addresses whether a expelled student may reapply for admission in a later year. Therefore, the specific question of re‑application after expulsion is not covered by the given regulations.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 6: Academic Integrity (`93821ee225e2`); regulations.md / Institute of Applied Sciences and Technology > Section 6: Academic Integrity (`93821ee225e2`)
- Reasoning: The passages describe expulsion and lack of appeal but do not mention any mechanism for future re‑application, so the scenario is not addressed.

### U9 — Does a Society event that runs past 9:00 PM on a Saturday need the same Dean approval as a weekday event under Article 6.4?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: Article 6.4 explicitly requires Dean of Student Affairs approval only for Society events that extend past 9:00 PM on a weekday. The constitution does not contain any provision that extends this requirement to events on Saturdays, so the specific scenario of a Saturday event past 9:00 PM is not addressed.
- Citations: student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 6: Events and External Sponsorship (`c9ee7ef67626`)
- Reasoning: The passage covers weekday events only and provides no rule for Saturday events; therefore the question is not answered by the given texts.

### U10 — Can a first-year student, who hasn't completed two semesters yet, be elected as a Class Representative?
- Expected: `NOT_FOUND` | Actual: `ANSWERED` | FAIL
- Answer: Yes. The two‑semester completion rule applies only to the General, Cultural, Technical and Sports Secretary positions; the Constitution does not impose any semester‑completion requirement for Class Representatives, so a first‑year student can be elected as a Class Representative.
- Citations: student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 2: Council Composition (`509d7526a89f`)
- Reasoning: The passage explicitly states the two‑semester eligibility applies to the other Council offices, and provides no restriction for Class Representatives, directly answering the question.

### U11 — If the Council Treasurer (an appointed, not elected, position) resigns mid-year, who fills the vacancy and how?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196972, Requested 4464. Please try again in 10m20.352s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196972, Requested 4464. Please try again in 10m20.352s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U12 — Is there a limit on how many different Societies a single student can hold an office-bearer position in at the same time?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196971, Requested 4251. Please try again in 8m47.904s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196971, Requested 4251. Please try again in 8m47.904s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U13 — If I take a Medical Leave of Absence for a semester, how is my CGPA-based scholarship eligibility calculated for the semester right after I return?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196970, Requested 4558. Please try again in 11m0.096s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196970, Requested 4558. Please try again in 11m0.096s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U14 — Does the attendance policy have any different provisions for international students who may have visa-related travel obligations?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196968, Requested 4033. Please try again in 7m12.432s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196968, Requested 4033. Please try again in 7m12.432s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U15 — Can a student on Academic Probation still hold a leadership position within a Society that isn't a Council office (e.g., a Society's internal head, not a Council Secretary)?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196967, Requested 4732. Please try again in 12m13.968s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196967, Requested 4732. Please try again in 12m13.968s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U16 — Does the Institute provide extra time or accommodations during examinations for students with disabilities?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196966, Requested 4089. Please try again in 7m35.76s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196966, Requested 4089. Please try again in 7m35.76s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U17 — Can a student doing a credit-bearing final-semester internship under Section 16.1 also register for regular, non-internship courses in that same semester?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196965, Requested 4491. Please try again in 10m28.992s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196965, Requested 4491. Please try again in 10m28.992s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U18 — If a Warden refuses to grant a student a Night-Out Pass, can the student appeal that specific refusal?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196963, Requested 4718. Please try again in 12m6.191999999s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196963, Requested 4718. Please try again in 12m6.191999999s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U19 — Are hostel residents permitted to keep pets in their rooms?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196962, Requested 4340. Please try again in 9m22.464s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196962, Requested 4340. Please try again in 9m22.464s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U20 — What happens if a demand draft submitted for fee payment is dishonoured or bounces?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196961, Requested 4689. Please try again in 11m52.8s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196961, Requested 4689. Please try again in 11m52.8s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U21 — If a scholarship recipient graduates early under Section 14.3, is any remaining scholarship amount paid out or forfeited?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196960, Requested 4691. Please try again in 11m53.232s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196960, Requested 4691. Please try again in 11m53.232s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U22 — Does a national-level esports achievement qualify a student for a Sports Scholarship under Section 8.1?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196958, Requested 4780. Please try again in 12m30.816s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196958, Requested 4780. Please try again in 12m30.816s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U23 — If I'm approved for the two-installment tuition payment plan and then miss the second installment, does the provisional cancellation process in Section 9.3 apply the same way as it would to a normal missed payment?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196957, Requested 4753. Please try again in 12m18.72s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196957, Requested 4753. Please try again in 12m18.72s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U24 — Can a Society use part of its Student Activity Fund allocation to pay a stipend or honorarium to a guest speaker?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196956, Requested 4568. Please try again in 10m58.368s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196956, Requested 4568. Please try again in 10m58.368s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U25 — If two Societies want to co-host a single event and split the funding request, how is the ₹50,000 approval threshold in Article 5.3 applied -- per Society or per event?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196954, Requested 4586. Please try again in 11m5.28s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196954, Requested 4586. Please try again in 11m5.28s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U26 — If a student qualifies for both a Merit Scholarship and a Sports Scholarship in the same semester, can they receive both at once?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196953, Requested 4466. Please try again in 10m13.007999999s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196953, Requested 4466. Please try again in 10m13.007999999s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U27 — If a hostel resident switches from the "with mess" plan to the "without mess" plan partway through a semester, is any portion of the mess fee refunded or adjusted?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196951, Requested 4869. Please try again in 13m6.24s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196951, Requested 4869. Please try again in 13m6.24s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

### U28 — If two candidates receive the exact same number of votes in a Council election, how is the tie broken?
- Expected: `NOT_FOUND` | Actual: `ERROR` | FAIL
- Answer: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196950, Requested 4575. Please try again in 10m58.8s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
- Reasoning: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kv6f03mzfed9b4y81nrzfwcc` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196950, Requested 4575. Please try again in 10m58.8s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
