# Evaluation Results

**Overall: 35/41 correct**

- answerable: 9/13
- contradiction: 3/3
- unanswerable: 23/25

## Detail

| ID | Bucket | Expected | Actual | Result | Question |
|---|---|---|---|---|---|
| A1 | answerable | ANSWERED | ANSWERED | ✅ | What is the minimum attendance percentage required to sit for the end-semester e |
| A2 | answerable | ANSWERED | NOT_FOUND | ❌ | What is the minimum CGPA a student must maintain to avoid being placed on Academ |
| A3 | answerable | ANSWERED | ANSWERED | ✅ | Within how many working days of result declaration can a student request revalua |
| A4 | answerable | ANSWERED | NOT_FOUND | ❌ | What is the tuition fee for a UG student in the Odd semester of 2025-26? |
| A5 | answerable | ANSWERED | ANSWERED | ✅ | Can a guest stay overnight in a student's hostel room? |
| A6 | answerable | ANSWERED | ANSWERED | ✅ | How many founding members are required to register a new student Society? |
| A7 | answerable | ANSWERED | NOT_FOUND | ❌ | Can a student report ragging anonymously? |
| A8 | answerable | ANSWERED | NOT_FOUND | ❌ | What CGPA must a Merit Scholarship recipient maintain to continue receiving it? |
| A9 | answerable | ANSWERED | ANSWERED | ✅ | If a student arrives late to an exam, after how many minutes will they not be al |
| A10 | answerable | ANSWERED | ANSWERED | ✅ | What is the maximum permitted duration of the B.Tech programme, including medica |
| A11 | answerable | ANSWERED | ANSWERED | ✅ | What happens to my exam eligibility if I miss classes because I had to attend my |
| A12 | answerable | ANSWERED | ANSWERED | ✅ | Can I get my attendance shortfall condoned if I was traveling internationally fo |
| A13 | answerable | ANSWERED | ANSWERED | ✅ | Does attending my sibling's graduation ceremony count toward the Medical Exempti |
| C1 | contradiction | CONTRADICTION | CONTRADICTION | ✅ | What attendance percentage does a student need to maintain to continue receiving |
| C2 | contradiction | CONTRADICTION | CONTRADICTION | ✅ | How much is the late fee if I pay my tuition fee one week late? |
| C3 | contradiction | CONTRADICTION | CONTRADICTION | ✅ | What time is the hostel curfew? |
| U4 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | If I represent my city (not the Institute) in a personal, non-Institute-affiliat |
| U5 | unanswerable | NOT_FOUND | ANSWERED | ❌ | Does the Medical Exemption's attendance denominator adjustment (Section 7.2) sti |
| U6 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | If a Merit Scholarship recipient's CGPA drops because they took a Medical Leave  |
| U7 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | Can a student challenge an Academic Integrity Committee's finding through the Gr |
| U8 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | If a student is expelled under Section 6.4 for a second academic integrity viola |
| U9 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | Does a Society event that runs past 9:00 PM on a Saturday need the same Dean app |
| U10 | unanswerable | NOT_FOUND | ANSWERED | ❌ | Can a first-year student, who hasn't completed two semesters yet, be elected as  |
| U11 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | If the Council Treasurer (an appointed, not elected, position) resigns mid-year, |
| U12 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | Is there a limit on how many different Societies a single student can hold an of |
| U13 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | If I take a Medical Leave of Absence for a semester, how is my CGPA-based schola |
| U14 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | Does the attendance policy have any different provisions for international stude |
| U15 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | Can a student on Academic Probation still hold a leadership position within a So |
| U16 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | Does the Institute provide extra time or accommodations during examinations for  |
| U17 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | Can a student doing a credit-bearing final-semester internship under Section 16. |
| U18 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | If a Warden refuses to grant a student a Night-Out Pass, can the student appeal  |
| U19 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | Are hostel residents permitted to keep pets in their rooms? |
| U20 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | What happens if a demand draft submitted for fee payment is dishonoured or bounc |
| U21 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | If a scholarship recipient graduates early under Section 14.3, is any remaining  |
| U22 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | Does a national-level esports achievement qualify a student for a Sports Scholar |
| U23 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | If I'm approved for the two-installment tuition payment plan and then miss the s |
| U24 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | Can a Society use part of its Student Activity Fund allocation to pay a stipend  |
| U25 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | If two Societies want to co-host a single event and split the funding request, h |
| U26 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | If a student qualifies for both a Merit Scholarship and a Sports Scholarship in  |
| U27 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | If a hostel resident switches from the "with mess" plan to the "without mess" pl |
| U28 | unanswerable | NOT_FOUND | NOT_FOUND | ✅ | If two candidates receive the exact same number of votes in a Council election,  |

## Full answers and citations

### A1 — What is the minimum attendance percentage required to sit for the end-semester exam, according to Section 3?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: A student must maintain at least 75% attendance in a course to sit for the end-semester exam.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`7f84e49b1bf4`)
- Reasoning: Section 3.2 directly states the 75% attendance requirement for examination eligibility, and no other passage contradicts this specific value.

### A2 — What is the minimum CGPA a student must maintain to avoid being placed on Academic Probation?
- Expected: `ANSWERED` | Actual: `NOT_FOUND` | FAIL
- Answer: 
- Reasoning: 

### A3 — Within how many working days of result declaration can a student request revaluation of an answer script?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: A student may request revaluation of an End-Semester Examination answer script within seven working days of result declaration.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 4: Internal Assessment and Grading (`21dd08400f0a`)
- Reasoning: Section 4.4 of the regulations directly states the timeframe for requesting revaluation.

### A4 — What is the tuition fee for a UG student in the Odd semester of 2025-26?
- Expected: `ANSWERED` | Actual: `NOT_FOUND` | FAIL
- Answer: 
- Reasoning: 

### A5 — Can a guest stay overnight in a student's hostel room?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: Overnight stays by guests are not permitted in student rooms under any circumstances.
- Citations: hostel_policy.pdf / 1. Scope > 4. Guest Policy (`e9fbe82eaf40`)
- Reasoning: Section 4.2 of the Hostel Policy explicitly states that overnight stays by guests are not permitted in student rooms.

### A6 — How many founding members are required to register a new student Society?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: A new student Society must have at least fifteen founding members to register.
- Citations: student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 4: Recognition of Societies (`e6e84fd0a5c6`)
- Reasoning: Article 4.1 of the Constitution of the Institute Student Council and Affiliated Societies explicitly states the requirement for at least fifteen founding members.

### A7 — Can a student report ragging anonymously?
- Expected: `ANSWERED` | Actual: `NOT_FOUND` | FAIL
- Answer: 
- Reasoning: 

### A8 — What CGPA must a Merit Scholarship recipient maintain to continue receiving it?
- Expected: `ANSWERED` | Actual: `NOT_FOUND` | FAIL
- Answer: 
- Reasoning: 

### A9 — If a student arrives late to an exam, after how many minutes will they not be allowed to enter?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: A student arriving more than 30 minutes after the start of an examination will not be permitted to enter the examination hall.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 10: Examination Conduct (`2db4b4308c88`)
- Reasoning: Section 10.3 of the regulations directly states the threshold for late entry to an examination.

### A10 — What is the maximum permitted duration of the B.Tech programme, including medical leave?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: The maximum permitted duration of the B.Tech programme, including Medical Leave of Absence, is fourteen semesters.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 14: Degree Requirements and Duration (`f62cbdd6b50d`)
- Reasoning: Section 14.1 of the regulations directly states the maximum permitted duration of the B.Tech programme, including Medical Leave of Absence.

### A11 — What happens to my exam eligibility if I miss classes because I had to attend my sister's wedding out of town?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: If you miss classes due to attending your sister's wedding out of town, you will not be eligible for attendance condonation under Section 3.4, as it only covers circumstances beyond your control such as bereavement or Institute-sanctioned events. Therefore, you must maintain at least 75% attendance to sit the End-Semester Examination.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`db4b1eebaf7b`); regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`4b7fb2c9120d`)
- Reasoning: Section 3.4 explicitly states that condonation is only granted for circumstances beyond the student's control, such as bereavement or Institute-sanctioned events, and does not include personal travel or family functions.

### A12 — Can I get my attendance shortfall condoned if I was traveling internationally for personal reasons during the semester?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: No, attendance shortfalls arising from personal travel, including international travel, are not eligible for condonation under the Institute's regulations.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`4b7fb2c9120d`)
- Reasoning: Section 3.5 explicitly states that personal travel does not qualify for condonation of attendance shortfall.

### A13 — Does attending my sibling's graduation ceremony count toward the Medical Exemption Clause?
- Expected: `ANSWERED` | Actual: `ANSWERED` | PASS
- Answer: Attending a sibling's graduation ceremony does not count toward the Medical Exemption Clause and is not condoned under the attendance requirement.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`4b7fb2c9120d`); regulations.md / Institute of Applied Sciences and Technology > Section 7: Medical Exemption and Leave of Absence (`ddbfe13d9f01`)
- Reasoning: Section 3.5 explicitly states that personal travel and family functions do not qualify for condonation under the Medical Exemption Clause, and Section 7.5 reiterates that leave of absence for family events does not qualify for attendance adjustment.

### C1 — What attendance percentage does a student need to maintain to continue receiving their scholarship?
- Expected: `CONTRADICTION` | Actual: `CONTRADICTION` | PASS
- Answer: The attendance percentage required to continue receiving a scholarship is stated as 75% in Section 3.2, but Section 12.3 incorrectly states it as 80%.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`7f84e49b1bf4`); regulations.md / Institute of Applied Sciences and Technology > Section 12: Committee Powers and Waivers (`7fa31d5deb0d`)
- Reasoning: Section 3.2 directly states the 75% attendance requirement for examination eligibility, which is referenced for scholarship continuation. However, Section 12.3 incorrectly states an 80% requirement, creating a contradiction.

### C2 — How much is the late fee if I pay my tuition fee one week late?
- Expected: `CONTRADICTION` | Actual: `CONTRADICTION` | PASS
- Answer: The late fee is either 2% of the total outstanding fee amount for every week of delay, compounding weekly, or a flat charge of ₹500 per week or part thereof of delay, applied uniformly regardless of the total fee amount outstanding.
- Citations: fee_deadlines.md / Fee Schedule — Academic Year 2025–26 > Late Payment Policy (`91646c01c019`); regulations.md / Institute of Applied Sciences and Technology > Section 9.2 (`ffdf2c152000`)
- Reasoning: 

### C3 — What time is the hostel curfew?
- Expected: `CONTRADICTION` | Actual: `CONTRADICTION` | PASS
- Answer: The hostel curfew is stated to be 11:00 PM in the Scope section, but the Curfew and Night-Out Policy section states that residents must be back by 10:00 PM.
- Citations: hostel_policy.pdf / 1. Scope (`e4df0dc08fd2`); hostel_policy.pdf / 1. Scope > 5. Curfew and Night-Out Policy (`0df2d590f007`)
- Reasoning: The Scope section explicitly states the standard night curfew is 11:00 PM, while the Curfew and Night-Out Policy section states residents must be back by 10:00 PM.

### U4 — If I represent my city (not the Institute) in a personal, non-Institute-affiliated hackathon, can that count as grounds for attendance condonation?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The regulations do not provide for attendance condonation based on participation in personal, non-Institute-affiliated hackathons. The rules only mention condonation for circumstances beyond the student's control, such as Institute-sanctioned events or bereavement, and do not include personal hackathons.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`db4b1eebaf7b`); regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`4b7fb2c9120d`)
- Reasoning: The passages specify that condonation is only granted for circumstances beyond the student's control, such as Institute-sanctioned events or bereavement, and do not mention personal hackathons.

### U5 — Does the Medical Exemption's attendance denominator adjustment (Section 7.2) still apply if the medical absence happens during the Summer Term?
- Expected: `NOT_FOUND` | Actual: `ANSWERED` | FAIL
- Answer: The Medical Exemption's attendance denominator adjustment (Section 7.2) still applies if the medical absence happens during the Summer Term.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 7: Medical Exemption and Leave of Absence (`be8fcc04d012`); regulations.md / Institute of Applied Sciences and Technology > Appendix B: Cross-Reference Notes for Administrative Staff (`f0b3fccc4058`); regulations.md / Institute of Applied Sciences and Technology > Section 7: Medical Exemption and Leave of Absence (`1561fd7b2504`); regulations.md / Institute of Applied Sciences and Technology > Appendix B: Cross-Reference Notes for Administrative Staff (`f0b3fccc4058`); regulations.md / Institute of Applied Sciences and Technology > Section 13: Summer Term (`13.2`)
- Reasoning: Section 7.2 explicitly states the Medical Exemption's attendance denominator adjustment applies, and Section 13.2 confirms that Summer Term follows Section 3 in full, without any indication that Section 7 is excluded.

### U6 — If a Merit Scholarship recipient's CGPA drops because they took a Medical Leave of Absence semester, does the scholarship get paused rather than permanently lost?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The regulations do not specify whether a Merit Scholarship recipient's scholarship is paused or permanently lost if their CGPA drops due to a Medical Leave of Absence semester. The rules cover CGPA requirements and medical leaves separately but do not address the interaction between these two scenarios.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 8: Scholarships and Financial Aid (`802711830ef4`); regulations.md / Institute of Applied Sciences and Technology > Section 7: Medical Exemption and Leave of Absence (`309155b895bb`)
- Reasoning: The passages cover CGPA requirements and medical leaves separately, but do not address the specific scenario of a scholarship recipient's CGPA dropping due to a medical leave of absence.

### U7 — Can a student challenge an Academic Integrity Committee's finding through the Grievance Redressal Committee (Section 11) instead of the procedural review in Section 6.5?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: 
- Reasoning: 

### U8 — If a student is expelled under Section 6.4 for a second academic integrity violation, can they ever reapply for admission in a future year?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The specific scenario of whether a student who misses the second installment of an approved installment plan faces the same provisional cancellation process as a student who misses the first installment is not addressed in the provided passages. The passages cover installment plans and cancellation processes generally but do not specify different rules for missing subsequent installments.
- Citations: regulations.md / Section 2: Registration and Withdrawal Procedures (`a1b2c3d4e5f6`); refund_policy.md / withdrawal_before_classes (`g7h8i9j0k1l2`)
- Reasoning: No passage directly addresses the specific scenario of missing a subsequent installment plan payment and its consequences.

### U9 — Does a Society event that runs past 9:00 PM on a Saturday need the same Dean approval as a weekday event under Article 6.4?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The specific requirement for Dean approval for Society events running past 9:00 PM on a Saturday is not addressed in the provided passages. Article 6.4 only mentions weekday events, and no other passage explicitly covers Saturday events.
- Citations: student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 6: Events and External Sponsorship (`c9ee7ef67626`)
- Reasoning: The passages do not provide a specific rule for Dean approval for events on Saturdays, only for weekdays.

### U10 — Can a first-year student, who hasn't completed two semesters yet, be elected as a Class Representative?
- Expected: `NOT_FOUND` | Actual: `ANSWERED` | FAIL
- Answer: A first-year student who has not completed two semesters yet cannot be elected as a Class Representative.
- Citations: student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 2: Council Composition (`509d7526a89f`)
- Reasoning: Article 2.2 of the Constitution of the Institute Student Council and Affiliated Societies specifies that students must have completed at least two semesters to contest a Council office, which includes the position of Class Representative.

### U11 — If the Council Treasurer (an appointed, not elected, position) resigns mid-year, who fills the vacancy and how?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The specific process for filling a vacancy in the Council Treasurer position mid-year is not covered in the provided passages. The passages discuss the general process for filling vacancies through by-elections but do not specify a unique process for appointed positions like the Council Treasurer.
- Citations: student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 3: Term and Removal (`a08211e137e6`)
- Reasoning: The passages provide general rules for filling vacancies through by-elections but do not specify a unique process for appointed positions like the Council Treasurer.

### U12 — Is there a limit on how many different Societies a single student can hold an office-bearer position in at the same time?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: There is no specific limit stated in the retrieved passages regarding the number of Society office-bearer positions a single student can hold simultaneously.
- Citations: student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 2: Council Composition (`509d7526a89f`); student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 3: Term and Removal (`a08211e137e6`); student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 1: Name and Purpose (`70cdbd9bf59e`); student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies (`9241983c2874`); student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 8: Amendments (`a6f45e3413b0`); student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 4: Recognition of Societies (`e6e84fd0a5c6`); student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 7: Inter-Society Disputes and Grievances (`08b17acd129a`)
- Reasoning: 

### U13 — If I take a Medical Leave of Absence for a semester, how is my CGPA-based scholarship eligibility calculated for the semester right after I return?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The specific calculation method for CGPA-based scholarship eligibility after returning from a Medical Leave of Absence is not directly addressed in the provided regulations. The rules cover general scholarship continuation requirements and medical leave policies but do not specify how scholarship eligibility is calculated for the semester immediately following a medical leave.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 8: Scholarships and Financial Aid (`802711830ef4`); regulations.md / Institute of Applied Sciences and Technology > Section 7: Medical Exemption and Leave of Absence (`309155b895bb`)
- Reasoning: The passages discuss general scholarship requirements and medical leave policies but do not provide specific guidance on how scholarship eligibility is calculated for the semester immediately following a medical leave.

### U14 — Does the attendance policy have any different provisions for international students who may have visa-related travel obligations?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The attendance policy does not have any specific provisions for international students who may have visa-related travel obligations. The policy uniformly applies to all students without distinguishing between domestic and international students.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`7fa31d5deb0d`); regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`d628f2d64786`); regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`4b7fb2c9120d`); regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`7f84e49b1bf4`); regulations.md / Institute of Applied Sciences and Technology > Section 7: Medical Exemption and Leave of Absence (`1561fd7b2504`)
- Reasoning: The retrieved passages do not mention any special provisions for international students with visa-related travel obligations. The attendance policy applies uniformly to all students without differentiation.

### U15 — Can a student on Academic Probation still hold a leadership position within a Society that isn't a Council office (e.g., a Society's internal head, not a Council Secretary)?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The retrieved passages do not specify whether a student on Academic Probation can hold a leadership position within a Society that is not a Council office. The passages cover eligibility for Council offices and general rules for Societies but do not address this specific scenario for Society leadership roles.
- Citations: student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 2: Council Composition (`509d7526a89f`); student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 8: Amendments (`a6f45e3413b0`)
- Reasoning: The passages provide information on eligibility for Council offices and general rules for Societies, but they do not specify the eligibility criteria for leadership positions within Societies that are not Council offices. There is no explicit mention of whether a student on Academic Probation can hold such positions.

### U16 — Does the Institute provide extra time or accommodations during examinations for students with disabilities?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The regulations do not explicitly state whether the Institute provides extra time or accommodations during examinations for students with disabilities. The passages retrieved do not address this specific scenario.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 10: Examination Conduct (`2db4b4308c88`); regulations.md / Institute of Applied Sciences and Technology > Section 16: Internships and Placements (`5bd93d4671db`); hostel_policy.pdf / 1. Scope > 5. Curfew and Night-Out Policy (`0df2d590f007`); regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`1c610bf397aa`); student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 8: Amendments (`a6f45e3413b0`); hostel_policy.pdf / 1. Scope (`e4df0dc08fd2`); regulations.md / Institute of Applied Sciences and Technology > Section 7: Medical Exemption and Leave of Absence (`ddbfe13d9f01`); regulations.md / Institute of Applied Sciences and Technology > Section 7: Medical Exemption and Leave of Absence (`5a75060fea3c`); regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`7f84e49b1bf4`); regulations.md / Institute of Applied Sciences and Technology > Section 7: Medical Exemption and Leave of Absence (`1561fd7b2504`)
- Reasoning: 

### U17 — Can a student doing a credit-bearing final-semester internship under Section 16.1 also register for regular, non-internship courses in that same semester?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The regulations do not specify whether a student doing a credit-bearing final-semester internship can also register for regular, non-internship courses in the same semester. Section 16.1 only mentions the conditions for undertaking a credit-bearing internship but does not address concurrent course registration.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 16: Internship and Project Work (`5bd93d469bca`)
- Reasoning: 

### U18 — If a Warden refuses to grant a student a Night-Out Pass, can the student appeal that specific refusal?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: 
- Reasoning: 

### U19 — Are hostel residents permitted to keep pets in their rooms?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The hostel policy does not explicitly address whether students are permitted to keep pets in their rooms. The handbook covers various aspects of student conduct and living conditions but does not mention pets specifically.
- Citations: hostel_policy.pdf / 1. Scope (`e4df0dc08fd2`); hostel_policy.pdf / 1. Scope > 4. Guest Policy (`e9fbe82eaf40`); hostel_policy.pdf / 1. Scope > 7. Electrical Appliances (`b2ac1b7dc8f9`); hostel_policy.pdf / 1. Scope > 5. Curfew and Night-Out Policy (`0df2d590f007`)
- Reasoning: None of the retrieved passages directly address the issue of keeping pets in hostel rooms.

### U20 — What happens if a demand draft submitted for fee payment is dishonoured or bounces?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: 
- Reasoning: 

### U21 — If a scholarship recipient graduates early under Section 14.3, is any remaining scholarship amount paid out or forfeited?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: 
- Reasoning: 

### U22 — Does a national-level esports achievement qualify a student for a Sports Scholarship under Section 8.1?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: 
- Reasoning: 

### U23 — If I'm approved for the two-installment tuition payment plan and then miss the second installment, does the provisional cancellation process in Section 9.3 apply the same way as it would to a normal missed payment?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The specific scenario of the provisional cancellation process applying to a missed second installment of an approved two-installment tuition payment plan is not addressed in the provided passages. The passages cover general fee payment rules and the consequences of missed payments but do not specify how the provisional cancellation process applies to installment plans.
- Citations: fee_deadlines.md / Fee Schedule — Academic Year 2025–26 > Late Payment Policy (`c02b54469bca`); regulations.md / Institute of Applied Sciences and Technology > Section 2: Academic Calendar and Registration (`9b794a9afd7d`); regulations.md / Institute of Applied Sciences and Technology > Section 16: Internships and Placements (`5bd93d4671db`); regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`4b7fb2c9120d`); regulations.md / Institute of Applied Sciences and Technology > Section 3: Attendance Requirement for Examination Eligibility (`1c610bf397aa`); regulations.md / Institute of Applied Sciences and Technology > Section 12: Committee Powers and Waivers (`9a717e8eb90e`); regulations.md / Institute of Applied Sciences and Technology > Section 4: Internal Assessment and Grading (`21dd08400f0a`); fee_deadlines.md / Fee Schedule — Academic Year 2025–26 > Late Payment Policy (`91646c01c019`); regulations.md / Institute of Applied Sciences and Technology > Section 1: Scope and Applicability (`015cf6a3eb40`)
- Reasoning: The passages provide general rules regarding fee payments, late payments, and the consequences of non-payment, but they do not specify how these rules apply to installment plans or the specific scenario of a missed second installment of an approved installment plan. Therefore, the exact application of the provisional cancellation process to this scenario is not covered.

### U24 — Can a Society use part of its Student Activity Fund allocation to pay a stipend or honorarium to a guest speaker?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The regulations and constitution documents do not specify whether a Society can use part of its Student Activity Fund allocation to pay a stipend or honorarium to a guest speaker. The rules cover various aspects of fund usage and event organization but do not address this specific scenario.
- Citations: student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 5: Student Activity Fund (`80a058464a41`); student_society_constitution.md / Constitution of the Institute Student Council and Affiliated Societies > Article 6: Events and External Sponsorship (`c9ee7ef67626`)
- Reasoning: The passages retrieved do not contain a direct statement regarding the use of Student Activity Fund for paying a stipend or honorarium to a guest speaker.

### U25 — If two Societies want to co-host a single event and split the funding request, how is the ₹50,000 approval threshold in Article 5.3 applied -- per Society or per event?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: 
- Reasoning: 

### U26 — If a student qualifies for both a Merit Scholarship and a Sports Scholarship in the same semester, can they receive both at once?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The regulations do not specify whether a student can receive both a Merit Scholarship and a Sports Scholarship in the same semester. The rules cover individual eligibility criteria for each scholarship type but do not address concurrent receipt of multiple scholarship categories.
- Citations: regulations.md / Institute of Applied Sciences and Technology > Section 8: Scholarships and Financial Aid (`802711830ef4`)
- Reasoning: The passages describe eligibility criteria for Merit Scholarships and Sports Scholarships separately but do not address the possibility of receiving both simultaneously.

### U27 — If a hostel resident switches from the "with mess" plan to the "without mess" plan partway through a semester, is any portion of the mess fee refunded or adjusted?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: 
- Reasoning: 

### U28 — If two candidates receive the exact same number of votes in a Council election, how is the tie broken?
- Expected: `NOT_FOUND` | Actual: `NOT_FOUND` | PASS
- Answer: The Constitution of the Institute Student Council and Affiliated Societies does not specify a procedure for breaking ties in Council elections. The passages retrieved do not address how ties are resolved in elections.
- Citations: None / Constitution of the Institute Student Council and Affiliated Societies > Article 1: Name and Purpose (`509d7526a89a`); None / Constitution of the Institute Student Council and Affiliated Societies > Article 4: Recognition of Societies (`509d7526a89b`); None / Constitution of the Institute Student Council and Affiliated Societies > Article 5: Student Activity Fund (`509d7526a89c`); None / Constitution of the Institute Student Council and Affiliated Societies > Article 6: Events and External Sponsorship (`509d7526a89d`); None / Constitution of the Institute Student Council and Affiliated Societies > Article 7: Inter-Society Disputes and Grievances (`509d7526a89e`); None / Constitution of the Institute Student Council and Affiliated Societies > Article 8: Amendments (`509d7526a89f`); None / Constitution of the Institute Student Council and Affiliated Societies > Article 9: Dissolution (`509d7526a8a0`)
- Reasoning: 
