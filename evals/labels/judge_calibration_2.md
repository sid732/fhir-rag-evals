# Judge calibration: dev-1-judge3

Labeled on 2026-10-30 by Claude Opus 5.5 in five batches of 10, blind to the judge's
verdicts (each batch saw only the rubric and its own items). Each `note:` line is the
labeler's reason.

50 answer sentences. Label each one by the rubric below, then run
`uv run python -m fhir_rag.evals.calibrate score --set judge_calibration_2`. Don't open
`judge_calibration_2.verdicts.jsonl` or the run's report until you're done.

On each `label:` line write `s` (supported), `p` (partially supported) or `n`
(not supported). Add `?` after the letter (`s?`) when the case is unclear to
you; unclear cases are reported apart from clear ones. The sentence being
labeled is in bold inside its whole answer.

The rubric, which the judge's prompt also states:

- Facts about specific entries (names, numbers, units, dates, statuses,
  reasons, how entries relate) must be stated in the cards the sentence cites.
- Claims about the whole record (most recent, latest, first or only one of its
  kind, counts, a complete list, something absent or never done) are checked
  against everything the model saw.
- `s`: every claim passes its check. `p`: the main claim passes, but a detail
  is missing from its evidence or goes beyond it. `n`: the main claim fails or
  the evidence contradicts it; a fact about an entry fails when the sentence
  cites nothing.

## 1. `last-colonoscopy:8d945e28#0#0`

Question: When was the patient's most recent colonoscopy?

Answer: **The patient's most recent colonoscopy was on 2024-07-15 (status completed), performed during a check-up encounter for colon cancer screening.** A prior colonoscopy was completed on 2019-05-18.

Cards this sentence cites:

- `[Procedure/8d945e28-1d8a-bd72-fa00-cb2b98cde6f2]` Procedure | 2024-07-15 | Colonoscopy (procedure) | status completed | SNOMED 73761001
- `[Encounter/8d945e28-1d8a-bd72-a161-8598789128ea]` Encounter | 2024-07-15 | Encounter for check up (procedure) | class AMB | reason: Screening for malignant neoplasm of colon (procedure) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
- `[DocumentReference/88c639eb-a410-4ab2-0de3-1ec2e7c00f9d#2]` Clinical note | 2024-07-15 | part 2 of 2 | # Medications 1 ml epoetin alfa 4000 unt/ml injection [epogen]; acetaminophen 325 mg oral tablet; hydrochlorothiazide 25 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; ibuprofen 200 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - colonoscopy (procedure)

<details><summary>Everything the model saw (39 cards)</summary>

```text
[Condition/8d945e28-1d8a-bd72-9d6c-259e17157c55] Condition | onset 2026-09-07 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8d945e28-1d8a-bd72-3102-64b703ba601c] Condition | onset 2026-07-13 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8d945e28-1d8a-bd72-6b51-0718e8cd7a5e] Condition | onset 2021-01-01 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/8d945e28-1d8a-bd72-db4c-2552d073039a] Condition | onset 2020-11-09 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/8d945e28-1d8a-bd72-ed26-25aa62be033c] Condition | onset 2020-08-18 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/8d945e28-1d8a-bd72-05bf-4b4b02b03fe9] Condition | onset 2018-01-22 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/8d945e28-1d8a-bd72-38fb-c4bf927332c6] Condition | onset 2013-09-16 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/8d945e28-1d8a-bd72-1379-82140e2d1648] Condition | onset 2013-09-16 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/8d945e28-1d8a-bd72-cd47-b95fb1e4464b] Condition | onset 2009-07-06 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/8d945e28-1d8a-bd72-be1a-fb710d842e34] Condition | onset 2009-07-06 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/8d945e28-1d8a-bd72-2a55-0f3c986db8dd] Condition | onset 2009-07-06 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8d945e28-1d8a-bd72-4277-241d976b7354] Condition | onset 2007-06-25 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8d945e28-1d8a-bd72-e0ac-a99a0168ad8a] Condition | onset 2004-06-07 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/8d945e28-1d8a-bd72-a508-e7d1553f7f62] Condition | onset 2004-06-07 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/8d945e28-1d8a-bd72-2622-8fe0a1a30909] Condition | onset 2003-06-02 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8d945e28-1d8a-bd72-12e3-17db162c8f0b] Condition | onset 2001-06-04 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/8d945e28-1d8a-bd72-d01e-086bb9d1d22f] Condition | onset 2001-05-07 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/8d945e28-1d8a-bd72-f5fa-42692b5be159] Condition | onset 1996-08-05 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8d945e28-1d8a-bd72-e601-8e5493910aec] Condition | onset 1981-07-20 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8d945e28-1d8a-bd72-52ca-256d6584412c] Condition | onset 1981-07-20 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8d945e28-1d8a-bd72-d644-66738e889d91] Condition | onset 1977-07-11 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/8d945e28-1d8a-bd72-fbf9-3e6f6bd97f57] Condition | onset 1977-03-07 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/8d945e28-1d8a-bd72-ff5c-41daf21d65a9] MedicationRequest | prescribed 2026-09-07 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/8d945e28-1d8a-bd72-d409-38c0124f2c47] MedicationRequest | prescribed 2026-09-07 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/8d945e28-1d8a-bd72-bcd6-3304c42dca58] MedicationRequest | prescribed 1981-07-27 | Vitamin B12 5 MG/ML Injectable Solution | status active | RxNorm 2001499
[Encounter/8d945e28-1d8a-bd72-016c-9af67d7199fd] Encounter | 2026-09-27 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-3f01-7946bd8f2be1] Encounter | 2026-09-26 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-9dbd-785d1f0e4915] Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Immunization/8d945e28-1d8a-bd72-6a94-32775be2d4e6] Immunization | 2026-01-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Procedure/8d945e28-1d8a-bd72-fa00-cb2b98cde6f2] Procedure | 2024-07-15 | Colonoscopy (procedure) | status completed | SNOMED 73761001
[Procedure/8d945e28-1d8a-bd72-b348-144a6a050f47] Procedure | 2019-05-18 | Colonoscopy (procedure) | status completed | SNOMED 73761001
[DocumentReference/88c639eb-a410-4ab2-0de3-1ec2e7c00f9d#2] Clinical note | 2024-07-15 | part 2 of 2 | # Medications 1 ml epoetin alfa 4000 unt/ml injection [epogen]; acetaminophen 325 mg oral tablet; hydrochlorothiazide 25 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; ibuprofen 200 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - colonoscopy (procedure)
[DocumentReference/9ec79051-94df-9aa9-813c-d2df074b3c81#1] Clinical note | 2019-05-18 | part 1 of 1 | 2019-05-18 # Chief Complaint - Thirst - Fatigue - Hunger # History of Present Illness Tien590 Marcela739 is a 60 year-old nonhispanic white female. Patient has a history of medication review due (situation), chronic periodontitis, generalized, victim of intimate partner abuse (finding), dental caries, unspecified, leukoplakia of oral mucosa, including tongue, part-time employment (finding), acute apical periodontitis of pulpal origin, limited social contact (finding), not in labor force (finding), reports of violence in the environment (finding), full-time employment (finding), stress (finding), social isolation (finding). # Social History Patient is married. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications hydrochlorothiazide 25 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] # Assessment and Plan ## Plan The following procedures were conducted: - colonoscopy (procedure)
[Immunization/8d945e28-1d8a-bd72-28c7-936105552d76] Immunization | 2021-05-17 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/8d945e28-1d8a-bd72-c212-27d34e4b0eef] Immunization | 2021-04-26 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Encounter/8d945e28-1d8a-bd72-a161-8598789128ea] Encounter | 2024-07-15 | Encounter for check up (procedure) | class AMB | reason: Screening for malignant neoplasm of colon (procedure) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-bf7c-5015881d46b9] Encounter | 2019-05-18 | Encounter for check up (procedure) | class AMB | reason: Screening for malignant neoplasm of colon (procedure) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[DocumentReference/39c3ccb8-f3ba-af45-7465-13f2298b9b36#2] Clinical note | 2021-05-10 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose. The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[Encounter/8d945e28-1d8a-bd72-6ff1-449c646d29c6] Encounter | 2020-09-07 | General examination of patient (procedure) | class AMB | at TREE OF LIFE HEALTHCARE ASSOCIATES
```

</details>

label: s
note: Procedure card shows colonoscopy 2024-07-15 completed, and the same-day check-up encounter's reason is screening for malignant neoplasm of colon. The only other colonoscopy seen is 2019-05-18, so 2024-07-15 is the most recent.

## 2. `last-er-visit:8446fe54#0#0`

Question: Why was the patient last seen in the emergency department, and when?

Answer: **The patient was last seen in the emergency department on 2026-01-11 for an emergency room admission with the reason listed as Injury of neck (disorder), at VNA & HOSPICE OF GREATER MILFORD.** The prior emergency room admission was on 2022-03-08 for Myocardial infarction (disorder).

Cards this sentence cites:

- `[Encounter/8446fe54-5b2e-6a46-0c7b-96ece126bd57]` Encounter | 2026-01-11 | Emergency room admission (procedure) | class EMER | reason: Injury of neck (disorder) | at VNA & HOSPICE OF GREATER MILFORD

<details><summary>Everything the model saw (49 cards)</summary>

```text
[Condition/8446fe54-5b2e-6a46-c855-6376bf616037] Condition | onset 2025-10-03 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/8446fe54-5b2e-6a46-3883-408ea2da0a37] Condition | onset 2025-05-15 | Nonproliferative diabetic retinopathy due to type II diabetes mellitus | clinical status active | SNOMED 1551000119108
[Condition/8446fe54-5b2e-6a46-2283-ccf89bdfa001] Condition | onset 2024-09-27 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8446fe54-5b2e-6a46-8ab7-b639a56aa55f] Condition | onset 2023-09-22 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/8446fe54-5b2e-6a46-169f-475724b93b14] Condition | onset 2022-03-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/8446fe54-5b2e-6a46-7c5e-428350d41910] Condition | onset 2022-03-08 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/8446fe54-5b2e-6a46-b854-dbfe1d5848d8] Condition | onset 2019-08-30 | Neuropathy due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 368581000119106
[Condition/8446fe54-5b2e-6a46-9883-d3e4fb3c92c7] Condition | onset 2017-08-18 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8446fe54-5b2e-6a46-90ec-9d5bb7f4215c] Condition | onset 2015-08-07 | Limited social contact (finding) | clinical status active | SNOMED 423315002
[Condition/8446fe54-5b2e-6a46-ac98-749a48641300] Condition | onset 2009-07-27 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/8446fe54-5b2e-6a46-ac45-606071904f4c] Condition | onset 2009-07-03 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/8446fe54-5b2e-6a46-19e1-02a0cca64803] Condition | onset 2009-07-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8446fe54-5b2e-6a46-9731-2ba07e7b3f8a] Condition | onset 2002-05-24 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/8446fe54-5b2e-6a46-5645-a8fdbdfcefa0] Condition | onset 1997-04-25 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8446fe54-5b2e-6a46-6984-e3082708b597] Condition | onset 1997-01-20 | Localized, primary osteoarthritis of the hand (disorder) | clinical status active | SNOMED 201834006
[Condition/8446fe54-5b2e-6a46-918b-8a35802414ef] Condition | onset 1996-11-29 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8446fe54-5b2e-6a46-8453-0b6ddcc40622] Condition | onset 1996-11-29 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/8446fe54-5b2e-6a46-71d0-e1231acfc548] Condition | onset 1996-04-19 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/8446fe54-5b2e-6a46-53e3-b8317bbea5b4] Condition | onset 1973-08-15 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/8446fe54-5b2e-6a46-efe6-1830fbd69235] Condition | onset 1971-06-11 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8446fe54-5b2e-6a46-a0b3-4dfcdfdaffac] Condition | onset 1965-06-04 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8446fe54-5b2e-6a46-26e1-de3ad83381e7] Condition | onset 1965-06-04 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8446fe54-5b2e-6a46-3a03-f8734c3aad20] Condition | onset 1961-05-26 | Received higher education (finding) | clinical status active | SNOMED 224299000
[MedicationRequest/8446fe54-5b2e-6a46-659f-46ecea0cf5ef] MedicationRequest | prescribed 2025-10-04 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8446fe54-5b2e-6a46-88a0-c7dd9e8fc1a1] MedicationRequest | prescribed 2025-10-03 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/8446fe54-5b2e-6a46-7320-4ef7c8ad8f40] MedicationRequest | prescribed 2025-10-03 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/8446fe54-5b2e-6a46-bf69-9fef69e23979] MedicationRequest | prescribed 2022-03-10 | rosuvastatin calcium 10 MG Oral Tablet [Crestor] | status active | RxNorm 859749
[MedicationRequest/8446fe54-5b2e-6a46-4de5-bb23365c2bff] MedicationRequest | prescribed 2022-03-10 | carvedilol 25 MG Oral Tablet | status active | RxNorm 200033
[MedicationRequest/8446fe54-5b2e-6a46-49d9-f1a38344333d] MedicationRequest | prescribed 2022-03-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/8446fe54-5b2e-6a46-3148-e44c765beb21] MedicationRequest | prescribed 2022-03-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/8446fe54-5b2e-6a46-2330-5a6c9a9f35f4] MedicationRequest | prescribed 2022-03-10 | losartan potassium 25 MG Oral Tablet | status active | RxNorm 979485
[MedicationRequest/8446fe54-5b2e-6a46-abfb-29ebed5ed8f5] MedicationRequest | prescribed 2009-07-10 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/8446fe54-5b2e-6a46-a1b3-bc484b4b6e59] MedicationRequest | prescribed 2009-07-10 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/8446fe54-5b2e-6a46-31e7-0fab4c5ed076] MedicationRequest | prescribed 2009-07-10 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/8446fe54-5b2e-6a46-2210-4b4518283f4c] MedicationRequest | prescribed 2009-07-10 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[Encounter/8446fe54-5b2e-6a46-f799-ff1c9d688587] Encounter | 2026-04-10 | Ophthalmic examination and evaluation (procedure) | class AMB | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-7463-6a2732ff7cd0] Encounter | 2026-03-06 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-f36c-8ce8c10cff85] Encounter | 2026-01-11 | Hospital admission (procedure) | class IMP | reason: Patient transfer to skilled nursing facility (procedure) | at CLAFLIN HILL CORPORATION
[Immunization/8446fe54-5b2e-6a46-dae8-760a54add250] Immunization | 2025-10-03 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Encounter/8446fe54-5b2e-6a46-a277-c12ebf90fcd4] Encounter | 2022-03-08 | Emergency room admission (procedure) | class EMER | reason: Myocardial infarction (disorder) | at Fitchburg Outpatient Clinic
[Encounter/8446fe54-5b2e-6a46-0c7b-96ece126bd57] Encounter | 2026-01-11 | Emergency room admission (procedure) | class EMER | reason: Injury of neck (disorder) | at VNA & HOSPICE OF GREATER MILFORD
[Condition/8446fe54-5b2e-6a46-d6d5-0b162f66b9f1] Condition | onset 2013-07-26 | Medication review due (situation) | clinical status resolved | resolved 2017-08-18 | SNOMED 314529007
[Condition/8446fe54-5b2e-6a46-ab3f-1283e0997016] Condition | onset 2023-09-22 | Medication review due (situation) | clinical status resolved | resolved 2023-09-22 | SNOMED 314529007
[Condition/8446fe54-5b2e-6a46-d24f-e5a007a27b81] Condition | onset 2018-08-24 | Medication review due (situation) | clinical status resolved | resolved 2022-09-16 | SNOMED 314529007
[Observation/8446fe54-5b2e-6a46-7295-884fec90ed7a] Observation (survey) | 2023-09-22 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level Somewhat; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Phone; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 58167 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education More than high school; Address 554 Donnelly Dam; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/8446fe54-5b2e-6a46-a5e1-4ce2f8177382] Observation (survey) | 2025-10-03 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level A little bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 1 or 2 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Utilities; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 58167 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education More than high school; Address 554 Donnelly Dam; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/8446fe54-5b2e-6a46-9e43-454ae660a0b2] Observation (survey) | 2024-09-27 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level Not at all; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 58167 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education More than high school; Address 554 Donnelly Dam; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/8446fe54-5b2e-6a46-a409-337b2b0bbf82] Observation (vital-signs) | 2020-09-04 | Heart rate = 85 /min | status final | LOINC 8867-4
[Observation/8446fe54-5b2e-6a46-24cb-72ba3fc3bc07] Observation (vital-signs) | 2025-10-03 | Heart rate = 88 /min | status final | LOINC 8867-4
```

</details>

label: s
note: The EMER encounter on 2026-01-11 has reason Injury of neck at VNA & HOSPICE OF GREATER MILFORD. The only other EMER encounter is 2022-03-08, and the same-day 2026-01-11 hospital admission is class IMP, not ER.

## 3. `latest-lipid-panel:d14e9292#0#0`

Question: What did the patient's most recent lipid panel show?

Answer: **The most recent lipid panel, dated 2025-05-15, showed total cholesterol 154.16 mg/dL, triglycerides 126.13 mg/dL, direct LDL cholesterol 73.93 mg/dL, and HDL cholesterol 55.01 mg/dL.** For comparison, the prior panel on 2022-05-12 showed total cholesterol 157.9 mg/dL, triglycerides 114.8 mg/dL, LDL 81.28 mg/dL, and HDL 53.67 mg/dL.

Cards this sentence cites:

- `[DiagnosticReport/d14e9292-537d-9ab5-247c-23f70af07df4]` DiagnosticReport | 2025-05-15 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 154.16 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 126.13 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 73.93 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 55.01 mg/dL | LOINC 57698-3
- `[Observation/d14e9292-537d-9ab5-d72e-4581e7198e01]` Observation (laboratory) | 2025-05-15 | Cholesterol [Mass/volume] in Serum or Plasma = 154.16 mg/dL | status final | LOINC 2093-3

<details><summary>Everything the model saw (19 cards)</summary>

```text
[Condition/d14e9292-537d-9ab5-d719-3444368e63f2] Condition | onset 2026-07-15 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/d14e9292-537d-9ab5-f5e1-81b5b14a8a8d] Condition | onset 2025-05-15 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/d14e9292-537d-9ab5-3fd5-303fdca87268] Condition | onset 2024-03-30 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/d14e9292-537d-9ab5-2de8-ff9612c4dc80] Condition | onset 2022-05-12 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/d14e9292-537d-9ab5-c205-6c7176a1d8e2] Condition | onset 2013-05-02 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/d14e9292-537d-9ab5-3a99-525060b2d8c3] Condition | onset 2009-04-23 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Encounter/d14e9292-537d-9ab5-75a2-660a8b4ef3eb] Encounter | 2026-07-15 | Admission to surgical department (procedure) | class IMP | reason: Sterilization requested (situation) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-cd48-29e15dfdc267] Encounter | 2026-06-26 | Consultation for treatment (procedure) | class AMB | reason: Sterilization requested (situation) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-a94e-2f619d52ef93] Encounter | 2026-03-12 | Encounter for check up (procedure) | class AMB | reason: Epidermal burn of skin (disorder) | at MOUNT AUBURN HOSPITAL
[DocumentReference/5d7e8894-208a-874e-33ac-3649b0d730b4#2] Clinical note | 2025-05-15 | part 2 of 2 | # Assessment and Plan Patient is presenting with medication review due (situation), full-time employment (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - screening for drug abuse (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - lipid panel with direct ldl - serum or plasma - cbc panel - blood by automated count - generalized anxiety disorder 7 item (gad-7) - patient health questionnaire 2 item (phq-2) [reported] - drug abuse screening test-10 [dast-10]
[DiagnosticReport/d14e9292-537d-9ab5-5472-e0204c5ab213] DiagnosticReport | 2022-05-12 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 157.9 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 114.8 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 81.28 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 53.67 mg/dL | LOINC 57698-3
[DiagnosticReport/d14e9292-537d-9ab5-247c-23f70af07df4] DiagnosticReport | 2025-05-15 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 154.16 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 126.13 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 73.93 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 55.01 mg/dL | LOINC 57698-3
[DocumentReference/be555e47-465e-8f07-752b-9f79ebf5e7be#2] Clinical note | 2022-05-12 | part 2 of 2 | # Assessment and Plan Patient is presenting with victim of intimate partner abuse (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf, td (adult), 5 lf tetanus toxoid, preservative free, adsorbed. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - screening for domestic abuse (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - assessment using alcohol use disorders identification test - consumption (procedure) The following lab reports were completed: - lipid panel with direct ldl - serum or plasma - humiliation, afraid, rape, and kick questionnaire [hark] - patient health questionnaire 2 item (phq-2) [reported] - alcohol use disorder identification test - consumption [audit-c]
[Observation/d14e9292-537d-9ab5-0834-9f04da106253] Observation (vital-signs) | 2025-05-15 | Blood pressure panel with all children optional = Diastolic Blood Pressure 84 mm[Hg]; Systolic Blood Pressure 119 mm[Hg] | status final | LOINC 85354-9
[Observation/d14e9292-537d-9ab5-a42e-7ccbb04852f3] Observation (vital-signs) | 2022-05-12 | Blood pressure panel with all children optional = Diastolic Blood Pressure 83 mm[Hg]; Systolic Blood Pressure 124 mm[Hg] | status final | LOINC 85354-9
[Observation/d14e9292-537d-9ab5-bbb1-3c3764984cc0] Observation (vital-signs) | 2019-05-09 | Blood pressure panel with all children optional = Diastolic Blood Pressure 81 mm[Hg]; Systolic Blood Pressure 122 mm[Hg] | status final | LOINC 85354-9
[DocumentReference/af7300ca-3cc8-004d-c649-db92631cb338#1] Clinical note | 2019-05-09 | part 1 of 1 | 2019-05-09 # Chief Complaint No complaints. # History of Present Illness Onita767 Goldie436 is a 28 year-old nonhispanic white female. Patient has a history of dental caries, part-time employment (finding), acute gingivitis, limited social contact (finding), acute viral pharyngitis (disorder), laceration of hand (disorder), laceration - injury (disorder), normal pregnancy (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Humana. # Allergies No Known Allergies. # Medications naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with medication review due (situation), stress (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - assessment of health and social care needs (procedure) - screening for domestic abuse (procedure) - depression screening (procedure) - depression screening (procedure) The following lab reports were completed: - cbc panel - blood by automated count - humiliation, afraid, rape, and kick questionnaire [hark] - patient health questionnaire 2 item (phq-2) [reported]
[Observation/d14e9292-537d-9ab5-d72e-4581e7198e01] Observation (laboratory) | 2025-05-15 | Cholesterol [Mass/volume] in Serum or Plasma = 154.16 mg/dL | status final | LOINC 2093-3
[Observation/d14e9292-537d-9ab5-dd19-909e7a3ab50d] Observation (laboratory) | 2022-05-12 | Cholesterol [Mass/volume] in Serum or Plasma = 157.9 mg/dL | status final | LOINC 2093-3
```

</details>

label: s
note: The 2025-05-15 lipid panel card lists 154.16, 126.13, 73.93 (direct LDL) and 55.01 mg/dL, exactly as stated. The only other panel is 2022-05-12, so this is the most recent.

## 4. `lay-high-blood-pressure:e56a8cde#0#1`

Question: Has the patient ever been diagnosed with high blood pressure? If so, when?

Answer: Yes, the patient has essential hypertension with onset 1991-06-13, and its clinical status is active. **A clinical note dated 1991-06-13 documents the patient presenting with essential hypertension. The patient was placed on a careplan of lifestyle education regarding hypertension.** Lisinopril 10 MG Oral Tablet, prescribed 2025-12-25, is active with the reason listed as essential hypertension. The most recent blood pressure, on 2025-12-25, was Systolic 106 mm[Hg] and Diastolic 75 mm[Hg].

Cards this sentence cites:

- `[DocumentReference/7504f1c0-58e2-6285-f81f-87337a5ecce1#1]` Clinical note | 1991-06-13 | part 1 of 1 | 1991-06-13 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 46 year-old nonhispanic white male. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicaid. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with essential hypertension (disorder). ## Plan The patient was placed on a careplan: - lifestyle education regarding hypertension (procedure)

<details><summary>Everything the model saw (56 cards)</summary>

```text
[Condition/e56a8cde-8395-a37d-f7ae-15d35f13e9f0] Condition | onset 2025-12-25 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/e56a8cde-8395-a37d-80d3-3984f14d8bb3] Condition | onset 2025-12-25 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/e56a8cde-8395-a37d-5c7c-75429c6f1e56] Condition | onset 2025-12-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/e56a8cde-8395-a37d-354e-df92238c35a7] Condition | onset 2025-12-25 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/e56a8cde-8395-a37d-6690-7ef5746552bd] Condition | onset 2017-11-09 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/e56a8cde-8395-a37d-922a-d32061194c0b] Condition | onset 2016-11-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/e56a8cde-8395-a37d-e775-23849ffbe97b] Condition | onset 2014-02-01 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/e56a8cde-8395-a37d-a82c-6129bc784139] Condition | onset 2014-02-01 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/e56a8cde-8395-a37d-64b8-86023f198a46] Condition | onset 2014-02-01 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/e56a8cde-8395-a37d-e547-8e085bacfa8e] Condition | onset 2007-09-13 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/e56a8cde-8395-a37d-37b4-500cf9e797e9] Condition | onset 2005-09-01 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/e56a8cde-8395-a37d-d5cb-6239a28a0055] Condition | onset 2003-12-16 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/e56a8cde-8395-a37d-4d5f-670d3e1632bc] Condition | onset 2003-12-16 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/e56a8cde-8395-a37d-1853-568436ee1ea2] Condition | onset 2001-08-20 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/e56a8cde-8395-a37d-810b-643d651149ba] Condition | onset 2001-08-18 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/e56a8cde-8395-a37d-2761-7d0bfc799087] Condition | onset 2001-08-09 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/e56a8cde-8395-a37d-ed31-c4144dbefb9e] Condition | onset 1996-05-17 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
[Condition/e56a8cde-8395-a37d-333f-0835bee4de98] Condition | onset 1991-06-13 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/e56a8cde-8395-a37d-30cd-5f4f9de67da3] Condition | onset 1967-07-27 | Lack of access to transportation (finding) | clinical status active | SNOMED 713458007
[Condition/e56a8cde-8395-a37d-ac70-0b466edf16a1] Condition | onset 1963-07-18 | Transport problem (finding) | clinical status active | SNOMED 266934004
[Condition/e56a8cde-8395-a37d-99e6-93fe1e3f6036] Condition | onset 1963-07-18 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/e56a8cde-8395-a37d-0c1b-7da0b396a0c4] MedicationRequest | prescribed 2026-01-01 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/e56a8cde-8395-a37d-f153-06ed5ef5b40a] MedicationRequest | prescribed 2025-12-25 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/e56a8cde-8395-a37d-b70b-d6ff9e66fb91] MedicationRequest | prescribed 2025-12-25 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/e56a8cde-8395-a37d-1cff-386c29158923] MedicationRequest | prescribed 2025-12-25 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/e56a8cde-8395-a37d-f778-f1044e9a8316] MedicationRequest | prescribed 2003-12-16 | atorvastatin 10 MG Oral Tablet | status active | RxNorm 617312
[MedicationRequest/e56a8cde-8395-a37d-e36e-ab680e0ad841] MedicationRequest | prescribed 2003-12-16 | hydrochlorothiazide 25 MG / lisinopril 20 MG Oral Tablet | status active | RxNorm 197887
[MedicationRequest/e56a8cde-8395-a37d-d237-6e376bbcb9a6] MedicationRequest | prescribed 2003-12-16 | metoprolol tartrate 25 MG Oral Tablet | status active | RxNorm 866924
[MedicationRequest/e56a8cde-8395-a37d-2fb4-edeac8b69b00] MedicationRequest | prescribed 2003-12-16 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/e56a8cde-8395-a37d-228f-f6135c165caa] MedicationRequest | prescribed 2003-12-16 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/e56a8cde-8395-a37d-eee1-8d05287f0e29] MedicationRequest | prescribed 2001-08-16 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/e56a8cde-8395-a37d-d36b-2e3fc9df975e] MedicationRequest | prescribed 2001-08-16 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/e56a8cde-8395-a37d-a8c0-f9ed9ed3ea83] MedicationRequest | prescribed 2001-08-16 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/e56a8cde-8395-a37d-321f-ecd1d25263ad] MedicationRequest | prescribed 2001-08-16 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/e56a8cde-8395-a37d-9456-c58ec0c7de32] MedicationRequest | prescribed 1949-01-17 | diphenhydrAMINE Hydrochloride 25 MG Oral Tablet | status active | RxNorm 1049630
[AllergyIntolerance/e56a8cde-8395-a37d-b318-8f34a7d6b5f7] AllergyIntolerance | recorded 1946-06-09 | Animal dander (substance) | allergy, category environment, criticality low | clinical status active | reactions: Eruption of skin (disorder); Rhinoconjunctivitis (disorder) | SNOMED 264287008
[AllergyIntolerance/e56a8cde-8395-a37d-a098-9831a40ac85b] AllergyIntolerance | recorded 1946-06-09 | Mold (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 84489001
[AllergyIntolerance/e56a8cde-8395-a37d-85d4-fe7519012219] AllergyIntolerance | recorded 1946-06-09 | House dust mite (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 260147004
[AllergyIntolerance/e56a8cde-8395-a37d-60c2-b75e4a4d4513] AllergyIntolerance | recorded 1946-06-09 | Tree pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 782576004
[AllergyIntolerance/e56a8cde-8395-a37d-5834-224d1127b6f9] AllergyIntolerance | recorded 1946-06-09 | Grass pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 256277009
[AllergyIntolerance/e56a8cde-8395-a37d-2daa-dbe0dbcf6ecf] AllergyIntolerance | recorded 1946-06-09 | Shellfish (substance) | allergy, category food, criticality low | clinical status active | reactions: Dyspnea (finding); Allergic angioedema (disorder); Itching (finding); Cough (finding); Diarrhea (finding) | SNOMED 735029006
[AllergyIntolerance/e56a8cde-8395-a37d-1508-bdb84bdc4c5d] AllergyIntolerance | recorded 1946-06-09 | Allergic disposition (finding) | allergy, category environment, criticality low | clinical status active | SNOMED 609328004
[Encounter/e56a8cde-8395-a37d-9f47-5b69723a8690] Encounter | 2026-01-01 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Encounter/e56a8cde-8395-a37d-2450-250d53d64dc7] Encounter | 2025-12-25 | General examination of patient (procedure) | class AMB | at SOUTH SHORE PRIMARY CARE PC
[Encounter/e56a8cde-8395-a37d-20eb-f707e34a4164] Encounter | 2024-12-20 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Immunization/e56a8cde-8395-a37d-7cd1-bb3bac5572f3] Immunization | 2025-12-25 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/e56a8cde-8395-a37d-cd94-ac1e06ff3aac] Observation (vital-signs) | 2021-12-02 | Blood pressure panel with all children optional = Diastolic Blood Pressure 73 mm[Hg]; Systolic Blood Pressure 116 mm[Hg] | status final | LOINC 85354-9
[Observation/e56a8cde-8395-a37d-c7f1-f8947e6d7810] Observation (vital-signs) | 2025-12-25 | Blood pressure panel with all children optional = Diastolic Blood Pressure 75 mm[Hg]; Systolic Blood Pressure 106 mm[Hg] | status final | LOINC 85354-9
[Observation/e56a8cde-8395-a37d-9a08-8f6c538f4d3d] Observation (vital-signs) | 2024-12-19 | Blood pressure panel with all children optional = Diastolic Blood Pressure 74 mm[Hg]; Systolic Blood Pressure 108 mm[Hg] | status final | LOINC 85354-9
[Observation/e56a8cde-8395-a37d-17dd-076107990533] Observation (vital-signs) | 2023-12-14 | Blood pressure panel with all children optional = Diastolic Blood Pressure 71 mm[Hg]; Systolic Blood Pressure 112 mm[Hg] | status final | LOINC 85354-9
[DocumentReference/7504f1c0-58e2-6285-f81f-87337a5ecce1#1] Clinical note | 1991-06-13 | part 1 of 1 | 1991-06-13 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 46 year-old nonhispanic white male. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicaid. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with essential hypertension (disorder). ## Plan The patient was placed on a careplan: - lifestyle education regarding hypertension (procedure)
[Condition/e56a8cde-8395-a37d-1815-01a34059f1ca] Condition | onset 2022-12-08 | Stress (finding) | clinical status resolved | resolved 2023-12-14 | SNOMED 73595000
[Condition/e56a8cde-8395-a37d-8f9a-508090a4ffda] Condition | onset 2017-11-09 | Stress (finding) | clinical status resolved | resolved 2018-11-15 | SNOMED 73595000
[DiagnosticReport/e56a8cde-8395-a37d-3f4f-0347df4d9217] DiagnosticReport | 2021-12-02 | CBC panel - Blood by Automated count | results: Leukocytes [#/volume] in Blood by Automated count 4.7251 10*3/uL; Erythrocytes [#/volume] in Blood by Automated count 5.3883 10*6/uL; Hemoglobin [Mass/volume] in Blood 12.046 g/dL; Hematocrit [Volume Fraction] of Blood by Automated count 39.229 %; MCV [Entitic mean volume] in Red Blood Cells by Automated count 80.875 fL; MCH [Entitic mass] by Automated count 32.2 pg; MCHC [Entitic Mass/volume] in Red Blood Cells by Automated count 33.52 g/dL; Erythrocyte [DistWidth] in Blood by Automated count 43.265 fL; Platelets [#/volume] in Blood by Automated count 379.77 10*3/uL; Platelet distribution width [Entitic volume] in Blood by Automated count 472.58 fL; Platelet [Entitic mean volume] in Blood by Automated count 11.132 fL | LOINC 58410-2
[DiagnosticReport/e56a8cde-8395-a37d-4ba2-972e3d1ff301] DiagnosticReport | 2016-11-03 | CBC panel - Blood by Automated count | results: Leukocytes [#/volume] in Blood by Automated count 4.7152 10*3/uL; Erythrocytes [#/volume] in Blood by Automated count 5.4279 10*6/uL; Hemoglobin [Mass/volume] in Blood 17.444 g/dL; Hematocrit [Volume Fraction] of Blood by Automated count 35.356 %; MCV [Entitic mean volume] in Red Blood Cells by Automated count 81.833 fL; MCH [Entitic mass] by Automated count 28.393 pg; MCHC [Entitic Mass/volume] in Red Blood Cells by Automated count 33.537 g/dL; Erythrocyte [DistWidth] in Blood by Automated count 44.311 fL; Platelets [#/volume] in Blood by Automated count 156.23 10*3/uL; Platelet distribution width [Entitic volume] in Blood by Automated count 311.85 fL; Platelet [Entitic mean volume] in Blood by Automated count 9.4606 fL | LOINC 58410-2
[Condition/e56a8cde-8395-a37d-e08a-eebe5956bc62] Condition | onset 2007-09-13 | Medication review due (situation) | clinical status resolved | resolved 2018-11-15 | SNOMED 314529007
```

</details>

label: s
note: The 1991-06-13 note states the patient presented with essential hypertension and was placed on a careplan of lifestyle education regarding hypertension.

## 5. `lay-a-low-red-blood-cell-count:760e0542#0#2`

Question: Has the patient ever been diagnosed with a low red blood cell count? If so, when?

Answer: The record lists Anemia (disorder) with onset 1988-12-28 and clinical status active. The most recent CBC on 2023-10-25 showed an erythrocyte count of 4.0598 10*6/uL and hemoglobin of 12.165 g/dL. **The prior CBC on 2018-10-17 showed an erythrocyte count of 5.0448 10*6/uL and hemoglobin of 13.286 g/dL.**

Cards this sentence cites:

- `[DiagnosticReport/760e0542-9c61-9c1a-141e-8616bcbc05f8]` DiagnosticReport | 2018-10-17 | CBC panel - Blood by Automated count | results: Leukocytes [#/volume] in Blood by Automated count 10.029 10*3/uL; Erythrocytes [#/volume] in Blood by Automated count 5.0448 10*6/uL; Hemoglobin [Mass/volume] in Blood 13.286 g/dL; Hematocrit [Volume Fraction] of Blood by Automated count 45.396 %; MCV [Entitic mean volume] in Red Blood Cells by Automated count 83.058 fL; MCH [Entitic mass] by Automated count 27.103 pg; MCHC [Entitic Mass/volume] in Red Blood Cells by Automated count 33.665 g/dL; Erythrocyte [DistWidth] in Blood by Automated count 40.922 fL; Platelets [#/volume] in Blood by Automated count 416.64 10*3/uL; Platelet distribution width [Entitic volume] in Blood by Automated count 438.94 fL; Platelet [Entitic mean volume] in Blood by Automated count 10.768 fL | LOINC 58410-2
- `[Observation/760e0542-9c61-9c1a-9811-dd5090bc51b5]` Observation (laboratory) | 2018-10-17 | Erythrocytes [#/volume] in Blood by Automated count = 5.0448 10*6/uL | status final | LOINC 789-8

<details><summary>Everything the model saw (44 cards)</summary>

```text
[Condition/760e0542-9c61-9c1a-f014-d96ecb52354b] Condition | onset 2026-09-09 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/760e0542-9c61-9c1a-3909-ca43a58a2be0] Condition | onset 2023-02-08 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/760e0542-9c61-9c1a-0603-33ac04e928e9] Condition | onset 2017-07-26 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/760e0542-9c61-9c1a-7969-97405f2cda90] Condition | onset 2016-09-28 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/760e0542-9c61-9c1a-bc04-975a613f7bef] Condition | onset 2016-05-04 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/760e0542-9c61-9c1a-19fd-96240fc0e3b9] Condition | onset 2016-05-04 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/760e0542-9c61-9c1a-e1cf-d1bcca0d3b69] Condition | onset 2016-03-02 | Familial Alzheimer's disease of early onset (disorder) | clinical status active | SNOMED 230265002
[Condition/760e0542-9c61-9c1a-bf45-3800d10bb908] Condition | onset 2012-09-12 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/760e0542-9c61-9c1a-6a42-9364f5d685e7] Condition | onset 2009-10-14 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/760e0542-9c61-9c1a-6844-45eca3bcbf32] Condition | onset 2009-10-14 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/760e0542-9c61-9c1a-c55b-b73483d412d5] Condition | onset 2004-09-01 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/760e0542-9c61-9c1a-8f20-42b2a944fe6e] Condition | onset 2004-09-01 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/760e0542-9c61-9c1a-426d-1b0e47f6ef3a] Condition | onset 2004-09-01 | Hyperglycemia (disorder) | clinical status active | SNOMED 80394007
[Condition/760e0542-9c61-9c1a-84cc-6ec1252b5c47] Condition | onset 1998-10-12 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/760e0542-9c61-9c1a-d618-c814cd687574] Condition | onset 1998-01-07 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/760e0542-9c61-9c1a-addb-545c11e2d54a] Condition | onset 1998-01-07 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/760e0542-9c61-9c1a-393d-4476d7ede869] Condition | onset 1995-01-04 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/760e0542-9c61-9c1a-0e56-fe029b0a5419] Condition | onset 1990-08-12 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/760e0542-9c61-9c1a-8747-2a2b77e88f89] Condition | onset 1988-12-28 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/760e0542-9c61-9c1a-4f0e-0a94437d4aaa] Condition | onset 1988-12-28 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/760e0542-9c61-9c1a-771f-54deeed066bf] Condition | onset 1982-12-22 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/760e0542-9c61-9c1a-0604-679a8d525bc1] Condition | onset 1981-12-16 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/760e0542-9c61-9c1a-c792-3a8303530414] Condition | onset 1979-12-05 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[Condition/760e0542-9c61-9c1a-1d06-faad5e8f657c] Condition | onset 1974-01-03 | Adolescent idiopathic scoliosis (disorder) | clinical status active | SNOMED 203646004
[MedicationRequest/760e0542-9c61-9c1a-c29f-4c3b83db674e] MedicationRequest | prescribed 2026-09-09 | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 860975
[MedicationRequest/760e0542-9c61-9c1a-096d-4868f9087e48] MedicationRequest | prescribed 2026-09-09 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[MedicationRequest/760e0542-9c61-9c1a-c259-531395abfaa1] MedicationRequest | prescribed 2023-01-14 | 24 HR Donepezil hydrochloride 10 MG / Memantine hydrochloride 28 MG Extended Release Oral Capsule | status active | reason: Familial Alzheimer's disease of early onset (disorder) | RxNorm 1599803
[MedicationRequest/760e0542-9c61-9c1a-fd81-acf11c1ddec0] MedicationRequest | prescribed 1967-04-25 | Chlorpheniramine Maleate 2 MG/ML Oral Solution | status active | RxNorm 477045
[AllergyIntolerance/760e0542-9c61-9c1a-3695-658972edefe5] AllergyIntolerance | recorded 1967-05-01 | Allergic disposition (finding) | allergy, category environment, criticality low | clinical status active | SNOMED 609328004
[AllergyIntolerance/760e0542-9c61-9c1a-1887-b0f58a6117f4] AllergyIntolerance | recorded 1967-05-01 | Lisinopril | intolerance, category medication, criticality low | clinical status active | RxNorm 29046
[Encounter/760e0542-9c61-9c1a-6caa-86123ce8fd48] Encounter | 2026-09-09 | Urgent care clinic (environment) | class AMB | at MIDDLETON FAMILY MEDICINE URGENT CARE, LLC
[Encounter/760e0542-9c61-9c1a-dbc8-3964b3a3c72f] Encounter | 2026-08-05 | Urgent care clinic (environment) | class AMB | at MIDDLETON FAMILY MEDICINE URGENT CARE, LLC
[Encounter/760e0542-9c61-9c1a-d9e8-129c4edf531b] Encounter | 2026-05-27 | Encounter for check up (procedure) | class AMB | at LAWRENCE GENERAL HOSPITAL
[Immunization/760e0542-9c61-9c1a-bb77-51bf2da7f927] Immunization | 2026-04-08 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/760e0542-9c61-9c1a-5e7d-eeb84f171b2c] Observation (laboratory) | 2023-10-25 | Erythrocytes [#/volume] in Blood by Automated count = 4.0598 10*6/uL | status final | LOINC 789-8
[Observation/760e0542-9c61-9c1a-9811-dd5090bc51b5] Observation (laboratory) | 2018-10-17 | Erythrocytes [#/volume] in Blood by Automated count = 5.0448 10*6/uL | status final | LOINC 789-8
[Observation/760e0542-9c61-9c1a-95f6-578052ef3aab] Observation (laboratory) | 2023-10-25 | Erythrocyte [DistWidth] in Blood by Automated count = 45.163 fL | status final | LOINC 788-0
[Observation/760e0542-9c61-9c1a-af5b-5b53f4201ee7] Observation (laboratory) | 2018-10-17 | Erythrocyte [DistWidth] in Blood by Automated count = 40.922 fL | status final | LOINC 788-0
[DiagnosticReport/760e0542-9c61-9c1a-fbc8-1a3815b97d2e] DiagnosticReport | 2023-10-25 | CBC panel - Blood by Automated count | results: Leukocytes [#/volume] in Blood by Automated count 5.3277 10*3/uL; Erythrocytes [#/volume] in Blood by Automated count 4.0598 10*6/uL; Hemoglobin [Mass/volume] in Blood 12.165 g/dL; Hematocrit [Volume Fraction] of Blood by Automated count 49.644 %; MCV [Entitic mean volume] in Red Blood Cells by Automated count 92.3 fL; MCH [Entitic mass] by Automated count 28.774 pg; MCHC [Entitic Mass/volume] in Red Blood Cells by Automated count 35.395 g/dL; Erythrocyte [DistWidth] in Blood by Automated count 45.163 fL; Platelets [#/volume] in Blood by Automated count 202.61 10*3/uL; Platelet distribution width [Entitic volume] in Blood by Automated count 297.62 fL; Platelet [Entitic mean volume] in Blood by Automated count 11.41 fL | LOINC 58410-2
[DiagnosticReport/760e0542-9c61-9c1a-141e-8616bcbc05f8] DiagnosticReport | 2018-10-17 | CBC panel - Blood by Automated count | results: Leukocytes [#/volume] in Blood by Automated count 10.029 10*3/uL; Erythrocytes [#/volume] in Blood by Automated count 5.0448 10*6/uL; Hemoglobin [Mass/volume] in Blood 13.286 g/dL; Hematocrit [Volume Fraction] of Blood by Automated count 45.396 %; MCV [Entitic mean volume] in Red Blood Cells by Automated count 83.058 fL; MCH [Entitic mass] by Automated count 27.103 pg; MCHC [Entitic Mass/volume] in Red Blood Cells by Automated count 33.665 g/dL; Erythrocyte [DistWidth] in Blood by Automated count 40.922 fL; Platelets [#/volume] in Blood by Automated count 416.64 10*3/uL; Platelet distribution width [Entitic volume] in Blood by Automated count 438.94 fL; Platelet [Entitic mean volume] in Blood by Automated count 10.768 fL | LOINC 58410-2
[Observation/760e0542-9c61-9c1a-3a2b-0d5aa1eb48f1] Observation (laboratory) | 2023-10-25 | MCV [Entitic mean volume] in Red Blood Cells by Automated count = 92.3 fL | status final | LOINC 787-2
[Observation/760e0542-9c61-9c1a-8bcd-a183e86cc0c2] Observation (laboratory) | 2018-10-17 | MCV [Entitic mean volume] in Red Blood Cells by Automated count = 83.058 fL | status final | LOINC 787-2
[Observation/760e0542-9c61-9c1a-7071-c03ba19d98b2] Observation (laboratory) | 2020-12-23 | Hemoglobin A1c/Hemoglobin.total in Blood = 3.08 % | status final | LOINC 4548-4
[Observation/760e0542-9c61-9c1a-3e06-3feea0ae61ba] Observation (laboratory) | 2026-09-09 | Hemoglobin A1c/Hemoglobin.total in Blood = 3.08 % | status final | LOINC 4548-4
```

</details>

label: s
note: The 2018-10-17 CBC card shows erythrocytes 5.0448 10*6/uL and hemoglobin 13.286 g/dL. The only CBCs seen are 2023-10-25 and 2018-10-17, so calling it the prior CBC is correct.

## 6. `latest-lipid-panel:772fc930#0#0`

Question: What did the patient's most recent lipid panel show?

Answer: **The most recent lipid panel with direct LDL, dated 2026-03-06, showed total cholesterol 160.13 mg/dL, triglycerides 109.53 mg/dL, direct LDL cholesterol 147.68 mg/dL, and HDL cholesterol 41.761 mg/dL.** At that visit, simvastatin 10 mg oral tablet was prescribed. The prior panel on 2025-02-13 showed total cholesterol 227.41 mg/dL, triglycerides 285.82 mg/dL, LDL 169.29 mg/dL, and HDL 50.134 mg/dL.

Cards this sentence cites:

- `[DiagnosticReport/772fc930-5418-0bfa-22c6-056ccc4fedc3]` DiagnosticReport | 2026-03-06 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 160.13 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 109.53 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 147.68 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 41.761 mg/dL | LOINC 57698-3

<details><summary>Everything the model saw (41 cards)</summary>

```text
[Condition/772fc930-5418-0bfa-5baf-97b1667a332f] Condition | onset 2026-07-09 | Part-time employment (finding) | clinical status active | SNOMED 160904001
[Condition/772fc930-5418-0bfa-446c-c28d224cff31] Condition | onset 2026-06-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/772fc930-5418-0bfa-33d9-881f0ecc07c1] Condition | onset 2026-06-11 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/772fc930-5418-0bfa-d3cc-a2daa4832199] Condition | onset 2026-02-19 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/772fc930-5418-0bfa-600b-5558ca66220a] Condition | onset 2026-02-19 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/772fc930-5418-0bfa-6352-6c3984966ef8] Condition | onset 2025-02-13 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/772fc930-5418-0bfa-bb6d-8a0b90cf95e4] Condition | onset 2020-01-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/772fc930-5418-0bfa-ab71-24a74b1745fd] Condition | onset 2020-01-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/772fc930-5418-0bfa-beac-a103fe7f3fd2] Condition | onset 2019-01-10 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/772fc930-5418-0bfa-2c4f-3f5ed5953c36] Condition | onset 2019-01-10 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/772fc930-5418-0bfa-3873-02589386889d] Condition | onset 2004-06-19 | Osteoarthritis of hip (disorder) | clinical status active | SNOMED 239872002
[Condition/772fc930-5418-0bfa-a4a0-5eff492015a6] Condition | onset 1991-08-28 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/772fc930-5418-0bfa-01dc-3613408a83a6] Condition | onset 1991-08-22 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/772fc930-5418-0bfa-35d2-44b4eb4fcccc] Condition | onset 1991-08-08 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/772fc930-5418-0bfa-43ec-8fdd443cc6ce] Condition | onset 1988-07-21 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/772fc930-5418-0bfa-91e4-e46a214921b9] Condition | onset 1986-07-10 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/772fc930-5418-0bfa-47df-a943ca27aa29] Condition | onset 1986-07-10 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/772fc930-5418-0bfa-7d09-0ea3ca1e93ba] Condition | onset 1986-03-30 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/772fc930-5418-0bfa-1be5-06b5144b5817] Condition | onset 1986-03-01 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/772fc930-5418-0bfa-0cdf-ac369e474ff3] Condition | onset 1977-05-19 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/772fc930-5418-0bfa-f6df-7e2448081e0f] Condition | onset 1967-05-04 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/772fc930-5418-0bfa-ffbe-e3692c7542d7] Condition | onset 1964-01-15 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/772fc930-5418-0bfa-d2b4-bc5609421614] MedicationRequest | prescribed 2026-07-16 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/772fc930-5418-0bfa-35ed-4b81c08cb46e] MedicationRequest | prescribed 2026-07-16 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/772fc930-5418-0bfa-0d23-3b3c40dabcae] MedicationRequest | prescribed 2026-07-16 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/772fc930-5418-0bfa-ac79-a5117bd68db1] MedicationRequest | prescribed 2026-03-06 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/772fc930-5418-0bfa-dfc7-922f9300bced] MedicationRequest | prescribed 2004-06-19 | Naproxen sodium 220 MG Oral Tablet | status active | reason: Osteoarthritis of hip (disorder) | RxNorm 849574
[Encounter/772fc930-5418-0bfa-dd45-e4b82fc97e3d] Encounter | 2026-07-23 | Encounter for check up (procedure) | class AMB | at BOSTON MEDICAL CENTER CORPORATION-
[Encounter/772fc930-5418-0bfa-6606-662b1312d21c] Encounter | 2026-07-16 | Urgent care clinic (environment) | class AMB | at LYNN URGENT CARE LLC
[Encounter/772fc930-5418-0bfa-54c7-a3b13e8997b9] Encounter | 2026-07-09 | Emergency room admission (procedure) | class EMER | at LEONARD FLORENCE CENTER FOR LIVING
[Immunization/772fc930-5418-0bfa-fcca-2fca6db3fac3] Immunization | 2026-02-19 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/5ed40be8-7733-d4cc-46e1-1d88e4d32c9c#2] Clinical note | 2026-03-06 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/4a74e5a2-43f3-9150-48f5-b6bc4acd86cd#2] Clinical note | 2025-02-13 | part 2 of 2 | # Assessment and Plan Patient is presenting with hyperlipidemia (disorder), part-time employment (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - sleep apnea assessment (procedure) - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - assessment using morse fall scale (procedure) The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine - lipid panel with direct ldl - serum or plasma - comprehensive metabolic 2000 panel - serum or plasma - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - generalized anxiety disorder 7 item (gad-7) - morse fall scale panel The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet
[DocumentReference/b242eb36-3c8d-6617-9d3c-e8379ec173cb#2] Clinical note | 2022-01-27 | part 2 of 2 | # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - medication reconciliation (procedure) - sleep apnea assessment (procedure) - assessment of health and social care needs (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - assessment using alcohol use disorders identification test - consumption (procedure) The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - patient health questionnaire 2 item (phq-2) [reported] - alcohol use disorder identification test - consumption [audit-c] The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet
[DocumentReference/1547ea6c-3921-dbce-eb3b-e46f7d89f735#2] Clinical note | 2026-04-30 | part 2 of 2 | # Assessment and Plan Patient is presenting with medication review due (situation), full-time employment (finding). ## Plan The following procedures were conducted: - assessment of health and social care needs (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine - basic metabolic panel - blood The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet
[DocumentReference/edfd5f98-1014-5a9d-f16a-5a568f54b32a#2] Clinical note | 2023-07-20 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - medication reconciliation (procedure) - sleep apnea assessment (procedure) - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine - basic metabolic panel - blood - generalized anxiety disorder 7 item (gad-7) The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet
[DocumentReference/78efda72-f21e-360a-288f-aa89155f1149#2] Clinical note | 2026-07-16 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet
[DocumentReference/ede4c092-9490-5d66-6eb5-da996e85da65#2] Clinical note | 2026-05-07 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet
[DiagnosticReport/772fc930-5418-0bfa-8d34-6948d42b3a6a] DiagnosticReport | 2019-01-10 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 201.38 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 140.23 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 122.71 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 50.62 mg/dL | LOINC 57698-3
[DiagnosticReport/772fc930-5418-0bfa-22c6-056ccc4fedc3] DiagnosticReport | 2026-03-06 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 160.13 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 109.53 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 147.68 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 41.761 mg/dL | LOINC 57698-3
[DiagnosticReport/772fc930-5418-0bfa-e67c-adaa4fb5325d] DiagnosticReport | 2025-02-13 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 227.41 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 285.82 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 169.29 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 50.134 mg/dL | LOINC 57698-3
```

</details>

label: s
note: The 2026-03-06 lipid panel with direct LDL lists 160.13, 109.53, 147.68 and 41.761 mg/dL, matching exactly. The other panels are 2025-02-13 and 2019-01-10, so this is the most recent.

## 7. `prescribed-for-prediabetes:772fc930#0#1`

Question: Which medications have been prescribed for the patient's prediabetes?

Answer: The only medication prescribed for prediabetes is insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin]. **It was prescribed on 2026-06-18, 2026-07-02 and 2026-07-09 (status completed), and most recently on 2026-07-16 (status active).**

Cards this sentence cites:

- `[MedicationRequest/772fc930-5418-0bfa-33a2-f9ba59153396]` MedicationRequest | prescribed 2026-06-18 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status completed | reason: Prediabetes (finding) | RxNorm 106892
- `[MedicationRequest/772fc930-5418-0bfa-b7b4-e0eeaf292c02]` MedicationRequest | prescribed 2026-07-02 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status completed | reason: Prediabetes (finding) | RxNorm 106892
- `[MedicationRequest/772fc930-5418-0bfa-2708-af6c2cf0984d]` MedicationRequest | prescribed 2026-07-09 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status completed | reason: Prediabetes (finding) | RxNorm 106892
- `[MedicationRequest/772fc930-5418-0bfa-d2b4-bc5609421614]` MedicationRequest | prescribed 2026-07-16 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892

<details><summary>Everything the model saw (41 cards)</summary>

```text
[Condition/772fc930-5418-0bfa-5baf-97b1667a332f] Condition | onset 2026-07-09 | Part-time employment (finding) | clinical status active | SNOMED 160904001
[Condition/772fc930-5418-0bfa-446c-c28d224cff31] Condition | onset 2026-06-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/772fc930-5418-0bfa-33d9-881f0ecc07c1] Condition | onset 2026-06-11 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/772fc930-5418-0bfa-d3cc-a2daa4832199] Condition | onset 2026-02-19 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/772fc930-5418-0bfa-600b-5558ca66220a] Condition | onset 2026-02-19 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/772fc930-5418-0bfa-6352-6c3984966ef8] Condition | onset 2025-02-13 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/772fc930-5418-0bfa-bb6d-8a0b90cf95e4] Condition | onset 2020-01-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/772fc930-5418-0bfa-ab71-24a74b1745fd] Condition | onset 2020-01-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/772fc930-5418-0bfa-beac-a103fe7f3fd2] Condition | onset 2019-01-10 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/772fc930-5418-0bfa-2c4f-3f5ed5953c36] Condition | onset 2019-01-10 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/772fc930-5418-0bfa-3873-02589386889d] Condition | onset 2004-06-19 | Osteoarthritis of hip (disorder) | clinical status active | SNOMED 239872002
[Condition/772fc930-5418-0bfa-a4a0-5eff492015a6] Condition | onset 1991-08-28 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/772fc930-5418-0bfa-01dc-3613408a83a6] Condition | onset 1991-08-22 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/772fc930-5418-0bfa-35d2-44b4eb4fcccc] Condition | onset 1991-08-08 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/772fc930-5418-0bfa-43ec-8fdd443cc6ce] Condition | onset 1988-07-21 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/772fc930-5418-0bfa-91e4-e46a214921b9] Condition | onset 1986-07-10 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/772fc930-5418-0bfa-47df-a943ca27aa29] Condition | onset 1986-07-10 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/772fc930-5418-0bfa-7d09-0ea3ca1e93ba] Condition | onset 1986-03-30 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/772fc930-5418-0bfa-1be5-06b5144b5817] Condition | onset 1986-03-01 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/772fc930-5418-0bfa-0cdf-ac369e474ff3] Condition | onset 1977-05-19 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/772fc930-5418-0bfa-f6df-7e2448081e0f] Condition | onset 1967-05-04 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/772fc930-5418-0bfa-ffbe-e3692c7542d7] Condition | onset 1964-01-15 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/772fc930-5418-0bfa-d2b4-bc5609421614] MedicationRequest | prescribed 2026-07-16 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/772fc930-5418-0bfa-35ed-4b81c08cb46e] MedicationRequest | prescribed 2026-07-16 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/772fc930-5418-0bfa-0d23-3b3c40dabcae] MedicationRequest | prescribed 2026-07-16 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/772fc930-5418-0bfa-ac79-a5117bd68db1] MedicationRequest | prescribed 2026-03-06 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/772fc930-5418-0bfa-dfc7-922f9300bced] MedicationRequest | prescribed 2004-06-19 | Naproxen sodium 220 MG Oral Tablet | status active | reason: Osteoarthritis of hip (disorder) | RxNorm 849574
[Encounter/772fc930-5418-0bfa-dd45-e4b82fc97e3d] Encounter | 2026-07-23 | Encounter for check up (procedure) | class AMB | at BOSTON MEDICAL CENTER CORPORATION-
[Encounter/772fc930-5418-0bfa-6606-662b1312d21c] Encounter | 2026-07-16 | Urgent care clinic (environment) | class AMB | at LYNN URGENT CARE LLC
[Encounter/772fc930-5418-0bfa-54c7-a3b13e8997b9] Encounter | 2026-07-09 | Emergency room admission (procedure) | class EMER | at LEONARD FLORENCE CENTER FOR LIVING
[Immunization/772fc930-5418-0bfa-fcca-2fca6db3fac3] Immunization | 2026-02-19 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/772fc930-5418-0bfa-33a2-f9ba59153396] MedicationRequest | prescribed 2026-06-18 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status completed | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/772fc930-5418-0bfa-2708-af6c2cf0984d] MedicationRequest | prescribed 2026-07-09 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status completed | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/772fc930-5418-0bfa-b7b4-e0eeaf292c02] MedicationRequest | prescribed 2026-07-02 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status completed | reason: Prediabetes (finding) | RxNorm 106892
[DocumentReference/78efda72-f21e-360a-288f-aa89155f1149#2] Clinical note | 2026-07-16 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet
[DocumentReference/5ed40be8-7733-d4cc-46e1-1d88e4d32c9c#2] Clinical note | 2026-03-06 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/ede4c092-9490-5d66-6eb5-da996e85da65#2] Clinical note | 2026-05-07 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet
[DocumentReference/c1a211be-a298-20e9-3f01-515ed6dea2a0#2] Clinical note | 2026-07-02 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet
[DocumentReference/5dba0b33-aea4-34dd-7921-e127a8a77945#2] Clinical note | 2026-05-21 | part 2 of 2 | # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet
[DocumentReference/14f63e37-f7f1-1f39-6cc6-264309918cd8#2] Clinical note | 2020-12-24 | part 2 of 2 | # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet
[DocumentReference/bee957e2-a02a-0f22-ffc4-96923ffa2545#2] Clinical note | 2021-01-28 | part 2 of 2 | # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet
```

</details>

label: p?
note: The four cited Humulin MedicationRequests match the stated dates and statuses, and 2026-07-16 is the latest. But the date list reads as complete, and the clinical notes the model saw show Humulin also prescribed on 2020-12-24, 2021-01-28, 2026-05-07 and 2026-05-21 (no reason given in those notes).

## 8. `prescribed-for-essential-hypertension:ef5e136c#0#2`

Question: Which medications have been prescribed for the patient's essential hypertension?

Answer: Three medications have been prescribed for essential hypertension: hydrochlorothiazide 25 MG oral tablet, lisinopril 10 MG oral tablet, and amLODIPine 2.5 MG oral tablet, all with active prescriptions dated 2026-09-30. Earlier prescriptions of all three, now completed, were written on 2026-09-16 and 2026-09-23. **The earliest hypertension prescription is a hydrochlorothiazide prescription from 2016-10-12, now completed.**

Cards this sentence cites:

- `[MedicationRequest/ef5e136c-ff1e-0695-c2ec-a322bf20e076]` MedicationRequest | prescribed 2016-10-12 | Hydrochlorothiazide 25 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 310798

<details><summary>Everything the model saw (44 cards)</summary>

```text
[Condition/ef5e136c-ff1e-0695-1f8c-935a12106cac] Condition | onset 2026-09-30 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/ef5e136c-ff1e-0695-7e5d-470b95f60db2] Condition | onset 2026-09-23 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/ef5e136c-ff1e-0695-9d2d-c4be459bc9f4] Condition | onset 2026-09-09 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/ef5e136c-ff1e-0695-7b9c-f43e5ca3f6c6] Condition | onset 2026-08-12 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-aa04-94486c99258f] Condition | onset 2025-08-27 | End-stage renal disease (disorder) | clinical status active | SNOMED 46177005
[Condition/ef5e136c-ff1e-0695-423f-ed71d76e81e3] Condition | onset 2025-03-30 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/ef5e136c-ff1e-0695-71df-3a96389b0a39] Condition | onset 2025-02-05 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/ef5e136c-ff1e-0695-5331-2d63eb213c34] Condition | onset 2024-05-15 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/ef5e136c-ff1e-0695-3834-fa6cb282a475] Condition | onset 2024-05-15 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/ef5e136c-ff1e-0695-68fe-9e2010333061] Condition | onset 2023-08-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/ef5e136c-ff1e-0695-65f5-8d04f278a661] Condition | onset 2023-08-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/ef5e136c-ff1e-0695-aac2-46a0ff462178] Condition | onset 2023-04-19 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/ef5e136c-ff1e-0695-fda2-40e12f6b17a7] Condition | onset 2017-11-15 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/ef5e136c-ff1e-0695-bf3f-30946ad3f8b4] Condition | onset 2017-11-15 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/ef5e136c-ff1e-0695-eac4-d545a0296998] Condition | onset 2011-07-27 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/ef5e136c-ff1e-0695-b228-2f5ff5bb47cb] Condition | onset 2010-05-19 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/ef5e136c-ff1e-0695-af16-82f03f777ba8] Condition | onset 2010-05-19 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/ef5e136c-ff1e-0695-5ca5-51bfdc51320e] Condition | onset 2010-05-12 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/ef5e136c-ff1e-0695-f7ec-ceae0c2566bc] Condition | onset 2004-06-16 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/ef5e136c-ff1e-0695-c94a-5d81ddd88117] Condition | onset 1997-05-07 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/ef5e136c-ff1e-0695-6efc-9f7d5e6b04ef] Condition | onset 1993-09-01 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/ef5e136c-ff1e-0695-1f68-dac24351dbaa] Condition | onset 1993-04-14 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/ef5e136c-ff1e-0695-2d8d-328849698529] Condition | onset 1993-01-22 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/ef5e136c-ff1e-0695-0825-c31e8b252683] Condition | onset 1983-11-14 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/ef5e136c-ff1e-0695-cb16-3a98eeb2de7a] Condition | onset 1976-01-07 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/ef5e136c-ff1e-0695-3278-6a86eaf1fb5d] Condition | onset 1975-06-27 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/ef5e136c-ff1e-0695-337f-d12087c8dbb5] Condition | onset 1975-01-01 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/ef5e136c-ff1e-0695-ffec-2ea7ac772a27] MedicationRequest | prescribed 2026-09-30 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/ef5e136c-ff1e-0695-b3ba-a1ec7bcfb9f4] MedicationRequest | prescribed 2026-09-30 | albuterol 0.83 MG/ML Inhalation Solution | status active | RxNorm 630208
[MedicationRequest/ef5e136c-ff1e-0695-901e-2e1f9afb0cca] MedicationRequest | prescribed 2026-09-30 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/ef5e136c-ff1e-0695-76a6-8eeb54f8a75e] MedicationRequest | prescribed 2026-09-30 | 120 ACTUAT fluticasone propionate 0.044 MG/ACTUAT Metered Dose Inhaler [Flovent] | status active | RxNorm 895996
[MedicationRequest/ef5e136c-ff1e-0695-6c6d-182c3b9c47c1] MedicationRequest | prescribed 2026-09-30 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/ef5e136c-ff1e-0695-6804-cf31640a9491] MedicationRequest | prescribed 2026-09-30 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[Encounter/ef5e136c-ff1e-0695-08ba-2471a16a6570] Encounter | 2026-09-30 | Emergency room admission (procedure) | class EMER | at APPLE VALLEY CENTER
[Encounter/ef5e136c-ff1e-0695-aea4-11055569fd51] Encounter | 2026-09-23 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/ef5e136c-ff1e-0695-4a41-6fca58c80cb7] Encounter | 2026-09-16 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Immunization/ef5e136c-ff1e-0695-6beb-93901776b619] Immunization | 2026-05-13 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/ef5e136c-ff1e-0695-1251-51c1c26a1668] MedicationRequest | prescribed 2026-09-23 | amLODIPine 2.5 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/ef5e136c-ff1e-0695-172a-0146b6e9fb46] MedicationRequest | prescribed 2026-09-16 | amLODIPine 2.5 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/ef5e136c-ff1e-0695-c2ec-a322bf20e076] MedicationRequest | prescribed 2016-10-12 | Hydrochlorothiazide 25 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/ef5e136c-ff1e-0695-7191-63270eabbc1f] MedicationRequest | prescribed 2026-09-23 | Hydrochlorothiazide 25 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/ef5e136c-ff1e-0695-f8d9-fe4835ad1318] MedicationRequest | prescribed 2026-09-16 | Hydrochlorothiazide 25 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/ef5e136c-ff1e-0695-8fe4-75eb2b2d7363] MedicationRequest | prescribed 2026-09-23 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/ef5e136c-ff1e-0695-81a9-aec67a2da004] MedicationRequest | prescribed 2026-09-16 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
```

</details>

label: s
note: Every hypertension-reason MedicationRequest seen is dated 2026-09-16, 09-23 or 09-30, except hydrochlorothiazide on 2016-10-12 with status completed, which is the earliest.

## 9. `current-meds:7280f7f8#0#1`

Question: What medications is the patient currently prescribed?

Answer: The patient's active prescriptions from 2026-04-12 to 2026-04-13 are Simvastatin 10 MG Oral Tablet (for hyperlipidemia), Ibuprofen 400 MG Oral Tablet [Ibu], Acetaminophen 325 MG / Oxycodone Hydrochloride 10 MG Oral Tablet [Percocet], Galantamine 4 MG Oral Tablet (for Alzheimer's disease), and Acetaminophen 325 MG Oral Tablet [Tylenol]. **Also still listed as active from 2018-11-11 are Simvastatin 20 MG Oral Tablet, Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray, Clopidogrel 75 MG Oral Tablet, and 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet.** Two simvastatin prescriptions are active at the same time: 20 MG from 2018-11-11 and 10 MG from 2026-04-13.

Cards this sentence cites:

- `[MedicationRequest/7280f7f8-315d-7c6a-e1ca-6672a64e96d6]` MedicationRequest | prescribed 2018-11-11 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
- `[MedicationRequest/7280f7f8-315d-7c6a-d3dc-bf227b26b9de]` MedicationRequest | prescribed 2018-11-11 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
- `[MedicationRequest/7280f7f8-315d-7c6a-40f0-094ac0d35606]` MedicationRequest | prescribed 2018-11-11 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
- `[MedicationRequest/7280f7f8-315d-7c6a-344e-7b21fe48818f]` MedicationRequest | prescribed 2018-11-11 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412

<details><summary>Everything the model saw (43 cards)</summary>

```text
[Condition/7280f7f8-315d-7c6a-5183-1fc53612d856] Condition | onset 2026-04-12 | Alzheimer's disease (disorder) | clinical status active | SNOMED 26929004
[Condition/7280f7f8-315d-7c6a-069f-25fdb34e3e53] Condition | onset 2025-04-06 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/7280f7f8-315d-7c6a-06ae-a26712c6cfb7] Condition | onset 2024-03-31 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/7280f7f8-315d-7c6a-84b2-d6045a9b8deb] Condition | onset 2018-11-12 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/7280f7f8-315d-7c6a-60b8-1b2b3b190d66] Condition | onset 2018-11-04 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/7280f7f8-315d-7c6a-eee1-33d3eda16b26] Condition | onset 2014-02-16 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/7280f7f8-315d-7c6a-23b9-2a24d0c43093] Condition | onset 2014-02-16 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/7280f7f8-315d-7c6a-f371-666500850eb4] Condition | onset 2014-02-02 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/7280f7f8-315d-7c6a-b5ea-aa0955ebc2c7] Condition | onset 2010-01-10 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/7280f7f8-315d-7c6a-929f-e845c91bba18] Condition | onset 1993-02-06 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/7280f7f8-315d-7c6a-6159-244929402415] Condition | onset 1991-07-09 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/7280f7f8-315d-7c6a-7561-551dd4fb980c] Condition | onset 1990-11-11 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/7280f7f8-315d-7c6a-69cb-9f6bde195716] Condition | onset 1990-10-25 | Impacted molars (disorder) | clinical status active | SNOMED 196416002
[Condition/7280f7f8-315d-7c6a-e183-7fc41f06abde] Condition | onset 1990-02-06 | Chronic intractable migraine without aura (disorder) | clinical status active | SNOMED 124171000119105
[Condition/7280f7f8-315d-7c6a-57cd-16215a141add] Condition | onset 1988-11-06 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/7280f7f8-315d-7c6a-7c25-7a247f43e721] Condition | onset 1981-01-18 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/7280f7f8-315d-7c6a-50ac-70390520f5d8] Condition | onset 1981-01-18 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/7280f7f8-315d-7c6a-a35c-5f2c4404e1cd] Condition | onset 1971-02-18 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/7280f7f8-315d-7c6a-cf3c-1559c1e270a8] Condition | onset 1964-12-20 | Housing unsatisfactory (finding) | clinical status active | SNOMED 105531004
[Condition/7280f7f8-315d-7c6a-3735-89103641aea2] Condition | onset 1964-12-20 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/7280f7f8-315d-7c6a-d103-5f5cf25ace53] MedicationRequest | prescribed 2026-04-13 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/7280f7f8-315d-7c6a-dd3c-435b565b36d4] MedicationRequest | prescribed 2026-04-12 | Ibuprofen 400 MG Oral Tablet [Ibu] | status active | RxNorm 206905
[MedicationRequest/7280f7f8-315d-7c6a-698d-8c3f4a330263] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG / Oxycodone Hydrochloride 10 MG Oral Tablet [Percocet] | status active | RxNorm 1049625
[MedicationRequest/7280f7f8-315d-7c6a-53dc-677516ba315e] MedicationRequest | prescribed 2026-04-12 | Galantamine 4 MG Oral Tablet | status active | reason: Alzheimer's disease (disorder) | RxNorm 310436
[MedicationRequest/7280f7f8-315d-7c6a-21fd-127361ce4eae] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-e1ca-6672a64e96d6] MedicationRequest | prescribed 2018-11-11 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/7280f7f8-315d-7c6a-d3dc-bf227b26b9de] MedicationRequest | prescribed 2018-11-11 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/7280f7f8-315d-7c6a-40f0-094ac0d35606] MedicationRequest | prescribed 2018-11-11 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/7280f7f8-315d-7c6a-344e-7b21fe48818f] MedicationRequest | prescribed 2018-11-11 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[Encounter/7280f7f8-315d-7c6a-ddbc-56619e72a429] Encounter | 2026-04-26 | Encounter for check up (procedure) | class AMB | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-e49f-7858d34e1916] Encounter | 2026-04-13 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-79c7-b2135168eae6] Encounter | 2026-04-12 | General examination of patient (procedure) | class AMB | at HOLY FAMILY MEDICAL SPECIALTY PRACTICE PLLC
[Immunization/7280f7f8-315d-7c6a-89f5-f28321d6dbe8] Immunization | 2026-04-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/7280f7f8-315d-7c6a-bff4-e18d95f7f79b] MedicationRequest | prescribed 2021-03-14 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status completed | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-bbcd-ae9102946cec] MedicationRequest | prescribed 2025-04-06 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status completed | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-4c3e-27b79818327b] MedicationRequest | prescribed 2024-11-24 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status completed | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-1656-a49c2a84baae] MedicationRequest | prescribed 2021-03-14 | Ibuprofen 400 MG Oral Tablet [Ibu] | status completed | RxNorm 206905
[MedicationRequest/7280f7f8-315d-7c6a-9203-04a436d5611e] MedicationRequest | prescribed 2025-04-06 | Ibuprofen 400 MG Oral Tablet [Ibu] | status completed | RxNorm 206905
[MedicationRequest/7280f7f8-315d-7c6a-12d1-81b620daaf62] MedicationRequest | prescribed 2024-11-24 | Ibuprofen 400 MG Oral Tablet [Ibu] | status completed | RxNorm 206905
[DocumentReference/750cb41b-d9ad-3c1d-b6d7-fadb5db1236e#1] Clinical note | 2010-01-31 | part 1 of 1 | 2010-01-31 # Chief Complaint - Memory Loss - Decreased in Judgement # History of Present Illness Neil122 is a 63 year-old nonhispanic white male. Patient has a history of victim of intimate partner abuse (finding). # Social History Patient is married. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a low socioeconomic background. Patient did not finish high school. Patient currently has Cigna Health. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The patient was prescribed the following medications: - simvastatin 10 mg oral tablet The patient was placed on a careplan: - hyperlipidemia clinical management plan (record artifact)
[DocumentReference/ae41b370-e3ce-e406-ac51-c30e28d61121#2] Clinical note | 2018-02-25 | part 2 of 2 | # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf, td (adult), 5 lf tetanus toxoid, preservative free, adsorbed. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - assessment using morse fall scale (procedure) - depression screening (procedure) - depression screening (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - generalized anxiety disorder 7 item (gad-7) - morse fall scale panel - patient health questionnaire 2 item (phq-2) [reported] The patient was prescribed the following medications: - acetaminophen 325 mg / oxycodone hydrochloride 10 mg oral tablet [percocet] - acetaminophen 325 mg oral tablet [tylenol] - ibuprofen 400 mg oral tablet [ibu]
[DocumentReference/6b0d0857-4700-f6ee-c3e4-f8d7c3eb1f27#2] Clinical note | 2026-04-13 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/d33f5325-2f82-5aa9-5d4d-a95b2ba279e4#2] Clinical note | 2017-02-19 | part 2 of 2 | # Assessment and Plan Patient is presenting with full-time employment (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - screening for domestic abuse (procedure) - depression screening (procedure) - depression screening (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - basic metabolic panel - blood - generalized anxiety disorder 7 item (gad-7) - humiliation, afraid, rape, and kick questionnaire [hark] - patient health questionnaire 2 item (phq-2) [reported] The patient was prescribed the following medications: - acetaminophen 325 mg / oxycodone hydrochloride 10 mg oral tablet [percocet] - acetaminophen 325 mg oral tablet [tylenol] - ibuprofen 400 mg oral tablet [ibu]
```

</details>

label: s
note: The four cited MedicationRequests are each dated 2018-11-11 with status active and match the stated names and strengths. No other 2018-11-11 prescriptions appear in the cards seen.

## 10. `latest-lab-718-7:8ff46e01#0#0`

Question: What was the patient's most recent hemoglobin result, and when was it measured?

Answer: **The most recent hemoglobin result was 13.041 g/dL, measured on 2025-12-31.**

Cards this sentence cites:

- `[Observation/8ff46e01-0333-fefb-3a38-2f30acbac2c3]` Observation (laboratory) | 2025-12-31 | Hemoglobin [Mass/volume] in Blood = 13.041 g/dL | status final | LOINC 718-7

<details><summary>Everything the model saw (35 cards)</summary>

```text
[Condition/8ff46e01-0333-fefb-e078-a2c79f9b5570] Condition | onset 2025-11-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/8ff46e01-0333-fefb-ca9a-9c89d481d534] Condition | onset 2025-11-10 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/8ff46e01-0333-fefb-f69f-b001b28f2b81] Condition | onset 2023-12-27 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8ff46e01-0333-fefb-d37b-fa17bc4619e6] Condition | onset 2023-12-27 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/8ff46e01-0333-fefb-1085-7240f563162c] Condition | onset 2023-12-27 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8ff46e01-0333-fefb-0d5f-96af345c8178] Condition | onset 2023-12-27 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8ff46e01-0333-fefb-a724-e7508612ceb2] Condition | onset 2015-12-19 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/8ff46e01-0333-fefb-c4b8-0da5f4d9d6af] Condition | onset 2010-09-29 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/8ff46e01-0333-fefb-3eac-29a6b80382d5] Condition | onset 1998-06-27 | Recurrent urinary tract infection (disorder) | clinical status active | SNOMED 197927001
[Condition/8ff46e01-0333-fefb-1001-1cc553e61d65] Condition | onset 1998-02-04 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[Condition/8ff46e01-0333-fefb-2118-3da43e594952] Condition | onset 1995-01-18 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[Condition/8ff46e01-0333-fefb-400e-c9db591e5ada] Condition | onset 1988-12-14 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8ff46e01-0333-fefb-6f8d-08005729c21a] Condition | onset 1980-10-17 | History of seizure (situation) | clinical status active | SNOMED 1290882004
[Condition/8ff46e01-0333-fefb-334a-c4ab11856973] Condition | onset 1980-10-17 | Seizure disorder (disorder) | clinical status active | SNOMED 128613002
[Condition/8ff46e01-0333-fefb-493a-f8d458075b36] Condition | onset 1980-04-22 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/8ff46e01-0333-fefb-081b-4d95e98b7814] MedicationRequest | prescribed 2026-01-16 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8ff46e01-0333-fefb-cca1-202b10a1b90d] MedicationRequest | prescribed 2025-11-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/8ff46e01-0333-fefb-6306-60b207f6bcda] MedicationRequest | prescribed 2025-11-10 | rosuvastatin calcium 10 MG Oral Tablet | status active | RxNorm 859747
[MedicationRequest/8ff46e01-0333-fefb-5a32-7c872c74242b] MedicationRequest | prescribed 2025-11-10 | atenolol 50 MG Oral Tablet | status active | RxNorm 197381
[MedicationRequest/8ff46e01-0333-fefb-5632-79d28eb2f69d] MedicationRequest | prescribed 2025-11-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/8ff46e01-0333-fefb-0f09-741ffc0ecb79] MedicationRequest | prescribed 2025-11-10 | lisinopril 10 MG Oral Tablet | status active | RxNorm 314076
[Encounter/8ff46e01-0333-fefb-2842-108bae2a93b7] Encounter | 2026-01-16 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at STEWARD HOLY FAMILY HOSPITAL INC
[Encounter/8ff46e01-0333-fefb-deac-7d54a2e717b0] Encounter | 2025-12-31 | General examination of patient (procedure) | class AMB | at GREATER LAWRENCE FAMILY HEALTH CENTER INC
[Encounter/8ff46e01-0333-fefb-bdb4-35663b36a4c8] Encounter | 2025-11-10 | Emergency room admission (procedure) | class EMER | reason: Myocardial infarction (disorder) | at Fitchburg Outpatient Clinic
[Immunization/8ff46e01-0333-fefb-0b35-b6fa97749e42] Immunization | 2025-12-31 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/8ff46e01-0333-fefb-357e-03381b314d73] Observation (laboratory) | 2025-11-10 | Hemoglobin A1c/Hemoglobin.total in Blood = 5.84 % | status final | LOINC 4548-4
[Observation/8ff46e01-0333-fefb-6319-316be37c9f55] Observation (laboratory) | 2025-12-31 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.11 % | status final | LOINC 4548-4
[Observation/8ff46e01-0333-fefb-ded7-cf1ce0aed14b] Observation (laboratory) | 2023-12-27 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.27 % | status final | LOINC 4548-4
[Observation/8ff46e01-0333-fefb-3a38-2f30acbac2c3] Observation (laboratory) | 2025-12-31 | Hemoglobin [Mass/volume] in Blood = 13.041 g/dL | status final | LOINC 718-7
[Observation/8ff46e01-0333-fefb-b95b-1f4a18e273fb] Observation (laboratory) | 2025-11-10 | Hemoglobin [Mass/volume] in Blood = 12.648 g/dL | status final | LOINC 718-7
[Observation/8ff46e01-0333-fefb-e531-b159b1f6a429] Observation (laboratory) | 2024-01-03 | Hemoglobin [Mass/volume] in Blood = 11.315 g/dL | status final | LOINC 718-7
[Observation/8ff46e01-0333-fefb-1765-cdc406fd83a6] Observation (laboratory) | 2025-11-10 | aPTT in Blood by Coagulation assay = 27.1 s | status final | LOINC 3173-2
[Observation/8ff46e01-0333-fefb-5879-e39dccdbecad] Observation (laboratory) | 2025-12-31 | Glucose [Mass/volume] in Blood = 81.98 mg/dL | status final | LOINC 2339-0
[Observation/8ff46e01-0333-fefb-9f81-c8ccdf796297] Observation (laboratory) | 2026-01-16 | Glucose [Mass/volume] in Blood = 71.06 mg/dL | status final | LOINC 2339-0
[Observation/8ff46e01-0333-fefb-a580-d631746a3e88] Observation (laboratory) | 2025-01-16 | Glucose [Mass/volume] in Blood = 79.72 mg/dL | status final | LOINC 2339-0
```

</details>

label: s
note: The hemoglobin (LOINC 718-7) observations are 2025-12-31 = 13.041 g/dL, 2025-11-10 = 12.648 and 2024-01-03 = 11.315, so 13.041 g/dL on 2025-12-31 is the most recent.

## 11. `vaccines-last-year:7280f7f8#0#0`

Question: Which vaccines did the patient receive in the last year?

Answer: **In the year before the record's as-of date of 2026-10-01, the patient received one vaccine: Influenza, split virus, trivalent, PF (CVX 140) on 2026-04-12.** The previous recorded vaccine was an influenza dose on 2024-11-24, which falls outside that window.

Cards this sentence cites:

- `[Immunization/7280f7f8-315d-7c6a-89f5-f28321d6dbe8]` Immunization | 2026-04-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140

<details><summary>Everything the model saw (43 cards)</summary>

```text
[Condition/7280f7f8-315d-7c6a-5183-1fc53612d856] Condition | onset 2026-04-12 | Alzheimer's disease (disorder) | clinical status active | SNOMED 26929004
[Condition/7280f7f8-315d-7c6a-069f-25fdb34e3e53] Condition | onset 2025-04-06 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/7280f7f8-315d-7c6a-06ae-a26712c6cfb7] Condition | onset 2024-03-31 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/7280f7f8-315d-7c6a-84b2-d6045a9b8deb] Condition | onset 2018-11-12 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/7280f7f8-315d-7c6a-60b8-1b2b3b190d66] Condition | onset 2018-11-04 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/7280f7f8-315d-7c6a-eee1-33d3eda16b26] Condition | onset 2014-02-16 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/7280f7f8-315d-7c6a-23b9-2a24d0c43093] Condition | onset 2014-02-16 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/7280f7f8-315d-7c6a-f371-666500850eb4] Condition | onset 2014-02-02 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/7280f7f8-315d-7c6a-b5ea-aa0955ebc2c7] Condition | onset 2010-01-10 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/7280f7f8-315d-7c6a-929f-e845c91bba18] Condition | onset 1993-02-06 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/7280f7f8-315d-7c6a-6159-244929402415] Condition | onset 1991-07-09 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/7280f7f8-315d-7c6a-7561-551dd4fb980c] Condition | onset 1990-11-11 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/7280f7f8-315d-7c6a-69cb-9f6bde195716] Condition | onset 1990-10-25 | Impacted molars (disorder) | clinical status active | SNOMED 196416002
[Condition/7280f7f8-315d-7c6a-e183-7fc41f06abde] Condition | onset 1990-02-06 | Chronic intractable migraine without aura (disorder) | clinical status active | SNOMED 124171000119105
[Condition/7280f7f8-315d-7c6a-57cd-16215a141add] Condition | onset 1988-11-06 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/7280f7f8-315d-7c6a-7c25-7a247f43e721] Condition | onset 1981-01-18 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/7280f7f8-315d-7c6a-50ac-70390520f5d8] Condition | onset 1981-01-18 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/7280f7f8-315d-7c6a-a35c-5f2c4404e1cd] Condition | onset 1971-02-18 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/7280f7f8-315d-7c6a-cf3c-1559c1e270a8] Condition | onset 1964-12-20 | Housing unsatisfactory (finding) | clinical status active | SNOMED 105531004
[Condition/7280f7f8-315d-7c6a-3735-89103641aea2] Condition | onset 1964-12-20 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/7280f7f8-315d-7c6a-d103-5f5cf25ace53] MedicationRequest | prescribed 2026-04-13 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/7280f7f8-315d-7c6a-dd3c-435b565b36d4] MedicationRequest | prescribed 2026-04-12 | Ibuprofen 400 MG Oral Tablet [Ibu] | status active | RxNorm 206905
[MedicationRequest/7280f7f8-315d-7c6a-698d-8c3f4a330263] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG / Oxycodone Hydrochloride 10 MG Oral Tablet [Percocet] | status active | RxNorm 1049625
[MedicationRequest/7280f7f8-315d-7c6a-53dc-677516ba315e] MedicationRequest | prescribed 2026-04-12 | Galantamine 4 MG Oral Tablet | status active | reason: Alzheimer's disease (disorder) | RxNorm 310436
[MedicationRequest/7280f7f8-315d-7c6a-21fd-127361ce4eae] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-e1ca-6672a64e96d6] MedicationRequest | prescribed 2018-11-11 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/7280f7f8-315d-7c6a-d3dc-bf227b26b9de] MedicationRequest | prescribed 2018-11-11 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/7280f7f8-315d-7c6a-40f0-094ac0d35606] MedicationRequest | prescribed 2018-11-11 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/7280f7f8-315d-7c6a-344e-7b21fe48818f] MedicationRequest | prescribed 2018-11-11 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[Encounter/7280f7f8-315d-7c6a-ddbc-56619e72a429] Encounter | 2026-04-26 | Encounter for check up (procedure) | class AMB | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-e49f-7858d34e1916] Encounter | 2026-04-13 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-79c7-b2135168eae6] Encounter | 2026-04-12 | General examination of patient (procedure) | class AMB | at HOLY FAMILY MEDICAL SPECIALTY PRACTICE PLLC
[Immunization/7280f7f8-315d-7c6a-89f5-f28321d6dbe8] Immunization | 2026-04-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/7280f7f8-315d-7c6a-2c12-076f4ebe4a00] Immunization | 2021-04-11 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/7280f7f8-315d-7c6a-03fb-59ac9d44c133] Immunization | 2021-03-21 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Observation/7280f7f8-315d-7c6a-3bcf-660371c4df20] Observation (survey) | 2024-03-31 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Somewhat; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Food; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/7280f7f8-315d-7c6a-17d4-3bde7faffa5a] Observation (survey) | 2026-04-12 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level A little bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/7280f7f8-315d-7c6a-073a-b5db76259ffb] Observation (survey) | 2025-04-06 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Quite a bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Medicine or Any Health Care (Medical, Dental, Mental Health, Vision); What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/7280f7f8-315d-7c6a-f0b4-d6fc3b03db28] Observation (survey) | 2024-11-24 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Not at all; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Utilities; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Immunization/7280f7f8-315d-7c6a-4150-9fa667bfd111] Immunization | 2021-03-14 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/7280f7f8-315d-7c6a-a994-7340336c5a95] Immunization | 2024-11-24 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/7280f7f8-315d-7c6a-5206-3912d1550e2d] Immunization | 2024-03-31 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/37069e82-27e3-b54c-3800-72d29ab5652d#1] Clinical note | 1991-07-09 | part 1 of 1 | 1991-07-09 # Chief Complaint - Memory Loss - Decreased in Judgement # History of Present Illness Neil122 is a 44 year-old nonhispanic white male. # Social History Patient is married. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a low socioeconomic background. Patient did not finish high school. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with chronic pain (finding). ## Plan
```

</details>

label: s
note: Of the six immunization cards (2021-03-14, 2021-03-21, 2021-04-11, 2024-03-31, 2024-11-24, 2026-04-12), only the 2026-04-12 Influenza, split virus, trivalent, PF (CVX 140) dose falls after 2025-10-01, so 'one vaccine' and its details match the cited card.

## 12. `last-visit:d14e9292#0#1`

Question: When was the patient's most recent visit, and what kind of visit was it?

Answer: The patient's most recent visit was on 2026-07-15, an inpatient admission to the surgical department at MOUNT AUBURN HOSPITAL for the reason "Sterilization requested." **A history of tubal ligation is recorded with onset on the same date, 2026-07-15.**

Cards this sentence cites:

- `[Condition/d14e9292-537d-9ab5-d719-3444368e63f2]` Condition | onset 2026-07-15 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005

<details><summary>Everything the model saw (19 cards)</summary>

```text
[Condition/d14e9292-537d-9ab5-d719-3444368e63f2] Condition | onset 2026-07-15 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/d14e9292-537d-9ab5-f5e1-81b5b14a8a8d] Condition | onset 2025-05-15 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/d14e9292-537d-9ab5-3fd5-303fdca87268] Condition | onset 2024-03-30 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/d14e9292-537d-9ab5-2de8-ff9612c4dc80] Condition | onset 2022-05-12 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/d14e9292-537d-9ab5-c205-6c7176a1d8e2] Condition | onset 2013-05-02 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/d14e9292-537d-9ab5-3a99-525060b2d8c3] Condition | onset 2009-04-23 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Encounter/d14e9292-537d-9ab5-75a2-660a8b4ef3eb] Encounter | 2026-07-15 | Admission to surgical department (procedure) | class IMP | reason: Sterilization requested (situation) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-cd48-29e15dfdc267] Encounter | 2026-06-26 | Consultation for treatment (procedure) | class AMB | reason: Sterilization requested (situation) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-a94e-2f619d52ef93] Encounter | 2026-03-12 | Encounter for check up (procedure) | class AMB | reason: Epidermal burn of skin (disorder) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-4838-2eb3f73199d8] Encounter | 2020-07-16 | Postnatal visit (regime/therapy) | class AMB | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-1dd3-33a421d5bfd3] Encounter | 2017-11-23 | Postnatal visit (regime/therapy) | class AMB | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-b610-b0e5d0d48258] Encounter | 2020-04-16 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-d65f-46bee4e6fd1a] Encounter | 2020-05-14 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-b502-516bf9817f77] Encounter | 2020-05-28 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-c51a-f0a903c02bfc] Encounter | 2020-02-20 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-3e80-1532df5f1179] Encounter | 2020-01-23 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at MOUNT AUBURN HOSPITAL
[Condition/d14e9292-537d-9ab5-8df5-9cc66cd66320] Condition | onset 2025-05-15 | Medication review due (situation) | clinical status resolved | resolved 2025-05-15 | SNOMED 314529007
[Condition/d14e9292-537d-9ab5-5a63-386b21bc2d6e] Condition | onset 2019-05-09 | Medication review due (situation) | clinical status resolved | resolved 2022-05-12 | SNOMED 314529007
[Immunization/d14e9292-537d-9ab5-9519-1481d5ace894] Immunization | 2021-05-13 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
```

</details>

label: s
note: Cited Condition card shows History of tubal ligation with onset 2026-07-15, the same date as the surgical admission encounter.

## 13. `current-meds:8ff46e01#0#1`

Question: What medications is the patient currently prescribed?

Answer: The patient's active prescriptions are aspirin 81 MG Oral Tablet, rosuvastatin calcium 10 MG Oral Tablet, atenolol 50 MG Oral Tablet, prasugrel 10 MG Oral Tablet, and lisinopril 10 MG Oral Tablet, all prescribed 2025-11-10. **Simvastatin 10 MG Oral Tablet, prescribed 2026-01-16 for hyperlipidemia, is also active.**

Cards this sentence cites:

- `[MedicationRequest/8ff46e01-0333-fefb-081b-4d95e98b7814]` MedicationRequest | prescribed 2026-01-16 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231

<details><summary>Everything the model saw (35 cards)</summary>

```text
[Condition/8ff46e01-0333-fefb-e078-a2c79f9b5570] Condition | onset 2025-11-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/8ff46e01-0333-fefb-ca9a-9c89d481d534] Condition | onset 2025-11-10 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/8ff46e01-0333-fefb-f69f-b001b28f2b81] Condition | onset 2023-12-27 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8ff46e01-0333-fefb-d37b-fa17bc4619e6] Condition | onset 2023-12-27 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/8ff46e01-0333-fefb-1085-7240f563162c] Condition | onset 2023-12-27 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8ff46e01-0333-fefb-0d5f-96af345c8178] Condition | onset 2023-12-27 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8ff46e01-0333-fefb-a724-e7508612ceb2] Condition | onset 2015-12-19 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/8ff46e01-0333-fefb-c4b8-0da5f4d9d6af] Condition | onset 2010-09-29 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/8ff46e01-0333-fefb-3eac-29a6b80382d5] Condition | onset 1998-06-27 | Recurrent urinary tract infection (disorder) | clinical status active | SNOMED 197927001
[Condition/8ff46e01-0333-fefb-1001-1cc553e61d65] Condition | onset 1998-02-04 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[Condition/8ff46e01-0333-fefb-2118-3da43e594952] Condition | onset 1995-01-18 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[Condition/8ff46e01-0333-fefb-400e-c9db591e5ada] Condition | onset 1988-12-14 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8ff46e01-0333-fefb-6f8d-08005729c21a] Condition | onset 1980-10-17 | History of seizure (situation) | clinical status active | SNOMED 1290882004
[Condition/8ff46e01-0333-fefb-334a-c4ab11856973] Condition | onset 1980-10-17 | Seizure disorder (disorder) | clinical status active | SNOMED 128613002
[Condition/8ff46e01-0333-fefb-493a-f8d458075b36] Condition | onset 1980-04-22 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/8ff46e01-0333-fefb-081b-4d95e98b7814] MedicationRequest | prescribed 2026-01-16 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8ff46e01-0333-fefb-cca1-202b10a1b90d] MedicationRequest | prescribed 2025-11-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/8ff46e01-0333-fefb-6306-60b207f6bcda] MedicationRequest | prescribed 2025-11-10 | rosuvastatin calcium 10 MG Oral Tablet | status active | RxNorm 859747
[MedicationRequest/8ff46e01-0333-fefb-5a32-7c872c74242b] MedicationRequest | prescribed 2025-11-10 | atenolol 50 MG Oral Tablet | status active | RxNorm 197381
[MedicationRequest/8ff46e01-0333-fefb-5632-79d28eb2f69d] MedicationRequest | prescribed 2025-11-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/8ff46e01-0333-fefb-0f09-741ffc0ecb79] MedicationRequest | prescribed 2025-11-10 | lisinopril 10 MG Oral Tablet | status active | RxNorm 314076
[Encounter/8ff46e01-0333-fefb-2842-108bae2a93b7] Encounter | 2026-01-16 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at STEWARD HOLY FAMILY HOSPITAL INC
[Encounter/8ff46e01-0333-fefb-deac-7d54a2e717b0] Encounter | 2025-12-31 | General examination of patient (procedure) | class AMB | at GREATER LAWRENCE FAMILY HEALTH CENTER INC
[Encounter/8ff46e01-0333-fefb-bdb4-35663b36a4c8] Encounter | 2025-11-10 | Emergency room admission (procedure) | class EMER | reason: Myocardial infarction (disorder) | at Fitchburg Outpatient Clinic
[Immunization/8ff46e01-0333-fefb-0b35-b6fa97749e42] Immunization | 2025-12-31 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/8ff46e01-0333-fefb-071f-4a32d7ee3611] MedicationRequest | prescribed 2025-11-10 | status completed
[MedicationRequest/8ff46e01-0333-fefb-6b5e-9f6740d55d90] MedicationRequest | prescribed 2025-11-10 | status completed
[MedicationRequest/8ff46e01-0333-fefb-881b-968118aa2f40] MedicationRequest | prescribed 2025-11-10 | status completed
[MedicationRequest/8ff46e01-0333-fefb-f0e1-cfc081e03b69] MedicationRequest | prescribed 2025-11-10 | status completed
[MedicationRequest/8ff46e01-0333-fefb-e5ec-bf946b3fdf85] MedicationRequest | prescribed 2019-02-22 | Acetaminophen 325 MG Oral Tablet | status completed | RxNorm 313782
[DocumentReference/9733939e-9ff2-9322-c737-a55ece3a8f15#1] Clinical note | 2019-02-22 | part 1 of 1 | 2019-02-22 # Chief Complaint No complaints. # History of Present Illness Lupe126 is a 39 year-old hispanic white female. Patient has a history of malignant neoplasm of head, face and neck, other specified diseases of jaws, medication review due (situation), full-time employment (finding), other specified disorders of teeth and supporting structures, dental caries, unspecified. # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with sprain (morphologic abnormality), sprain of wrist (disorder). ## Plan The patient was prescribed the following medications: - acetaminophen 325 mg oral tablet The patient was placed on a careplan: - physiotherapy care plan (record artifact)
[DocumentReference/2b583abb-ebce-d62b-2d63-1ad30fcccfc3#1] Clinical note | 2024-01-17 | part 1 of 1 | 2024-01-17 # Chief Complaint No complaints. # History of Present Illness Lupe126 is a 44 year-old hispanic white female. Patient has a history of part-time employment (finding), malignant neoplasm of head, face and neck, sprain (morphologic abnormality), other specified diseases of jaws, medication review due (situation), full-time employment (finding), sprain of ankle (disorder), sprain of wrist (disorder), viral sinusitis (disorder), other specified disorders of teeth and supporting structures, dental caries, unspecified. # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications acetaminophen 325 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The patient was prescribed the following medications: - simvastatin 10 mg oral tablet The patient was placed on a careplan: - hyperlipidemia clinical management plan (record artifact)
[DocumentReference/47fddcb0-4702-402b-2c7d-9be347439c2e#1] Clinical note | 2022-02-08 | part 1 of 1 | 2022-02-08 # Chief Complaint No complaints. # History of Present Illness Lupe126 is a 42 year-old hispanic white female. Patient has a history of part-time employment (finding), malignant neoplasm of head, face and neck, sprain (morphologic abnormality), other specified diseases of jaws, medication review due (situation), full-time employment (finding), sprain of wrist (disorder), viral sinusitis (disorder), other specified disorders of teeth and supporting structures, dental caries, unspecified. # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications acetaminophen 325 mg oral tablet # Assessment and Plan Patient is presenting with sprain (morphologic abnormality), sprain of ankle (disorder). ## Plan The patient was prescribed the following medications: - naproxen sodium 220 mg oral tablet The patient was placed on a careplan: - physiotherapy care plan (record artifact)
[MedicationRequest/8ff46e01-0333-fefb-8a46-b576798484c9] MedicationRequest | prescribed 2025-01-16 | Simvastatin 10 MG Oral Tablet | status completed | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8ff46e01-0333-fefb-7f78-a97308c8b605] MedicationRequest | prescribed 2024-01-17 | Simvastatin 10 MG Oral Tablet | status completed | reason: Hyperlipidemia (disorder) | RxNorm 314231
```

</details>

label: s
note: Cited MedicationRequest shows Simvastatin 10 MG Oral Tablet prescribed 2026-01-16, status active, reason Hyperlipidemia (disorder).

## 14. `current-meds:8446fe54#0#2`

Question: What medications is the patient currently prescribed?

Answer: Active prescriptions from 2025-10 are Simvastatin 10 MG Oral Tablet (for hyperlipidemia), lisinopril 10 MG Oral Tablet (for essential hypertension), and Alendronic acid 10 MG Oral Tablet (for osteoporosis). Also active since 2022-03-10 are rosuvastatin calcium 10 MG Oral Tablet [Crestor], carvedilol 25 MG Oral Tablet, aspirin 81 MG Oral Tablet, prasugrel 10 MG Oral Tablet, and losartan potassium 25 MG Oral Tablet. **Active since 2009-07-10 are 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet, Clopidogrel 75 MG Oral Tablet, Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray, and Simvastatin 20 MG Oral Tablet.**

Cards this sentence cites:

- `[MedicationRequest/8446fe54-5b2e-6a46-abfb-29ebed5ed8f5]` MedicationRequest | prescribed 2009-07-10 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
- `[MedicationRequest/8446fe54-5b2e-6a46-a1b3-bc484b4b6e59]` MedicationRequest | prescribed 2009-07-10 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
- `[MedicationRequest/8446fe54-5b2e-6a46-31e7-0fab4c5ed076]` MedicationRequest | prescribed 2009-07-10 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
- `[MedicationRequest/8446fe54-5b2e-6a46-2210-4b4518283f4c]` MedicationRequest | prescribed 2009-07-10 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961

<details><summary>Everything the model saw (49 cards)</summary>

```text
[Condition/8446fe54-5b2e-6a46-c855-6376bf616037] Condition | onset 2025-10-03 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/8446fe54-5b2e-6a46-3883-408ea2da0a37] Condition | onset 2025-05-15 | Nonproliferative diabetic retinopathy due to type II diabetes mellitus | clinical status active | SNOMED 1551000119108
[Condition/8446fe54-5b2e-6a46-2283-ccf89bdfa001] Condition | onset 2024-09-27 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8446fe54-5b2e-6a46-8ab7-b639a56aa55f] Condition | onset 2023-09-22 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/8446fe54-5b2e-6a46-169f-475724b93b14] Condition | onset 2022-03-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/8446fe54-5b2e-6a46-7c5e-428350d41910] Condition | onset 2022-03-08 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/8446fe54-5b2e-6a46-b854-dbfe1d5848d8] Condition | onset 2019-08-30 | Neuropathy due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 368581000119106
[Condition/8446fe54-5b2e-6a46-9883-d3e4fb3c92c7] Condition | onset 2017-08-18 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8446fe54-5b2e-6a46-90ec-9d5bb7f4215c] Condition | onset 2015-08-07 | Limited social contact (finding) | clinical status active | SNOMED 423315002
[Condition/8446fe54-5b2e-6a46-ac98-749a48641300] Condition | onset 2009-07-27 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/8446fe54-5b2e-6a46-ac45-606071904f4c] Condition | onset 2009-07-03 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/8446fe54-5b2e-6a46-19e1-02a0cca64803] Condition | onset 2009-07-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8446fe54-5b2e-6a46-9731-2ba07e7b3f8a] Condition | onset 2002-05-24 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/8446fe54-5b2e-6a46-5645-a8fdbdfcefa0] Condition | onset 1997-04-25 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8446fe54-5b2e-6a46-6984-e3082708b597] Condition | onset 1997-01-20 | Localized, primary osteoarthritis of the hand (disorder) | clinical status active | SNOMED 201834006
[Condition/8446fe54-5b2e-6a46-918b-8a35802414ef] Condition | onset 1996-11-29 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8446fe54-5b2e-6a46-8453-0b6ddcc40622] Condition | onset 1996-11-29 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/8446fe54-5b2e-6a46-71d0-e1231acfc548] Condition | onset 1996-04-19 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/8446fe54-5b2e-6a46-53e3-b8317bbea5b4] Condition | onset 1973-08-15 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/8446fe54-5b2e-6a46-efe6-1830fbd69235] Condition | onset 1971-06-11 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8446fe54-5b2e-6a46-a0b3-4dfcdfdaffac] Condition | onset 1965-06-04 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8446fe54-5b2e-6a46-26e1-de3ad83381e7] Condition | onset 1965-06-04 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8446fe54-5b2e-6a46-3a03-f8734c3aad20] Condition | onset 1961-05-26 | Received higher education (finding) | clinical status active | SNOMED 224299000
[MedicationRequest/8446fe54-5b2e-6a46-659f-46ecea0cf5ef] MedicationRequest | prescribed 2025-10-04 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8446fe54-5b2e-6a46-88a0-c7dd9e8fc1a1] MedicationRequest | prescribed 2025-10-03 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/8446fe54-5b2e-6a46-7320-4ef7c8ad8f40] MedicationRequest | prescribed 2025-10-03 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/8446fe54-5b2e-6a46-bf69-9fef69e23979] MedicationRequest | prescribed 2022-03-10 | rosuvastatin calcium 10 MG Oral Tablet [Crestor] | status active | RxNorm 859749
[MedicationRequest/8446fe54-5b2e-6a46-4de5-bb23365c2bff] MedicationRequest | prescribed 2022-03-10 | carvedilol 25 MG Oral Tablet | status active | RxNorm 200033
[MedicationRequest/8446fe54-5b2e-6a46-49d9-f1a38344333d] MedicationRequest | prescribed 2022-03-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/8446fe54-5b2e-6a46-3148-e44c765beb21] MedicationRequest | prescribed 2022-03-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/8446fe54-5b2e-6a46-2330-5a6c9a9f35f4] MedicationRequest | prescribed 2022-03-10 | losartan potassium 25 MG Oral Tablet | status active | RxNorm 979485
[MedicationRequest/8446fe54-5b2e-6a46-abfb-29ebed5ed8f5] MedicationRequest | prescribed 2009-07-10 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/8446fe54-5b2e-6a46-a1b3-bc484b4b6e59] MedicationRequest | prescribed 2009-07-10 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/8446fe54-5b2e-6a46-31e7-0fab4c5ed076] MedicationRequest | prescribed 2009-07-10 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/8446fe54-5b2e-6a46-2210-4b4518283f4c] MedicationRequest | prescribed 2009-07-10 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[Encounter/8446fe54-5b2e-6a46-f799-ff1c9d688587] Encounter | 2026-04-10 | Ophthalmic examination and evaluation (procedure) | class AMB | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-7463-6a2732ff7cd0] Encounter | 2026-03-06 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-f36c-8ce8c10cff85] Encounter | 2026-01-11 | Hospital admission (procedure) | class IMP | reason: Patient transfer to skilled nursing facility (procedure) | at CLAFLIN HILL CORPORATION
[Immunization/8446fe54-5b2e-6a46-dae8-760a54add250] Immunization | 2025-10-03 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/8446fe54-5b2e-6a46-cbe0-330eed1bd176] MedicationRequest | prescribed 2021-08-04 | status completed
[MedicationRequest/8446fe54-5b2e-6a46-448c-bb1e4a24ca5a] MedicationRequest | prescribed 2022-03-10 | status completed
[MedicationRequest/8446fe54-5b2e-6a46-3dfa-0a8aa3812f7d] MedicationRequest | prescribed 2018-11-18 | status completed
[MedicationRequest/8446fe54-5b2e-6a46-5113-44993fde61e4] MedicationRequest | prescribed 2019-10-14 | status completed
[MedicationRequest/8446fe54-5b2e-6a46-8d86-18f729728011] MedicationRequest | prescribed 2020-09-08 | status completed
[MedicationRequest/8446fe54-5b2e-6a46-d1b0-886d1cae3bc3] MedicationRequest | prescribed 2022-03-08 | status completed
[MedicationRequest/8446fe54-5b2e-6a46-cfc3-1a744fff8f0c] MedicationRequest | prescribed 2026-04-10 | status completed
[MedicationRequest/8446fe54-5b2e-6a46-48df-08b610367b3e] MedicationRequest | prescribed 2022-06-30 | status completed
[MedicationRequest/8446fe54-5b2e-6a46-e723-27e8c54fe12a] MedicationRequest | prescribed 2022-03-08 | status completed
[MedicationRequest/8446fe54-5b2e-6a46-9603-2c7a050dcc49] MedicationRequest | prescribed 2024-05-20 | status completed
```

</details>

label: s
note: All four cited cards (metoprolol succinate 100 MG ER, Clopidogrel 75 MG, Nitroglycerin 0.4 MG/ACTUAT spray, Simvastatin 20 MG) are prescribed 2009-07-10 with status active; names and doses match exactly.

## 15. `current-meds:9292c3d5#0#1`

Question: What medications is the patient currently prescribed?

Answer: The patient's active prescriptions, all prescribed 2011-08-22, are 24 HR metoprolol succinate 50 MG Extended Release Oral Tablet, prasugrel 10 MG Oral Tablet, aspirin 81 MG Oral Tablet, simvastatin 40 MG Oral Tablet, and lisinopril 2.5 MG Oral Tablet. **Other prescriptions in the record, including ibuprofen, naproxen sodium, amoxicillin, and amoxicillin/clavulanate, have status completed.**

Cards this sentence cites:

- `[MedicationRequest/9292c3d5-3db6-f4f9-413b-eedd619f333c]` MedicationRequest | prescribed 2024-10-15 | Ibuprofen 200 MG Oral Tablet | status completed | RxNorm 310965
- `[MedicationRequest/9292c3d5-3db6-f4f9-2ef8-1b3000d13edd]` MedicationRequest | prescribed 2022-06-08 | Naproxen sodium 220 MG Oral Tablet | status completed | RxNorm 849574
- `[MedicationRequest/9292c3d5-3db6-f4f9-8b41-e6deee80781b]` MedicationRequest | prescribed 2022-06-08 | Amoxicillin 250 MG Oral Capsule | status completed | RxNorm 308182
- `[MedicationRequest/9292c3d5-3db6-f4f9-0ce7-31822895d58f]` MedicationRequest | prescribed 2022-07-16 | amoxicillin 875 MG / clavulanate 125 MG Oral Tablet | status completed | reason: Acute infective cystitis (disorder) | RxNorm 562508

<details><summary>Everything the model saw (31 cards)</summary>

```text
[Condition/9292c3d5-3db6-f4f9-b5ec-3a44e8649597] Condition | onset 2026-04-26 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/9292c3d5-3db6-f4f9-861b-f7159312202f] Condition | onset 2026-04-26 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/9292c3d5-3db6-f4f9-483e-3d8d3b0f4690] Condition | onset 2026-04-26 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/9292c3d5-3db6-f4f9-38dc-147de4ac63a8] Condition | onset 2026-04-26 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/9292c3d5-3db6-f4f9-5b6c-1c0ed0fd0321] Condition | onset 2020-03-22 | Opioid abuse | clinical status active | SNOMED 5602001
[Condition/9292c3d5-3db6-f4f9-f835-25af6c77c701] Condition | onset 2011-08-22 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/9292c3d5-3db6-f4f9-54d1-d4b6d2666838] Condition | onset 2011-08-22 | Acute ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401303003
[Condition/9292c3d5-3db6-f4f9-2b48-fd31edda50b0] Condition | onset 2010-03-21 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/9292c3d5-3db6-f4f9-1b0c-65cb31846f75] Condition | onset 2005-05-29 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/9292c3d5-3db6-f4f9-2a82-9615e45bb615] Condition | onset 1986-05-04 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
[Condition/9292c3d5-3db6-f4f9-24a0-fe08e411b951] Condition | onset 1986-05-04 | Serving in military service (finding) | clinical status active | SNOMED 1187604002
[Condition/9292c3d5-3db6-f4f9-97fc-b779fe5ffdd4] Condition | onset 1985-04-28 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/9292c3d5-3db6-f4f9-c2ad-ca0afa2369e8] MedicationRequest | prescribed 2011-08-22 | 24 HR metoprolol succinate 50 MG Extended Release Oral Tablet | status active | RxNorm 866436
[MedicationRequest/9292c3d5-3db6-f4f9-b955-8ddb9b72de69] MedicationRequest | prescribed 2011-08-22 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/9292c3d5-3db6-f4f9-8b49-28e15899c04a] MedicationRequest | prescribed 2011-08-22 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/9292c3d5-3db6-f4f9-7675-f5ee99ae0c4e] MedicationRequest | prescribed 2011-08-22 | simvastatin 40 MG Oral Tablet | status active | RxNorm 198211
[MedicationRequest/9292c3d5-3db6-f4f9-2744-8b9a3e3302b8] MedicationRequest | prescribed 2011-08-22 | lisinopril 2.5 MG Oral Tablet | status active | RxNorm 311353
[Encounter/9292c3d5-3db6-f4f9-f8cd-08dfcc81ed12] Encounter | 2026-04-26 | General examination of patient (procedure) | class AMB | at COMMUNITY HEALTH PROGRAMS INC
[Encounter/9292c3d5-3db6-f4f9-2526-cf0c3fc1dcaa] Encounter | 2025-08-10 | Encounter for check up (procedure) | class AMB | reason: Gingivitis (disorder) | at Pittsfield Outpatient Clinic
[Encounter/9292c3d5-3db6-f4f9-d85c-7f88671a1881] Encounter | 2025-08-03 | Encounter for symptom (procedure) | class AMB | reason: Acute viral pharyngitis (disorder) | at Pittsfield Outpatient Clinic
[Immunization/9292c3d5-3db6-f4f9-2e74-b2ab508532b8] Immunization | 2026-04-26 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/9292c3d5-3db6-f4f9-413b-eedd619f333c] MedicationRequest | prescribed 2024-10-15 | Ibuprofen 200 MG Oral Tablet | status completed | RxNorm 310965
[DocumentReference/cc209432-2e7a-bbd5-50b2-aa410955342b#1] Clinical note | 2011-08-22 | part 1 of 1 | 2011-08-22 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 43 year-old nonhispanic white male. Patient has a history of disorder of teeth and/or supporting structures, full-time employment (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with history of myocardial infarction (situation). ## Plan The patient was prescribed the following medications: - aspirin 81 mg oral tablet - 24 hr metoprolol succinate 50 mg extended release oral tablet - simvastatin 40 mg oral tablet - lisinopril 2.5 mg oral tablet - prasugrel 10 mg oral tablet The patient was placed on a careplan: - discharge care plan (record artifact)
[DocumentReference/6f157407-95e3-c2ff-0d2a-d52c1b6779b6#1] Clinical note | 2022-06-08 | part 1 of 1 | 2022-06-08 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 54 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with otitis media (disorder), acute infective cystitis (disorder). ## Plan The patient was prescribed the following medications: - amoxicillin 250 mg oral capsule - naproxen sodium 220 mg oral tablet
[MedicationRequest/9292c3d5-3db6-f4f9-2ef8-1b3000d13edd] MedicationRequest | prescribed 2022-06-08 | Naproxen sodium 220 MG Oral Tablet | status completed | RxNorm 849574
[MedicationRequest/9292c3d5-3db6-f4f9-8b41-e6deee80781b] MedicationRequest | prescribed 2022-06-08 | Amoxicillin 250 MG Oral Capsule | status completed | RxNorm 308182
[DocumentReference/2e6981ed-9c54-471b-712b-5d48eb5ef7ad#1] Clinical note | 2024-10-15 | part 1 of 1 | 2024-10-15 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 56 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), concussion with no loss of consciousness (disorder), medication review due (situation), otitis media (disorder), concussion injury of brain (disorder), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), acute infective cystitis (disorder), gingivitis (disorder), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications amoxicillin 875 mg / clavulanate 125 mg oral tablet; amoxicillin 250 mg oral capsule; cephalexin 500 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with sprain (morphologic abnormality), sprain of ankle (disorder). ## Plan The patient was prescribed the following medications: - ibuprofen 200 mg oral tablet The patient was placed on a careplan: - physiotherapy care plan (record artifact)
[DocumentReference/686906dc-15c8-9d97-a493-c92520cf0b04#1] Clinical note | 2023-04-23 | part 1 of 1 | 2023-04-23 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 55 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), acute infective cystitis (disorder), otitis media (disorder), gingivitis (disorder), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications amoxicillin 875 mg / clavulanate 125 mg oral tablet; amoxicillin 250 mg oral capsule; cephalexin 500 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - prophylaxis adult
[MedicationRequest/9292c3d5-3db6-f4f9-0ce7-31822895d58f] MedicationRequest | prescribed 2022-07-16 | amoxicillin 875 MG / clavulanate 125 MG Oral Tablet | status completed | reason: Acute infective cystitis (disorder) | RxNorm 562508
[MedicationRequest/9292c3d5-3db6-f4f9-b91c-acd36b418571] MedicationRequest | prescribed 2022-07-16 | amoxicillin 875 MG / clavulanate 125 MG Oral Tablet | status completed | reason: Acute infective cystitis (disorder) | RxNorm 562508
[DocumentReference/6d36946b-c72f-9887-ce5b-19ef7de6369c#1] Clinical note | 2022-07-17 | part 1 of 2 | 2022-07-17 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 54 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), acute infective cystitis (disorder), otitis media (disorder), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications amoxicillin 875 mg / clavulanate 125 mg oral tablet; amoxicillin 250 mg oral capsule; naproxen sodium 220 mg oral tablet
```

</details>

label: s?
note: Cited cards show ibuprofen 200 MG, naproxen sodium 220 MG, amoxicillin 250 MG and amoxicillin/clavulanate (both cards) all status completed, and every non-active MedicationRequest card is completed. Cephalexin appears only in note medication lists with no status, which some might count against the 'other prescriptions' generalization.

## 16. `latest-lab-718-7:e56a8cde#0#1`

Question: What was the patient's most recent hemoglobin result, and when was it measured?

Answer: The most recent blood hemoglobin result was 12.046 g/dL, measured on 2021-12-02 as part of a CBC panel. **The prior blood hemoglobin was 17.444 g/dL on 2016-11-03.**

Cards this sentence cites:

- `[Observation/e56a8cde-8395-a37d-d5b6-19adbbada9ba]` Observation (laboratory) | 2016-11-03 | Hemoglobin [Mass/volume] in Blood = 17.444 g/dL | status final | LOINC 718-7

<details><summary>Everything the model saw (56 cards)</summary>

```text
[Condition/e56a8cde-8395-a37d-f7ae-15d35f13e9f0] Condition | onset 2025-12-25 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/e56a8cde-8395-a37d-80d3-3984f14d8bb3] Condition | onset 2025-12-25 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/e56a8cde-8395-a37d-5c7c-75429c6f1e56] Condition | onset 2025-12-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/e56a8cde-8395-a37d-354e-df92238c35a7] Condition | onset 2025-12-25 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/e56a8cde-8395-a37d-6690-7ef5746552bd] Condition | onset 2017-11-09 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/e56a8cde-8395-a37d-922a-d32061194c0b] Condition | onset 2016-11-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/e56a8cde-8395-a37d-e775-23849ffbe97b] Condition | onset 2014-02-01 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/e56a8cde-8395-a37d-a82c-6129bc784139] Condition | onset 2014-02-01 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/e56a8cde-8395-a37d-64b8-86023f198a46] Condition | onset 2014-02-01 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/e56a8cde-8395-a37d-e547-8e085bacfa8e] Condition | onset 2007-09-13 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/e56a8cde-8395-a37d-37b4-500cf9e797e9] Condition | onset 2005-09-01 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/e56a8cde-8395-a37d-d5cb-6239a28a0055] Condition | onset 2003-12-16 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/e56a8cde-8395-a37d-4d5f-670d3e1632bc] Condition | onset 2003-12-16 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/e56a8cde-8395-a37d-1853-568436ee1ea2] Condition | onset 2001-08-20 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/e56a8cde-8395-a37d-810b-643d651149ba] Condition | onset 2001-08-18 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/e56a8cde-8395-a37d-2761-7d0bfc799087] Condition | onset 2001-08-09 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/e56a8cde-8395-a37d-ed31-c4144dbefb9e] Condition | onset 1996-05-17 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
[Condition/e56a8cde-8395-a37d-333f-0835bee4de98] Condition | onset 1991-06-13 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/e56a8cde-8395-a37d-30cd-5f4f9de67da3] Condition | onset 1967-07-27 | Lack of access to transportation (finding) | clinical status active | SNOMED 713458007
[Condition/e56a8cde-8395-a37d-ac70-0b466edf16a1] Condition | onset 1963-07-18 | Transport problem (finding) | clinical status active | SNOMED 266934004
[Condition/e56a8cde-8395-a37d-99e6-93fe1e3f6036] Condition | onset 1963-07-18 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/e56a8cde-8395-a37d-0c1b-7da0b396a0c4] MedicationRequest | prescribed 2026-01-01 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/e56a8cde-8395-a37d-f153-06ed5ef5b40a] MedicationRequest | prescribed 2025-12-25 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/e56a8cde-8395-a37d-b70b-d6ff9e66fb91] MedicationRequest | prescribed 2025-12-25 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/e56a8cde-8395-a37d-1cff-386c29158923] MedicationRequest | prescribed 2025-12-25 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/e56a8cde-8395-a37d-f778-f1044e9a8316] MedicationRequest | prescribed 2003-12-16 | atorvastatin 10 MG Oral Tablet | status active | RxNorm 617312
[MedicationRequest/e56a8cde-8395-a37d-e36e-ab680e0ad841] MedicationRequest | prescribed 2003-12-16 | hydrochlorothiazide 25 MG / lisinopril 20 MG Oral Tablet | status active | RxNorm 197887
[MedicationRequest/e56a8cde-8395-a37d-d237-6e376bbcb9a6] MedicationRequest | prescribed 2003-12-16 | metoprolol tartrate 25 MG Oral Tablet | status active | RxNorm 866924
[MedicationRequest/e56a8cde-8395-a37d-2fb4-edeac8b69b00] MedicationRequest | prescribed 2003-12-16 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/e56a8cde-8395-a37d-228f-f6135c165caa] MedicationRequest | prescribed 2003-12-16 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/e56a8cde-8395-a37d-eee1-8d05287f0e29] MedicationRequest | prescribed 2001-08-16 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/e56a8cde-8395-a37d-d36b-2e3fc9df975e] MedicationRequest | prescribed 2001-08-16 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/e56a8cde-8395-a37d-a8c0-f9ed9ed3ea83] MedicationRequest | prescribed 2001-08-16 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/e56a8cde-8395-a37d-321f-ecd1d25263ad] MedicationRequest | prescribed 2001-08-16 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/e56a8cde-8395-a37d-9456-c58ec0c7de32] MedicationRequest | prescribed 1949-01-17 | diphenhydrAMINE Hydrochloride 25 MG Oral Tablet | status active | RxNorm 1049630
[AllergyIntolerance/e56a8cde-8395-a37d-b318-8f34a7d6b5f7] AllergyIntolerance | recorded 1946-06-09 | Animal dander (substance) | allergy, category environment, criticality low | clinical status active | reactions: Eruption of skin (disorder); Rhinoconjunctivitis (disorder) | SNOMED 264287008
[AllergyIntolerance/e56a8cde-8395-a37d-a098-9831a40ac85b] AllergyIntolerance | recorded 1946-06-09 | Mold (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 84489001
[AllergyIntolerance/e56a8cde-8395-a37d-85d4-fe7519012219] AllergyIntolerance | recorded 1946-06-09 | House dust mite (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 260147004
[AllergyIntolerance/e56a8cde-8395-a37d-60c2-b75e4a4d4513] AllergyIntolerance | recorded 1946-06-09 | Tree pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 782576004
[AllergyIntolerance/e56a8cde-8395-a37d-5834-224d1127b6f9] AllergyIntolerance | recorded 1946-06-09 | Grass pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 256277009
[AllergyIntolerance/e56a8cde-8395-a37d-2daa-dbe0dbcf6ecf] AllergyIntolerance | recorded 1946-06-09 | Shellfish (substance) | allergy, category food, criticality low | clinical status active | reactions: Dyspnea (finding); Allergic angioedema (disorder); Itching (finding); Cough (finding); Diarrhea (finding) | SNOMED 735029006
[AllergyIntolerance/e56a8cde-8395-a37d-1508-bdb84bdc4c5d] AllergyIntolerance | recorded 1946-06-09 | Allergic disposition (finding) | allergy, category environment, criticality low | clinical status active | SNOMED 609328004
[Encounter/e56a8cde-8395-a37d-9f47-5b69723a8690] Encounter | 2026-01-01 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Encounter/e56a8cde-8395-a37d-2450-250d53d64dc7] Encounter | 2025-12-25 | General examination of patient (procedure) | class AMB | at SOUTH SHORE PRIMARY CARE PC
[Encounter/e56a8cde-8395-a37d-20eb-f707e34a4164] Encounter | 2024-12-20 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Immunization/e56a8cde-8395-a37d-7cd1-bb3bac5572f3] Immunization | 2025-12-25 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/e56a8cde-8395-a37d-4226-8f740b76c934] Observation (laboratory) | 2021-12-02 | Hemoglobin [Mass/volume] in Blood = 12.046 g/dL | status final | LOINC 718-7
[Observation/e56a8cde-8395-a37d-d5b6-19adbbada9ba] Observation (laboratory) | 2016-11-03 | Hemoglobin [Mass/volume] in Blood = 17.444 g/dL | status final | LOINC 718-7
[Observation/e56a8cde-8395-a37d-1ef8-6ba8ea1d1430] Observation (laboratory) | 2021-11-03 | Hemoglobin [Presence] in Urine by Test strip = Urine blood test = + (finding) | status final | LOINC 5794-3
[Observation/e56a8cde-8395-a37d-1f52-c1c154141040] Observation (laboratory) | 2020-11-29 | Glucose [Mass/volume] in Blood = 97.39 mg/dL | status final | LOINC 2339-0
[Observation/e56a8cde-8395-a37d-1b9c-9f8ffab8b485] Observation (laboratory) | 2026-01-01 | Glucose [Mass/volume] in Blood = 68.84 mg/dL | status final | LOINC 2339-0
[Observation/e56a8cde-8395-a37d-86a6-60c7b0e163a5] Observation (laboratory) | 2024-12-20 | Glucose [Mass/volume] in Blood = 69.59 mg/dL | status final | LOINC 2339-0
[Observation/e56a8cde-8395-a37d-5037-60397fbc6883] Observation (laboratory) | 2023-12-21 | Glucose [Mass/volume] in Blood = 72.42 mg/dL | status final | LOINC 2339-0
[Immunization/e56a8cde-8395-a37d-ded2-6b37ccc4ca99] Immunization | 2021-02-18 | COVID-19, mRNA, LNP-S, PF, 100 mcg/0.5mL dose or 50 mcg/0.25mL dose | status completed | CVX 207
[Immunization/e56a8cde-8395-a37d-7678-458aa2ed7c54] Immunization | 2021-01-21 | COVID-19, mRNA, LNP-S, PF, 100 mcg/0.5mL dose or 50 mcg/0.25mL dose | status completed | CVX 207
[DiagnosticReport/e56a8cde-8395-a37d-3f4f-0347df4d9217] DiagnosticReport | 2021-12-02 | CBC panel - Blood by Automated count | results: Leukocytes [#/volume] in Blood by Automated count 4.7251 10*3/uL; Erythrocytes [#/volume] in Blood by Automated count 5.3883 10*6/uL; Hemoglobin [Mass/volume] in Blood 12.046 g/dL; Hematocrit [Volume Fraction] of Blood by Automated count 39.229 %; MCV [Entitic mean volume] in Red Blood Cells by Automated count 80.875 fL; MCH [Entitic mass] by Automated count 32.2 pg; MCHC [Entitic Mass/volume] in Red Blood Cells by Automated count 33.52 g/dL; Erythrocyte [DistWidth] in Blood by Automated count 43.265 fL; Platelets [#/volume] in Blood by Automated count 379.77 10*3/uL; Platelet distribution width [Entitic volume] in Blood by Automated count 472.58 fL; Platelet [Entitic mean volume] in Blood by Automated count 11.132 fL | LOINC 58410-2
```

</details>

label: s
note: The only blood hemoglobin (LOINC 718-7) cards are 2021-12-02 (12.046 g/dL) and 2016-11-03 (17.444 g/dL), so the cited 2016-11-03 value of 17.444 g/dL is correctly the prior one; the urine strip test is a different measure.

## 17. `prescribed-for-hyperlipidemia:8ff46e01#0#1`

Question: Which medications have been prescribed for the patient's hyperlipidemia?

Answer: Simvastatin 10 MG Oral Tablet is the only medication the record explicitly links to hyperlipidemia; it was prescribed on 2024-01-17 and 2025-01-16 (both completed) and again on 2026-01-16 (status active). **Rosuvastatin calcium 10 MG Oral Tablet was also prescribed on 2025-11-10 and is active, but no reason is listed for that prescription.**

Cards this sentence cites:

- `[MedicationRequest/8ff46e01-0333-fefb-6306-60b207f6bcda]` MedicationRequest | prescribed 2025-11-10 | rosuvastatin calcium 10 MG Oral Tablet | status active | RxNorm 859747

<details><summary>Everything the model saw (35 cards)</summary>

```text
[Condition/8ff46e01-0333-fefb-e078-a2c79f9b5570] Condition | onset 2025-11-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/8ff46e01-0333-fefb-ca9a-9c89d481d534] Condition | onset 2025-11-10 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/8ff46e01-0333-fefb-f69f-b001b28f2b81] Condition | onset 2023-12-27 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8ff46e01-0333-fefb-d37b-fa17bc4619e6] Condition | onset 2023-12-27 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/8ff46e01-0333-fefb-1085-7240f563162c] Condition | onset 2023-12-27 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8ff46e01-0333-fefb-0d5f-96af345c8178] Condition | onset 2023-12-27 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8ff46e01-0333-fefb-a724-e7508612ceb2] Condition | onset 2015-12-19 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/8ff46e01-0333-fefb-c4b8-0da5f4d9d6af] Condition | onset 2010-09-29 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/8ff46e01-0333-fefb-3eac-29a6b80382d5] Condition | onset 1998-06-27 | Recurrent urinary tract infection (disorder) | clinical status active | SNOMED 197927001
[Condition/8ff46e01-0333-fefb-1001-1cc553e61d65] Condition | onset 1998-02-04 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[Condition/8ff46e01-0333-fefb-2118-3da43e594952] Condition | onset 1995-01-18 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[Condition/8ff46e01-0333-fefb-400e-c9db591e5ada] Condition | onset 1988-12-14 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8ff46e01-0333-fefb-6f8d-08005729c21a] Condition | onset 1980-10-17 | History of seizure (situation) | clinical status active | SNOMED 1290882004
[Condition/8ff46e01-0333-fefb-334a-c4ab11856973] Condition | onset 1980-10-17 | Seizure disorder (disorder) | clinical status active | SNOMED 128613002
[Condition/8ff46e01-0333-fefb-493a-f8d458075b36] Condition | onset 1980-04-22 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/8ff46e01-0333-fefb-081b-4d95e98b7814] MedicationRequest | prescribed 2026-01-16 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8ff46e01-0333-fefb-cca1-202b10a1b90d] MedicationRequest | prescribed 2025-11-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/8ff46e01-0333-fefb-6306-60b207f6bcda] MedicationRequest | prescribed 2025-11-10 | rosuvastatin calcium 10 MG Oral Tablet | status active | RxNorm 859747
[MedicationRequest/8ff46e01-0333-fefb-5a32-7c872c74242b] MedicationRequest | prescribed 2025-11-10 | atenolol 50 MG Oral Tablet | status active | RxNorm 197381
[MedicationRequest/8ff46e01-0333-fefb-5632-79d28eb2f69d] MedicationRequest | prescribed 2025-11-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/8ff46e01-0333-fefb-0f09-741ffc0ecb79] MedicationRequest | prescribed 2025-11-10 | lisinopril 10 MG Oral Tablet | status active | RxNorm 314076
[Encounter/8ff46e01-0333-fefb-2842-108bae2a93b7] Encounter | 2026-01-16 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at STEWARD HOLY FAMILY HOSPITAL INC
[Encounter/8ff46e01-0333-fefb-deac-7d54a2e717b0] Encounter | 2025-12-31 | General examination of patient (procedure) | class AMB | at GREATER LAWRENCE FAMILY HEALTH CENTER INC
[Encounter/8ff46e01-0333-fefb-bdb4-35663b36a4c8] Encounter | 2025-11-10 | Emergency room admission (procedure) | class EMER | reason: Myocardial infarction (disorder) | at Fitchburg Outpatient Clinic
[Immunization/8ff46e01-0333-fefb-0b35-b6fa97749e42] Immunization | 2025-12-31 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/8ff46e01-0333-fefb-8a46-b576798484c9] MedicationRequest | prescribed 2025-01-16 | Simvastatin 10 MG Oral Tablet | status completed | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8ff46e01-0333-fefb-7f78-a97308c8b605] MedicationRequest | prescribed 2024-01-17 | Simvastatin 10 MG Oral Tablet | status completed | reason: Hyperlipidemia (disorder) | RxNorm 314231
[CarePlan/8ff46e01-0333-fefb-721e-f6c3b85f514e] CarePlan | started 2024-01-17 | Hyperlipidemia clinical management plan (record artifact) | status active | activities: Low salt diet education (procedure); Physical exercises (regime/therapy)
[DocumentReference/2b583abb-ebce-d62b-2d63-1ad30fcccfc3#1] Clinical note | 2024-01-17 | part 1 of 1 | 2024-01-17 # Chief Complaint No complaints. # History of Present Illness Lupe126 is a 44 year-old hispanic white female. Patient has a history of part-time employment (finding), malignant neoplasm of head, face and neck, sprain (morphologic abnormality), other specified diseases of jaws, medication review due (situation), full-time employment (finding), sprain of ankle (disorder), sprain of wrist (disorder), viral sinusitis (disorder), other specified disorders of teeth and supporting structures, dental caries, unspecified. # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications acetaminophen 325 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The patient was prescribed the following medications: - simvastatin 10 mg oral tablet The patient was placed on a careplan: - hyperlipidemia clinical management plan (record artifact)
[MedicationRequest/8ff46e01-0333-fefb-071f-4a32d7ee3611] MedicationRequest | prescribed 2025-11-10 | status completed
[Encounter/8ff46e01-0333-fefb-1e97-8e040a11da81] Encounter | 2024-01-17 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at STEWARD HOLY FAMILY HOSPITAL INC
[Encounter/8ff46e01-0333-fefb-9ac8-1737e111a289] Encounter | 2025-01-16 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at STEWARD HOLY FAMILY HOSPITAL INC
[MedicationRequest/8ff46e01-0333-fefb-6b5e-9f6740d55d90] MedicationRequest | prescribed 2025-11-10 | status completed
[MedicationRequest/8ff46e01-0333-fefb-881b-968118aa2f40] MedicationRequest | prescribed 2025-11-10 | status completed
[MedicationRequest/8ff46e01-0333-fefb-f0e1-cfc081e03b69] MedicationRequest | prescribed 2025-11-10 | status completed
```

</details>

label: s
note: Cited card shows rosuvastatin calcium 10 MG Oral Tablet prescribed 2025-11-10, status active, with no reason field.

## 18. `latest-lab-18262-6:d14e9292#0#0`

Question: What was the patient's most recent LDL cholesterol result, and when was it measured?

Answer: **The most recent LDL cholesterol (direct assay) result was 73.93 mg/dL, measured on 2025-05-15.** The prior result was 81.28 mg/dL on 2022-05-12.

Cards this sentence cites:

- `[Observation/d14e9292-537d-9ab5-97be-903717da54bb]` Observation (laboratory) | 2025-05-15 | Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay = 73.93 mg/dL | status final | LOINC 18262-6
- `[DiagnosticReport/d14e9292-537d-9ab5-247c-23f70af07df4]` DiagnosticReport | 2025-05-15 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 154.16 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 126.13 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 73.93 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 55.01 mg/dL | LOINC 57698-3

<details><summary>Everything the model saw (19 cards)</summary>

```text
[Condition/d14e9292-537d-9ab5-d719-3444368e63f2] Condition | onset 2026-07-15 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/d14e9292-537d-9ab5-f5e1-81b5b14a8a8d] Condition | onset 2025-05-15 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/d14e9292-537d-9ab5-3fd5-303fdca87268] Condition | onset 2024-03-30 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/d14e9292-537d-9ab5-2de8-ff9612c4dc80] Condition | onset 2022-05-12 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/d14e9292-537d-9ab5-c205-6c7176a1d8e2] Condition | onset 2013-05-02 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/d14e9292-537d-9ab5-3a99-525060b2d8c3] Condition | onset 2009-04-23 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Encounter/d14e9292-537d-9ab5-75a2-660a8b4ef3eb] Encounter | 2026-07-15 | Admission to surgical department (procedure) | class IMP | reason: Sterilization requested (situation) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-cd48-29e15dfdc267] Encounter | 2026-06-26 | Consultation for treatment (procedure) | class AMB | reason: Sterilization requested (situation) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-a94e-2f619d52ef93] Encounter | 2026-03-12 | Encounter for check up (procedure) | class AMB | reason: Epidermal burn of skin (disorder) | at MOUNT AUBURN HOSPITAL
[Observation/d14e9292-537d-9ab5-97be-903717da54bb] Observation (laboratory) | 2025-05-15 | Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay = 73.93 mg/dL | status final | LOINC 18262-6
[Observation/d14e9292-537d-9ab5-6444-bc231a3a4203] Observation (laboratory) | 2022-05-12 | Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay = 81.28 mg/dL | status final | LOINC 18262-6
[Observation/d14e9292-537d-9ab5-d72e-4581e7198e01] Observation (laboratory) | 2025-05-15 | Cholesterol [Mass/volume] in Serum or Plasma = 154.16 mg/dL | status final | LOINC 2093-3
[Observation/d14e9292-537d-9ab5-dd19-909e7a3ab50d] Observation (laboratory) | 2022-05-12 | Cholesterol [Mass/volume] in Serum or Plasma = 157.9 mg/dL | status final | LOINC 2093-3
[DiagnosticReport/d14e9292-537d-9ab5-247c-23f70af07df4] DiagnosticReport | 2025-05-15 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 154.16 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 126.13 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 73.93 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 55.01 mg/dL | LOINC 57698-3
[DiagnosticReport/d14e9292-537d-9ab5-5472-e0204c5ab213] DiagnosticReport | 2022-05-12 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 157.9 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 114.8 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 81.28 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 53.67 mg/dL | LOINC 57698-3
[Observation/d14e9292-537d-9ab5-9f71-917261302190] Observation (laboratory) | 2025-05-15 | Cholesterol in HDL [Mass/volume] in Serum or Plasma = 55.01 mg/dL | status final | LOINC 2085-9
[Observation/d14e9292-537d-9ab5-17f8-5e9caf327ec3] Observation (laboratory) | 2022-05-12 | Cholesterol in HDL [Mass/volume] in Serum or Plasma = 53.67 mg/dL | status final | LOINC 2085-9
[DocumentReference/5d7e8894-208a-874e-33ac-3649b0d730b4#2] Clinical note | 2025-05-15 | part 2 of 2 | # Assessment and Plan Patient is presenting with medication review due (situation), full-time employment (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - screening for drug abuse (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - lipid panel with direct ldl - serum or plasma - cbc panel - blood by automated count - generalized anxiety disorder 7 item (gad-7) - patient health questionnaire 2 item (phq-2) [reported] - drug abuse screening test-10 [dast-10]
[DocumentReference/be555e47-465e-8f07-752b-9f79ebf5e7be#2] Clinical note | 2022-05-12 | part 2 of 2 | # Assessment and Plan Patient is presenting with victim of intimate partner abuse (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf, td (adult), 5 lf tetanus toxoid, preservative free, adsorbed. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - screening for domestic abuse (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - assessment using alcohol use disorders identification test - consumption (procedure) The following lab reports were completed: - lipid panel with direct ldl - serum or plasma - humiliation, afraid, rape, and kick questionnaire [hark] - patient health questionnaire 2 item (phq-2) [reported] - alcohol use disorder identification test - consumption [audit-c]
```

</details>

label: s
note: Direct LDL cards are 2025-05-15 (73.93 mg/dL) and 2022-05-12 (81.28 mg/dL); the cited 2025-05-15 observation and lipid panel give 73.93 mg/dL, the latest.

## 19. `last-visit:d14e9292#0#0`

Question: When was the patient's most recent visit, and what kind of visit was it?

Answer: **The patient's most recent visit was on 2026-07-15, an inpatient admission to the surgical department at MOUNT AUBURN HOSPITAL for the reason "Sterilization requested."** A history of tubal ligation is recorded with onset on the same date, 2026-07-15.

Cards this sentence cites:

- `[Encounter/d14e9292-537d-9ab5-75a2-660a8b4ef3eb]` Encounter | 2026-07-15 | Admission to surgical department (procedure) | class IMP | reason: Sterilization requested (situation) | at MOUNT AUBURN HOSPITAL

<details><summary>Everything the model saw (19 cards)</summary>

```text
[Condition/d14e9292-537d-9ab5-d719-3444368e63f2] Condition | onset 2026-07-15 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/d14e9292-537d-9ab5-f5e1-81b5b14a8a8d] Condition | onset 2025-05-15 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/d14e9292-537d-9ab5-3fd5-303fdca87268] Condition | onset 2024-03-30 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/d14e9292-537d-9ab5-2de8-ff9612c4dc80] Condition | onset 2022-05-12 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/d14e9292-537d-9ab5-c205-6c7176a1d8e2] Condition | onset 2013-05-02 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/d14e9292-537d-9ab5-3a99-525060b2d8c3] Condition | onset 2009-04-23 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Encounter/d14e9292-537d-9ab5-75a2-660a8b4ef3eb] Encounter | 2026-07-15 | Admission to surgical department (procedure) | class IMP | reason: Sterilization requested (situation) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-cd48-29e15dfdc267] Encounter | 2026-06-26 | Consultation for treatment (procedure) | class AMB | reason: Sterilization requested (situation) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-a94e-2f619d52ef93] Encounter | 2026-03-12 | Encounter for check up (procedure) | class AMB | reason: Epidermal burn of skin (disorder) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-4838-2eb3f73199d8] Encounter | 2020-07-16 | Postnatal visit (regime/therapy) | class AMB | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-1dd3-33a421d5bfd3] Encounter | 2017-11-23 | Postnatal visit (regime/therapy) | class AMB | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-b610-b0e5d0d48258] Encounter | 2020-04-16 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-d65f-46bee4e6fd1a] Encounter | 2020-05-14 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-b502-516bf9817f77] Encounter | 2020-05-28 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-c51a-f0a903c02bfc] Encounter | 2020-02-20 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at MOUNT AUBURN HOSPITAL
[Encounter/d14e9292-537d-9ab5-3e80-1532df5f1179] Encounter | 2020-01-23 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at MOUNT AUBURN HOSPITAL
[Condition/d14e9292-537d-9ab5-8df5-9cc66cd66320] Condition | onset 2025-05-15 | Medication review due (situation) | clinical status resolved | resolved 2025-05-15 | SNOMED 314529007
[Condition/d14e9292-537d-9ab5-5a63-386b21bc2d6e] Condition | onset 2019-05-09 | Medication review due (situation) | clinical status resolved | resolved 2022-05-12 | SNOMED 314529007
[Immunization/d14e9292-537d-9ab5-9519-1481d5ace894] Immunization | 2021-05-13 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
```

</details>

label: s
note: The 2026-07-15 encounter is the latest of all encounters seen; it is class IMP, Admission to surgical department, reason Sterilization requested, at MOUNT AUBURN HOSPITAL.

## 20. `last-er-visit:7280f7f8#0#0`

Question: Why was the patient last seen in the emergency department, and when?

Answer: **The patient was last seen in the emergency department on 2023-09-13, an emergency room admission at BLISSFUL HOMECARE, LLC with the reason listed as Overdose (disorder).**

Cards this sentence cites:

- `[Encounter/7280f7f8-315d-7c6a-2f4a-ef77bf8ed805]` Encounter | 2023-09-13 | Emergency room admission (procedure) | class EMER | reason: Overdose (disorder) | at BLISSFUL HOMECARE, LLC

<details><summary>Everything the model saw (43 cards)</summary>

```text
[Condition/7280f7f8-315d-7c6a-5183-1fc53612d856] Condition | onset 2026-04-12 | Alzheimer's disease (disorder) | clinical status active | SNOMED 26929004
[Condition/7280f7f8-315d-7c6a-069f-25fdb34e3e53] Condition | onset 2025-04-06 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/7280f7f8-315d-7c6a-06ae-a26712c6cfb7] Condition | onset 2024-03-31 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/7280f7f8-315d-7c6a-84b2-d6045a9b8deb] Condition | onset 2018-11-12 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/7280f7f8-315d-7c6a-60b8-1b2b3b190d66] Condition | onset 2018-11-04 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/7280f7f8-315d-7c6a-eee1-33d3eda16b26] Condition | onset 2014-02-16 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/7280f7f8-315d-7c6a-23b9-2a24d0c43093] Condition | onset 2014-02-16 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/7280f7f8-315d-7c6a-f371-666500850eb4] Condition | onset 2014-02-02 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/7280f7f8-315d-7c6a-b5ea-aa0955ebc2c7] Condition | onset 2010-01-10 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/7280f7f8-315d-7c6a-929f-e845c91bba18] Condition | onset 1993-02-06 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/7280f7f8-315d-7c6a-6159-244929402415] Condition | onset 1991-07-09 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/7280f7f8-315d-7c6a-7561-551dd4fb980c] Condition | onset 1990-11-11 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/7280f7f8-315d-7c6a-69cb-9f6bde195716] Condition | onset 1990-10-25 | Impacted molars (disorder) | clinical status active | SNOMED 196416002
[Condition/7280f7f8-315d-7c6a-e183-7fc41f06abde] Condition | onset 1990-02-06 | Chronic intractable migraine without aura (disorder) | clinical status active | SNOMED 124171000119105
[Condition/7280f7f8-315d-7c6a-57cd-16215a141add] Condition | onset 1988-11-06 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/7280f7f8-315d-7c6a-7c25-7a247f43e721] Condition | onset 1981-01-18 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/7280f7f8-315d-7c6a-50ac-70390520f5d8] Condition | onset 1981-01-18 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/7280f7f8-315d-7c6a-a35c-5f2c4404e1cd] Condition | onset 1971-02-18 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/7280f7f8-315d-7c6a-cf3c-1559c1e270a8] Condition | onset 1964-12-20 | Housing unsatisfactory (finding) | clinical status active | SNOMED 105531004
[Condition/7280f7f8-315d-7c6a-3735-89103641aea2] Condition | onset 1964-12-20 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/7280f7f8-315d-7c6a-d103-5f5cf25ace53] MedicationRequest | prescribed 2026-04-13 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/7280f7f8-315d-7c6a-dd3c-435b565b36d4] MedicationRequest | prescribed 2026-04-12 | Ibuprofen 400 MG Oral Tablet [Ibu] | status active | RxNorm 206905
[MedicationRequest/7280f7f8-315d-7c6a-698d-8c3f4a330263] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG / Oxycodone Hydrochloride 10 MG Oral Tablet [Percocet] | status active | RxNorm 1049625
[MedicationRequest/7280f7f8-315d-7c6a-53dc-677516ba315e] MedicationRequest | prescribed 2026-04-12 | Galantamine 4 MG Oral Tablet | status active | reason: Alzheimer's disease (disorder) | RxNorm 310436
[MedicationRequest/7280f7f8-315d-7c6a-21fd-127361ce4eae] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-e1ca-6672a64e96d6] MedicationRequest | prescribed 2018-11-11 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/7280f7f8-315d-7c6a-d3dc-bf227b26b9de] MedicationRequest | prescribed 2018-11-11 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/7280f7f8-315d-7c6a-40f0-094ac0d35606] MedicationRequest | prescribed 2018-11-11 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/7280f7f8-315d-7c6a-344e-7b21fe48818f] MedicationRequest | prescribed 2018-11-11 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[Encounter/7280f7f8-315d-7c6a-ddbc-56619e72a429] Encounter | 2026-04-26 | Encounter for check up (procedure) | class AMB | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-e49f-7858d34e1916] Encounter | 2026-04-13 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-79c7-b2135168eae6] Encounter | 2026-04-12 | General examination of patient (procedure) | class AMB | at HOLY FAMILY MEDICAL SPECIALTY PRACTICE PLLC
[Immunization/7280f7f8-315d-7c6a-89f5-f28321d6dbe8] Immunization | 2026-04-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Encounter/7280f7f8-315d-7c6a-72da-216e7280849b] Encounter | 1991-07-09 | Emergency hospital admission (procedure) | class EMER | reason: Chronic pain (finding) | at BLISSFUL HOMECARE, LLC
[Encounter/7280f7f8-315d-7c6a-d73a-e1518f31d3e0] Encounter | 1993-06-28 | Emergency room admission (procedure) | class EMER | reason: Overdose (disorder) | at BLISSFUL HOMECARE, LLC
[Encounter/7280f7f8-315d-7c6a-2f4a-ef77bf8ed805] Encounter | 2023-09-13 | Emergency room admission (procedure) | class EMER | reason: Overdose (disorder) | at BLISSFUL HOMECARE, LLC
[Encounter/7280f7f8-315d-7c6a-ffaf-a54d0114dbd7] Encounter | 1990-10-25 | Emergency room admission (procedure) | class EMER | reason: Impacted molars (disorder) | at BLISSFUL HOMECARE, LLC
[Encounter/7280f7f8-315d-7c6a-008a-4bc39aafd6f9] Encounter | 1990-02-06 | Emergency room admission (procedure) | class EMER | reason: Chronic intractable migraine without aura (disorder) | at BLISSFUL HOMECARE, LLC
[Condition/7280f7f8-315d-7c6a-7f07-4101a3bc1409] Condition | onset 2018-11-04 | Medication review due (situation) | clinical status resolved | resolved 2024-11-24 | SNOMED 314529007
[Condition/7280f7f8-315d-7c6a-427d-c12b1b47d60e] Condition | onset 2026-04-12 | Medication review due (situation) | clinical status resolved | resolved 2026-04-12 | SNOMED 314529007
[Condition/7280f7f8-315d-7c6a-de5d-e5b452291178] Condition | onset 2025-04-06 | Medication review due (situation) | clinical status resolved | resolved 2025-04-06 | SNOMED 314529007
[Encounter/7280f7f8-315d-7c6a-32c1-1508c5256ae4] Encounter | 2020-03-11 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-e175-5339df9bbe9c] Encounter | 2014-04-11 | Follow-up encounter (procedure) | class AMB | reason: Chronic pain (finding) | at LAWRENCE GENERAL HOSPITAL
```

</details>

label: s
note: Of the EMER encounters (1990-02-06, 1990-10-25, 1991-07-09, 1993-06-28, 2023-09-13), 2023-09-13 is latest; cited card shows Emergency room admission at BLISSFUL HOMECARE, LLC, reason Overdose (disorder).

## 21. `active-problems:8d945e28#0#2`

Question: What active diagnoses does the patient have?

Answer: Active diagnoses include chronic kidney disease stage 4 (onset 2020-11-09) with awaiting kidney transplantation, as well as chronic kidney disease stages 1, 2 and 3, disorder of kidney due to diabetes mellitus, proteinuria due to type 2 diabetes mellitus, and microalbuminuria due to type 2 diabetes mellitus. Other active disorders are essential hypertension, metabolic syndrome X, prediabetes, anemia, obesity (body mass index 30+), obstructive sleep apnea syndrome, sleep disorder, gingivitis, and dependent drug abuse. **Active non-disease findings and situations include medication review due (onset 2026-07-13), full-time employment, has a criminal record, received higher education, and risk activity involvement.**

Cards this sentence cites:

- `[Condition/8d945e28-1d8a-bd72-3102-64b703ba601c]` Condition | onset 2026-07-13 | Medication review due (situation) | clinical status active | SNOMED 314529007
- `[Condition/8d945e28-1d8a-bd72-9d6c-259e17157c55]` Condition | onset 2026-09-07 | Full-time employment (finding) | clinical status active | SNOMED 160903007
- `[Condition/8d945e28-1d8a-bd72-05bf-4b4b02b03fe9]` Condition | onset 2018-01-22 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
- `[Condition/8d945e28-1d8a-bd72-d644-66738e889d91]` Condition | onset 1977-07-11 | Received higher education (finding) | clinical status active | SNOMED 224299000
- `[Condition/8d945e28-1d8a-bd72-fbf9-3e6f6bd97f57]` Condition | onset 1977-03-07 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000

<details><summary>Everything the model saw (39 cards)</summary>

```text
[Condition/8d945e28-1d8a-bd72-9d6c-259e17157c55] Condition | onset 2026-09-07 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8d945e28-1d8a-bd72-3102-64b703ba601c] Condition | onset 2026-07-13 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8d945e28-1d8a-bd72-6b51-0718e8cd7a5e] Condition | onset 2021-01-01 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/8d945e28-1d8a-bd72-db4c-2552d073039a] Condition | onset 2020-11-09 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/8d945e28-1d8a-bd72-ed26-25aa62be033c] Condition | onset 2020-08-18 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/8d945e28-1d8a-bd72-05bf-4b4b02b03fe9] Condition | onset 2018-01-22 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/8d945e28-1d8a-bd72-38fb-c4bf927332c6] Condition | onset 2013-09-16 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/8d945e28-1d8a-bd72-1379-82140e2d1648] Condition | onset 2013-09-16 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/8d945e28-1d8a-bd72-cd47-b95fb1e4464b] Condition | onset 2009-07-06 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/8d945e28-1d8a-bd72-be1a-fb710d842e34] Condition | onset 2009-07-06 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/8d945e28-1d8a-bd72-2a55-0f3c986db8dd] Condition | onset 2009-07-06 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8d945e28-1d8a-bd72-4277-241d976b7354] Condition | onset 2007-06-25 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8d945e28-1d8a-bd72-e0ac-a99a0168ad8a] Condition | onset 2004-06-07 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/8d945e28-1d8a-bd72-a508-e7d1553f7f62] Condition | onset 2004-06-07 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/8d945e28-1d8a-bd72-2622-8fe0a1a30909] Condition | onset 2003-06-02 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8d945e28-1d8a-bd72-12e3-17db162c8f0b] Condition | onset 2001-06-04 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/8d945e28-1d8a-bd72-d01e-086bb9d1d22f] Condition | onset 2001-05-07 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/8d945e28-1d8a-bd72-f5fa-42692b5be159] Condition | onset 1996-08-05 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8d945e28-1d8a-bd72-e601-8e5493910aec] Condition | onset 1981-07-20 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8d945e28-1d8a-bd72-52ca-256d6584412c] Condition | onset 1981-07-20 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8d945e28-1d8a-bd72-d644-66738e889d91] Condition | onset 1977-07-11 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/8d945e28-1d8a-bd72-fbf9-3e6f6bd97f57] Condition | onset 1977-03-07 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/8d945e28-1d8a-bd72-ff5c-41daf21d65a9] MedicationRequest | prescribed 2026-09-07 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/8d945e28-1d8a-bd72-d409-38c0124f2c47] MedicationRequest | prescribed 2026-09-07 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/8d945e28-1d8a-bd72-bcd6-3304c42dca58] MedicationRequest | prescribed 1981-07-27 | Vitamin B12 5 MG/ML Injectable Solution | status active | RxNorm 2001499
[Encounter/8d945e28-1d8a-bd72-016c-9af67d7199fd] Encounter | 2026-09-27 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-3f01-7946bd8f2be1] Encounter | 2026-09-26 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-9dbd-785d1f0e4915] Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Immunization/8d945e28-1d8a-bd72-6a94-32775be2d4e6] Immunization | 2026-01-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Condition/8d945e28-1d8a-bd72-37d8-7a1beb2edbc6] Condition | onset 2026-06-22 | Full-time employment (finding) | clinical status resolved | resolved 2026-07-13 | SNOMED 160903007
[Condition/8d945e28-1d8a-bd72-8f4c-47e57231942e] Condition | onset 2025-03-31 | Full-time employment (finding) | clinical status resolved | resolved 2026-05-11 | SNOMED 160903007
[Condition/8d945e28-1d8a-bd72-a7e0-bc786c26dcac] Condition | onset 2025-10-20 | Medication review due (situation) | clinical status resolved | resolved 2026-06-22 | SNOMED 314529007
[Condition/8d945e28-1d8a-bd72-7a33-55af8cacbbe5] Condition | onset 2025-03-31 | Medication review due (situation) | clinical status resolved | resolved 2025-08-18 | SNOMED 314529007
[Device/8d945e28-1d8a-bd72-692f-ee9ae322c3eb] Device | Respiratory humidifier (physical object) | status active | manufactured 2026-03-23 | SNOMED 706180003
[Condition/8d945e28-1d8a-bd72-cd9e-54612f63ecb5] Condition | onset 2016-05-16 | Stress (finding) | clinical status resolved | resolved 2016-11-28 | SNOMED 73595000
[Condition/8d945e28-1d8a-bd72-68dc-f3c46fef6e31] Condition | onset 2026-07-13 | Stress (finding) | clinical status resolved | resolved 2026-09-07 | SNOMED 73595000
[Condition/8d945e28-1d8a-bd72-7909-a2246f86242f] Condition | onset 2025-08-18 | Stress (finding) | clinical status resolved | resolved 2025-10-20 | SNOMED 73595000
[Condition/8d945e28-1d8a-bd72-b812-8dbb0257464f] Condition | onset 2025-03-03 | Stress (finding) | clinical status resolved | resolved 2025-03-31 | SNOMED 73595000
[Device/8d945e28-1d8a-bd72-4eb4-96add5cfb6a6] Device | Respiratory humidifier (physical object) | status active | manufactured 2025-03-31 | SNOMED 706180003
```

</details>

label: s
note: All five named findings/situations appear in the cited cards with clinical status active, and medication review due onset 2026-07-13 matches; 'include' makes no completeness claim.

## 22. `last-colonoscopy:ef5e136c#0#0`

Question: When was the patient's most recent colonoscopy?

Answer: **The patient's most recent colonoscopy was on 2024-04-17 (status completed).** Earlier colonoscopies were performed on 2022-11-29 and 2017-11-29. A colon polyp found on 2022-11-29 was recorded as resolved on 2024-04-17.

Cards this sentence cites:

- `[Procedure/ef5e136c-ff1e-0695-6492-376000eaabc8]` Procedure | 2024-04-17 | Colonoscopy (procedure) | status completed | SNOMED 73761001
- `[DocumentReference/ad64bd03-d904-8f43-8f5e-28147af12244#2]` Clinical note | 2024-04-17 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - colonoscopy (procedure)

<details><summary>Everything the model saw (47 cards)</summary>

```text
[Condition/ef5e136c-ff1e-0695-1f8c-935a12106cac] Condition | onset 2026-09-30 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/ef5e136c-ff1e-0695-7e5d-470b95f60db2] Condition | onset 2026-09-23 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/ef5e136c-ff1e-0695-9d2d-c4be459bc9f4] Condition | onset 2026-09-09 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/ef5e136c-ff1e-0695-7b9c-f43e5ca3f6c6] Condition | onset 2026-08-12 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-aa04-94486c99258f] Condition | onset 2025-08-27 | End-stage renal disease (disorder) | clinical status active | SNOMED 46177005
[Condition/ef5e136c-ff1e-0695-423f-ed71d76e81e3] Condition | onset 2025-03-30 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/ef5e136c-ff1e-0695-71df-3a96389b0a39] Condition | onset 2025-02-05 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/ef5e136c-ff1e-0695-5331-2d63eb213c34] Condition | onset 2024-05-15 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/ef5e136c-ff1e-0695-3834-fa6cb282a475] Condition | onset 2024-05-15 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/ef5e136c-ff1e-0695-68fe-9e2010333061] Condition | onset 2023-08-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/ef5e136c-ff1e-0695-65f5-8d04f278a661] Condition | onset 2023-08-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/ef5e136c-ff1e-0695-aac2-46a0ff462178] Condition | onset 2023-04-19 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/ef5e136c-ff1e-0695-fda2-40e12f6b17a7] Condition | onset 2017-11-15 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/ef5e136c-ff1e-0695-bf3f-30946ad3f8b4] Condition | onset 2017-11-15 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/ef5e136c-ff1e-0695-eac4-d545a0296998] Condition | onset 2011-07-27 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/ef5e136c-ff1e-0695-b228-2f5ff5bb47cb] Condition | onset 2010-05-19 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/ef5e136c-ff1e-0695-af16-82f03f777ba8] Condition | onset 2010-05-19 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/ef5e136c-ff1e-0695-5ca5-51bfdc51320e] Condition | onset 2010-05-12 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/ef5e136c-ff1e-0695-f7ec-ceae0c2566bc] Condition | onset 2004-06-16 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/ef5e136c-ff1e-0695-c94a-5d81ddd88117] Condition | onset 1997-05-07 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/ef5e136c-ff1e-0695-6efc-9f7d5e6b04ef] Condition | onset 1993-09-01 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/ef5e136c-ff1e-0695-1f68-dac24351dbaa] Condition | onset 1993-04-14 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/ef5e136c-ff1e-0695-2d8d-328849698529] Condition | onset 1993-01-22 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/ef5e136c-ff1e-0695-0825-c31e8b252683] Condition | onset 1983-11-14 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/ef5e136c-ff1e-0695-cb16-3a98eeb2de7a] Condition | onset 1976-01-07 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/ef5e136c-ff1e-0695-3278-6a86eaf1fb5d] Condition | onset 1975-06-27 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/ef5e136c-ff1e-0695-337f-d12087c8dbb5] Condition | onset 1975-01-01 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/ef5e136c-ff1e-0695-ffec-2ea7ac772a27] MedicationRequest | prescribed 2026-09-30 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/ef5e136c-ff1e-0695-b3ba-a1ec7bcfb9f4] MedicationRequest | prescribed 2026-09-30 | albuterol 0.83 MG/ML Inhalation Solution | status active | RxNorm 630208
[MedicationRequest/ef5e136c-ff1e-0695-901e-2e1f9afb0cca] MedicationRequest | prescribed 2026-09-30 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/ef5e136c-ff1e-0695-76a6-8eeb54f8a75e] MedicationRequest | prescribed 2026-09-30 | 120 ACTUAT fluticasone propionate 0.044 MG/ACTUAT Metered Dose Inhaler [Flovent] | status active | RxNorm 895996
[MedicationRequest/ef5e136c-ff1e-0695-6c6d-182c3b9c47c1] MedicationRequest | prescribed 2026-09-30 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/ef5e136c-ff1e-0695-6804-cf31640a9491] MedicationRequest | prescribed 2026-09-30 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[Encounter/ef5e136c-ff1e-0695-08ba-2471a16a6570] Encounter | 2026-09-30 | Emergency room admission (procedure) | class EMER | at APPLE VALLEY CENTER
[Encounter/ef5e136c-ff1e-0695-aea4-11055569fd51] Encounter | 2026-09-23 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/ef5e136c-ff1e-0695-4a41-6fca58c80cb7] Encounter | 2026-09-16 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Immunization/ef5e136c-ff1e-0695-6beb-93901776b619] Immunization | 2026-05-13 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Procedure/ef5e136c-ff1e-0695-6492-376000eaabc8] Procedure | 2024-04-17 | Colonoscopy (procedure) | status completed | SNOMED 73761001
[Procedure/ef5e136c-ff1e-0695-f09f-74f1d600c1f4] Procedure | 2022-11-29 | Colonoscopy (procedure) | status completed | SNOMED 73761001
[Procedure/ef5e136c-ff1e-0695-8a4e-a9576c900754] Procedure | 2017-11-29 | Colonoscopy (procedure) | status completed | SNOMED 73761001
[Condition/ef5e136c-ff1e-0695-48e1-d64ec86cb18d] Condition | onset 2022-11-29 | Polyp of colon (disorder) | clinical status resolved | resolved 2024-04-17 | SNOMED 68496003
[Immunization/ef5e136c-ff1e-0695-358d-908aa385ad32] Immunization | 2021-07-28 | COVID-19, mRNA, LNP-S, PF, 100 mcg/0.5mL dose or 50 mcg/0.25mL dose | status completed | CVX 207
[Immunization/ef5e136c-ff1e-0695-43d1-1c013e357b6c] Immunization | 2021-06-30 | COVID-19, mRNA, LNP-S, PF, 100 mcg/0.5mL dose or 50 mcg/0.25mL dose | status completed | CVX 207
[Procedure/ef5e136c-ff1e-0695-a1b4-af5e716e7746] Procedure | 2022-11-29 | Screening for occult blood in feces (procedure) | status completed | reason: Polyp of colon (disorder) | SNOMED 104435004
[Condition/ef5e136c-ff1e-0695-fa1e-dadf939797f8] Condition | onset 2025-05-14 | Maxillary fracture, unspecified side, sequela | clinical status resolved | resolved 2025-07-23 | http://hl7.org/fhir/sid/icd-10 S02.401S
[Procedure/ef5e136c-ff1e-0695-e258-f6ce1deb890c] Procedure | 2022-11-29 | Rectal polypectomy (procedure) | status completed | reason: Polyp of colon (disorder) | SNOMED 274031008
[DocumentReference/ad64bd03-d904-8f43-8f5e-28147af12244#2] Clinical note | 2024-04-17 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - colonoscopy (procedure)
```

</details>

label: s
note: Cited Procedure shows colonoscopy 2024-04-17 status completed; the only other colonoscopies seen are 2022-11-29 and 2017-11-29, so it is the most recent.

## 23. `latest-bp:772fc930#0#0`

Question: What was the patient's most recent blood pressure reading?

Answer: **The most recent blood pressure reading was on 2026-07-09: Systolic Blood Pressure 129 mm[Hg] and Diastolic Blood Pressure 89 mm[Hg].**

Cards this sentence cites:

- `[Observation/772fc930-5418-0bfa-f73e-cc815f68abee]` Observation (vital-signs) | 2026-07-09 | Blood pressure panel with all children optional = Diastolic Blood Pressure 89 mm[Hg]; Systolic Blood Pressure 129 mm[Hg] | status final | LOINC 85354-9

<details><summary>Everything the model saw (41 cards)</summary>

```text
[Condition/772fc930-5418-0bfa-5baf-97b1667a332f] Condition | onset 2026-07-09 | Part-time employment (finding) | clinical status active | SNOMED 160904001
[Condition/772fc930-5418-0bfa-446c-c28d224cff31] Condition | onset 2026-06-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/772fc930-5418-0bfa-33d9-881f0ecc07c1] Condition | onset 2026-06-11 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/772fc930-5418-0bfa-d3cc-a2daa4832199] Condition | onset 2026-02-19 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/772fc930-5418-0bfa-600b-5558ca66220a] Condition | onset 2026-02-19 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/772fc930-5418-0bfa-6352-6c3984966ef8] Condition | onset 2025-02-13 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/772fc930-5418-0bfa-bb6d-8a0b90cf95e4] Condition | onset 2020-01-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/772fc930-5418-0bfa-ab71-24a74b1745fd] Condition | onset 2020-01-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/772fc930-5418-0bfa-beac-a103fe7f3fd2] Condition | onset 2019-01-10 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/772fc930-5418-0bfa-2c4f-3f5ed5953c36] Condition | onset 2019-01-10 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/772fc930-5418-0bfa-3873-02589386889d] Condition | onset 2004-06-19 | Osteoarthritis of hip (disorder) | clinical status active | SNOMED 239872002
[Condition/772fc930-5418-0bfa-a4a0-5eff492015a6] Condition | onset 1991-08-28 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/772fc930-5418-0bfa-01dc-3613408a83a6] Condition | onset 1991-08-22 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/772fc930-5418-0bfa-35d2-44b4eb4fcccc] Condition | onset 1991-08-08 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/772fc930-5418-0bfa-43ec-8fdd443cc6ce] Condition | onset 1988-07-21 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/772fc930-5418-0bfa-91e4-e46a214921b9] Condition | onset 1986-07-10 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/772fc930-5418-0bfa-47df-a943ca27aa29] Condition | onset 1986-07-10 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/772fc930-5418-0bfa-7d09-0ea3ca1e93ba] Condition | onset 1986-03-30 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/772fc930-5418-0bfa-1be5-06b5144b5817] Condition | onset 1986-03-01 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/772fc930-5418-0bfa-0cdf-ac369e474ff3] Condition | onset 1977-05-19 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/772fc930-5418-0bfa-f6df-7e2448081e0f] Condition | onset 1967-05-04 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/772fc930-5418-0bfa-ffbe-e3692c7542d7] Condition | onset 1964-01-15 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/772fc930-5418-0bfa-d2b4-bc5609421614] MedicationRequest | prescribed 2026-07-16 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/772fc930-5418-0bfa-35ed-4b81c08cb46e] MedicationRequest | prescribed 2026-07-16 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/772fc930-5418-0bfa-0d23-3b3c40dabcae] MedicationRequest | prescribed 2026-07-16 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/772fc930-5418-0bfa-ac79-a5117bd68db1] MedicationRequest | prescribed 2026-03-06 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/772fc930-5418-0bfa-dfc7-922f9300bced] MedicationRequest | prescribed 2004-06-19 | Naproxen sodium 220 MG Oral Tablet | status active | reason: Osteoarthritis of hip (disorder) | RxNorm 849574
[Encounter/772fc930-5418-0bfa-dd45-e4b82fc97e3d] Encounter | 2026-07-23 | Encounter for check up (procedure) | class AMB | at BOSTON MEDICAL CENTER CORPORATION-
[Encounter/772fc930-5418-0bfa-6606-662b1312d21c] Encounter | 2026-07-16 | Urgent care clinic (environment) | class AMB | at LYNN URGENT CARE LLC
[Encounter/772fc930-5418-0bfa-54c7-a3b13e8997b9] Encounter | 2026-07-09 | Emergency room admission (procedure) | class EMER | at LEONARD FLORENCE CENTER FOR LIVING
[Immunization/772fc930-5418-0bfa-fcca-2fca6db3fac3] Immunization | 2026-02-19 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/772fc930-5418-0bfa-087d-26d660060cbf] Observation (vital-signs) | 2026-05-14 | Blood pressure panel with all children optional = Diastolic Blood Pressure 90 mm[Hg]; Systolic Blood Pressure 133 mm[Hg] | status final | LOINC 85354-9
[Observation/772fc930-5418-0bfa-f73e-cc815f68abee] Observation (vital-signs) | 2026-07-09 | Blood pressure panel with all children optional = Diastolic Blood Pressure 89 mm[Hg]; Systolic Blood Pressure 129 mm[Hg] | status final | LOINC 85354-9
[Observation/772fc930-5418-0bfa-3624-43888808217d] Observation (vital-signs) | 2026-06-25 | Blood pressure panel with all children optional = Diastolic Blood Pressure 91 mm[Hg]; Systolic Blood Pressure 128 mm[Hg] | status final | LOINC 85354-9
[Observation/772fc930-5418-0bfa-bc0d-cdf9d9eece08] Observation (vital-signs) | 2026-06-11 | Blood pressure panel with all children optional = Diastolic Blood Pressure 93 mm[Hg]; Systolic Blood Pressure 130 mm[Hg] | status final | LOINC 85354-9
[Device/772fc930-5418-0bfa-6cc6-12625e5fa8cc] Device | Home continuous positive airway pressure unit (physical object) | status active | manufactured 2026-04-23 | SNOMED 702172008
[Observation/772fc930-5418-0bfa-8bc1-95e16fd05e4e] Observation (vital-signs) | 2020-04-02 | Heart rate = 71 /min | status final | LOINC 8867-4
[Observation/772fc930-5418-0bfa-d488-492fd547f7af] Observation (vital-signs) | 2026-07-09 | Heart rate = 67 /min | status final | LOINC 8867-4
[Observation/772fc930-5418-0bfa-b153-6084cc5fe5f8] Observation (vital-signs) | 2026-06-25 | Heart rate = 84 /min | status final | LOINC 8867-4
[Observation/772fc930-5418-0bfa-0a08-2c64c1ce098c] Observation (vital-signs) | 2026-06-11 | Heart rate = 65 /min | status final | LOINC 8867-4
[Device/772fc930-5418-0bfa-28ef-1962c834cc1d] Device | Home continuous positive airway pressure unit (physical object) | status active | manufactured 2026-01-29 | SNOMED 702172008
```

</details>

label: s
note: Cited panel 2026-07-09 shows 129/89 mm[Hg]; the other BP panels seen (2026-05-14, 2026-06-11, 2026-06-25) are all earlier.

## 24. `prescribed-for-anemia:8d945e28#0#1`

Question: Which medications have been prescribed for the patient's anemia?

Answer: The record has several completed medication requests with the reason Anemia (disorder), prescribed 2021-02-18, 2021-04-22, 2021-08-18, 2021-10-18, 2021-12-19, 2026-09-20, 2026-09-23 and 2026-09-27, but these entries do not name the medication. **Clinical notes from 2021-04-19 and 2021-05-10 record prescriptions of 1 ml epoetin alfa 4000 unt/ml injection [epogen], though these notes do not state the reason for it.** An active Vitamin B12 5 MG/ML Injectable Solution was prescribed 1981-07-27, but no reason is listed for it.

Cards this sentence cites:

- `[DocumentReference/3f628097-7433-7ecf-0911-07f6fe088905#2]` Clinical note | 2021-04-19 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose. The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
- `[DocumentReference/39c3ccb8-f3ba-af45-7465-13f2298b9b36#2]` Clinical note | 2021-05-10 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose. The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]

<details><summary>Everything the model saw (39 cards)</summary>

```text
[Condition/8d945e28-1d8a-bd72-9d6c-259e17157c55] Condition | onset 2026-09-07 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8d945e28-1d8a-bd72-3102-64b703ba601c] Condition | onset 2026-07-13 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8d945e28-1d8a-bd72-6b51-0718e8cd7a5e] Condition | onset 2021-01-01 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/8d945e28-1d8a-bd72-db4c-2552d073039a] Condition | onset 2020-11-09 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/8d945e28-1d8a-bd72-ed26-25aa62be033c] Condition | onset 2020-08-18 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/8d945e28-1d8a-bd72-05bf-4b4b02b03fe9] Condition | onset 2018-01-22 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/8d945e28-1d8a-bd72-38fb-c4bf927332c6] Condition | onset 2013-09-16 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/8d945e28-1d8a-bd72-1379-82140e2d1648] Condition | onset 2013-09-16 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/8d945e28-1d8a-bd72-cd47-b95fb1e4464b] Condition | onset 2009-07-06 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/8d945e28-1d8a-bd72-be1a-fb710d842e34] Condition | onset 2009-07-06 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/8d945e28-1d8a-bd72-2a55-0f3c986db8dd] Condition | onset 2009-07-06 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8d945e28-1d8a-bd72-4277-241d976b7354] Condition | onset 2007-06-25 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8d945e28-1d8a-bd72-e0ac-a99a0168ad8a] Condition | onset 2004-06-07 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/8d945e28-1d8a-bd72-a508-e7d1553f7f62] Condition | onset 2004-06-07 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/8d945e28-1d8a-bd72-2622-8fe0a1a30909] Condition | onset 2003-06-02 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8d945e28-1d8a-bd72-12e3-17db162c8f0b] Condition | onset 2001-06-04 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/8d945e28-1d8a-bd72-d01e-086bb9d1d22f] Condition | onset 2001-05-07 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/8d945e28-1d8a-bd72-f5fa-42692b5be159] Condition | onset 1996-08-05 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8d945e28-1d8a-bd72-e601-8e5493910aec] Condition | onset 1981-07-20 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8d945e28-1d8a-bd72-52ca-256d6584412c] Condition | onset 1981-07-20 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8d945e28-1d8a-bd72-d644-66738e889d91] Condition | onset 1977-07-11 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/8d945e28-1d8a-bd72-fbf9-3e6f6bd97f57] Condition | onset 1977-03-07 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/8d945e28-1d8a-bd72-ff5c-41daf21d65a9] MedicationRequest | prescribed 2026-09-07 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/8d945e28-1d8a-bd72-d409-38c0124f2c47] MedicationRequest | prescribed 2026-09-07 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/8d945e28-1d8a-bd72-bcd6-3304c42dca58] MedicationRequest | prescribed 1981-07-27 | Vitamin B12 5 MG/ML Injectable Solution | status active | RxNorm 2001499
[Encounter/8d945e28-1d8a-bd72-016c-9af67d7199fd] Encounter | 2026-09-27 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-3f01-7946bd8f2be1] Encounter | 2026-09-26 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-9dbd-785d1f0e4915] Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Immunization/8d945e28-1d8a-bd72-6a94-32775be2d4e6] Immunization | 2026-01-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/39c3ccb8-f3ba-af45-7465-13f2298b9b36#2] Clinical note | 2021-05-10 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose. The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[MedicationRequest/8d945e28-1d8a-bd72-d1d1-ade610dfcc7f] MedicationRequest | prescribed 2021-10-18 | status completed | reason: Anemia (disorder)
[DocumentReference/3f628097-7433-7ecf-0911-07f6fe088905#2] Clinical note | 2021-04-19 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose. The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[MedicationRequest/8d945e28-1d8a-bd72-2310-7887f27830d3] MedicationRequest | prescribed 2021-08-18 | status completed | reason: Anemia (disorder)
[MedicationRequest/8d945e28-1d8a-bd72-1c5f-e1356b8956dd] MedicationRequest | prescribed 2026-09-27 | status completed | reason: Anemia (disorder)
[MedicationRequest/8d945e28-1d8a-bd72-b130-0ab0ae19f5ef] MedicationRequest | prescribed 2021-02-18 | status completed | reason: Anemia (disorder)
[MedicationRequest/8d945e28-1d8a-bd72-5f50-134a5a073f4d] MedicationRequest | prescribed 2026-09-23 | status completed | reason: Anemia (disorder)
[MedicationRequest/8d945e28-1d8a-bd72-6a8e-71a80daaea46] MedicationRequest | prescribed 2021-12-19 | status completed | reason: Anemia (disorder)
[MedicationRequest/8d945e28-1d8a-bd72-84b2-c9e1d128173c] MedicationRequest | prescribed 2026-09-20 | status completed | reason: Anemia (disorder)
[MedicationRequest/8d945e28-1d8a-bd72-9d0f-7f2bf255038a] MedicationRequest | prescribed 2021-04-22 | status completed | reason: Anemia (disorder)
```

</details>

label: s
note: Both cited notes (2021-04-19, 2021-05-10) list prescription of 1 ml epoetin alfa 4000 unt/ml injection [epogen] and give no reason in the excerpt.

## 25. `latest-bp:9292c3d5#0#0`

Question: What was the patient's most recent blood pressure reading?

Answer: **The most recent blood pressure reading was on 2026-04-26, with a systolic blood pressure of 133 mm[Hg] and a diastolic blood pressure of 76 mm[Hg].**

Cards this sentence cites:

- `[Observation/9292c3d5-3db6-f4f9-a42e-d26907d21bcc]` Observation (vital-signs) | 2026-04-26 | Blood pressure panel with all children optional = Diastolic Blood Pressure 76 mm[Hg]; Systolic Blood Pressure 133 mm[Hg] | status final | LOINC 85354-9

<details><summary>Everything the model saw (31 cards)</summary>

```text
[Condition/9292c3d5-3db6-f4f9-b5ec-3a44e8649597] Condition | onset 2026-04-26 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/9292c3d5-3db6-f4f9-861b-f7159312202f] Condition | onset 2026-04-26 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/9292c3d5-3db6-f4f9-483e-3d8d3b0f4690] Condition | onset 2026-04-26 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/9292c3d5-3db6-f4f9-38dc-147de4ac63a8] Condition | onset 2026-04-26 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/9292c3d5-3db6-f4f9-5b6c-1c0ed0fd0321] Condition | onset 2020-03-22 | Opioid abuse | clinical status active | SNOMED 5602001
[Condition/9292c3d5-3db6-f4f9-f835-25af6c77c701] Condition | onset 2011-08-22 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/9292c3d5-3db6-f4f9-54d1-d4b6d2666838] Condition | onset 2011-08-22 | Acute ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401303003
[Condition/9292c3d5-3db6-f4f9-2b48-fd31edda50b0] Condition | onset 2010-03-21 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/9292c3d5-3db6-f4f9-1b0c-65cb31846f75] Condition | onset 2005-05-29 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/9292c3d5-3db6-f4f9-2a82-9615e45bb615] Condition | onset 1986-05-04 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
[Condition/9292c3d5-3db6-f4f9-24a0-fe08e411b951] Condition | onset 1986-05-04 | Serving in military service (finding) | clinical status active | SNOMED 1187604002
[Condition/9292c3d5-3db6-f4f9-97fc-b779fe5ffdd4] Condition | onset 1985-04-28 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/9292c3d5-3db6-f4f9-c2ad-ca0afa2369e8] MedicationRequest | prescribed 2011-08-22 | 24 HR metoprolol succinate 50 MG Extended Release Oral Tablet | status active | RxNorm 866436
[MedicationRequest/9292c3d5-3db6-f4f9-b955-8ddb9b72de69] MedicationRequest | prescribed 2011-08-22 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/9292c3d5-3db6-f4f9-8b49-28e15899c04a] MedicationRequest | prescribed 2011-08-22 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/9292c3d5-3db6-f4f9-7675-f5ee99ae0c4e] MedicationRequest | prescribed 2011-08-22 | simvastatin 40 MG Oral Tablet | status active | RxNorm 198211
[MedicationRequest/9292c3d5-3db6-f4f9-2744-8b9a3e3302b8] MedicationRequest | prescribed 2011-08-22 | lisinopril 2.5 MG Oral Tablet | status active | RxNorm 311353
[Encounter/9292c3d5-3db6-f4f9-f8cd-08dfcc81ed12] Encounter | 2026-04-26 | General examination of patient (procedure) | class AMB | at COMMUNITY HEALTH PROGRAMS INC
[Encounter/9292c3d5-3db6-f4f9-2526-cf0c3fc1dcaa] Encounter | 2025-08-10 | Encounter for check up (procedure) | class AMB | reason: Gingivitis (disorder) | at Pittsfield Outpatient Clinic
[Encounter/9292c3d5-3db6-f4f9-d85c-7f88671a1881] Encounter | 2025-08-03 | Encounter for symptom (procedure) | class AMB | reason: Acute viral pharyngitis (disorder) | at Pittsfield Outpatient Clinic
[Immunization/9292c3d5-3db6-f4f9-2e74-b2ab508532b8] Immunization | 2026-04-26 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/9292c3d5-3db6-f4f9-d6ae-d5bc6ac24288] Observation (vital-signs) | 2025-04-20 | Blood pressure panel with all children optional = Diastolic Blood Pressure 72 mm[Hg]; Systolic Blood Pressure 133 mm[Hg] | status final | LOINC 85354-9
[Observation/9292c3d5-3db6-f4f9-a42e-d26907d21bcc] Observation (vital-signs) | 2026-04-26 | Blood pressure panel with all children optional = Diastolic Blood Pressure 76 mm[Hg]; Systolic Blood Pressure 133 mm[Hg] | status final | LOINC 85354-9
[Observation/9292c3d5-3db6-f4f9-fd41-dcb48122a394] Observation (vital-signs) | 2025-07-27 | Blood pressure panel with all children optional = Diastolic Blood Pressure 71 mm[Hg]; Systolic Blood Pressure 126 mm[Hg] | status final | LOINC 85354-9
[Device/9292c3d5-3db6-f4f9-16bf-070cd3eccb10] Device | Blood glucose meter (physical object) | status active | manufactured 2005-05-08 | SNOMED 337414009
[Observation/9292c3d5-3db6-f4f9-953a-0782202a41c7] Observation (vital-signs) | 2022-07-17 | Oxygen saturation in Arterial blood = 99.481 % | status final | LOINC 2708-6
[Observation/9292c3d5-3db6-f4f9-3ec7-28f2216df6fe] Observation (laboratory) | 2025-07-27 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.32 % | status final | LOINC 4548-4
[Observation/9292c3d5-3db6-f4f9-c64b-dbfe35d3ba7c] Observation (laboratory) | 2026-04-26 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.06 % | status final | LOINC 4548-4
[Observation/9292c3d5-3db6-f4f9-26fe-8f3077e9a156] Observation (laboratory) | 2025-04-20 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.06 % | status final | LOINC 4548-4
[Immunization/9292c3d5-3db6-f4f9-0e55-dcf5b05aeef5] Immunization | 2021-04-04 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/9292c3d5-3db6-f4f9-0865-19e45ffab679] Immunization | 2021-03-14 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
```

</details>

label: s
note: Cited panel 2026-04-26 shows systolic 133 and diastolic 76 mm[Hg]; other BP panels seen (2025-04-20, 2025-07-27) are earlier.

## 26. `last-colonoscopy:8d945e28#0#1`

Question: When was the patient's most recent colonoscopy?

Answer: The patient's most recent colonoscopy was on 2024-07-15 (status completed), performed during a check-up encounter for colon cancer screening. **A prior colonoscopy was completed on 2019-05-18.**

Cards this sentence cites:

- `[Procedure/8d945e28-1d8a-bd72-b348-144a6a050f47]` Procedure | 2019-05-18 | Colonoscopy (procedure) | status completed | SNOMED 73761001
- `[DocumentReference/9ec79051-94df-9aa9-813c-d2df074b3c81#1]` Clinical note | 2019-05-18 | part 1 of 1 | 2019-05-18 # Chief Complaint - Thirst - Fatigue - Hunger # History of Present Illness Tien590 Marcela739 is a 60 year-old nonhispanic white female. Patient has a history of medication review due (situation), chronic periodontitis, generalized, victim of intimate partner abuse (finding), dental caries, unspecified, leukoplakia of oral mucosa, including tongue, part-time employment (finding), acute apical periodontitis of pulpal origin, limited social contact (finding), not in labor force (finding), reports of violence in the environment (finding), full-time employment (finding), stress (finding), social isolation (finding). # Social History Patient is married. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications hydrochlorothiazide 25 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] # Assessment and Plan ## Plan The following procedures were conducted: - colonoscopy (procedure)

<details><summary>Everything the model saw (39 cards)</summary>

```text
[Condition/8d945e28-1d8a-bd72-9d6c-259e17157c55] Condition | onset 2026-09-07 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8d945e28-1d8a-bd72-3102-64b703ba601c] Condition | onset 2026-07-13 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8d945e28-1d8a-bd72-6b51-0718e8cd7a5e] Condition | onset 2021-01-01 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/8d945e28-1d8a-bd72-db4c-2552d073039a] Condition | onset 2020-11-09 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/8d945e28-1d8a-bd72-ed26-25aa62be033c] Condition | onset 2020-08-18 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/8d945e28-1d8a-bd72-05bf-4b4b02b03fe9] Condition | onset 2018-01-22 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/8d945e28-1d8a-bd72-38fb-c4bf927332c6] Condition | onset 2013-09-16 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/8d945e28-1d8a-bd72-1379-82140e2d1648] Condition | onset 2013-09-16 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/8d945e28-1d8a-bd72-cd47-b95fb1e4464b] Condition | onset 2009-07-06 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/8d945e28-1d8a-bd72-be1a-fb710d842e34] Condition | onset 2009-07-06 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/8d945e28-1d8a-bd72-2a55-0f3c986db8dd] Condition | onset 2009-07-06 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8d945e28-1d8a-bd72-4277-241d976b7354] Condition | onset 2007-06-25 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8d945e28-1d8a-bd72-e0ac-a99a0168ad8a] Condition | onset 2004-06-07 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/8d945e28-1d8a-bd72-a508-e7d1553f7f62] Condition | onset 2004-06-07 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/8d945e28-1d8a-bd72-2622-8fe0a1a30909] Condition | onset 2003-06-02 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8d945e28-1d8a-bd72-12e3-17db162c8f0b] Condition | onset 2001-06-04 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/8d945e28-1d8a-bd72-d01e-086bb9d1d22f] Condition | onset 2001-05-07 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/8d945e28-1d8a-bd72-f5fa-42692b5be159] Condition | onset 1996-08-05 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8d945e28-1d8a-bd72-e601-8e5493910aec] Condition | onset 1981-07-20 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8d945e28-1d8a-bd72-52ca-256d6584412c] Condition | onset 1981-07-20 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8d945e28-1d8a-bd72-d644-66738e889d91] Condition | onset 1977-07-11 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/8d945e28-1d8a-bd72-fbf9-3e6f6bd97f57] Condition | onset 1977-03-07 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/8d945e28-1d8a-bd72-ff5c-41daf21d65a9] MedicationRequest | prescribed 2026-09-07 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/8d945e28-1d8a-bd72-d409-38c0124f2c47] MedicationRequest | prescribed 2026-09-07 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/8d945e28-1d8a-bd72-bcd6-3304c42dca58] MedicationRequest | prescribed 1981-07-27 | Vitamin B12 5 MG/ML Injectable Solution | status active | RxNorm 2001499
[Encounter/8d945e28-1d8a-bd72-016c-9af67d7199fd] Encounter | 2026-09-27 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-3f01-7946bd8f2be1] Encounter | 2026-09-26 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-9dbd-785d1f0e4915] Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Immunization/8d945e28-1d8a-bd72-6a94-32775be2d4e6] Immunization | 2026-01-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Procedure/8d945e28-1d8a-bd72-fa00-cb2b98cde6f2] Procedure | 2024-07-15 | Colonoscopy (procedure) | status completed | SNOMED 73761001
[Procedure/8d945e28-1d8a-bd72-b348-144a6a050f47] Procedure | 2019-05-18 | Colonoscopy (procedure) | status completed | SNOMED 73761001
[DocumentReference/88c639eb-a410-4ab2-0de3-1ec2e7c00f9d#2] Clinical note | 2024-07-15 | part 2 of 2 | # Medications 1 ml epoetin alfa 4000 unt/ml injection [epogen]; acetaminophen 325 mg oral tablet; hydrochlorothiazide 25 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; ibuprofen 200 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - colonoscopy (procedure)
[DocumentReference/9ec79051-94df-9aa9-813c-d2df074b3c81#1] Clinical note | 2019-05-18 | part 1 of 1 | 2019-05-18 # Chief Complaint - Thirst - Fatigue - Hunger # History of Present Illness Tien590 Marcela739 is a 60 year-old nonhispanic white female. Patient has a history of medication review due (situation), chronic periodontitis, generalized, victim of intimate partner abuse (finding), dental caries, unspecified, leukoplakia of oral mucosa, including tongue, part-time employment (finding), acute apical periodontitis of pulpal origin, limited social contact (finding), not in labor force (finding), reports of violence in the environment (finding), full-time employment (finding), stress (finding), social isolation (finding). # Social History Patient is married. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications hydrochlorothiazide 25 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] # Assessment and Plan ## Plan The following procedures were conducted: - colonoscopy (procedure)
[Immunization/8d945e28-1d8a-bd72-28c7-936105552d76] Immunization | 2021-05-17 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/8d945e28-1d8a-bd72-c212-27d34e4b0eef] Immunization | 2021-04-26 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Encounter/8d945e28-1d8a-bd72-a161-8598789128ea] Encounter | 2024-07-15 | Encounter for check up (procedure) | class AMB | reason: Screening for malignant neoplasm of colon (procedure) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-bf7c-5015881d46b9] Encounter | 2019-05-18 | Encounter for check up (procedure) | class AMB | reason: Screening for malignant neoplasm of colon (procedure) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[DocumentReference/39c3ccb8-f3ba-af45-7465-13f2298b9b36#2] Clinical note | 2021-05-10 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose. The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[Encounter/8d945e28-1d8a-bd72-6ff1-449c646d29c6] Encounter | 2020-09-07 | General examination of patient (procedure) | class AMB | at TREE OF LIFE HEALTHCARE ASSOCIATES
```

</details>

label: s
note: Cited Procedure shows colonoscopy 2019-05-18 status completed, which precedes the 2024-07-15 colonoscopy.

## 27. `latest-lipid-panel:9292c3d5#0#1`

Question: What did the patient's most recent lipid panel show?

Answer: The most recent lipid panel (direct LDL, serum or plasma) was on 2024-04-14 and showed total cholesterol 176 mg/dL, triglycerides 149.68 mg/dL, LDL cholesterol by direct assay 98.91 mg/dL, and HDL cholesterol 47.16 mg/dL. **For comparison, the prior panel on 2021-03-28 showed total cholesterol 143.24 mg/dL, triglycerides 134.54 mg/dL, LDL 61.64 mg/dL, and HDL 54.69 mg/dL.**

Cards this sentence cites:

- `[DiagnosticReport/9292c3d5-3db6-f4f9-e482-70e5335a4db9]` DiagnosticReport | 2021-03-28 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 143.24 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 134.54 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 61.64 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 54.69 mg/dL | LOINC 57698-3

<details><summary>Everything the model saw (31 cards)</summary>

```text
[Condition/9292c3d5-3db6-f4f9-b5ec-3a44e8649597] Condition | onset 2026-04-26 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/9292c3d5-3db6-f4f9-861b-f7159312202f] Condition | onset 2026-04-26 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/9292c3d5-3db6-f4f9-483e-3d8d3b0f4690] Condition | onset 2026-04-26 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/9292c3d5-3db6-f4f9-38dc-147de4ac63a8] Condition | onset 2026-04-26 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/9292c3d5-3db6-f4f9-5b6c-1c0ed0fd0321] Condition | onset 2020-03-22 | Opioid abuse | clinical status active | SNOMED 5602001
[Condition/9292c3d5-3db6-f4f9-f835-25af6c77c701] Condition | onset 2011-08-22 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/9292c3d5-3db6-f4f9-54d1-d4b6d2666838] Condition | onset 2011-08-22 | Acute ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401303003
[Condition/9292c3d5-3db6-f4f9-2b48-fd31edda50b0] Condition | onset 2010-03-21 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/9292c3d5-3db6-f4f9-1b0c-65cb31846f75] Condition | onset 2005-05-29 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/9292c3d5-3db6-f4f9-2a82-9615e45bb615] Condition | onset 1986-05-04 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
[Condition/9292c3d5-3db6-f4f9-24a0-fe08e411b951] Condition | onset 1986-05-04 | Serving in military service (finding) | clinical status active | SNOMED 1187604002
[Condition/9292c3d5-3db6-f4f9-97fc-b779fe5ffdd4] Condition | onset 1985-04-28 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/9292c3d5-3db6-f4f9-c2ad-ca0afa2369e8] MedicationRequest | prescribed 2011-08-22 | 24 HR metoprolol succinate 50 MG Extended Release Oral Tablet | status active | RxNorm 866436
[MedicationRequest/9292c3d5-3db6-f4f9-b955-8ddb9b72de69] MedicationRequest | prescribed 2011-08-22 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/9292c3d5-3db6-f4f9-8b49-28e15899c04a] MedicationRequest | prescribed 2011-08-22 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/9292c3d5-3db6-f4f9-7675-f5ee99ae0c4e] MedicationRequest | prescribed 2011-08-22 | simvastatin 40 MG Oral Tablet | status active | RxNorm 198211
[MedicationRequest/9292c3d5-3db6-f4f9-2744-8b9a3e3302b8] MedicationRequest | prescribed 2011-08-22 | lisinopril 2.5 MG Oral Tablet | status active | RxNorm 311353
[Encounter/9292c3d5-3db6-f4f9-f8cd-08dfcc81ed12] Encounter | 2026-04-26 | General examination of patient (procedure) | class AMB | at COMMUNITY HEALTH PROGRAMS INC
[Encounter/9292c3d5-3db6-f4f9-2526-cf0c3fc1dcaa] Encounter | 2025-08-10 | Encounter for check up (procedure) | class AMB | reason: Gingivitis (disorder) | at Pittsfield Outpatient Clinic
[Encounter/9292c3d5-3db6-f4f9-d85c-7f88671a1881] Encounter | 2025-08-03 | Encounter for symptom (procedure) | class AMB | reason: Acute viral pharyngitis (disorder) | at Pittsfield Outpatient Clinic
[Immunization/9292c3d5-3db6-f4f9-2e74-b2ab508532b8] Immunization | 2026-04-26 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/4b956949-62f0-1b19-b576-bf5bab485684#2] Clinical note | 2024-04-14 | part 2 of 2 | # Assessment and Plan Patient is presenting with stress (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - depression screening (procedure) - depression screening (procedure) The following lab reports were completed: - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - generalized anxiety disorder 7 item (gad-7) - patient health questionnaire 2 item (phq-2) [reported]
[DiagnosticReport/9292c3d5-3db6-f4f9-e482-70e5335a4db9] DiagnosticReport | 2021-03-28 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 143.24 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 134.54 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 61.64 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 54.69 mg/dL | LOINC 57698-3
[DiagnosticReport/9292c3d5-3db6-f4f9-942b-fd42eb23bc7e] DiagnosticReport | 2024-04-14 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 176 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 149.68 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 98.91 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 47.16 mg/dL | LOINC 57698-3
[DiagnosticReport/9292c3d5-3db6-f4f9-a143-1b13eb3cb929] DiagnosticReport | 2018-03-11 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 153.58 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 128.83 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 77.47 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 50.34 mg/dL | LOINC 57698-3
[DocumentReference/5922e550-66a0-0ffd-b471-f000f8e2d198#1] Clinical note | 2018-03-11 | part 1 of 1 | 2018-03-11 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 50 year-old nonhispanic white male. Patient has a history of medication review due (situation), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with stress (finding). ## Plan Patient was given the following immunizations: zoster vaccine, live, influenza, split virus, trivalent, pf. The following procedures were conducted: - assessment of health and social care needs (procedure) - depression screening (procedure) - depression screening (procedure) The following lab reports were completed: - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - patient health questionnaire 2 item (phq-2) [reported]
[DocumentReference/62150bd0-ea5c-0b8b-1705-b6da0e882541#1] Clinical note | 2021-03-28 | part 1 of 1 | 2021-03-28 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 53 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with full-time employment (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - screening for domestic abuse (procedure) The following lab reports were completed: - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - generalized anxiety disorder 7 item (gad-7) - humiliation, afraid, rape, and kick questionnaire [hark]
[DocumentReference/43776b3d-60c3-c1e3-e18c-cc61e6477899#2] Clinical note | 2020-03-22 | part 2 of 2 | # Assessment and Plan Patient is presenting with opioid abuse, stress (finding), severe anxiety (panic) (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - depression screening (procedure) - depression screening (procedure) - depression screening using patient health questionnaire nine item score (procedure) The following lab reports were completed: - basic metabolic panel - blood - cbc panel - blood by automated count - generalized anxiety disorder 7 item (gad-7) - patient health questionnaire 2 item (phq-2) [reported] - phq-9 quick depression assessment panel [reported.phq]
[DocumentReference/27beb8ef-05a0-4ef4-0299-31448a326503#2] Clinical note | 2025-04-20 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - depression screening (procedure) - depression screening (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - basic metabolic panel - blood - cbc panel - blood by automated count - patient health questionnaire 2 item (phq-2) [reported]
[Observation/9292c3d5-3db6-f4f9-d6ae-d5bc6ac24288] Observation (vital-signs) | 2025-04-20 | Blood pressure panel with all children optional = Diastolic Blood Pressure 72 mm[Hg]; Systolic Blood Pressure 133 mm[Hg] | status final | LOINC 85354-9
[Observation/9292c3d5-3db6-f4f9-a42e-d26907d21bcc] Observation (vital-signs) | 2026-04-26 | Blood pressure panel with all children optional = Diastolic Blood Pressure 76 mm[Hg]; Systolic Blood Pressure 133 mm[Hg] | status final | LOINC 85354-9
```

</details>

label: s
note: Cited 2021-03-28 lipid panel shows 143.24, 134.54, 61.64 and 54.69 mg/dL exactly; it is the panel immediately before 2024-04-14 (other panel is 2018-03-11).

## 28. `latest-lab-38483-4:8d945e28#0#0`

Question: What was the patient's most recent creatinine result, and when was it measured?

Answer: **The most recent creatinine result was a blood creatinine of 3.2229 mg/dL, measured on 2026-09-27.** The most recent serum/plasma creatinine was 2.2207 mg/dL on 2026-09-07.

Cards this sentence cites:

- `[Observation/8d945e28-1d8a-bd72-4f72-25ff83156a8e]` Observation (laboratory) | 2026-09-27 | Creatinine [Mass/volume] in Blood = 3.2229 mg/dL | status final | LOINC 38483-4

<details><summary>Everything the model saw (39 cards)</summary>

```text
[Condition/8d945e28-1d8a-bd72-9d6c-259e17157c55] Condition | onset 2026-09-07 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8d945e28-1d8a-bd72-3102-64b703ba601c] Condition | onset 2026-07-13 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8d945e28-1d8a-bd72-6b51-0718e8cd7a5e] Condition | onset 2021-01-01 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/8d945e28-1d8a-bd72-db4c-2552d073039a] Condition | onset 2020-11-09 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/8d945e28-1d8a-bd72-ed26-25aa62be033c] Condition | onset 2020-08-18 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/8d945e28-1d8a-bd72-05bf-4b4b02b03fe9] Condition | onset 2018-01-22 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/8d945e28-1d8a-bd72-38fb-c4bf927332c6] Condition | onset 2013-09-16 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/8d945e28-1d8a-bd72-1379-82140e2d1648] Condition | onset 2013-09-16 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/8d945e28-1d8a-bd72-cd47-b95fb1e4464b] Condition | onset 2009-07-06 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/8d945e28-1d8a-bd72-be1a-fb710d842e34] Condition | onset 2009-07-06 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/8d945e28-1d8a-bd72-2a55-0f3c986db8dd] Condition | onset 2009-07-06 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8d945e28-1d8a-bd72-4277-241d976b7354] Condition | onset 2007-06-25 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8d945e28-1d8a-bd72-e0ac-a99a0168ad8a] Condition | onset 2004-06-07 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/8d945e28-1d8a-bd72-a508-e7d1553f7f62] Condition | onset 2004-06-07 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/8d945e28-1d8a-bd72-2622-8fe0a1a30909] Condition | onset 2003-06-02 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8d945e28-1d8a-bd72-12e3-17db162c8f0b] Condition | onset 2001-06-04 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/8d945e28-1d8a-bd72-d01e-086bb9d1d22f] Condition | onset 2001-05-07 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/8d945e28-1d8a-bd72-f5fa-42692b5be159] Condition | onset 1996-08-05 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8d945e28-1d8a-bd72-e601-8e5493910aec] Condition | onset 1981-07-20 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8d945e28-1d8a-bd72-52ca-256d6584412c] Condition | onset 1981-07-20 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8d945e28-1d8a-bd72-d644-66738e889d91] Condition | onset 1977-07-11 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/8d945e28-1d8a-bd72-fbf9-3e6f6bd97f57] Condition | onset 1977-03-07 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/8d945e28-1d8a-bd72-ff5c-41daf21d65a9] MedicationRequest | prescribed 2026-09-07 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/8d945e28-1d8a-bd72-d409-38c0124f2c47] MedicationRequest | prescribed 2026-09-07 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/8d945e28-1d8a-bd72-bcd6-3304c42dca58] MedicationRequest | prescribed 1981-07-27 | Vitamin B12 5 MG/ML Injectable Solution | status active | RxNorm 2001499
[Encounter/8d945e28-1d8a-bd72-016c-9af67d7199fd] Encounter | 2026-09-27 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-3f01-7946bd8f2be1] Encounter | 2026-09-26 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-9dbd-785d1f0e4915] Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Immunization/8d945e28-1d8a-bd72-6a94-32775be2d4e6] Immunization | 2026-01-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/8d945e28-1d8a-bd72-e819-1af4731a79a8] Observation (laboratory) | 2025-08-18 | Creatinine [Mass/volume] in Blood = 14.65 mg/dL | status final | LOINC 38483-4
[Observation/8d945e28-1d8a-bd72-4f72-25ff83156a8e] Observation (laboratory) | 2026-09-27 | Creatinine [Mass/volume] in Blood = 3.2229 mg/dL | status final | LOINC 38483-4
[Observation/8d945e28-1d8a-bd72-6e70-f557b6766462] Observation (laboratory) | 2026-09-07 | Creatinine [Mass/volume] in Blood = 5.99 mg/dL | status final | LOINC 38483-4
[Observation/8d945e28-1d8a-bd72-dca2-97572a754115] Observation (laboratory) | 2026-08-27 | Creatinine [Mass/volume] in Blood = 2.9136 mg/dL | status final | LOINC 38483-4
[Immunization/8d945e28-1d8a-bd72-28c7-936105552d76] Immunization | 2021-05-17 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/8d945e28-1d8a-bd72-c212-27d34e4b0eef] Immunization | 2021-04-26 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Observation/8d945e28-1d8a-bd72-e39a-4e9f8c967431] Observation (laboratory) | 2020-02-17 | Creatinine [Mass/volume] in Serum or Plasma = 2.0175 mg/dL | status final | LOINC 2160-0
[Observation/8d945e28-1d8a-bd72-9051-a2597bc4f892] Observation (laboratory) | 2026-09-07 | Creatinine [Mass/volume] in Serum or Plasma = 2.2207 mg/dL | status final | LOINC 2160-0
[Observation/8d945e28-1d8a-bd72-f9f5-d1566ac0df20] Observation (laboratory) | 2026-07-13 | Creatinine [Mass/volume] in Serum or Plasma = 2.3357 mg/dL | status final | LOINC 2160-0
[Observation/8d945e28-1d8a-bd72-32fd-3b3868fecc1b] Observation (laboratory) | 2026-06-22 | Creatinine [Mass/volume] in Serum or Plasma = 2.4608 mg/dL | status final | LOINC 2160-0
```

</details>

label: s
note: Cited blood creatinine 3.2229 mg/dL on 2026-09-27; all other creatinine results seen (blood and serum) are dated earlier.

## 29. `lay-kidney-disease:772fc930#0#3`

Question: Has the patient ever been diagnosed with kidney disease? If so, when?

Answer: Yes, the patient has active kidney disease diagnoses: chronic kidney disease stage 1 and disorder of kidney due to diabetes mellitus, both with onset 2019-01-10. Chronic kidney disease stage 2 and microalbuminuria due to type 2 diabetes mellitus were recorded with onset 2020-01-16. Most recently, chronic kidney disease stage 3 and proteinuria due to type 2 diabetes mellitus were recorded with onset 2026-02-19. **All of these conditions are listed with clinical status active.**

Cards this sentence cites:

- `[Condition/772fc930-5418-0bfa-2c4f-3f5ed5953c36]` Condition | onset 2019-01-10 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
- `[Condition/772fc930-5418-0bfa-beac-a103fe7f3fd2]` Condition | onset 2019-01-10 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
- `[Condition/772fc930-5418-0bfa-ab71-24a74b1745fd]` Condition | onset 2020-01-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
- `[Condition/772fc930-5418-0bfa-bb6d-8a0b90cf95e4]` Condition | onset 2020-01-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
- `[Condition/772fc930-5418-0bfa-d3cc-a2daa4832199]` Condition | onset 2026-02-19 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
- `[Condition/772fc930-5418-0bfa-600b-5558ca66220a]` Condition | onset 2026-02-19 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108

<details><summary>Everything the model saw (41 cards)</summary>

```text
[Condition/772fc930-5418-0bfa-5baf-97b1667a332f] Condition | onset 2026-07-09 | Part-time employment (finding) | clinical status active | SNOMED 160904001
[Condition/772fc930-5418-0bfa-446c-c28d224cff31] Condition | onset 2026-06-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/772fc930-5418-0bfa-33d9-881f0ecc07c1] Condition | onset 2026-06-11 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/772fc930-5418-0bfa-d3cc-a2daa4832199] Condition | onset 2026-02-19 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/772fc930-5418-0bfa-600b-5558ca66220a] Condition | onset 2026-02-19 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/772fc930-5418-0bfa-6352-6c3984966ef8] Condition | onset 2025-02-13 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/772fc930-5418-0bfa-bb6d-8a0b90cf95e4] Condition | onset 2020-01-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/772fc930-5418-0bfa-ab71-24a74b1745fd] Condition | onset 2020-01-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/772fc930-5418-0bfa-beac-a103fe7f3fd2] Condition | onset 2019-01-10 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/772fc930-5418-0bfa-2c4f-3f5ed5953c36] Condition | onset 2019-01-10 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/772fc930-5418-0bfa-3873-02589386889d] Condition | onset 2004-06-19 | Osteoarthritis of hip (disorder) | clinical status active | SNOMED 239872002
[Condition/772fc930-5418-0bfa-a4a0-5eff492015a6] Condition | onset 1991-08-28 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/772fc930-5418-0bfa-01dc-3613408a83a6] Condition | onset 1991-08-22 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/772fc930-5418-0bfa-35d2-44b4eb4fcccc] Condition | onset 1991-08-08 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/772fc930-5418-0bfa-43ec-8fdd443cc6ce] Condition | onset 1988-07-21 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/772fc930-5418-0bfa-91e4-e46a214921b9] Condition | onset 1986-07-10 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/772fc930-5418-0bfa-47df-a943ca27aa29] Condition | onset 1986-07-10 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/772fc930-5418-0bfa-7d09-0ea3ca1e93ba] Condition | onset 1986-03-30 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/772fc930-5418-0bfa-1be5-06b5144b5817] Condition | onset 1986-03-01 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/772fc930-5418-0bfa-0cdf-ac369e474ff3] Condition | onset 1977-05-19 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/772fc930-5418-0bfa-f6df-7e2448081e0f] Condition | onset 1967-05-04 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/772fc930-5418-0bfa-ffbe-e3692c7542d7] Condition | onset 1964-01-15 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/772fc930-5418-0bfa-d2b4-bc5609421614] MedicationRequest | prescribed 2026-07-16 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/772fc930-5418-0bfa-35ed-4b81c08cb46e] MedicationRequest | prescribed 2026-07-16 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/772fc930-5418-0bfa-0d23-3b3c40dabcae] MedicationRequest | prescribed 2026-07-16 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/772fc930-5418-0bfa-ac79-a5117bd68db1] MedicationRequest | prescribed 2026-03-06 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/772fc930-5418-0bfa-dfc7-922f9300bced] MedicationRequest | prescribed 2004-06-19 | Naproxen sodium 220 MG Oral Tablet | status active | reason: Osteoarthritis of hip (disorder) | RxNorm 849574
[Encounter/772fc930-5418-0bfa-dd45-e4b82fc97e3d] Encounter | 2026-07-23 | Encounter for check up (procedure) | class AMB | at BOSTON MEDICAL CENTER CORPORATION-
[Encounter/772fc930-5418-0bfa-6606-662b1312d21c] Encounter | 2026-07-16 | Urgent care clinic (environment) | class AMB | at LYNN URGENT CARE LLC
[Encounter/772fc930-5418-0bfa-54c7-a3b13e8997b9] Encounter | 2026-07-09 | Emergency room admission (procedure) | class EMER | at LEONARD FLORENCE CENTER FOR LIVING
[Immunization/772fc930-5418-0bfa-fcca-2fca6db3fac3] Immunization | 2026-02-19 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/d7c0c753-f1ba-0f21-189c-0603918a2545#2] Clinical note | 2019-01-10 | part 2 of 2 | # Assessment and Plan Patient is presenting with chronic kidney disease stage 1 (disorder), disorder of kidney due to diabetes mellitus (disorder). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - sleep apnea assessment (procedure) - assessment of health and social care needs (procedure) - screening for domestic abuse (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - assessment using alcohol use disorders identification test - consumption (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - humiliation, afraid, rape, and kick questionnaire [hark] - patient health questionnaire 2 item (phq-2) [reported] - alcohol use disorder identification test - consumption [audit-c] The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]
[DocumentReference/dfa76361-a821-a3f2-02e8-3ea057c17409#2] Clinical note | 2026-02-19 | part 2 of 2 | # Assessment and Plan Patient is presenting with chronic kidney disease stage 3 (disorder), proteinuria due to type 2 diabetes mellitus (disorder), unemployed (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - sleep apnea assessment (procedure) - assessment of health and social care needs (procedure) - assessment using morse fall scale (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - assessment using alcohol use disorders identification test - consumption (procedure) The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine - basic metabolic panel - blood - morse fall scale panel - patient health questionnaire 2 item (phq-2) [reported] - alcohol use disorder identification test - consumption [audit-c] The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet
[DocumentReference/aa9a00bd-5594-50a1-dee0-8273d2f39041#1] Clinical note | 1991-08-08 | part 1 of 1 | 1991-08-08 # Chief Complaint - Hunger - Thirst - Fatigue - Frequent Urination # History of Present Illness Jimmie93 is a 42 year-old nonhispanic black male. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with ischemic heart disease (disorder). ## Plan
[DocumentReference/7d4f0552-8104-33cf-98b6-db467b077837#2] Clinical note | 2019-01-24 | part 2 of 2 | # Assessment and Plan Patient is presenting with dental caries on pit and fissure surface penetrating into pulp. ## Plan The following procedures were conducted: - extraction, erupted tooth requiring removal of bone and/or sectioning of tooth, and including elevation of mucoperiosteal flap if indicated - extraction, erupted tooth requiring removal of bone and/or sectioning of tooth, and including elevation of mucoperiosteal flap if indicated - extraction, erupted tooth requiring removal of bone and/or sectioning of tooth, and including elevation of mucoperiosteal flap if indicated
[Encounter/772fc930-5418-0bfa-df2a-dbe8c1f037b3] Encounter | 1991-08-22 | Encounter for problem (procedure) | class AMB | reason: Ischemic heart disease (disorder) | at Fitchburg Outpatient Clinic
[Procedure/772fc930-5418-0bfa-0852-bc6028aad8cf] Procedure | 2019-06-20 | extraction, erupted tooth requiring removal of bone and/or sectioning of tooth, and including elevation of mucoperiosteal flap if indicated | status completed | http://www.ada.org/cdt D7210
[Procedure/772fc930-5418-0bfa-a48e-e93b1f25ac84] Procedure | 2019-01-24 | extraction, erupted tooth requiring removal of bone and/or sectioning of tooth, and including elevation of mucoperiosteal flap if indicated | status completed | http://www.ada.org/cdt D7210
[Procedure/772fc930-5418-0bfa-267c-ea76a7a32965] Procedure | 2019-01-24 | extraction, erupted tooth requiring removal of bone and/or sectioning of tooth, and including elevation of mucoperiosteal flap if indicated | status completed | http://www.ada.org/cdt D7210
[Condition/772fc930-5418-0bfa-6707-0fea8a3379ca] Condition | onset 2018-01-04 | Full-time employment (finding) | clinical status resolved | resolved 2020-11-19 | SNOMED 160903007
[Condition/772fc930-5418-0bfa-6ff6-df88955e5668] Condition | onset 2026-04-30 | Full-time employment (finding) | clinical status resolved | resolved 2026-07-09 | SNOMED 160903007
```

</details>

label: s
note: All six kidney conditions named in the answer are cited and each card shows clinical status active.

## 30. `prescribed-for-essential-hypertension:e56a8cde#0#0`

Question: Which medications have been prescribed for the patient's essential hypertension?

Answer: **The only medication explicitly prescribed with essential hypertension as the reason is lisinopril 10 MG Oral Tablet, with an active prescription dated 2025-12-25.** Earlier lisinopril 10 MG Oral Tablet prescriptions for essential hypertension, now completed, were dated 2018-11-15, 2023-12-14, and 2024-12-19. The patient also has an active hydrochlorothiazide 25 MG / lisinopril 20 MG Oral Tablet prescribed 2003-12-16, but no reason is listed for it.

Cards this sentence cites:

- `[MedicationRequest/e56a8cde-8395-a37d-1cff-386c29158923]` MedicationRequest | prescribed 2025-12-25 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076

<details><summary>Everything the model saw (56 cards)</summary>

```text
[Condition/e56a8cde-8395-a37d-f7ae-15d35f13e9f0] Condition | onset 2025-12-25 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/e56a8cde-8395-a37d-80d3-3984f14d8bb3] Condition | onset 2025-12-25 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/e56a8cde-8395-a37d-5c7c-75429c6f1e56] Condition | onset 2025-12-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/e56a8cde-8395-a37d-354e-df92238c35a7] Condition | onset 2025-12-25 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/e56a8cde-8395-a37d-6690-7ef5746552bd] Condition | onset 2017-11-09 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/e56a8cde-8395-a37d-922a-d32061194c0b] Condition | onset 2016-11-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/e56a8cde-8395-a37d-e775-23849ffbe97b] Condition | onset 2014-02-01 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/e56a8cde-8395-a37d-a82c-6129bc784139] Condition | onset 2014-02-01 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/e56a8cde-8395-a37d-64b8-86023f198a46] Condition | onset 2014-02-01 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/e56a8cde-8395-a37d-e547-8e085bacfa8e] Condition | onset 2007-09-13 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/e56a8cde-8395-a37d-37b4-500cf9e797e9] Condition | onset 2005-09-01 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/e56a8cde-8395-a37d-d5cb-6239a28a0055] Condition | onset 2003-12-16 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/e56a8cde-8395-a37d-4d5f-670d3e1632bc] Condition | onset 2003-12-16 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/e56a8cde-8395-a37d-1853-568436ee1ea2] Condition | onset 2001-08-20 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/e56a8cde-8395-a37d-810b-643d651149ba] Condition | onset 2001-08-18 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/e56a8cde-8395-a37d-2761-7d0bfc799087] Condition | onset 2001-08-09 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/e56a8cde-8395-a37d-ed31-c4144dbefb9e] Condition | onset 1996-05-17 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
[Condition/e56a8cde-8395-a37d-333f-0835bee4de98] Condition | onset 1991-06-13 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/e56a8cde-8395-a37d-30cd-5f4f9de67da3] Condition | onset 1967-07-27 | Lack of access to transportation (finding) | clinical status active | SNOMED 713458007
[Condition/e56a8cde-8395-a37d-ac70-0b466edf16a1] Condition | onset 1963-07-18 | Transport problem (finding) | clinical status active | SNOMED 266934004
[Condition/e56a8cde-8395-a37d-99e6-93fe1e3f6036] Condition | onset 1963-07-18 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/e56a8cde-8395-a37d-0c1b-7da0b396a0c4] MedicationRequest | prescribed 2026-01-01 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/e56a8cde-8395-a37d-f153-06ed5ef5b40a] MedicationRequest | prescribed 2025-12-25 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/e56a8cde-8395-a37d-b70b-d6ff9e66fb91] MedicationRequest | prescribed 2025-12-25 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/e56a8cde-8395-a37d-1cff-386c29158923] MedicationRequest | prescribed 2025-12-25 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/e56a8cde-8395-a37d-f778-f1044e9a8316] MedicationRequest | prescribed 2003-12-16 | atorvastatin 10 MG Oral Tablet | status active | RxNorm 617312
[MedicationRequest/e56a8cde-8395-a37d-e36e-ab680e0ad841] MedicationRequest | prescribed 2003-12-16 | hydrochlorothiazide 25 MG / lisinopril 20 MG Oral Tablet | status active | RxNorm 197887
[MedicationRequest/e56a8cde-8395-a37d-d237-6e376bbcb9a6] MedicationRequest | prescribed 2003-12-16 | metoprolol tartrate 25 MG Oral Tablet | status active | RxNorm 866924
[MedicationRequest/e56a8cde-8395-a37d-2fb4-edeac8b69b00] MedicationRequest | prescribed 2003-12-16 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/e56a8cde-8395-a37d-228f-f6135c165caa] MedicationRequest | prescribed 2003-12-16 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/e56a8cde-8395-a37d-eee1-8d05287f0e29] MedicationRequest | prescribed 2001-08-16 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/e56a8cde-8395-a37d-d36b-2e3fc9df975e] MedicationRequest | prescribed 2001-08-16 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/e56a8cde-8395-a37d-a8c0-f9ed9ed3ea83] MedicationRequest | prescribed 2001-08-16 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/e56a8cde-8395-a37d-321f-ecd1d25263ad] MedicationRequest | prescribed 2001-08-16 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/e56a8cde-8395-a37d-9456-c58ec0c7de32] MedicationRequest | prescribed 1949-01-17 | diphenhydrAMINE Hydrochloride 25 MG Oral Tablet | status active | RxNorm 1049630
[AllergyIntolerance/e56a8cde-8395-a37d-b318-8f34a7d6b5f7] AllergyIntolerance | recorded 1946-06-09 | Animal dander (substance) | allergy, category environment, criticality low | clinical status active | reactions: Eruption of skin (disorder); Rhinoconjunctivitis (disorder) | SNOMED 264287008
[AllergyIntolerance/e56a8cde-8395-a37d-a098-9831a40ac85b] AllergyIntolerance | recorded 1946-06-09 | Mold (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 84489001
[AllergyIntolerance/e56a8cde-8395-a37d-85d4-fe7519012219] AllergyIntolerance | recorded 1946-06-09 | House dust mite (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 260147004
[AllergyIntolerance/e56a8cde-8395-a37d-60c2-b75e4a4d4513] AllergyIntolerance | recorded 1946-06-09 | Tree pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 782576004
[AllergyIntolerance/e56a8cde-8395-a37d-5834-224d1127b6f9] AllergyIntolerance | recorded 1946-06-09 | Grass pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 256277009
[AllergyIntolerance/e56a8cde-8395-a37d-2daa-dbe0dbcf6ecf] AllergyIntolerance | recorded 1946-06-09 | Shellfish (substance) | allergy, category food, criticality low | clinical status active | reactions: Dyspnea (finding); Allergic angioedema (disorder); Itching (finding); Cough (finding); Diarrhea (finding) | SNOMED 735029006
[AllergyIntolerance/e56a8cde-8395-a37d-1508-bdb84bdc4c5d] AllergyIntolerance | recorded 1946-06-09 | Allergic disposition (finding) | allergy, category environment, criticality low | clinical status active | SNOMED 609328004
[Encounter/e56a8cde-8395-a37d-9f47-5b69723a8690] Encounter | 2026-01-01 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Encounter/e56a8cde-8395-a37d-2450-250d53d64dc7] Encounter | 2025-12-25 | General examination of patient (procedure) | class AMB | at SOUTH SHORE PRIMARY CARE PC
[Encounter/e56a8cde-8395-a37d-20eb-f707e34a4164] Encounter | 2024-12-20 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Immunization/e56a8cde-8395-a37d-7cd1-bb3bac5572f3] Immunization | 2025-12-25 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/e56a8cde-8395-a37d-1c97-f6f1f0dcff32] MedicationRequest | prescribed 2018-11-15 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/e56a8cde-8395-a37d-113f-0e46a68fe792] MedicationRequest | prescribed 2024-12-19 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/e56a8cde-8395-a37d-d302-91764b74fa83] MedicationRequest | prescribed 2023-12-14 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
[CarePlan/e56a8cde-8395-a37d-a7c9-f2e28ace776b] CarePlan | started 1991-06-13 | Lifestyle education regarding hypertension (procedure) | status active | activities: Prescribed activity/exercise education (procedure); Counseling about alcohol consumption (procedure); Dietary Approaches to Stop Hypertension diet (regime/therapy); Smoking cessation education (procedure)
[DocumentReference/776858d3-4a9b-c831-91ff-7999eff89090#2] Clinical note | 2021-12-09 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/494317a8-1900-de5b-7b5a-de4de13287b2#2] Clinical note | 2026-01-01 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/2e83ca5b-0566-c4f8-c3f6-ebd76fc34712#2] Clinical note | 2023-12-21 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/7504f1c0-58e2-6285-f81f-87337a5ecce1#1] Clinical note | 1991-06-13 | part 1 of 1 | 1991-06-13 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 46 year-old nonhispanic white male. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicaid. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with essential hypertension (disorder). ## Plan The patient was placed on a careplan: - lifestyle education regarding hypertension (procedure)
[DocumentReference/b90b3a01-6a64-0ced-e3f1-7cfa3f1d1322#2] Clinical note | 2024-12-20 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/67c3d2e5-fd00-fa7a-99db-998bc532a3d1#2] Clinical note | 2022-12-09 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
```

</details>

label: s
note: Every MedicationRequest with reason Essential hypertension is lisinopril 10 MG Oral Tablet, and the cited 2025-12-25 one is active; the HCTZ/lisinopril combo has no reason listed.

## 31. `latest-lab-2947-0:0eeb6aa3#0#0`

Question: What was the patient's most recent sodium result, and when was it measured?

Answer: **The most recent sodium result was 141.35 mmol/L, measured on 2026-08-09.**

Cards this sentence cites:

- `[Observation/0eeb6aa3-c249-0e46-ac92-4cb517815376]` Observation (laboratory) | 2026-08-09 | Sodium [Moles/volume] in Blood = 141.35 mmol/L | status final | LOINC 2947-0

<details><summary>Everything the model saw (36 cards)</summary>

```text
[Condition/0eeb6aa3-c249-0e46-6f19-eb10a1f328db] Condition | onset 2026-07-29 | Primary fibromyalgia syndrome (disorder) | clinical status active | SNOMED 95417003
[Condition/0eeb6aa3-c249-0e46-44b4-3580330e81b7] Condition | onset 2025-12-14 | Misuses drugs (finding) | clinical status active | SNOMED 361055000
[Condition/0eeb6aa3-c249-0e46-2c95-28a9408c6896] Condition | onset 2025-12-14 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/0eeb6aa3-c249-0e46-b1be-047f25b1022e] Condition | onset 2022-11-27 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/0eeb6aa3-c249-0e46-6def-33ad344a7a9b] Condition | onset 2022-11-27 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/0eeb6aa3-c249-0e46-06a5-9d3ec2ee65d0] Condition | onset 2022-11-27 | Hyperglycemia (disorder) | clinical status active | SNOMED 80394007
[Condition/0eeb6aa3-c249-0e46-d84e-f3245ad02f8e] Condition | onset 2021-11-21 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/0eeb6aa3-c249-0e46-ce58-8dd4753fcdb4] Condition | onset 2021-11-21 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/0eeb6aa3-c249-0e46-8d5d-18bd4ff7c429] Condition | onset 2021-11-21 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/0eeb6aa3-c249-0e46-0e2a-b4435a3e06d7] Condition | onset 2021-04-07 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
[Condition/0eeb6aa3-c249-0e46-c1e0-a1835f8dfe99] Condition | onset 2013-11-03 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/0eeb6aa3-c249-0e46-7e82-50da4e26d936] Condition | onset 2009-08-25 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/0eeb6aa3-c249-0e46-05b2-ee89706489e7] Condition | onset 2008-01-13 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/0eeb6aa3-c249-0e46-1bf9-48c5ad5ed3c4] Condition | onset 1991-12-22 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/0eeb6aa3-c249-0e46-7231-74f682325091] Condition | onset 1988-12-04 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/0eeb6aa3-c249-0e46-d035-2af008a23544] MedicationRequest | prescribed 2026-08-09 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/0eeb6aa3-c249-0e46-9e8f-3bc3a049dcd6] MedicationRequest | prescribed 2026-08-09 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/0eeb6aa3-c249-0e46-9979-087d4ecb9395] MedicationRequest | prescribed 2026-08-09 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/0eeb6aa3-c249-0e46-8801-c4efefa8fdf6] MedicationRequest | prescribed 2026-08-09 | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 860975
[MedicationRequest/0eeb6aa3-c249-0e46-48fb-484102ab7f68] MedicationRequest | prescribed 2026-07-29 | Naproxen 500 MG Oral Tablet | status active | reason: Primary fibromyalgia syndrome (disorder) | RxNorm 198014
[MedicationRequest/0eeb6aa3-c249-0e46-7cb4-1e0c24948d9a] MedicationRequest | prescribed 2021-04-07 | Naproxen sodium 220 MG Oral Tablet | status active | reason: Osteoarthritis of knee (disorder) | RxNorm 849574
[MedicationRequest/0eeb6aa3-c249-0e46-6749-08c77e3ff56d] MedicationRequest | prescribed 1993-03-28 | ferrous sulfate 325 MG Oral Tablet | status active | RxNorm 310325
[Encounter/0eeb6aa3-c249-0e46-4c0e-5bc7f2736fbd] Encounter | 2026-08-09 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/0eeb6aa3-c249-0e46-43a1-ecea1c0a2a61] Encounter | 2026-07-29 | Encounter for problem (procedure) | class AMB | reason: Primary fibromyalgia syndrome (disorder) | at HOLY FAMILY HOSPITAL
[Encounter/0eeb6aa3-c249-0e46-d415-7e8395059f69] Encounter | 2026-01-04 | Encounter for check up (procedure) | class AMB | reason: Patient referral for dental care (procedure) | at HOLY FAMILY HOSPITAL
[Immunization/0eeb6aa3-c249-0e46-99a3-4dae451772fe] Immunization | 2026-08-09 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/0eeb6aa3-c249-0e46-5394-ebecf2313549] Observation (laboratory) | 2025-12-14 | Sodium [Moles/volume] in Blood = 140.48 mmol/L | status final | LOINC 2947-0
[Observation/0eeb6aa3-c249-0e46-ac92-4cb517815376] Observation (laboratory) | 2026-08-09 | Sodium [Moles/volume] in Blood = 141.35 mmol/L | status final | LOINC 2947-0
[Observation/0eeb6aa3-c249-0e46-a647-e63c62329e74] Observation (laboratory) | 2025-07-20 | Sodium [Moles/volume] in Blood = 138.76 mmol/L | status final | LOINC 2947-0
[Immunization/0eeb6aa3-c249-0e46-7a2a-645241e28212] Immunization | 2021-04-11 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/0eeb6aa3-c249-0e46-b7a5-0b7440de25ee] Immunization | 2021-03-21 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Observation/0eeb6aa3-c249-0e46-8a24-69571225b941] Observation (laboratory) | 2025-12-14 | Potassium [Moles/volume] in Blood = 3.89 mmol/L | status final | LOINC 6298-4
[Observation/0eeb6aa3-c249-0e46-840c-852b8864af07] Observation (laboratory) | 2026-08-09 | Potassium [Moles/volume] in Blood = 4.92 mmol/L | status final | LOINC 6298-4
[Observation/0eeb6aa3-c249-0e46-03fb-b6910e51290e] Observation (laboratory) | 2025-07-20 | Potassium [Moles/volume] in Blood = 3.88 mmol/L | status final | LOINC 6298-4
[Observation/0eeb6aa3-c249-0e46-ba58-54660e75d0aa] Observation (laboratory) | 2025-07-20 | Triglyceride [Mass/volume] in Serum or Plasma = 128.87 mg/dL | status final | LOINC 2571-8
[Observation/0eeb6aa3-c249-0e46-06cb-b1c687975c99] Observation (laboratory) | 2026-08-09 | Triglyceride [Mass/volume] in Serum or Plasma = 117.89 mg/dL | status final | LOINC 2571-8
```

</details>

label: s
note: Cited card shows sodium 141.35 mmol/L on 2026-08-09; the other sodium cards (2025-12-14 140.48, 2025-07-20 138.76) are older, so it is the most recent.

## 32. `latest-lab-4548-4:772fc930#0#1`

Question: What was the patient's most recent hemoglobin A1c result, and when was it measured?

Answer: The most recent hemoglobin A1c result was 3.11 %, measured on 2026-07-16. **Earlier values were 2.96 % on 2026-07-09 and 3.35 % on 2026-07-02.**

Cards this sentence cites:

- `[Observation/772fc930-5418-0bfa-6626-57894070b798]` Observation (laboratory) | 2026-07-09 | Hemoglobin A1c/Hemoglobin.total in Blood = 2.96 % | status final | LOINC 4548-4
- `[Observation/772fc930-5418-0bfa-addb-602a5c27802f]` Observation (laboratory) | 2026-07-02 | Hemoglobin A1c/Hemoglobin.total in Blood = 3.35 % | status final | LOINC 4548-4

<details><summary>Everything the model saw (41 cards)</summary>

```text
[Condition/772fc930-5418-0bfa-5baf-97b1667a332f] Condition | onset 2026-07-09 | Part-time employment (finding) | clinical status active | SNOMED 160904001
[Condition/772fc930-5418-0bfa-446c-c28d224cff31] Condition | onset 2026-06-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/772fc930-5418-0bfa-33d9-881f0ecc07c1] Condition | onset 2026-06-11 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/772fc930-5418-0bfa-d3cc-a2daa4832199] Condition | onset 2026-02-19 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/772fc930-5418-0bfa-600b-5558ca66220a] Condition | onset 2026-02-19 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/772fc930-5418-0bfa-6352-6c3984966ef8] Condition | onset 2025-02-13 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/772fc930-5418-0bfa-bb6d-8a0b90cf95e4] Condition | onset 2020-01-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/772fc930-5418-0bfa-ab71-24a74b1745fd] Condition | onset 2020-01-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/772fc930-5418-0bfa-beac-a103fe7f3fd2] Condition | onset 2019-01-10 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/772fc930-5418-0bfa-2c4f-3f5ed5953c36] Condition | onset 2019-01-10 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/772fc930-5418-0bfa-3873-02589386889d] Condition | onset 2004-06-19 | Osteoarthritis of hip (disorder) | clinical status active | SNOMED 239872002
[Condition/772fc930-5418-0bfa-a4a0-5eff492015a6] Condition | onset 1991-08-28 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/772fc930-5418-0bfa-01dc-3613408a83a6] Condition | onset 1991-08-22 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/772fc930-5418-0bfa-35d2-44b4eb4fcccc] Condition | onset 1991-08-08 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/772fc930-5418-0bfa-43ec-8fdd443cc6ce] Condition | onset 1988-07-21 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/772fc930-5418-0bfa-91e4-e46a214921b9] Condition | onset 1986-07-10 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/772fc930-5418-0bfa-47df-a943ca27aa29] Condition | onset 1986-07-10 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/772fc930-5418-0bfa-7d09-0ea3ca1e93ba] Condition | onset 1986-03-30 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/772fc930-5418-0bfa-1be5-06b5144b5817] Condition | onset 1986-03-01 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/772fc930-5418-0bfa-0cdf-ac369e474ff3] Condition | onset 1977-05-19 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/772fc930-5418-0bfa-f6df-7e2448081e0f] Condition | onset 1967-05-04 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/772fc930-5418-0bfa-ffbe-e3692c7542d7] Condition | onset 1964-01-15 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/772fc930-5418-0bfa-d2b4-bc5609421614] MedicationRequest | prescribed 2026-07-16 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/772fc930-5418-0bfa-35ed-4b81c08cb46e] MedicationRequest | prescribed 2026-07-16 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/772fc930-5418-0bfa-0d23-3b3c40dabcae] MedicationRequest | prescribed 2026-07-16 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/772fc930-5418-0bfa-ac79-a5117bd68db1] MedicationRequest | prescribed 2026-03-06 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/772fc930-5418-0bfa-dfc7-922f9300bced] MedicationRequest | prescribed 2004-06-19 | Naproxen sodium 220 MG Oral Tablet | status active | reason: Osteoarthritis of hip (disorder) | RxNorm 849574
[Encounter/772fc930-5418-0bfa-dd45-e4b82fc97e3d] Encounter | 2026-07-23 | Encounter for check up (procedure) | class AMB | at BOSTON MEDICAL CENTER CORPORATION-
[Encounter/772fc930-5418-0bfa-6606-662b1312d21c] Encounter | 2026-07-16 | Urgent care clinic (environment) | class AMB | at LYNN URGENT CARE LLC
[Encounter/772fc930-5418-0bfa-54c7-a3b13e8997b9] Encounter | 2026-07-09 | Emergency room admission (procedure) | class EMER | at LEONARD FLORENCE CENTER FOR LIVING
[Immunization/772fc930-5418-0bfa-fcca-2fca6db3fac3] Immunization | 2026-02-19 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/772fc930-5418-0bfa-8957-dbea8fe67de6] Observation (laboratory) | 2026-07-16 | Hemoglobin A1c/Hemoglobin.total in Blood = 3.11 % | status final | LOINC 4548-4
[Observation/772fc930-5418-0bfa-6626-57894070b798] Observation (laboratory) | 2026-07-09 | Hemoglobin A1c/Hemoglobin.total in Blood = 2.96 % | status final | LOINC 4548-4
[Observation/772fc930-5418-0bfa-addb-602a5c27802f] Observation (laboratory) | 2026-07-02 | Hemoglobin A1c/Hemoglobin.total in Blood = 3.35 % | status final | LOINC 4548-4
[Immunization/772fc930-5418-0bfa-f6dc-d21e77adc05b] Immunization | 2021-03-25 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/772fc930-5418-0bfa-21ee-34551e99d21d] Immunization | 2021-03-04 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Observation/772fc930-5418-0bfa-7e47-5513c13c06fe] Observation (laboratory) | 2020-11-19 | Glucose [Mass/volume] in Serum or Plasma = 80.4 mg/dL | status final | LOINC 2345-7
[Observation/772fc930-5418-0bfa-3780-16c841b6aea4] Observation (laboratory) | 2026-07-16 | Glucose [Mass/volume] in Serum or Plasma = 80.62 mg/dL | status final | LOINC 2345-7
[Observation/772fc930-5418-0bfa-c067-0d6fbb03112f] Observation (laboratory) | 2026-07-09 | Glucose [Mass/volume] in Serum or Plasma = 71.92 mg/dL | status final | LOINC 2345-7
[Observation/772fc930-5418-0bfa-c227-27c7dbd5f578] Observation (laboratory) | 2026-07-02 | Glucose [Mass/volume] in Serum or Plasma = 82.74 mg/dL | status final | LOINC 2345-7
[Observation/772fc930-5418-0bfa-0901-f1e59b801f10] Observation (laboratory) | 2023-02-02 | Hemoglobin [Mass/volume] in Blood = 14.966 g/dL | status final | LOINC 718-7
```

</details>

label: s
note: Cited cards show A1c 2.96 % on 2026-07-09 and 3.35 % on 2026-07-02; these are the only A1c values besides the 2026-07-16 one, so the list of earlier values is complete.

## 33. `latest-lab-718-7:0e6e0d73#0#0`

Question: What was the patient's most recent hemoglobin result, and when was it measured?

Answer: **The most recent hemoglobin result was 13.492 g/dL, measured on 2024-05-20.** The prior value was 13.379 g/dL on 2018-07-30.

Cards this sentence cites:

- `[Observation/0e6e0d73-619d-15c3-6786-d558c33391e3]` Observation (laboratory) | 2024-05-20 | Hemoglobin [Mass/volume] in Blood = 13.492 g/dL | status final | LOINC 718-7

<details><summary>Everything the model saw (26 cards)</summary>

```text
[Condition/0e6e0d73-619d-15c3-1198-27a3f1e6671d] Condition | onset 2026-05-25 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/0e6e0d73-619d-15c3-73bb-c4435e198a52] Condition | onset 2021-08-16 | Unhealthy alcohol drinking behavior (finding) | clinical status active | SNOMED 10939881000119105
[Condition/0e6e0d73-619d-15c3-a2af-2198a3d15909] Condition | onset 2021-08-02 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/0e6e0d73-619d-15c3-7d75-d0dd94ac6175] Condition | onset 2018-04-30 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/0e6e0d73-619d-15c3-dabb-3f18b4ab6eed] Condition | onset 2017-09-23 | Sepsis (disorder) | clinical status active | SNOMED 91302008
[Condition/0e6e0d73-619d-15c3-279b-bad1f131dc84] Condition | onset 2017-09-23 | Septic shock (disorder) | clinical status active | SNOMED 76571007
[Condition/0e6e0d73-619d-15c3-252c-3ec5aec72d7f] Condition | onset 2006-07-17 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/0e6e0d73-619d-15c3-a3b6-7fc6f2b594a9] Condition | onset 2002-07-08 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
[Condition/0e6e0d73-619d-15c3-a0ee-8e9994e38bf4] Condition | onset 2001-07-02 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/0e6e0d73-619d-15c3-e363-3a1afa521a17] MedicationRequest | prescribed 2026-07-12 | {21 (ethinyl estradiol 0.03 MG / levonorgestrel 0.15 MG Oral Tablet) / 7 (inert ingredients 1 MG Oral Tablet) } Pack [Levora 0.15/30 28 Day] | status active | RxNorm 748879
[Encounter/0e6e0d73-619d-15c3-9366-052e1e643c56] Encounter | 2026-07-12 | Consultation for treatment (procedure) | class AMB | reason: Contraception care (regime/therapy) | at NEW ENGLAND SINAI HOSPITAL
[Encounter/0e6e0d73-619d-15c3-60c1-89e78f0afd63] Encounter | 2026-05-25 | General examination of patient (procedure) | class AMB | at ENRICH WELLNESS HEALTH CENTER LLC
[Encounter/0e6e0d73-619d-15c3-08dc-dd55aa3a67ea] Encounter | 2025-07-17 | Consultation for treatment (procedure) | class AMB | reason: Contraception care (regime/therapy) | at NEW ENGLAND SINAI HOSPITAL
[Immunization/0e6e0d73-619d-15c3-f93b-2cd3ab790ac4] Immunization | 2026-05-25 | Hep A, adult | status completed | CVX 52
[Immunization/0e6e0d73-619d-15c3-e4c7-db7a86392a05] Immunization | 2026-05-25 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/0e6e0d73-619d-15c3-8254-2b4f6f2ea96c] Immunization | 2026-05-25 | Td (adult), 5 Lf tetanus toxoid, preservative free, adsorbed | status completed | CVX 113
[Observation/0e6e0d73-619d-15c3-6786-d558c33391e3] Observation (laboratory) | 2024-05-20 | Hemoglobin [Mass/volume] in Blood = 13.492 g/dL | status final | LOINC 718-7
[Observation/0e6e0d73-619d-15c3-00e7-bbb425757b35] Observation (laboratory) | 2018-07-30 | Hemoglobin [Mass/volume] in Blood = 13.379 g/dL | status final | LOINC 718-7
[Procedure/0e6e0d73-619d-15c3-52da-e54c292746b8] Procedure | 2024-02-26 | Hemogram, automated, with red blood cells, white blood cells, hemoglobin, hematocrit, indices, platelet count, and manual white blood cell differential (procedure) | status completed | reason: Normal pregnancy (finding) | SNOMED 104091002
[Procedure/0e6e0d73-619d-15c3-d90a-5b7b5334e56a] Procedure | 2023-10-09 | Hemogram, automated, with red blood cells, white blood cells, hemoglobin, hematocrit, indices, platelet count, and manual white blood cell differential (procedure) | status completed | reason: Normal pregnancy (finding) | SNOMED 104091002
[DocumentReference/6dd5703a-f87e-5aa8-16c9-3682c2b0d434#2] Clinical note | 2024-02-26 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - hemogram, automated, with red blood cells, white blood cells, hemoglobin, hematocrit, indices, platelet count, and manual white blood cell differential (procedure) - administration of vaccine product containing only bordetella pertussis and clostridium tetani and corynebacterium diphtheriae antigens (procedure) - urine screening for glucose (procedure) - evaluation of uterine fundal height (procedure) - auscultation of the fetal heart (procedure)
[Immunization/0e6e0d73-619d-15c3-d9fe-411f70377225] Immunization | 2021-05-03 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/0e6e0d73-619d-15c3-bcce-05ce5d24a078] Immunization | 2021-04-12 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Observation/0e6e0d73-619d-15c3-368d-f3ed675286b2] Observation (laboratory) | 2024-05-20 | Erythrocyte [DistWidth] in Blood by Automated count = 43.17 fL | status final | LOINC 788-0
[Observation/0e6e0d73-619d-15c3-3549-46314f19d8d2] Observation (laboratory) | 2018-07-30 | Erythrocyte [DistWidth] in Blood by Automated count = 42.042 fL | status final | LOINC 788-0
[Observation/0e6e0d73-619d-15c3-18a2-de2db5df728f] Observation (laboratory) | 2024-05-20 | Hematocrit [Volume Fraction] of Blood by Automated count = 45.425 % | status final | LOINC 4544-3
```

</details>

label: s
note: Cited card shows hemoglobin 13.492 g/dL on 2024-05-20; the only other hemoglobin value is 2018-07-30 and the hemogram procedures (2023-10-09, 2024-02-26) are earlier and carry no value.

## 34. `latest-lab-4548-4:7280f7f8#0#1`

Question: What was the patient's most recent hemoglobin A1c result, and when was it measured?

Answer: The most recent hemoglobin A1c was 5.88 %, measured on 2026-04-12. **Earlier values were 5.82 % on 2025-04-06 and 6.22 % on 2024-11-24.**

Cards this sentence cites:

- `[Observation/7280f7f8-315d-7c6a-f1f5-c7da1cd21d22]` Observation (laboratory) | 2025-04-06 | Hemoglobin A1c/Hemoglobin.total in Blood = 5.82 % | status final | LOINC 4548-4
- `[Observation/7280f7f8-315d-7c6a-e7ed-08eb1135a541]` Observation (laboratory) | 2024-11-24 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.22 % | status final | LOINC 4548-4

<details><summary>Everything the model saw (43 cards)</summary>

```text
[Condition/7280f7f8-315d-7c6a-5183-1fc53612d856] Condition | onset 2026-04-12 | Alzheimer's disease (disorder) | clinical status active | SNOMED 26929004
[Condition/7280f7f8-315d-7c6a-069f-25fdb34e3e53] Condition | onset 2025-04-06 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/7280f7f8-315d-7c6a-06ae-a26712c6cfb7] Condition | onset 2024-03-31 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/7280f7f8-315d-7c6a-84b2-d6045a9b8deb] Condition | onset 2018-11-12 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/7280f7f8-315d-7c6a-60b8-1b2b3b190d66] Condition | onset 2018-11-04 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/7280f7f8-315d-7c6a-eee1-33d3eda16b26] Condition | onset 2014-02-16 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/7280f7f8-315d-7c6a-23b9-2a24d0c43093] Condition | onset 2014-02-16 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/7280f7f8-315d-7c6a-f371-666500850eb4] Condition | onset 2014-02-02 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/7280f7f8-315d-7c6a-b5ea-aa0955ebc2c7] Condition | onset 2010-01-10 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/7280f7f8-315d-7c6a-929f-e845c91bba18] Condition | onset 1993-02-06 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/7280f7f8-315d-7c6a-6159-244929402415] Condition | onset 1991-07-09 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/7280f7f8-315d-7c6a-7561-551dd4fb980c] Condition | onset 1990-11-11 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/7280f7f8-315d-7c6a-69cb-9f6bde195716] Condition | onset 1990-10-25 | Impacted molars (disorder) | clinical status active | SNOMED 196416002
[Condition/7280f7f8-315d-7c6a-e183-7fc41f06abde] Condition | onset 1990-02-06 | Chronic intractable migraine without aura (disorder) | clinical status active | SNOMED 124171000119105
[Condition/7280f7f8-315d-7c6a-57cd-16215a141add] Condition | onset 1988-11-06 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/7280f7f8-315d-7c6a-7c25-7a247f43e721] Condition | onset 1981-01-18 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/7280f7f8-315d-7c6a-50ac-70390520f5d8] Condition | onset 1981-01-18 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/7280f7f8-315d-7c6a-a35c-5f2c4404e1cd] Condition | onset 1971-02-18 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/7280f7f8-315d-7c6a-cf3c-1559c1e270a8] Condition | onset 1964-12-20 | Housing unsatisfactory (finding) | clinical status active | SNOMED 105531004
[Condition/7280f7f8-315d-7c6a-3735-89103641aea2] Condition | onset 1964-12-20 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/7280f7f8-315d-7c6a-d103-5f5cf25ace53] MedicationRequest | prescribed 2026-04-13 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/7280f7f8-315d-7c6a-dd3c-435b565b36d4] MedicationRequest | prescribed 2026-04-12 | Ibuprofen 400 MG Oral Tablet [Ibu] | status active | RxNorm 206905
[MedicationRequest/7280f7f8-315d-7c6a-698d-8c3f4a330263] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG / Oxycodone Hydrochloride 10 MG Oral Tablet [Percocet] | status active | RxNorm 1049625
[MedicationRequest/7280f7f8-315d-7c6a-53dc-677516ba315e] MedicationRequest | prescribed 2026-04-12 | Galantamine 4 MG Oral Tablet | status active | reason: Alzheimer's disease (disorder) | RxNorm 310436
[MedicationRequest/7280f7f8-315d-7c6a-21fd-127361ce4eae] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-e1ca-6672a64e96d6] MedicationRequest | prescribed 2018-11-11 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/7280f7f8-315d-7c6a-d3dc-bf227b26b9de] MedicationRequest | prescribed 2018-11-11 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/7280f7f8-315d-7c6a-40f0-094ac0d35606] MedicationRequest | prescribed 2018-11-11 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/7280f7f8-315d-7c6a-344e-7b21fe48818f] MedicationRequest | prescribed 2018-11-11 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[Encounter/7280f7f8-315d-7c6a-ddbc-56619e72a429] Encounter | 2026-04-26 | Encounter for check up (procedure) | class AMB | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-e49f-7858d34e1916] Encounter | 2026-04-13 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-79c7-b2135168eae6] Encounter | 2026-04-12 | General examination of patient (procedure) | class AMB | at HOLY FAMILY MEDICAL SPECIALTY PRACTICE PLLC
[Immunization/7280f7f8-315d-7c6a-89f5-f28321d6dbe8] Immunization | 2026-04-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/7280f7f8-315d-7c6a-f1f5-c7da1cd21d22] Observation (laboratory) | 2025-04-06 | Hemoglobin A1c/Hemoglobin.total in Blood = 5.82 % | status final | LOINC 4548-4
[Observation/7280f7f8-315d-7c6a-23fb-add1bb094bf9] Observation (laboratory) | 2026-04-12 | Hemoglobin A1c/Hemoglobin.total in Blood = 5.88 % | status final | LOINC 4548-4
[Observation/7280f7f8-315d-7c6a-e7ed-08eb1135a541] Observation (laboratory) | 2024-11-24 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.22 % | status final | LOINC 4548-4
[Observation/7280f7f8-315d-7c6a-a415-14f2ba5d6dae] Observation (laboratory) | 2024-03-31 | Hemoglobin [Mass/volume] in Blood = 12.868 g/dL | status final | LOINC 718-7
[Observation/7280f7f8-315d-7c6a-bdb8-eee59dd4a75a] Observation (laboratory) | 2019-03-03 | Hemoglobin [Mass/volume] in Blood = 12.413 g/dL | status final | LOINC 718-7
[Observation/7280f7f8-315d-7c6a-6b21-ad7aa08dc589] Observation (laboratory) | 2020-03-11 | Glucose [Mass/volume] in Blood = 85.01 mg/dL | status final | LOINC 2339-0
[Observation/7280f7f8-315d-7c6a-8deb-4c4a6e0a3d05] Observation (laboratory) | 2026-04-13 | Glucose [Mass/volume] in Blood = 81.87 mg/dL | status final | LOINC 2339-0
[Observation/7280f7f8-315d-7c6a-ee99-17540b9dbdd8] Observation (laboratory) | 2026-04-12 | Glucose [Mass/volume] in Blood = 74.48 mg/dL | status final | LOINC 2339-0
[Observation/7280f7f8-315d-7c6a-9dce-58edd2b920ac] Observation (laboratory) | 2025-04-13 | Glucose [Mass/volume] in Blood = 68.57 mg/dL | status final | LOINC 2339-0
[Observation/7280f7f8-315d-7c6a-3d0f-07cee8a51ec0] Observation (laboratory) | 2018-05-03 | Hemoglobin [Presence] in Urine by Test strip = Urine blood test = + (finding) | status final | LOINC 5794-3
```

</details>

label: s
note: Cited cards show A1c 5.82 % on 2025-04-06 and 6.22 % on 2024-11-24; with the 2026-04-12 value these are the only three A1c cards.

## 35. `prescribed-for-diabetes-mellitus-type-2:0eeb6aa3#0#2`

Question: Which medications have been prescribed for the patient's diabetes mellitus type 2?

Answer: The only medication prescribed for diabetes mellitus type 2 is 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet, with an active prescription dated 2026-08-09. Earlier prescriptions of the same metformin on 2025-07-20 and 2025-12-14 are marked completed. **Metformin has been prescribed since 2021-11-21, when diabetes mellitus type 2 was diagnosed, and it appears again in later notes.**

Cards this sentence cites:

- `[DocumentReference/cea2caa6-1529-04d3-0c59-bc60063d9a30#2]` Clinical note | 2021-11-21 | part 2 of 2 | # Assessment and Plan Patient is presenting with essential hypertension (disorder), diabetes mellitus type 2 (disorder), victim of intimate partner abuse (finding), gingivitis (disorder). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - screening for domestic abuse (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - assessment using alcohol use disorders identification test - consumption (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - generalized anxiety disorder 7 item (gad-7) - humiliation, afraid, rape, and kick questionnaire [hark] - patient health questionnaire 2 item (phq-2) [reported] - alcohol use disorder identification test - consumption [audit-c] The patient was prescribed the following medications: - amlodipine 2.5 mg oral tablet - amlodipine 2.5 mg oral tablet - 24 hr metformin hydrochloride 500 mg extended release oral tablet The patient was placed on a careplan: - lifestyle education regarding hypertension (procedure)
- `[DocumentReference/01bffb32-7596-19d2-971c-38e967500ae6#2]` Clinical note | 2022-11-27 | part 2 of 2 | # Assessment and Plan Patient is presenting with hyperglycemia (disorder), hypertriglyceridemia (disorder), metabolic syndrome x (disorder), limited social contact (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - depression screening (procedure) - depression screening (procedure) The following lab reports were completed: - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - generalized anxiety disorder 7 item (gad-7) - patient health questionnaire 2 item (phq-2) [reported] The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - 24 hr metformin hydrochloride 500 mg extended release oral tablet - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet
- `[DocumentReference/bb53c693-35fa-1396-96c2-e2324743695a#2]` Clinical note | 2024-08-25 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - medication reconciliation (procedure) The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - 24 hr metformin hydrochloride 500 mg extended release oral tablet - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet
- `[DocumentReference/defee664-4d19-01ca-bbf7-70aefb37dd43#2]` Clinical note | 2025-07-13 | part 2 of 2 | # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - 24 hr metformin hydrochloride 500 mg extended release oral tablet - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet

<details><summary>Everything the model saw (36 cards)</summary>

```text
[Condition/0eeb6aa3-c249-0e46-6f19-eb10a1f328db] Condition | onset 2026-07-29 | Primary fibromyalgia syndrome (disorder) | clinical status active | SNOMED 95417003
[Condition/0eeb6aa3-c249-0e46-44b4-3580330e81b7] Condition | onset 2025-12-14 | Misuses drugs (finding) | clinical status active | SNOMED 361055000
[Condition/0eeb6aa3-c249-0e46-2c95-28a9408c6896] Condition | onset 2025-12-14 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/0eeb6aa3-c249-0e46-b1be-047f25b1022e] Condition | onset 2022-11-27 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/0eeb6aa3-c249-0e46-6def-33ad344a7a9b] Condition | onset 2022-11-27 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/0eeb6aa3-c249-0e46-06a5-9d3ec2ee65d0] Condition | onset 2022-11-27 | Hyperglycemia (disorder) | clinical status active | SNOMED 80394007
[Condition/0eeb6aa3-c249-0e46-d84e-f3245ad02f8e] Condition | onset 2021-11-21 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/0eeb6aa3-c249-0e46-ce58-8dd4753fcdb4] Condition | onset 2021-11-21 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/0eeb6aa3-c249-0e46-8d5d-18bd4ff7c429] Condition | onset 2021-11-21 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/0eeb6aa3-c249-0e46-0e2a-b4435a3e06d7] Condition | onset 2021-04-07 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
[Condition/0eeb6aa3-c249-0e46-c1e0-a1835f8dfe99] Condition | onset 2013-11-03 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/0eeb6aa3-c249-0e46-7e82-50da4e26d936] Condition | onset 2009-08-25 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/0eeb6aa3-c249-0e46-05b2-ee89706489e7] Condition | onset 2008-01-13 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/0eeb6aa3-c249-0e46-1bf9-48c5ad5ed3c4] Condition | onset 1991-12-22 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/0eeb6aa3-c249-0e46-7231-74f682325091] Condition | onset 1988-12-04 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/0eeb6aa3-c249-0e46-d035-2af008a23544] MedicationRequest | prescribed 2026-08-09 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/0eeb6aa3-c249-0e46-9e8f-3bc3a049dcd6] MedicationRequest | prescribed 2026-08-09 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/0eeb6aa3-c249-0e46-9979-087d4ecb9395] MedicationRequest | prescribed 2026-08-09 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/0eeb6aa3-c249-0e46-8801-c4efefa8fdf6] MedicationRequest | prescribed 2026-08-09 | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 860975
[MedicationRequest/0eeb6aa3-c249-0e46-48fb-484102ab7f68] MedicationRequest | prescribed 2026-07-29 | Naproxen 500 MG Oral Tablet | status active | reason: Primary fibromyalgia syndrome (disorder) | RxNorm 198014
[MedicationRequest/0eeb6aa3-c249-0e46-7cb4-1e0c24948d9a] MedicationRequest | prescribed 2021-04-07 | Naproxen sodium 220 MG Oral Tablet | status active | reason: Osteoarthritis of knee (disorder) | RxNorm 849574
[MedicationRequest/0eeb6aa3-c249-0e46-6749-08c77e3ff56d] MedicationRequest | prescribed 1993-03-28 | ferrous sulfate 325 MG Oral Tablet | status active | RxNorm 310325
[Encounter/0eeb6aa3-c249-0e46-4c0e-5bc7f2736fbd] Encounter | 2026-08-09 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/0eeb6aa3-c249-0e46-43a1-ecea1c0a2a61] Encounter | 2026-07-29 | Encounter for problem (procedure) | class AMB | reason: Primary fibromyalgia syndrome (disorder) | at HOLY FAMILY HOSPITAL
[Encounter/0eeb6aa3-c249-0e46-d415-7e8395059f69] Encounter | 2026-01-04 | Encounter for check up (procedure) | class AMB | reason: Patient referral for dental care (procedure) | at HOLY FAMILY HOSPITAL
[Immunization/0eeb6aa3-c249-0e46-99a3-4dae451772fe] Immunization | 2026-08-09 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/0eeb6aa3-c249-0e46-5e6e-8a2b01a90bd9] MedicationRequest | prescribed 2025-07-20 | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet | status completed | reason: Diabetes mellitus type 2 (disorder) | RxNorm 860975
[MedicationRequest/0eeb6aa3-c249-0e46-4a92-8623147ce9b5] MedicationRequest | prescribed 2025-12-14 | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet | status completed | reason: Diabetes mellitus type 2 (disorder) | RxNorm 860975
[Procedure/0eeb6aa3-c249-0e46-7fba-df171b06549c] Procedure | 2021-12-12 | History taking (procedure) | status completed | reason: Diabetes mellitus type 2 (disorder) | SNOMED 84100007
[DocumentReference/defee664-4d19-01ca-bbf7-70aefb37dd43#2] Clinical note | 2025-07-13 | part 2 of 2 | # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - 24 hr metformin hydrochloride 500 mg extended release oral tablet - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet
[DocumentReference/bb53c693-35fa-1396-96c2-e2324743695a#2] Clinical note | 2024-08-25 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - medication reconciliation (procedure) The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - 24 hr metformin hydrochloride 500 mg extended release oral tablet - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet
[DocumentReference/01bffb32-7596-19d2-971c-38e967500ae6#2] Clinical note | 2022-11-27 | part 2 of 2 | # Assessment and Plan Patient is presenting with hyperglycemia (disorder), hypertriglyceridemia (disorder), metabolic syndrome x (disorder), limited social contact (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - depression screening (procedure) - depression screening (procedure) The following lab reports were completed: - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - generalized anxiety disorder 7 item (gad-7) - patient health questionnaire 2 item (phq-2) [reported] The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - 24 hr metformin hydrochloride 500 mg extended release oral tablet - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet
[DocumentReference/cea2caa6-1529-04d3-0c59-bc60063d9a30#2] Clinical note | 2021-11-21 | part 2 of 2 | # Assessment and Plan Patient is presenting with essential hypertension (disorder), diabetes mellitus type 2 (disorder), victim of intimate partner abuse (finding), gingivitis (disorder). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - screening for domestic abuse (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - assessment using alcohol use disorders identification test - consumption (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - generalized anxiety disorder 7 item (gad-7) - humiliation, afraid, rape, and kick questionnaire [hark] - patient health questionnaire 2 item (phq-2) [reported] - alcohol use disorder identification test - consumption [audit-c] The patient was prescribed the following medications: - amlodipine 2.5 mg oral tablet - amlodipine 2.5 mg oral tablet - 24 hr metformin hydrochloride 500 mg extended release oral tablet The patient was placed on a careplan: - lifestyle education regarding hypertension (procedure)
[Procedure/0eeb6aa3-c249-0e46-47ce-4e46a9c37d33] Procedure | 2024-12-15 | Diabetic retinal eye exam (procedure) | status completed | reason: Diabetes mellitus type 2 (disorder) | SNOMED 722161008
[Procedure/0eeb6aa3-c249-0e46-05b2-e212902bd217] Procedure | 2025-12-21 | Diabetic retinal eye exam (procedure) | status completed | reason: Diabetes mellitus type 2 (disorder) | SNOMED 722161008
[Procedure/0eeb6aa3-c249-0e46-1dec-bc369c4def90] Procedure | 2023-12-10 | Diabetic retinal eye exam (procedure) | status completed | reason: Diabetes mellitus type 2 (disorder) | SNOMED 722161008
```

</details>

label: s
note: Cited 2021-11-21 note lists DM2 among presenting problems and 24 hr metformin 500 mg as prescribed, matching the DM2 onset date; no earlier metformin entry exists, and the cited 2022-11-27, 2024-08-25 and 2025-07-13 notes list metformin again.

## 36. `vaccines-last-year:7280f7f8#0#1`

Question: Which vaccines did the patient receive in the last year?

Answer: In the year before the record's as-of date of 2026-10-01, the patient received one vaccine: Influenza, split virus, trivalent, PF (CVX 140) on 2026-04-12. **The previous recorded vaccine was an influenza dose on 2024-11-24, which falls outside that window.**

Cards this sentence cites:

- `[Immunization/7280f7f8-315d-7c6a-a994-7340336c5a95]` Immunization | 2024-11-24 | Influenza, split virus, trivalent, PF | status completed | CVX 140

<details><summary>Everything the model saw (43 cards)</summary>

```text
[Condition/7280f7f8-315d-7c6a-5183-1fc53612d856] Condition | onset 2026-04-12 | Alzheimer's disease (disorder) | clinical status active | SNOMED 26929004
[Condition/7280f7f8-315d-7c6a-069f-25fdb34e3e53] Condition | onset 2025-04-06 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/7280f7f8-315d-7c6a-06ae-a26712c6cfb7] Condition | onset 2024-03-31 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/7280f7f8-315d-7c6a-84b2-d6045a9b8deb] Condition | onset 2018-11-12 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/7280f7f8-315d-7c6a-60b8-1b2b3b190d66] Condition | onset 2018-11-04 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/7280f7f8-315d-7c6a-eee1-33d3eda16b26] Condition | onset 2014-02-16 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/7280f7f8-315d-7c6a-23b9-2a24d0c43093] Condition | onset 2014-02-16 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/7280f7f8-315d-7c6a-f371-666500850eb4] Condition | onset 2014-02-02 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/7280f7f8-315d-7c6a-b5ea-aa0955ebc2c7] Condition | onset 2010-01-10 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/7280f7f8-315d-7c6a-929f-e845c91bba18] Condition | onset 1993-02-06 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/7280f7f8-315d-7c6a-6159-244929402415] Condition | onset 1991-07-09 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/7280f7f8-315d-7c6a-7561-551dd4fb980c] Condition | onset 1990-11-11 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/7280f7f8-315d-7c6a-69cb-9f6bde195716] Condition | onset 1990-10-25 | Impacted molars (disorder) | clinical status active | SNOMED 196416002
[Condition/7280f7f8-315d-7c6a-e183-7fc41f06abde] Condition | onset 1990-02-06 | Chronic intractable migraine without aura (disorder) | clinical status active | SNOMED 124171000119105
[Condition/7280f7f8-315d-7c6a-57cd-16215a141add] Condition | onset 1988-11-06 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/7280f7f8-315d-7c6a-7c25-7a247f43e721] Condition | onset 1981-01-18 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/7280f7f8-315d-7c6a-50ac-70390520f5d8] Condition | onset 1981-01-18 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/7280f7f8-315d-7c6a-a35c-5f2c4404e1cd] Condition | onset 1971-02-18 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/7280f7f8-315d-7c6a-cf3c-1559c1e270a8] Condition | onset 1964-12-20 | Housing unsatisfactory (finding) | clinical status active | SNOMED 105531004
[Condition/7280f7f8-315d-7c6a-3735-89103641aea2] Condition | onset 1964-12-20 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/7280f7f8-315d-7c6a-d103-5f5cf25ace53] MedicationRequest | prescribed 2026-04-13 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/7280f7f8-315d-7c6a-dd3c-435b565b36d4] MedicationRequest | prescribed 2026-04-12 | Ibuprofen 400 MG Oral Tablet [Ibu] | status active | RxNorm 206905
[MedicationRequest/7280f7f8-315d-7c6a-698d-8c3f4a330263] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG / Oxycodone Hydrochloride 10 MG Oral Tablet [Percocet] | status active | RxNorm 1049625
[MedicationRequest/7280f7f8-315d-7c6a-53dc-677516ba315e] MedicationRequest | prescribed 2026-04-12 | Galantamine 4 MG Oral Tablet | status active | reason: Alzheimer's disease (disorder) | RxNorm 310436
[MedicationRequest/7280f7f8-315d-7c6a-21fd-127361ce4eae] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-e1ca-6672a64e96d6] MedicationRequest | prescribed 2018-11-11 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/7280f7f8-315d-7c6a-d3dc-bf227b26b9de] MedicationRequest | prescribed 2018-11-11 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/7280f7f8-315d-7c6a-40f0-094ac0d35606] MedicationRequest | prescribed 2018-11-11 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/7280f7f8-315d-7c6a-344e-7b21fe48818f] MedicationRequest | prescribed 2018-11-11 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[Encounter/7280f7f8-315d-7c6a-ddbc-56619e72a429] Encounter | 2026-04-26 | Encounter for check up (procedure) | class AMB | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-e49f-7858d34e1916] Encounter | 2026-04-13 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-79c7-b2135168eae6] Encounter | 2026-04-12 | General examination of patient (procedure) | class AMB | at HOLY FAMILY MEDICAL SPECIALTY PRACTICE PLLC
[Immunization/7280f7f8-315d-7c6a-89f5-f28321d6dbe8] Immunization | 2026-04-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/7280f7f8-315d-7c6a-2c12-076f4ebe4a00] Immunization | 2021-04-11 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/7280f7f8-315d-7c6a-03fb-59ac9d44c133] Immunization | 2021-03-21 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Observation/7280f7f8-315d-7c6a-3bcf-660371c4df20] Observation (survey) | 2024-03-31 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Somewhat; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Food; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/7280f7f8-315d-7c6a-17d4-3bde7faffa5a] Observation (survey) | 2026-04-12 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level A little bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/7280f7f8-315d-7c6a-073a-b5db76259ffb] Observation (survey) | 2025-04-06 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Quite a bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Medicine or Any Health Care (Medical, Dental, Mental Health, Vision); What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/7280f7f8-315d-7c6a-f0b4-d6fc3b03db28] Observation (survey) | 2024-11-24 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Not at all; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Utilities; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Immunization/7280f7f8-315d-7c6a-4150-9fa667bfd111] Immunization | 2021-03-14 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/7280f7f8-315d-7c6a-a994-7340336c5a95] Immunization | 2024-11-24 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/7280f7f8-315d-7c6a-5206-3912d1550e2d] Immunization | 2024-03-31 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/37069e82-27e3-b54c-3800-72d29ab5652d#1] Clinical note | 1991-07-09 | part 1 of 1 | 1991-07-09 # Chief Complaint - Memory Loss - Decreased in Judgement # History of Present Illness Neil122 is a 44 year-old nonhispanic white male. # Social History Patient is married. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a low socioeconomic background. Patient did not finish high school. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with chronic pain (finding). ## Plan
```

</details>

label: s
note: Cited card is an influenza CVX 140 dose on 2024-11-24; among all immunization cards it is the latest before 2026-04-12 and falls before the 2025-10-01 window start.

## 37. `lay-obesity:530b9289#0#0`

Question: Has the patient ever been diagnosed with obesity? If so, when?

Answer: **Yes, the patient has an active condition of Body mass index 30+ - obesity (finding) with onset 2017-05-03.** The clinical note from 2017-05-03 also lists body mass index 30+ - obesity (finding) among the presenting problems. Subsequent BMI measurements were 30.07 kg/m2 on 2020-05-06, 2023-02-22, and 2025-02-26.

Cards this sentence cites:

- `[Condition/530b9289-dc96-576f-8734-8c3a0a9992bf]` Condition | onset 2017-05-03 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005

<details><summary>Everything the model saw (22 cards)</summary>

```text
[Condition/530b9289-dc96-576f-f6fc-11015cce065e] Condition | onset 2025-02-26 | Part-time employment (finding) | clinical status active | SNOMED 160904001
[Condition/530b9289-dc96-576f-888a-14c459fcf894] Condition | onset 2020-05-06 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/530b9289-dc96-576f-1809-1246e2ec41d9] Condition | onset 2018-10-06 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/530b9289-dc96-576f-8734-8c3a0a9992bf] Condition | onset 2017-05-03 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/530b9289-dc96-576f-bdaf-615dd0bc7cf7] Condition | onset 2005-04-20 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/530b9289-dc96-576f-d54d-1d2b15a86dde] Condition | onset 2001-04-11 | Housing unsatisfactory (finding) | clinical status active | SNOMED 105531004
[Condition/530b9289-dc96-576f-6f01-b29a29894132] Condition | onset 2001-04-11 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
[Condition/530b9289-dc96-576f-8fa7-f82a4cf5d127] Condition | onset 1996-04-03 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/530b9289-dc96-576f-f948-ba67b946cdb9] MedicationRequest | prescribed 2003-11-14 | ferrous sulfate 325 MG Oral Tablet | status active | RxNorm 310325
[Encounter/530b9289-dc96-576f-fa45-0629d4ad3b09] Encounter | 2025-03-12 | Encounter for check up (procedure) | class AMB | reason: Gingivitis (disorder) | at NORTH SHORE MEDICAL CENTER INC
[Encounter/530b9289-dc96-576f-4652-29db662eb77f] Encounter | 2025-02-26 | General examination of patient (procedure) | class AMB | at SALEM FAMILY HEALTH CENTER
[Encounter/530b9289-dc96-576f-3573-1253261abd75] Encounter | 2024-01-10 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at NORTH SHORE MEDICAL CENTER INC
[DocumentReference/8508df42-83be-a18c-bbc3-f0f758077806#2] Clinical note | 2017-05-03 | part 2 of 2 | # Assessment and Plan Patient is presenting with medication review due (situation), body mass index 30+ - obesity (finding), not in labor force (finding), stress (finding), reports of violence in the environment (finding), gingivitis (disorder). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - screening for domestic abuse (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - assessment using alcohol use disorders identification test - consumption (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - cbc panel - blood by automated count - generalized anxiety disorder 7 item (gad-7) - humiliation, afraid, rape, and kick questionnaire [hark] - patient health questionnaire 2 item (phq-2) [reported] - alcohol use disorder identification test - consumption [audit-c]
[DocumentReference/3b353527-aeac-b6b6-71cf-be327df38e18#1] Clinical note | 2005-04-20 | part 1 of 1 | 2005-04-20 # Chief Complaint No complaints. # History of Present Illness Carlee848 Anastasia959 is a 22 year-old nonhispanic white female. Patient has a history of dental caries, cracked tooth. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with prediabetes (finding). ## Plan The patient was placed on a careplan: - diabetes self management plan (record artifact)
[Condition/530b9289-dc96-576f-df8c-18c0cbeeae19] Condition | onset 2017-05-04 | Not in labor force (finding) | clinical status resolved | resolved 2020-05-06 | SNOMED 741062008
[DocumentReference/96282976-74b5-fc22-1f32-f8bd4c1832bd#1] Clinical note | 2016-09-25 | part 1 of 1 | 2016-09-25 # Chief Complaint No complaints. # History of Present Illness Carlee848 Anastasia959 is a 33 year-old nonhispanic white female. Patient has a history of dental caries, cracked tooth, full-time employment (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has UnitedHealthcare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The patient was prescribed the following medications: - levonorgestrel 0.000813 mg/hr intrauterine system [liletta]
[DocumentReference/4bea629f-433e-ad85-f28c-a55314f48612#1] Clinical note | 2001-04-11 | part 1 of 1 | 2001-04-11 # Chief Complaint No complaints. # History of Present Illness Carlee848 Anastasia959 is a 18 year-old nonhispanic white female. Patient has a history of dental caries. # Social History Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with housing unsatisfactory (finding), educated to high school level (finding). ## Plan
[DocumentReference/ddbde56d-c426-7811-b828-09990141d59a#1] Clinical note | 2014-04-30 | part 1 of 1 | 2014-04-30 # Chief Complaint No complaints. # History of Present Illness Carlee848 Anastasia959 is a 31 year-old nonhispanic white female. Patient has a history of dental caries, cracked tooth. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has UnitedHealthcare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with full-time employment (finding). ## Plan
[DocumentReference/8508df42-83be-a18c-bbc3-f0f758077806#1] Clinical note | 2017-05-03 | part 1 of 2 | 2017-05-03 # Chief Complaint No complaints. # History of Present Illness Carlee848 Anastasia959 is a 34 year-old nonhispanic white female. Patient has a history of dental caries, cracked tooth, full-time employment (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has UnitedHealthcare. # Allergies No Known Allergies. # Medications levonorgestrel 0.000813 mg/hr intrauterine system [liletta]
[Observation/530b9289-dc96-576f-38e5-7f625562b9b4] Observation (vital-signs) | 2020-05-06 | Body mass index (BMI) [Ratio] = 30.07 kg/m2 | status final | LOINC 39156-5
[Observation/530b9289-dc96-576f-f536-ffdaf31bf755] Observation (vital-signs) | 2025-02-26 | Body mass index (BMI) [Ratio] = 30.07 kg/m2 | status final | LOINC 39156-5
[Observation/530b9289-dc96-576f-ad27-f4cf27a6a437] Observation (vital-signs) | 2023-02-22 | Body mass index (BMI) [Ratio] = 30.07 kg/m2 | status final | LOINC 39156-5
```

</details>

label: s
note: Cited Condition card: Body mass index 30+ - obesity (finding), onset 2017-05-03, clinical status active.

## 38. `lay-high-blood-pressure:ef5e136c#0#1`

Question: Has the patient ever been diagnosed with high blood pressure? If so, when?

Answer: Yes, the patient has an active diagnosis of essential hypertension with onset 2011-07-27. **It is being treated with hydrochlorothiazide 25 MG, lisinopril 10 MG, and amlodipine 2.5 MG, all prescribed 2026-09-30 with essential hypertension as the reason.** The most recent recorded blood pressure was 115/60 mm[Hg] on 2026-09-23.

Cards this sentence cites:

- `[MedicationRequest/ef5e136c-ff1e-0695-ffec-2ea7ac772a27]` MedicationRequest | prescribed 2026-09-30 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
- `[MedicationRequest/ef5e136c-ff1e-0695-901e-2e1f9afb0cca]` MedicationRequest | prescribed 2026-09-30 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
- `[MedicationRequest/ef5e136c-ff1e-0695-6c6d-182c3b9c47c1]` MedicationRequest | prescribed 2026-09-30 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136

<details><summary>Everything the model saw (47 cards)</summary>

```text
[Condition/ef5e136c-ff1e-0695-1f8c-935a12106cac] Condition | onset 2026-09-30 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/ef5e136c-ff1e-0695-7e5d-470b95f60db2] Condition | onset 2026-09-23 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/ef5e136c-ff1e-0695-9d2d-c4be459bc9f4] Condition | onset 2026-09-09 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/ef5e136c-ff1e-0695-7b9c-f43e5ca3f6c6] Condition | onset 2026-08-12 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-aa04-94486c99258f] Condition | onset 2025-08-27 | End-stage renal disease (disorder) | clinical status active | SNOMED 46177005
[Condition/ef5e136c-ff1e-0695-423f-ed71d76e81e3] Condition | onset 2025-03-30 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/ef5e136c-ff1e-0695-71df-3a96389b0a39] Condition | onset 2025-02-05 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/ef5e136c-ff1e-0695-5331-2d63eb213c34] Condition | onset 2024-05-15 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/ef5e136c-ff1e-0695-3834-fa6cb282a475] Condition | onset 2024-05-15 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/ef5e136c-ff1e-0695-68fe-9e2010333061] Condition | onset 2023-08-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/ef5e136c-ff1e-0695-65f5-8d04f278a661] Condition | onset 2023-08-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/ef5e136c-ff1e-0695-aac2-46a0ff462178] Condition | onset 2023-04-19 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/ef5e136c-ff1e-0695-fda2-40e12f6b17a7] Condition | onset 2017-11-15 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/ef5e136c-ff1e-0695-bf3f-30946ad3f8b4] Condition | onset 2017-11-15 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/ef5e136c-ff1e-0695-eac4-d545a0296998] Condition | onset 2011-07-27 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/ef5e136c-ff1e-0695-b228-2f5ff5bb47cb] Condition | onset 2010-05-19 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/ef5e136c-ff1e-0695-af16-82f03f777ba8] Condition | onset 2010-05-19 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/ef5e136c-ff1e-0695-5ca5-51bfdc51320e] Condition | onset 2010-05-12 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/ef5e136c-ff1e-0695-f7ec-ceae0c2566bc] Condition | onset 2004-06-16 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/ef5e136c-ff1e-0695-c94a-5d81ddd88117] Condition | onset 1997-05-07 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/ef5e136c-ff1e-0695-6efc-9f7d5e6b04ef] Condition | onset 1993-09-01 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/ef5e136c-ff1e-0695-1f68-dac24351dbaa] Condition | onset 1993-04-14 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/ef5e136c-ff1e-0695-2d8d-328849698529] Condition | onset 1993-01-22 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/ef5e136c-ff1e-0695-0825-c31e8b252683] Condition | onset 1983-11-14 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/ef5e136c-ff1e-0695-cb16-3a98eeb2de7a] Condition | onset 1976-01-07 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/ef5e136c-ff1e-0695-3278-6a86eaf1fb5d] Condition | onset 1975-06-27 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/ef5e136c-ff1e-0695-337f-d12087c8dbb5] Condition | onset 1975-01-01 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/ef5e136c-ff1e-0695-ffec-2ea7ac772a27] MedicationRequest | prescribed 2026-09-30 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/ef5e136c-ff1e-0695-b3ba-a1ec7bcfb9f4] MedicationRequest | prescribed 2026-09-30 | albuterol 0.83 MG/ML Inhalation Solution | status active | RxNorm 630208
[MedicationRequest/ef5e136c-ff1e-0695-901e-2e1f9afb0cca] MedicationRequest | prescribed 2026-09-30 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/ef5e136c-ff1e-0695-76a6-8eeb54f8a75e] MedicationRequest | prescribed 2026-09-30 | 120 ACTUAT fluticasone propionate 0.044 MG/ACTUAT Metered Dose Inhaler [Flovent] | status active | RxNorm 895996
[MedicationRequest/ef5e136c-ff1e-0695-6c6d-182c3b9c47c1] MedicationRequest | prescribed 2026-09-30 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/ef5e136c-ff1e-0695-6804-cf31640a9491] MedicationRequest | prescribed 2026-09-30 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[Encounter/ef5e136c-ff1e-0695-08ba-2471a16a6570] Encounter | 2026-09-30 | Emergency room admission (procedure) | class EMER | at APPLE VALLEY CENTER
[Encounter/ef5e136c-ff1e-0695-aea4-11055569fd51] Encounter | 2026-09-23 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/ef5e136c-ff1e-0695-4a41-6fca58c80cb7] Encounter | 2026-09-16 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Immunization/ef5e136c-ff1e-0695-6beb-93901776b619] Immunization | 2026-05-13 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/ef5e136c-ff1e-0695-053e-35888232a105] Observation (vital-signs) | 2024-08-14 | Blood pressure panel with all children optional = Diastolic Blood Pressure 63 mm[Hg]; Systolic Blood Pressure 116 mm[Hg] | status final | LOINC 85354-9
[Observation/ef5e136c-ff1e-0695-8150-2ef2105a3233] Observation (vital-signs) | 2026-09-23 | Blood pressure panel with all children optional = Diastolic Blood Pressure 60 mm[Hg]; Systolic Blood Pressure 115 mm[Hg] | status final | LOINC 85354-9
[Observation/ef5e136c-ff1e-0695-e1dc-2e5f1dd38840] Observation (vital-signs) | 2026-09-09 | Blood pressure panel with all children optional = Diastolic Blood Pressure 60 mm[Hg]; Systolic Blood Pressure 114 mm[Hg] | status final | LOINC 85354-9
[Observation/ef5e136c-ff1e-0695-eceb-e6bdd735d27d] Observation (vital-signs) | 2026-08-26 | Blood pressure panel with all children optional = Diastolic Blood Pressure 67 mm[Hg]; Systolic Blood Pressure 111 mm[Hg] | status final | LOINC 85354-9
[Condition/ef5e136c-ff1e-0695-2400-b6bd7b148736] Condition | onset 2021-11-24 | Stress (finding) | clinical status resolved | resolved 2022-02-23 | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-0659-7182eb1d6004] Condition | onset 2026-07-15 | Stress (finding) | clinical status resolved | resolved 2026-07-29 | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-e041-99b1020df098] Condition | onset 2026-06-03 | Stress (finding) | clinical status resolved | resolved 2026-07-01 | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-3999-683e8e8b2ed4] Condition | onset 2021-03-03 | Full-time employment (finding) | clinical status resolved | resolved 2021-04-28 | SNOMED 160903007
[Condition/ef5e136c-ff1e-0695-e7b3-c8cd08a825eb] Condition | onset 2026-07-15 | Full-time employment (finding) | clinical status resolved | resolved 2026-09-09 | SNOMED 160903007
[Condition/ef5e136c-ff1e-0695-783a-b752897e96ab] Condition | onset 2026-06-17 | Full-time employment (finding) | clinical status resolved | resolved 2026-07-01 | SNOMED 160903007
```

</details>

label: s
note: The three cited MedicationRequest cards (hydrochlorothiazide 25 MG, lisinopril 10 MG, amlodipine 2.5 MG) are all prescribed 2026-09-30, active, with reason Essential hypertension.

## 39. `current-meds:8d945e28#0#1`

Question: What medications is the patient currently prescribed?

Answer: The patient's active prescriptions are Humulin (insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension), prescribed 2026-09-07 for prediabetes, and Hydrochlorothiazide 25 MG Oral Tablet, prescribed 2026-09-07 for essential hypertension. **Vitamin B12 5 MG/ML Injectable Solution, prescribed 1981-07-27, is also active.** Clinical notes through 2026-01-19 also list epoetin alfa 4000 unt/ml injection [epogen], acetaminophen, acetaminophen/oxycodone, ibuprofen and naproxen sodium among the medications, but these notes do not state an active status.

Cards this sentence cites:

- `[MedicationRequest/8d945e28-1d8a-bd72-bcd6-3304c42dca58]` MedicationRequest | prescribed 1981-07-27 | Vitamin B12 5 MG/ML Injectable Solution | status active | RxNorm 2001499

<details><summary>Everything the model saw (39 cards)</summary>

```text
[Condition/8d945e28-1d8a-bd72-9d6c-259e17157c55] Condition | onset 2026-09-07 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8d945e28-1d8a-bd72-3102-64b703ba601c] Condition | onset 2026-07-13 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8d945e28-1d8a-bd72-6b51-0718e8cd7a5e] Condition | onset 2021-01-01 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/8d945e28-1d8a-bd72-db4c-2552d073039a] Condition | onset 2020-11-09 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/8d945e28-1d8a-bd72-ed26-25aa62be033c] Condition | onset 2020-08-18 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/8d945e28-1d8a-bd72-05bf-4b4b02b03fe9] Condition | onset 2018-01-22 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/8d945e28-1d8a-bd72-38fb-c4bf927332c6] Condition | onset 2013-09-16 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/8d945e28-1d8a-bd72-1379-82140e2d1648] Condition | onset 2013-09-16 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/8d945e28-1d8a-bd72-cd47-b95fb1e4464b] Condition | onset 2009-07-06 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/8d945e28-1d8a-bd72-be1a-fb710d842e34] Condition | onset 2009-07-06 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/8d945e28-1d8a-bd72-2a55-0f3c986db8dd] Condition | onset 2009-07-06 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8d945e28-1d8a-bd72-4277-241d976b7354] Condition | onset 2007-06-25 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8d945e28-1d8a-bd72-e0ac-a99a0168ad8a] Condition | onset 2004-06-07 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/8d945e28-1d8a-bd72-a508-e7d1553f7f62] Condition | onset 2004-06-07 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/8d945e28-1d8a-bd72-2622-8fe0a1a30909] Condition | onset 2003-06-02 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8d945e28-1d8a-bd72-12e3-17db162c8f0b] Condition | onset 2001-06-04 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/8d945e28-1d8a-bd72-d01e-086bb9d1d22f] Condition | onset 2001-05-07 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/8d945e28-1d8a-bd72-f5fa-42692b5be159] Condition | onset 1996-08-05 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8d945e28-1d8a-bd72-e601-8e5493910aec] Condition | onset 1981-07-20 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8d945e28-1d8a-bd72-52ca-256d6584412c] Condition | onset 1981-07-20 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8d945e28-1d8a-bd72-d644-66738e889d91] Condition | onset 1977-07-11 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/8d945e28-1d8a-bd72-fbf9-3e6f6bd97f57] Condition | onset 1977-03-07 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/8d945e28-1d8a-bd72-ff5c-41daf21d65a9] MedicationRequest | prescribed 2026-09-07 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/8d945e28-1d8a-bd72-d409-38c0124f2c47] MedicationRequest | prescribed 2026-09-07 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/8d945e28-1d8a-bd72-bcd6-3304c42dca58] MedicationRequest | prescribed 1981-07-27 | Vitamin B12 5 MG/ML Injectable Solution | status active | RxNorm 2001499
[Encounter/8d945e28-1d8a-bd72-016c-9af67d7199fd] Encounter | 2026-09-27 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-3f01-7946bd8f2be1] Encounter | 2026-09-26 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-9dbd-785d1f0e4915] Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Immunization/8d945e28-1d8a-bd72-6a94-32775be2d4e6] Immunization | 2026-01-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/198dc0c0-ac2a-f381-c815-204a8135294a#2] Clinical note | 2025-12-19 | part 2 of 2 | # Medications 1 ml epoetin alfa 4000 unt/ml injection [epogen]; acetaminophen 325 mg oral tablet; hydrochlorothiazide 25 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; ibuprofen 200 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/ed2accc3-f181-6c76-019e-602100408021#1] Clinical note | 1981-07-27 | part 1 of 1 | 1981-07-27 # Chief Complaint - Thirst - Fatigue - Hunger # History of Present Illness Tien590 Marcela739 is a 22 year-old nonhispanic white female. # Social History Patient is married. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Cigna Health. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The patient was prescribed the following medications: - vitamin b12 5 mg/ml injectable solution
[DocumentReference/46621701-ca2a-cb98-5521-2aabde9e5ef5#1] Clinical note | 2016-08-15 | part 1 of 1 | 2016-08-15 # Chief Complaint - Thirst - Fatigue - Hunger # History of Present Illness Tien590 Marcela739 is a 57 year-old nonhispanic white female. Patient has a history of acute apical periodontitis of pulpal origin, medication review due (situation), chronic periodontitis, generalized, full-time employment (finding), victim of intimate partner abuse (finding), stress (finding). # Social History Patient is married. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet
[DocumentReference/80a3c86e-df5b-b958-28f5-96bc5396b5a7#2] Clinical note | 2024-12-19 | part 2 of 2 | # Medications 1 ml epoetin alfa 4000 unt/ml injection [epogen]; acetaminophen 325 mg oral tablet; hydrochlorothiazide 25 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; ibuprofen 200 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/0404ad4f-552b-33c0-8dd9-b7851ed9bb1f#2] Clinical note | 2024-09-19 | part 2 of 2 | # Medications 1 ml epoetin alfa 4000 unt/ml injection [epogen]; acetaminophen 325 mg oral tablet; hydrochlorothiazide 25 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; ibuprofen 200 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/f4d1a4ab-164b-5c81-a496-8f30333033c5#2] Clinical note | 2021-05-16 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/722b463c-e306-97a2-0f7b-e9997def0d9b#2] Clinical note | 2026-01-19 | part 2 of 2 | # Medications 1 ml epoetin alfa 4000 unt/ml injection [epogen]; acetaminophen 325 mg oral tablet; hydrochlorothiazide 25 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; ibuprofen 200 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/90a6e575-11cc-9dfb-2b8f-5b6daf1d4158#2] Clinical note | 2021-05-13 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/9dcc0331-09a7-627c-75ae-78739719ce1e#2] Clinical note | 2025-12-16 | part 2 of 2 | # Medications 1 ml epoetin alfa 4000 unt/ml injection [epogen]; acetaminophen 325 mg oral tablet; hydrochlorothiazide 25 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; ibuprofen 200 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/af9a9175-6ec4-7dfb-4a83-076e0c152158#2] Clinical note | 2021-04-25 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
```

</details>

label: s
note: Cited card: Vitamin B12 5 MG/ML Injectable Solution, prescribed 1981-07-27, status active.

## 40. `active-problems:0e6e0d73#0#1`

Question: What active diagnoses does the patient have?

Answer: The patient's active clinical diagnoses are sepsis and septic shock (both onset 2017-09-23), unhealthy alcohol drinking behavior (onset 2021-08-16), and past pregnancy history of miscarriage (onset 2018-04-30). **Other active entries are medication review due (onset 2021-08-02), full-time employment (onset 2026-05-25), victim of intimate partner abuse (onset 2006-07-17), educated to high school level (onset 2002-07-08), and risk activity involvement (onset 2001-07-02).**

Cards this sentence cites:

- `[Condition/0e6e0d73-619d-15c3-a2af-2198a3d15909]` Condition | onset 2021-08-02 | Medication review due (situation) | clinical status active | SNOMED 314529007
- `[Condition/0e6e0d73-619d-15c3-1198-27a3f1e6671d]` Condition | onset 2026-05-25 | Full-time employment (finding) | clinical status active | SNOMED 160903007
- `[Condition/0e6e0d73-619d-15c3-252c-3ec5aec72d7f]` Condition | onset 2006-07-17 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
- `[Condition/0e6e0d73-619d-15c3-a3b6-7fc6f2b594a9]` Condition | onset 2002-07-08 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
- `[Condition/0e6e0d73-619d-15c3-a0ee-8e9994e38bf4]` Condition | onset 2001-07-02 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000

<details><summary>Everything the model saw (26 cards)</summary>

```text
[Condition/0e6e0d73-619d-15c3-1198-27a3f1e6671d] Condition | onset 2026-05-25 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/0e6e0d73-619d-15c3-73bb-c4435e198a52] Condition | onset 2021-08-16 | Unhealthy alcohol drinking behavior (finding) | clinical status active | SNOMED 10939881000119105
[Condition/0e6e0d73-619d-15c3-a2af-2198a3d15909] Condition | onset 2021-08-02 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/0e6e0d73-619d-15c3-7d75-d0dd94ac6175] Condition | onset 2018-04-30 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/0e6e0d73-619d-15c3-dabb-3f18b4ab6eed] Condition | onset 2017-09-23 | Sepsis (disorder) | clinical status active | SNOMED 91302008
[Condition/0e6e0d73-619d-15c3-279b-bad1f131dc84] Condition | onset 2017-09-23 | Septic shock (disorder) | clinical status active | SNOMED 76571007
[Condition/0e6e0d73-619d-15c3-252c-3ec5aec72d7f] Condition | onset 2006-07-17 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/0e6e0d73-619d-15c3-a3b6-7fc6f2b594a9] Condition | onset 2002-07-08 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
[Condition/0e6e0d73-619d-15c3-a0ee-8e9994e38bf4] Condition | onset 2001-07-02 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/0e6e0d73-619d-15c3-e363-3a1afa521a17] MedicationRequest | prescribed 2026-07-12 | {21 (ethinyl estradiol 0.03 MG / levonorgestrel 0.15 MG Oral Tablet) / 7 (inert ingredients 1 MG Oral Tablet) } Pack [Levora 0.15/30 28 Day] | status active | RxNorm 748879
[Encounter/0e6e0d73-619d-15c3-9366-052e1e643c56] Encounter | 2026-07-12 | Consultation for treatment (procedure) | class AMB | reason: Contraception care (regime/therapy) | at NEW ENGLAND SINAI HOSPITAL
[Encounter/0e6e0d73-619d-15c3-60c1-89e78f0afd63] Encounter | 2026-05-25 | General examination of patient (procedure) | class AMB | at ENRICH WELLNESS HEALTH CENTER LLC
[Encounter/0e6e0d73-619d-15c3-08dc-dd55aa3a67ea] Encounter | 2025-07-17 | Consultation for treatment (procedure) | class AMB | reason: Contraception care (regime/therapy) | at NEW ENGLAND SINAI HOSPITAL
[Immunization/0e6e0d73-619d-15c3-f93b-2cd3ab790ac4] Immunization | 2026-05-25 | Hep A, adult | status completed | CVX 52
[Immunization/0e6e0d73-619d-15c3-e4c7-db7a86392a05] Immunization | 2026-05-25 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/0e6e0d73-619d-15c3-8254-2b4f6f2ea96c] Immunization | 2026-05-25 | Td (adult), 5 Lf tetanus toxoid, preservative free, adsorbed | status completed | CVX 113
[Condition/0e6e0d73-619d-15c3-424b-37a41b7d3666] Condition | onset 2011-10-03 | Full-time employment (finding) | clinical status resolved | resolved 2021-08-02 | SNOMED 160903007
[Condition/0e6e0d73-619d-15c3-8b0b-a55ba7a2f637] Condition | onset 2018-07-30 | Medication review due (situation) | clinical status resolved | resolved 2018-07-30 | SNOMED 314529007
[DocumentReference/19c46736-9ae7-37ce-0cdb-b91e2776cc33#1] Clinical note | 2003-07-14 | part 1 of 1 | 2003-07-14 # Chief Complaint No complaints. # History of Present Illness Farah862 Beryl690 is a 19 year-old nonhispanic black female. # Social History Patient is married. Patient quit smoking at age 16. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with stress (finding). ## Plan
[DocumentReference/603ad948-9dad-5b7c-260f-532bc19274b9#1] Clinical note | 2011-10-03 | part 1 of 1 | 2011-10-03 # Chief Complaint No complaints. # History of Present Illness Farah862 Beryl690 is a 27 year-old nonhispanic black female. Patient has a history of stress (finding). # Social History Patient is married. Patient quit smoking at age 16. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Blue Cross Blue Shield. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with full-time employment (finding). ## Plan
[DocumentReference/c2e66851-04e6-00cb-1217-dd6ffdaefa12#1] Clinical note | 2006-07-17 | part 1 of 1 | 2006-07-17 # Chief Complaint No complaints. # History of Present Illness Farah862 Beryl690 is a 22 year-old nonhispanic black female. Patient has a history of stress (finding). # Social History Patient is married. Patient quit smoking at age 16. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Blue Cross Blue Shield. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with victim of intimate partner abuse (finding). ## Plan
[DocumentReference/244b4572-088e-0707-076f-2a8b4553db81#1] Clinical note | 2001-07-02 | part 1 of 1 | 2001-07-02 # Chief Complaint No complaints. # History of Present Illness Farah862 Beryl690 is a 17 year-old nonhispanic black female. # Social History Patient quit smoking at age 16. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with risk activity involvement (finding). ## Plan
[DocumentReference/db21e2a5-eb64-6095-57c5-0a3ea5f39cfa#1] Clinical note | 2002-07-08 | part 1 of 1 | 2002-07-08 # Chief Complaint No complaints. # History of Present Illness Farah862 Beryl690 is a 18 year-old nonhispanic black female. # Social History Patient quit smoking at age 16. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with educated to high school level (finding). ## Plan
[DocumentReference/a99414e6-fef2-4a1f-3b86-a18561dc8711#1] Clinical note | 2016-01-25 | part 1 of 1 | 2016-01-25 # Chief Complaint No complaints. # History of Present Illness Farah862 Beryl690 is a 31 year-old nonhispanic black female. Patient has a history of full-time employment (finding), stress (finding). # Social History Patient is married. Patient quit smoking at age 16. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Blue Cross Blue Shield. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The patient was prescribed the following medications: - {5 (dienogest 2 mg / estradiol valerate 2 mg oral tablet) / 17 (dienogest 3 mg / estradiol valerate 2 mg oral tablet) / 2 (estradiol valerate 1 mg oral tablet) / 2 (estradiol valerate 3 mg oral tablet) / 2 (inert ingredients 1 mg oral tablet) } pack [natazia 28 day]
[Condition/0e6e0d73-619d-15c3-242a-1ed20c0c8704] Condition | onset 2021-08-02 | Unemployed (finding) | clinical status resolved | resolved 2024-05-20 | SNOMED 73438004
[Condition/0e6e0d73-619d-15c3-472c-5169c5759ce0] Condition | onset 2003-07-14 | Stress (finding) | clinical status resolved | resolved 2021-08-02 | SNOMED 73595000
```

</details>

label: s
note: All five cited Condition cards are active with the stated onset dates; together with the first sentence the answer covers all nine active conditions and leaves out the resolved ones.

## 41. `latest-lab-4548-4:8446fe54#0#1`

Question: What was the patient's most recent hemoglobin A1c result, and when was it measured?

Answer: The most recent hemoglobin A1c was 6.91 %, measured on 2025-10-03. **Earlier results on 2024-09-27 and 2023-09-22 were also 6.91 %.**

Cards this sentence cites:

- `[Observation/8446fe54-5b2e-6a46-3f49-a8117f3d22df]` Observation (laboratory) | 2024-09-27 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.91 % | status final | LOINC 4548-4
- `[Observation/8446fe54-5b2e-6a46-2871-fec03332d8c9]` Observation (laboratory) | 2023-09-22 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.91 % | status final | LOINC 4548-4

<details><summary>Everything the model saw (49 cards)</summary>

```text
[Condition/8446fe54-5b2e-6a46-c855-6376bf616037] Condition | onset 2025-10-03 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/8446fe54-5b2e-6a46-3883-408ea2da0a37] Condition | onset 2025-05-15 | Nonproliferative diabetic retinopathy due to type II diabetes mellitus | clinical status active | SNOMED 1551000119108
[Condition/8446fe54-5b2e-6a46-2283-ccf89bdfa001] Condition | onset 2024-09-27 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8446fe54-5b2e-6a46-8ab7-b639a56aa55f] Condition | onset 2023-09-22 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/8446fe54-5b2e-6a46-169f-475724b93b14] Condition | onset 2022-03-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/8446fe54-5b2e-6a46-7c5e-428350d41910] Condition | onset 2022-03-08 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/8446fe54-5b2e-6a46-b854-dbfe1d5848d8] Condition | onset 2019-08-30 | Neuropathy due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 368581000119106
[Condition/8446fe54-5b2e-6a46-9883-d3e4fb3c92c7] Condition | onset 2017-08-18 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8446fe54-5b2e-6a46-90ec-9d5bb7f4215c] Condition | onset 2015-08-07 | Limited social contact (finding) | clinical status active | SNOMED 423315002
[Condition/8446fe54-5b2e-6a46-ac98-749a48641300] Condition | onset 2009-07-27 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/8446fe54-5b2e-6a46-ac45-606071904f4c] Condition | onset 2009-07-03 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/8446fe54-5b2e-6a46-19e1-02a0cca64803] Condition | onset 2009-07-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8446fe54-5b2e-6a46-9731-2ba07e7b3f8a] Condition | onset 2002-05-24 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/8446fe54-5b2e-6a46-5645-a8fdbdfcefa0] Condition | onset 1997-04-25 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8446fe54-5b2e-6a46-6984-e3082708b597] Condition | onset 1997-01-20 | Localized, primary osteoarthritis of the hand (disorder) | clinical status active | SNOMED 201834006
[Condition/8446fe54-5b2e-6a46-918b-8a35802414ef] Condition | onset 1996-11-29 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8446fe54-5b2e-6a46-8453-0b6ddcc40622] Condition | onset 1996-11-29 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/8446fe54-5b2e-6a46-71d0-e1231acfc548] Condition | onset 1996-04-19 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/8446fe54-5b2e-6a46-53e3-b8317bbea5b4] Condition | onset 1973-08-15 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/8446fe54-5b2e-6a46-efe6-1830fbd69235] Condition | onset 1971-06-11 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8446fe54-5b2e-6a46-a0b3-4dfcdfdaffac] Condition | onset 1965-06-04 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8446fe54-5b2e-6a46-26e1-de3ad83381e7] Condition | onset 1965-06-04 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8446fe54-5b2e-6a46-3a03-f8734c3aad20] Condition | onset 1961-05-26 | Received higher education (finding) | clinical status active | SNOMED 224299000
[MedicationRequest/8446fe54-5b2e-6a46-659f-46ecea0cf5ef] MedicationRequest | prescribed 2025-10-04 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8446fe54-5b2e-6a46-88a0-c7dd9e8fc1a1] MedicationRequest | prescribed 2025-10-03 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/8446fe54-5b2e-6a46-7320-4ef7c8ad8f40] MedicationRequest | prescribed 2025-10-03 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/8446fe54-5b2e-6a46-bf69-9fef69e23979] MedicationRequest | prescribed 2022-03-10 | rosuvastatin calcium 10 MG Oral Tablet [Crestor] | status active | RxNorm 859749
[MedicationRequest/8446fe54-5b2e-6a46-4de5-bb23365c2bff] MedicationRequest | prescribed 2022-03-10 | carvedilol 25 MG Oral Tablet | status active | RxNorm 200033
[MedicationRequest/8446fe54-5b2e-6a46-49d9-f1a38344333d] MedicationRequest | prescribed 2022-03-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/8446fe54-5b2e-6a46-3148-e44c765beb21] MedicationRequest | prescribed 2022-03-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/8446fe54-5b2e-6a46-2330-5a6c9a9f35f4] MedicationRequest | prescribed 2022-03-10 | losartan potassium 25 MG Oral Tablet | status active | RxNorm 979485
[MedicationRequest/8446fe54-5b2e-6a46-abfb-29ebed5ed8f5] MedicationRequest | prescribed 2009-07-10 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/8446fe54-5b2e-6a46-a1b3-bc484b4b6e59] MedicationRequest | prescribed 2009-07-10 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/8446fe54-5b2e-6a46-31e7-0fab4c5ed076] MedicationRequest | prescribed 2009-07-10 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/8446fe54-5b2e-6a46-2210-4b4518283f4c] MedicationRequest | prescribed 2009-07-10 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[Encounter/8446fe54-5b2e-6a46-f799-ff1c9d688587] Encounter | 2026-04-10 | Ophthalmic examination and evaluation (procedure) | class AMB | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-7463-6a2732ff7cd0] Encounter | 2026-03-06 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-f36c-8ce8c10cff85] Encounter | 2026-01-11 | Hospital admission (procedure) | class IMP | reason: Patient transfer to skilled nursing facility (procedure) | at CLAFLIN HILL CORPORATION
[Immunization/8446fe54-5b2e-6a46-dae8-760a54add250] Immunization | 2025-10-03 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/8446fe54-5b2e-6a46-a7d0-f74e09b33da1] Observation (laboratory) | 2025-10-03 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.91 % | status final | LOINC 4548-4
[Observation/8446fe54-5b2e-6a46-3f49-a8117f3d22df] Observation (laboratory) | 2024-09-27 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.91 % | status final | LOINC 4548-4
[Observation/8446fe54-5b2e-6a46-2871-fec03332d8c9] Observation (laboratory) | 2023-09-22 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.91 % | status final | LOINC 4548-4
[Observation/8446fe54-5b2e-6a46-9ac0-8f2331e3952d] Observation (laboratory) | 2020-09-04 | Hemoglobin [Mass/volume] in Blood = 14.51 g/dL | status final | LOINC 718-7
[Observation/8446fe54-5b2e-6a46-3004-2f2ac3a1a5ac] Observation (laboratory) | 2025-10-03 | Hemoglobin [Mass/volume] in Blood = 16.946 g/dL | status final | LOINC 718-7
[Observation/8446fe54-5b2e-6a46-c76a-da88e588c9ae] Observation (laboratory) | 2022-03-08 | Hemoglobin [Mass/volume] in Blood = 12.751 g/dL | status final | LOINC 718-7
[Observation/8446fe54-5b2e-6a46-a1f0-b97be4fc91f1] Observation (laboratory) | 2022-03-08 | aPTT in Blood by Coagulation assay = 28.597 s | status final | LOINC 3173-2
[Observation/8446fe54-5b2e-6a46-eb75-0e1bbcd98d97] Observation (laboratory) | 2020-09-11 | Glucose [Mass/volume] in Blood = 124.54 mg/dL | status final | LOINC 2339-0
[Observation/8446fe54-5b2e-6a46-2262-d649e8bf4cce] Observation (laboratory) | 2025-10-04 | Glucose [Mass/volume] in Blood = 100.31 mg/dL | status final | LOINC 2339-0
[Observation/8446fe54-5b2e-6a46-102b-35b203651829] Observation (laboratory) | 2025-10-03 | Glucose [Mass/volume] in Blood = 104.23 mg/dL | status final | LOINC 2339-0
```

</details>

label: s
note: Both cited A1c cards read 6.91 % on 2024-09-27 and 2023-09-22; these are the only A1c results besides the 2025-10-03 one, so nothing in the record contradicts it.

## 42. `last-colonoscopy:760e0542#0#0`

Question: When was the patient's most recent colonoscopy?

Answer: **The patient's most recent colonoscopy was completed on 2023-09-25, during a check-up encounter at LAWRENCE GENERAL HOSPITAL for screening for malignant neoplasm of colon.** A prior colonoscopy was completed on 2018-09-25.

Cards this sentence cites:

- `[Procedure/760e0542-9c61-9c1a-36f9-74e96e29948b]` Procedure | 2023-09-25 | Colonoscopy (procedure) | status completed | SNOMED 73761001
- `[Encounter/760e0542-9c61-9c1a-1104-df6d704112e5]` Encounter | 2023-09-25 | Encounter for check up (procedure) | class AMB | reason: Screening for malignant neoplasm of colon (procedure) | at LAWRENCE GENERAL HOSPITAL
- `[DocumentReference/bb81eaa0-a868-c7f5-3800-99f99001c158#2]` Clinical note | 2023-09-25 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - colonoscopy (procedure)

<details><summary>Everything the model saw (44 cards)</summary>

```text
[Condition/760e0542-9c61-9c1a-f014-d96ecb52354b] Condition | onset 2026-09-09 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/760e0542-9c61-9c1a-3909-ca43a58a2be0] Condition | onset 2023-02-08 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/760e0542-9c61-9c1a-0603-33ac04e928e9] Condition | onset 2017-07-26 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/760e0542-9c61-9c1a-7969-97405f2cda90] Condition | onset 2016-09-28 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/760e0542-9c61-9c1a-bc04-975a613f7bef] Condition | onset 2016-05-04 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/760e0542-9c61-9c1a-19fd-96240fc0e3b9] Condition | onset 2016-05-04 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/760e0542-9c61-9c1a-e1cf-d1bcca0d3b69] Condition | onset 2016-03-02 | Familial Alzheimer's disease of early onset (disorder) | clinical status active | SNOMED 230265002
[Condition/760e0542-9c61-9c1a-bf45-3800d10bb908] Condition | onset 2012-09-12 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/760e0542-9c61-9c1a-6a42-9364f5d685e7] Condition | onset 2009-10-14 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/760e0542-9c61-9c1a-6844-45eca3bcbf32] Condition | onset 2009-10-14 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/760e0542-9c61-9c1a-c55b-b73483d412d5] Condition | onset 2004-09-01 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/760e0542-9c61-9c1a-8f20-42b2a944fe6e] Condition | onset 2004-09-01 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/760e0542-9c61-9c1a-426d-1b0e47f6ef3a] Condition | onset 2004-09-01 | Hyperglycemia (disorder) | clinical status active | SNOMED 80394007
[Condition/760e0542-9c61-9c1a-84cc-6ec1252b5c47] Condition | onset 1998-10-12 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/760e0542-9c61-9c1a-d618-c814cd687574] Condition | onset 1998-01-07 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/760e0542-9c61-9c1a-addb-545c11e2d54a] Condition | onset 1998-01-07 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/760e0542-9c61-9c1a-393d-4476d7ede869] Condition | onset 1995-01-04 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/760e0542-9c61-9c1a-0e56-fe029b0a5419] Condition | onset 1990-08-12 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/760e0542-9c61-9c1a-8747-2a2b77e88f89] Condition | onset 1988-12-28 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/760e0542-9c61-9c1a-4f0e-0a94437d4aaa] Condition | onset 1988-12-28 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/760e0542-9c61-9c1a-771f-54deeed066bf] Condition | onset 1982-12-22 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/760e0542-9c61-9c1a-0604-679a8d525bc1] Condition | onset 1981-12-16 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/760e0542-9c61-9c1a-c792-3a8303530414] Condition | onset 1979-12-05 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[Condition/760e0542-9c61-9c1a-1d06-faad5e8f657c] Condition | onset 1974-01-03 | Adolescent idiopathic scoliosis (disorder) | clinical status active | SNOMED 203646004
[MedicationRequest/760e0542-9c61-9c1a-c29f-4c3b83db674e] MedicationRequest | prescribed 2026-09-09 | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 860975
[MedicationRequest/760e0542-9c61-9c1a-096d-4868f9087e48] MedicationRequest | prescribed 2026-09-09 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[MedicationRequest/760e0542-9c61-9c1a-c259-531395abfaa1] MedicationRequest | prescribed 2023-01-14 | 24 HR Donepezil hydrochloride 10 MG / Memantine hydrochloride 28 MG Extended Release Oral Capsule | status active | reason: Familial Alzheimer's disease of early onset (disorder) | RxNorm 1599803
[MedicationRequest/760e0542-9c61-9c1a-fd81-acf11c1ddec0] MedicationRequest | prescribed 1967-04-25 | Chlorpheniramine Maleate 2 MG/ML Oral Solution | status active | RxNorm 477045
[AllergyIntolerance/760e0542-9c61-9c1a-3695-658972edefe5] AllergyIntolerance | recorded 1967-05-01 | Allergic disposition (finding) | allergy, category environment, criticality low | clinical status active | SNOMED 609328004
[AllergyIntolerance/760e0542-9c61-9c1a-1887-b0f58a6117f4] AllergyIntolerance | recorded 1967-05-01 | Lisinopril | intolerance, category medication, criticality low | clinical status active | RxNorm 29046
[Encounter/760e0542-9c61-9c1a-6caa-86123ce8fd48] Encounter | 2026-09-09 | Urgent care clinic (environment) | class AMB | at MIDDLETON FAMILY MEDICINE URGENT CARE, LLC
[Encounter/760e0542-9c61-9c1a-dbc8-3964b3a3c72f] Encounter | 2026-08-05 | Urgent care clinic (environment) | class AMB | at MIDDLETON FAMILY MEDICINE URGENT CARE, LLC
[Encounter/760e0542-9c61-9c1a-d9e8-129c4edf531b] Encounter | 2026-05-27 | Encounter for check up (procedure) | class AMB | at LAWRENCE GENERAL HOSPITAL
[Immunization/760e0542-9c61-9c1a-bb77-51bf2da7f927] Immunization | 2026-04-08 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Procedure/760e0542-9c61-9c1a-36f9-74e96e29948b] Procedure | 2023-09-25 | Colonoscopy (procedure) | status completed | SNOMED 73761001
[Procedure/760e0542-9c61-9c1a-a8c0-9d4814ffe344] Procedure | 2018-09-25 | Colonoscopy (procedure) | status completed | SNOMED 73761001
[DocumentReference/bb81eaa0-a868-c7f5-3800-99f99001c158#2] Clinical note | 2023-09-25 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - colonoscopy (procedure)
[DocumentReference/992b3342-c16b-ddd9-384a-df18fb521c32#1] Clinical note | 2018-09-25 | part 1 of 1 | 2018-09-25 # Chief Complaint - Fatigue - Frequent Urination - Thirst - Hunger - Confusion # History of Present Illness Patrica776 Golda777 is a 55 year-old nonhispanic white female. Patient has a history of part-time employment (finding), medication review due (situation), limited social contact (finding), not in labor force (finding), chronic periodontitis, generalized, reports of violence in the environment (finding), full-time employment (finding), victim of intimate partner abuse (finding), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications tropicamide 5 mg/ml ophthalmic solution; 24 hr metformin hydrochloride 500 mg extended release oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; galantamine 4 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - colonoscopy (procedure)
[Encounter/760e0542-9c61-9c1a-1104-df6d704112e5] Encounter | 2023-09-25 | Encounter for check up (procedure) | class AMB | reason: Screening for malignant neoplasm of colon (procedure) | at LAWRENCE GENERAL HOSPITAL
[Encounter/760e0542-9c61-9c1a-fb02-56dab69984cd] Encounter | 2018-09-25 | Encounter for check up (procedure) | class AMB | reason: Screening for malignant neoplasm of colon (procedure) | at LAWRENCE GENERAL HOSPITAL
[Immunization/760e0542-9c61-9c1a-bb55-2e74e1870df5] Immunization | 2021-05-05 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/760e0542-9c61-9c1a-348d-850ee604a0a7] Immunization | 2021-04-14 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[ImagingStudy/760e0542-9c61-9c1a-fefe-8188d1f57d86] ImagingStudy | 2020-05-02 | Camera fundoscopy (procedure) | status available
[Encounter/760e0542-9c61-9c1a-2861-bf73d649f457] Encounter | 2024-11-06 | Follow-up consultation (procedure) | class AMB | reason: Familial Alzheimer's disease of early onset (disorder) | at LAWRENCE GENERAL HOSPITAL
```

</details>

label: s
note: Procedure card shows a completed colonoscopy on 2023-09-25, the later of the two colonoscopies in the record (the other is 2018-09-25). The only encounter that day is a check-up at LAWRENCE GENERAL HOSPITAL with reason screening for malignant neoplasm of colon, and the same-day note lists colonoscopy as performed.

## 43. `prescribed-for-essential-hypertension:8446fe54#0#1`

Question: Which medications have been prescribed for the patient's essential hypertension?

Answer: Lisinopril 10 MG Oral Tablet is the medication prescribed with essential hypertension as the reason, with a currently active prescription dated 2025-10-03. **Earlier lisinopril 10 MG Oral Tablet prescriptions for essential hypertension, dated 2021-09-10, 2023-09-22 and 2024-09-27, have status completed.** A lifestyle education care plan for hypertension, started 1997-04-25, is also active.

Cards this sentence cites:

- `[MedicationRequest/8446fe54-5b2e-6a46-386f-9221c610c0f4]` MedicationRequest | prescribed 2021-09-10 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
- `[MedicationRequest/8446fe54-5b2e-6a46-fbb9-e09c508bd3ef]` MedicationRequest | prescribed 2023-09-22 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
- `[MedicationRequest/8446fe54-5b2e-6a46-738a-d4c152c25a67]` MedicationRequest | prescribed 2024-09-27 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076

<details><summary>Everything the model saw (49 cards)</summary>

```text
[Condition/8446fe54-5b2e-6a46-c855-6376bf616037] Condition | onset 2025-10-03 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/8446fe54-5b2e-6a46-3883-408ea2da0a37] Condition | onset 2025-05-15 | Nonproliferative diabetic retinopathy due to type II diabetes mellitus | clinical status active | SNOMED 1551000119108
[Condition/8446fe54-5b2e-6a46-2283-ccf89bdfa001] Condition | onset 2024-09-27 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8446fe54-5b2e-6a46-8ab7-b639a56aa55f] Condition | onset 2023-09-22 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/8446fe54-5b2e-6a46-169f-475724b93b14] Condition | onset 2022-03-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/8446fe54-5b2e-6a46-7c5e-428350d41910] Condition | onset 2022-03-08 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/8446fe54-5b2e-6a46-b854-dbfe1d5848d8] Condition | onset 2019-08-30 | Neuropathy due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 368581000119106
[Condition/8446fe54-5b2e-6a46-9883-d3e4fb3c92c7] Condition | onset 2017-08-18 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8446fe54-5b2e-6a46-90ec-9d5bb7f4215c] Condition | onset 2015-08-07 | Limited social contact (finding) | clinical status active | SNOMED 423315002
[Condition/8446fe54-5b2e-6a46-ac98-749a48641300] Condition | onset 2009-07-27 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/8446fe54-5b2e-6a46-ac45-606071904f4c] Condition | onset 2009-07-03 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/8446fe54-5b2e-6a46-19e1-02a0cca64803] Condition | onset 2009-07-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8446fe54-5b2e-6a46-9731-2ba07e7b3f8a] Condition | onset 2002-05-24 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/8446fe54-5b2e-6a46-5645-a8fdbdfcefa0] Condition | onset 1997-04-25 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8446fe54-5b2e-6a46-6984-e3082708b597] Condition | onset 1997-01-20 | Localized, primary osteoarthritis of the hand (disorder) | clinical status active | SNOMED 201834006
[Condition/8446fe54-5b2e-6a46-918b-8a35802414ef] Condition | onset 1996-11-29 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8446fe54-5b2e-6a46-8453-0b6ddcc40622] Condition | onset 1996-11-29 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/8446fe54-5b2e-6a46-71d0-e1231acfc548] Condition | onset 1996-04-19 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/8446fe54-5b2e-6a46-53e3-b8317bbea5b4] Condition | onset 1973-08-15 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/8446fe54-5b2e-6a46-efe6-1830fbd69235] Condition | onset 1971-06-11 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8446fe54-5b2e-6a46-a0b3-4dfcdfdaffac] Condition | onset 1965-06-04 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8446fe54-5b2e-6a46-26e1-de3ad83381e7] Condition | onset 1965-06-04 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8446fe54-5b2e-6a46-3a03-f8734c3aad20] Condition | onset 1961-05-26 | Received higher education (finding) | clinical status active | SNOMED 224299000
[MedicationRequest/8446fe54-5b2e-6a46-659f-46ecea0cf5ef] MedicationRequest | prescribed 2025-10-04 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8446fe54-5b2e-6a46-88a0-c7dd9e8fc1a1] MedicationRequest | prescribed 2025-10-03 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/8446fe54-5b2e-6a46-7320-4ef7c8ad8f40] MedicationRequest | prescribed 2025-10-03 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/8446fe54-5b2e-6a46-bf69-9fef69e23979] MedicationRequest | prescribed 2022-03-10 | rosuvastatin calcium 10 MG Oral Tablet [Crestor] | status active | RxNorm 859749
[MedicationRequest/8446fe54-5b2e-6a46-4de5-bb23365c2bff] MedicationRequest | prescribed 2022-03-10 | carvedilol 25 MG Oral Tablet | status active | RxNorm 200033
[MedicationRequest/8446fe54-5b2e-6a46-49d9-f1a38344333d] MedicationRequest | prescribed 2022-03-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/8446fe54-5b2e-6a46-3148-e44c765beb21] MedicationRequest | prescribed 2022-03-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/8446fe54-5b2e-6a46-2330-5a6c9a9f35f4] MedicationRequest | prescribed 2022-03-10 | losartan potassium 25 MG Oral Tablet | status active | RxNorm 979485
[MedicationRequest/8446fe54-5b2e-6a46-abfb-29ebed5ed8f5] MedicationRequest | prescribed 2009-07-10 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/8446fe54-5b2e-6a46-a1b3-bc484b4b6e59] MedicationRequest | prescribed 2009-07-10 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/8446fe54-5b2e-6a46-31e7-0fab4c5ed076] MedicationRequest | prescribed 2009-07-10 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/8446fe54-5b2e-6a46-2210-4b4518283f4c] MedicationRequest | prescribed 2009-07-10 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[Encounter/8446fe54-5b2e-6a46-f799-ff1c9d688587] Encounter | 2026-04-10 | Ophthalmic examination and evaluation (procedure) | class AMB | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-7463-6a2732ff7cd0] Encounter | 2026-03-06 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-f36c-8ce8c10cff85] Encounter | 2026-01-11 | Hospital admission (procedure) | class IMP | reason: Patient transfer to skilled nursing facility (procedure) | at CLAFLIN HILL CORPORATION
[Immunization/8446fe54-5b2e-6a46-dae8-760a54add250] Immunization | 2025-10-03 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/8446fe54-5b2e-6a46-386f-9221c610c0f4] MedicationRequest | prescribed 2021-09-10 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/8446fe54-5b2e-6a46-738a-d4c152c25a67] MedicationRequest | prescribed 2024-09-27 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/8446fe54-5b2e-6a46-fbb9-e09c508bd3ef] MedicationRequest | prescribed 2023-09-22 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
[CarePlan/8446fe54-5b2e-6a46-a78b-87751e770c9f] CarePlan | started 1997-04-25 | Lifestyle education regarding hypertension (procedure) | status active | activities: Prescribed activity/exercise education (procedure); Counseling about alcohol consumption (procedure); Dietary Approaches to Stop Hypertension diet (regime/therapy); Smoking cessation education (procedure)
[DocumentReference/59779ffc-7e59-1b72-e992-5a4997b4b32d#2] Clinical note | 2025-10-04 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[MedicationRequest/8446fe54-5b2e-6a46-cbe0-330eed1bd176] MedicationRequest | prescribed 2021-08-04 | status completed
[DocumentReference/28ab82c8-e34e-aee8-b559-56a6ab5c0c0e#1] Clinical note | 1997-04-25 | part 1 of 1 | 1997-04-25 # Chief Complaint - Tingling in Hands and Feet - Blurred Vision # History of Present Illness Elfrieda676 Agustina460 is a 54 year-old nonhispanic white female. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with essential hypertension (disorder). ## Plan The patient was placed on a careplan: - lifestyle education regarding hypertension (procedure)
[MedicationRequest/8446fe54-5b2e-6a46-3dfa-0a8aa3812f7d] MedicationRequest | prescribed 2018-11-18 | status completed
[MedicationRequest/8446fe54-5b2e-6a46-d1b0-886d1cae3bc3] MedicationRequest | prescribed 2022-03-08 | status completed
[MedicationRequest/8446fe54-5b2e-6a46-8d86-18f729728011] MedicationRequest | prescribed 2020-09-08 | status completed
```

</details>

label: s
note: The three cited lisinopril 10 MG cards (2021-09-10, 2023-09-22, 2024-09-27) each show reason essential hypertension and status completed. The sentence makes no completeness claim.

## 44. `active-problems:ef5e136c#0#0`

Question: What active diagnoses does the patient have?

Answer: **Active kidney and metabolic diagnoses include end-stage renal disease (onset 2025-08-27), awaiting kidney transplantation, chronic kidney disease stages 1 through 4, disorder of kidney due to diabetes mellitus, proteinuria and microalbuminuria due to type 2 diabetes mellitus, diabetes mellitus type 2, prediabetes, metabolic syndrome X, hypertriglyceridemia, essential hypertension, and obesity (BMI 30+).** Other active disorders are anemia, gingivitis, and chronic sinusitis. Active findings and situations include medication review due (onset 2026-09-30), social isolation, unemployment, stress, history of tubal ligation, past miscarriage, criminal record, received higher education, and risk activity involvement.

Cards this sentence cites:

- `[Condition/ef5e136c-ff1e-0695-aa04-94486c99258f]` Condition | onset 2025-08-27 | End-stage renal disease (disorder) | clinical status active | SNOMED 46177005
- `[Condition/ef5e136c-ff1e-0695-423f-ed71d76e81e3]` Condition | onset 2025-03-30 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
- `[Condition/ef5e136c-ff1e-0695-fda2-40e12f6b17a7]` Condition | onset 2017-11-15 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
- `[Condition/ef5e136c-ff1e-0695-65f5-8d04f278a661]` Condition | onset 2023-08-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
- `[Condition/ef5e136c-ff1e-0695-3834-fa6cb282a475]` Condition | onset 2024-05-15 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
- `[Condition/ef5e136c-ff1e-0695-71df-3a96389b0a39]` Condition | onset 2025-02-05 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
- `[Condition/ef5e136c-ff1e-0695-bf3f-30946ad3f8b4]` Condition | onset 2017-11-15 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
- `[Condition/ef5e136c-ff1e-0695-5331-2d63eb213c34]` Condition | onset 2024-05-15 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
- `[Condition/ef5e136c-ff1e-0695-68fe-9e2010333061]` Condition | onset 2023-08-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
- `[Condition/ef5e136c-ff1e-0695-5ca5-51bfdc51320e]` Condition | onset 2010-05-12 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
- `[Condition/ef5e136c-ff1e-0695-1f68-dac24351dbaa]` Condition | onset 1993-04-14 | Prediabetes (finding) | clinical status active | SNOMED 714628002
- `[Condition/ef5e136c-ff1e-0695-b228-2f5ff5bb47cb]` Condition | onset 2010-05-19 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
- `[Condition/ef5e136c-ff1e-0695-af16-82f03f777ba8]` Condition | onset 2010-05-19 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
- `[Condition/ef5e136c-ff1e-0695-eac4-d545a0296998]` Condition | onset 2011-07-27 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
- `[Condition/ef5e136c-ff1e-0695-f7ec-ceae0c2566bc]` Condition | onset 2004-06-16 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005

<details><summary>Everything the model saw (47 cards)</summary>

```text
[Condition/ef5e136c-ff1e-0695-1f8c-935a12106cac] Condition | onset 2026-09-30 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/ef5e136c-ff1e-0695-7e5d-470b95f60db2] Condition | onset 2026-09-23 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/ef5e136c-ff1e-0695-9d2d-c4be459bc9f4] Condition | onset 2026-09-09 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/ef5e136c-ff1e-0695-7b9c-f43e5ca3f6c6] Condition | onset 2026-08-12 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-aa04-94486c99258f] Condition | onset 2025-08-27 | End-stage renal disease (disorder) | clinical status active | SNOMED 46177005
[Condition/ef5e136c-ff1e-0695-423f-ed71d76e81e3] Condition | onset 2025-03-30 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/ef5e136c-ff1e-0695-71df-3a96389b0a39] Condition | onset 2025-02-05 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/ef5e136c-ff1e-0695-5331-2d63eb213c34] Condition | onset 2024-05-15 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/ef5e136c-ff1e-0695-3834-fa6cb282a475] Condition | onset 2024-05-15 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/ef5e136c-ff1e-0695-68fe-9e2010333061] Condition | onset 2023-08-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/ef5e136c-ff1e-0695-65f5-8d04f278a661] Condition | onset 2023-08-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/ef5e136c-ff1e-0695-aac2-46a0ff462178] Condition | onset 2023-04-19 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/ef5e136c-ff1e-0695-fda2-40e12f6b17a7] Condition | onset 2017-11-15 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/ef5e136c-ff1e-0695-bf3f-30946ad3f8b4] Condition | onset 2017-11-15 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/ef5e136c-ff1e-0695-eac4-d545a0296998] Condition | onset 2011-07-27 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/ef5e136c-ff1e-0695-b228-2f5ff5bb47cb] Condition | onset 2010-05-19 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/ef5e136c-ff1e-0695-af16-82f03f777ba8] Condition | onset 2010-05-19 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/ef5e136c-ff1e-0695-5ca5-51bfdc51320e] Condition | onset 2010-05-12 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/ef5e136c-ff1e-0695-f7ec-ceae0c2566bc] Condition | onset 2004-06-16 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/ef5e136c-ff1e-0695-c94a-5d81ddd88117] Condition | onset 1997-05-07 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/ef5e136c-ff1e-0695-6efc-9f7d5e6b04ef] Condition | onset 1993-09-01 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/ef5e136c-ff1e-0695-1f68-dac24351dbaa] Condition | onset 1993-04-14 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/ef5e136c-ff1e-0695-2d8d-328849698529] Condition | onset 1993-01-22 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/ef5e136c-ff1e-0695-0825-c31e8b252683] Condition | onset 1983-11-14 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/ef5e136c-ff1e-0695-cb16-3a98eeb2de7a] Condition | onset 1976-01-07 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/ef5e136c-ff1e-0695-3278-6a86eaf1fb5d] Condition | onset 1975-06-27 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/ef5e136c-ff1e-0695-337f-d12087c8dbb5] Condition | onset 1975-01-01 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/ef5e136c-ff1e-0695-ffec-2ea7ac772a27] MedicationRequest | prescribed 2026-09-30 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/ef5e136c-ff1e-0695-b3ba-a1ec7bcfb9f4] MedicationRequest | prescribed 2026-09-30 | albuterol 0.83 MG/ML Inhalation Solution | status active | RxNorm 630208
[MedicationRequest/ef5e136c-ff1e-0695-901e-2e1f9afb0cca] MedicationRequest | prescribed 2026-09-30 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/ef5e136c-ff1e-0695-76a6-8eeb54f8a75e] MedicationRequest | prescribed 2026-09-30 | 120 ACTUAT fluticasone propionate 0.044 MG/ACTUAT Metered Dose Inhaler [Flovent] | status active | RxNorm 895996
[MedicationRequest/ef5e136c-ff1e-0695-6c6d-182c3b9c47c1] MedicationRequest | prescribed 2026-09-30 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/ef5e136c-ff1e-0695-6804-cf31640a9491] MedicationRequest | prescribed 2026-09-30 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[Encounter/ef5e136c-ff1e-0695-08ba-2471a16a6570] Encounter | 2026-09-30 | Emergency room admission (procedure) | class EMER | at APPLE VALLEY CENTER
[Encounter/ef5e136c-ff1e-0695-aea4-11055569fd51] Encounter | 2026-09-23 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/ef5e136c-ff1e-0695-4a41-6fca58c80cb7] Encounter | 2026-09-16 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Immunization/ef5e136c-ff1e-0695-6beb-93901776b619] Immunization | 2026-05-13 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Condition/ef5e136c-ff1e-0695-08d2-be5484c6a000] Condition | onset 2023-03-22 | Unemployed (finding) | clinical status resolved | resolved 2023-09-13 | SNOMED 73438004
[Condition/ef5e136c-ff1e-0695-0659-7182eb1d6004] Condition | onset 2026-07-15 | Stress (finding) | clinical status resolved | resolved 2026-07-29 | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-e041-99b1020df098] Condition | onset 2026-06-03 | Stress (finding) | clinical status resolved | resolved 2026-07-01 | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-692f-015054b9f312] Condition | onset 2026-06-17 | Social isolation (finding) | clinical status resolved | resolved 2026-07-01 | SNOMED 422650009
[Condition/ef5e136c-ff1e-0695-4933-cd2f72fdccfd] Condition | onset 2026-02-25 | Social isolation (finding) | clinical status resolved | resolved 2026-05-20 | SNOMED 422650009
[Condition/ef5e136c-ff1e-0695-015a-38b99f76c99a] Condition | onset 2026-07-15 | Medication review due (situation) | clinical status resolved | resolved 2026-09-23 | SNOMED 314529007
[Condition/ef5e136c-ff1e-0695-75e1-26880e235e23] Condition | onset 2026-06-24 | Medication review due (situation) | clinical status resolved | resolved 2026-07-08 | SNOMED 314529007
[Condition/ef5e136c-ff1e-0695-2f1a-03ff86dc5f30] Condition | onset 2022-06-22 | Gingivitis (disorder) | clinical status resolved | resolved 2022-07-06 | SNOMED 66383009
[Condition/ef5e136c-ff1e-0695-dbf4-8f4d3ac1dc0d] Condition | onset 2021-04-28 | Gingivitis (disorder) | clinical status resolved | resolved 2021-05-12 | SNOMED 66383009
[Device/ef5e136c-ff1e-0695-a6bd-061655f25eb7] Device | Manual wheelchair (physical object) | status active | manufactured 2019-10-04 | SNOMED 228869008
```

</details>

label: s
note: Every listed condition has a cited card with clinical status active, and the ESRD onset 2025-08-27 matches. The sentence says 'include', so it does not claim a complete list.

## 45. `prescribed-for-essential-hypertension:772fc930#0#1`

Question: Which medications have been prescribed for the patient's essential hypertension?

Answer: For essential hypertension, the patient has been prescribed Hydrochlorothiazide 25 MG Oral Tablet and lisinopril 10 MG Oral Tablet, both with active prescriptions dated 2026-07-16. **Earlier, now-completed prescriptions for Hydrochlorothiazide 25 MG Oral Tablet were dated 2026-07-02 and 2026-07-09.** Earlier, now-completed prescriptions for lisinopril 10 MG Oral Tablet were dated 2021-08-26, 2026-07-02 and 2026-07-09.

Cards this sentence cites:

- `[MedicationRequest/772fc930-5418-0bfa-5a75-777528122cac]` MedicationRequest | prescribed 2026-07-02 | Hydrochlorothiazide 25 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 310798
- `[MedicationRequest/772fc930-5418-0bfa-3648-8f2dee0d3e13]` MedicationRequest | prescribed 2026-07-09 | Hydrochlorothiazide 25 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 310798

<details><summary>Everything the model saw (36 cards)</summary>

```text
[Condition/772fc930-5418-0bfa-5baf-97b1667a332f] Condition | onset 2026-07-09 | Part-time employment (finding) | clinical status active | SNOMED 160904001
[Condition/772fc930-5418-0bfa-446c-c28d224cff31] Condition | onset 2026-06-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/772fc930-5418-0bfa-33d9-881f0ecc07c1] Condition | onset 2026-06-11 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/772fc930-5418-0bfa-d3cc-a2daa4832199] Condition | onset 2026-02-19 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/772fc930-5418-0bfa-600b-5558ca66220a] Condition | onset 2026-02-19 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/772fc930-5418-0bfa-6352-6c3984966ef8] Condition | onset 2025-02-13 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/772fc930-5418-0bfa-bb6d-8a0b90cf95e4] Condition | onset 2020-01-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/772fc930-5418-0bfa-ab71-24a74b1745fd] Condition | onset 2020-01-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/772fc930-5418-0bfa-beac-a103fe7f3fd2] Condition | onset 2019-01-10 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/772fc930-5418-0bfa-2c4f-3f5ed5953c36] Condition | onset 2019-01-10 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/772fc930-5418-0bfa-3873-02589386889d] Condition | onset 2004-06-19 | Osteoarthritis of hip (disorder) | clinical status active | SNOMED 239872002
[Condition/772fc930-5418-0bfa-a4a0-5eff492015a6] Condition | onset 1991-08-28 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/772fc930-5418-0bfa-01dc-3613408a83a6] Condition | onset 1991-08-22 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/772fc930-5418-0bfa-35d2-44b4eb4fcccc] Condition | onset 1991-08-08 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/772fc930-5418-0bfa-43ec-8fdd443cc6ce] Condition | onset 1988-07-21 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/772fc930-5418-0bfa-91e4-e46a214921b9] Condition | onset 1986-07-10 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/772fc930-5418-0bfa-47df-a943ca27aa29] Condition | onset 1986-07-10 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/772fc930-5418-0bfa-7d09-0ea3ca1e93ba] Condition | onset 1986-03-30 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/772fc930-5418-0bfa-1be5-06b5144b5817] Condition | onset 1986-03-01 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/772fc930-5418-0bfa-0cdf-ac369e474ff3] Condition | onset 1977-05-19 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/772fc930-5418-0bfa-f6df-7e2448081e0f] Condition | onset 1967-05-04 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/772fc930-5418-0bfa-ffbe-e3692c7542d7] Condition | onset 1964-01-15 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/772fc930-5418-0bfa-d2b4-bc5609421614] MedicationRequest | prescribed 2026-07-16 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/772fc930-5418-0bfa-35ed-4b81c08cb46e] MedicationRequest | prescribed 2026-07-16 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/772fc930-5418-0bfa-0d23-3b3c40dabcae] MedicationRequest | prescribed 2026-07-16 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/772fc930-5418-0bfa-ac79-a5117bd68db1] MedicationRequest | prescribed 2026-03-06 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/772fc930-5418-0bfa-dfc7-922f9300bced] MedicationRequest | prescribed 2004-06-19 | Naproxen sodium 220 MG Oral Tablet | status active | reason: Osteoarthritis of hip (disorder) | RxNorm 849574
[Encounter/772fc930-5418-0bfa-dd45-e4b82fc97e3d] Encounter | 2026-07-23 | Encounter for check up (procedure) | class AMB | at BOSTON MEDICAL CENTER CORPORATION-
[Encounter/772fc930-5418-0bfa-6606-662b1312d21c] Encounter | 2026-07-16 | Urgent care clinic (environment) | class AMB | at LYNN URGENT CARE LLC
[Encounter/772fc930-5418-0bfa-54c7-a3b13e8997b9] Encounter | 2026-07-09 | Emergency room admission (procedure) | class EMER | at LEONARD FLORENCE CENTER FOR LIVING
[Immunization/772fc930-5418-0bfa-fcca-2fca6db3fac3] Immunization | 2026-02-19 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/772fc930-5418-0bfa-3648-8f2dee0d3e13] MedicationRequest | prescribed 2026-07-09 | Hydrochlorothiazide 25 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/772fc930-5418-0bfa-5a75-777528122cac] MedicationRequest | prescribed 2026-07-02 | Hydrochlorothiazide 25 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/772fc930-5418-0bfa-54d4-0d5c54ef37f9] MedicationRequest | prescribed 2021-08-26 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/772fc930-5418-0bfa-92c6-1656ddca0b53] MedicationRequest | prescribed 2026-07-09 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/772fc930-5418-0bfa-0876-1f10630a892a] MedicationRequest | prescribed 2026-07-02 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
```

</details>

label: s
note: The cited HCTZ 25 MG cards dated 2026-07-02 and 2026-07-09 are both status completed with reason essential hypertension. The only other HCTZ prescription is the active 2026-07-16 one.

## 46. `latest-lab-4548-4:772fc930#0#0`

Question: What was the patient's most recent hemoglobin A1c result, and when was it measured?

Answer: **The most recent hemoglobin A1c result was 3.11 %, measured on 2026-07-16.** Earlier values were 2.96 % on 2026-07-09 and 3.35 % on 2026-07-02.

Cards this sentence cites:

- `[Observation/772fc930-5418-0bfa-8957-dbea8fe67de6]` Observation (laboratory) | 2026-07-16 | Hemoglobin A1c/Hemoglobin.total in Blood = 3.11 % | status final | LOINC 4548-4

<details><summary>Everything the model saw (41 cards)</summary>

```text
[Condition/772fc930-5418-0bfa-5baf-97b1667a332f] Condition | onset 2026-07-09 | Part-time employment (finding) | clinical status active | SNOMED 160904001
[Condition/772fc930-5418-0bfa-446c-c28d224cff31] Condition | onset 2026-06-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/772fc930-5418-0bfa-33d9-881f0ecc07c1] Condition | onset 2026-06-11 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/772fc930-5418-0bfa-d3cc-a2daa4832199] Condition | onset 2026-02-19 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/772fc930-5418-0bfa-600b-5558ca66220a] Condition | onset 2026-02-19 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/772fc930-5418-0bfa-6352-6c3984966ef8] Condition | onset 2025-02-13 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/772fc930-5418-0bfa-bb6d-8a0b90cf95e4] Condition | onset 2020-01-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/772fc930-5418-0bfa-ab71-24a74b1745fd] Condition | onset 2020-01-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/772fc930-5418-0bfa-beac-a103fe7f3fd2] Condition | onset 2019-01-10 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/772fc930-5418-0bfa-2c4f-3f5ed5953c36] Condition | onset 2019-01-10 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/772fc930-5418-0bfa-3873-02589386889d] Condition | onset 2004-06-19 | Osteoarthritis of hip (disorder) | clinical status active | SNOMED 239872002
[Condition/772fc930-5418-0bfa-a4a0-5eff492015a6] Condition | onset 1991-08-28 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/772fc930-5418-0bfa-01dc-3613408a83a6] Condition | onset 1991-08-22 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/772fc930-5418-0bfa-35d2-44b4eb4fcccc] Condition | onset 1991-08-08 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/772fc930-5418-0bfa-43ec-8fdd443cc6ce] Condition | onset 1988-07-21 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/772fc930-5418-0bfa-91e4-e46a214921b9] Condition | onset 1986-07-10 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/772fc930-5418-0bfa-47df-a943ca27aa29] Condition | onset 1986-07-10 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/772fc930-5418-0bfa-7d09-0ea3ca1e93ba] Condition | onset 1986-03-30 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/772fc930-5418-0bfa-1be5-06b5144b5817] Condition | onset 1986-03-01 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/772fc930-5418-0bfa-0cdf-ac369e474ff3] Condition | onset 1977-05-19 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/772fc930-5418-0bfa-f6df-7e2448081e0f] Condition | onset 1967-05-04 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/772fc930-5418-0bfa-ffbe-e3692c7542d7] Condition | onset 1964-01-15 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/772fc930-5418-0bfa-d2b4-bc5609421614] MedicationRequest | prescribed 2026-07-16 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/772fc930-5418-0bfa-35ed-4b81c08cb46e] MedicationRequest | prescribed 2026-07-16 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/772fc930-5418-0bfa-0d23-3b3c40dabcae] MedicationRequest | prescribed 2026-07-16 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/772fc930-5418-0bfa-ac79-a5117bd68db1] MedicationRequest | prescribed 2026-03-06 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/772fc930-5418-0bfa-dfc7-922f9300bced] MedicationRequest | prescribed 2004-06-19 | Naproxen sodium 220 MG Oral Tablet | status active | reason: Osteoarthritis of hip (disorder) | RxNorm 849574
[Encounter/772fc930-5418-0bfa-dd45-e4b82fc97e3d] Encounter | 2026-07-23 | Encounter for check up (procedure) | class AMB | at BOSTON MEDICAL CENTER CORPORATION-
[Encounter/772fc930-5418-0bfa-6606-662b1312d21c] Encounter | 2026-07-16 | Urgent care clinic (environment) | class AMB | at LYNN URGENT CARE LLC
[Encounter/772fc930-5418-0bfa-54c7-a3b13e8997b9] Encounter | 2026-07-09 | Emergency room admission (procedure) | class EMER | at LEONARD FLORENCE CENTER FOR LIVING
[Immunization/772fc930-5418-0bfa-fcca-2fca6db3fac3] Immunization | 2026-02-19 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/772fc930-5418-0bfa-8957-dbea8fe67de6] Observation (laboratory) | 2026-07-16 | Hemoglobin A1c/Hemoglobin.total in Blood = 3.11 % | status final | LOINC 4548-4
[Observation/772fc930-5418-0bfa-6626-57894070b798] Observation (laboratory) | 2026-07-09 | Hemoglobin A1c/Hemoglobin.total in Blood = 2.96 % | status final | LOINC 4548-4
[Observation/772fc930-5418-0bfa-addb-602a5c27802f] Observation (laboratory) | 2026-07-02 | Hemoglobin A1c/Hemoglobin.total in Blood = 3.35 % | status final | LOINC 4548-4
[Immunization/772fc930-5418-0bfa-f6dc-d21e77adc05b] Immunization | 2021-03-25 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/772fc930-5418-0bfa-21ee-34551e99d21d] Immunization | 2021-03-04 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Observation/772fc930-5418-0bfa-7e47-5513c13c06fe] Observation (laboratory) | 2020-11-19 | Glucose [Mass/volume] in Serum or Plasma = 80.4 mg/dL | status final | LOINC 2345-7
[Observation/772fc930-5418-0bfa-3780-16c841b6aea4] Observation (laboratory) | 2026-07-16 | Glucose [Mass/volume] in Serum or Plasma = 80.62 mg/dL | status final | LOINC 2345-7
[Observation/772fc930-5418-0bfa-c067-0d6fbb03112f] Observation (laboratory) | 2026-07-09 | Glucose [Mass/volume] in Serum or Plasma = 71.92 mg/dL | status final | LOINC 2345-7
[Observation/772fc930-5418-0bfa-c227-27c7dbd5f578] Observation (laboratory) | 2026-07-02 | Glucose [Mass/volume] in Serum or Plasma = 82.74 mg/dL | status final | LOINC 2345-7
[Observation/772fc930-5418-0bfa-0901-f1e59b801f10] Observation (laboratory) | 2023-02-02 | Hemoglobin [Mass/volume] in Blood = 14.966 g/dL | status final | LOINC 718-7
```

</details>

label: s
note: The cited card shows A1c 3.11 % on 2026-07-16. The record's other A1c results are 2026-07-09 and 2026-07-02, so this one is the most recent.

## 47. `active-problems:ef5e136c#0#1`

Question: What active diagnoses does the patient have?

Answer: Active kidney and metabolic diagnoses include end-stage renal disease (onset 2025-08-27), awaiting kidney transplantation, chronic kidney disease stages 1 through 4, disorder of kidney due to diabetes mellitus, proteinuria and microalbuminuria due to type 2 diabetes mellitus, diabetes mellitus type 2, prediabetes, metabolic syndrome X, hypertriglyceridemia, essential hypertension, and obesity (BMI 30+). **Other active disorders are anemia, gingivitis, and chronic sinusitis.** Active findings and situations include medication review due (onset 2026-09-30), social isolation, unemployment, stress, history of tubal ligation, past miscarriage, criminal record, received higher education, and risk activity involvement.

Cards this sentence cites:

- `[Condition/ef5e136c-ff1e-0695-6efc-9f7d5e6b04ef]` Condition | onset 1993-09-01 | Anemia (disorder) | clinical status active | SNOMED 271737000
- `[Condition/ef5e136c-ff1e-0695-aac2-46a0ff462178]` Condition | onset 2023-04-19 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
- `[Condition/ef5e136c-ff1e-0695-3278-6a86eaf1fb5d]` Condition | onset 1975-06-27 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000

<details><summary>Everything the model saw (47 cards)</summary>

```text
[Condition/ef5e136c-ff1e-0695-1f8c-935a12106cac] Condition | onset 2026-09-30 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/ef5e136c-ff1e-0695-7e5d-470b95f60db2] Condition | onset 2026-09-23 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/ef5e136c-ff1e-0695-9d2d-c4be459bc9f4] Condition | onset 2026-09-09 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/ef5e136c-ff1e-0695-7b9c-f43e5ca3f6c6] Condition | onset 2026-08-12 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-aa04-94486c99258f] Condition | onset 2025-08-27 | End-stage renal disease (disorder) | clinical status active | SNOMED 46177005
[Condition/ef5e136c-ff1e-0695-423f-ed71d76e81e3] Condition | onset 2025-03-30 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/ef5e136c-ff1e-0695-71df-3a96389b0a39] Condition | onset 2025-02-05 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/ef5e136c-ff1e-0695-5331-2d63eb213c34] Condition | onset 2024-05-15 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/ef5e136c-ff1e-0695-3834-fa6cb282a475] Condition | onset 2024-05-15 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/ef5e136c-ff1e-0695-68fe-9e2010333061] Condition | onset 2023-08-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/ef5e136c-ff1e-0695-65f5-8d04f278a661] Condition | onset 2023-08-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/ef5e136c-ff1e-0695-aac2-46a0ff462178] Condition | onset 2023-04-19 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/ef5e136c-ff1e-0695-fda2-40e12f6b17a7] Condition | onset 2017-11-15 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/ef5e136c-ff1e-0695-bf3f-30946ad3f8b4] Condition | onset 2017-11-15 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/ef5e136c-ff1e-0695-eac4-d545a0296998] Condition | onset 2011-07-27 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/ef5e136c-ff1e-0695-b228-2f5ff5bb47cb] Condition | onset 2010-05-19 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/ef5e136c-ff1e-0695-af16-82f03f777ba8] Condition | onset 2010-05-19 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/ef5e136c-ff1e-0695-5ca5-51bfdc51320e] Condition | onset 2010-05-12 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/ef5e136c-ff1e-0695-f7ec-ceae0c2566bc] Condition | onset 2004-06-16 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/ef5e136c-ff1e-0695-c94a-5d81ddd88117] Condition | onset 1997-05-07 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/ef5e136c-ff1e-0695-6efc-9f7d5e6b04ef] Condition | onset 1993-09-01 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/ef5e136c-ff1e-0695-1f68-dac24351dbaa] Condition | onset 1993-04-14 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/ef5e136c-ff1e-0695-2d8d-328849698529] Condition | onset 1993-01-22 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/ef5e136c-ff1e-0695-0825-c31e8b252683] Condition | onset 1983-11-14 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/ef5e136c-ff1e-0695-cb16-3a98eeb2de7a] Condition | onset 1976-01-07 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/ef5e136c-ff1e-0695-3278-6a86eaf1fb5d] Condition | onset 1975-06-27 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/ef5e136c-ff1e-0695-337f-d12087c8dbb5] Condition | onset 1975-01-01 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/ef5e136c-ff1e-0695-ffec-2ea7ac772a27] MedicationRequest | prescribed 2026-09-30 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/ef5e136c-ff1e-0695-b3ba-a1ec7bcfb9f4] MedicationRequest | prescribed 2026-09-30 | albuterol 0.83 MG/ML Inhalation Solution | status active | RxNorm 630208
[MedicationRequest/ef5e136c-ff1e-0695-901e-2e1f9afb0cca] MedicationRequest | prescribed 2026-09-30 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/ef5e136c-ff1e-0695-76a6-8eeb54f8a75e] MedicationRequest | prescribed 2026-09-30 | 120 ACTUAT fluticasone propionate 0.044 MG/ACTUAT Metered Dose Inhaler [Flovent] | status active | RxNorm 895996
[MedicationRequest/ef5e136c-ff1e-0695-6c6d-182c3b9c47c1] MedicationRequest | prescribed 2026-09-30 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/ef5e136c-ff1e-0695-6804-cf31640a9491] MedicationRequest | prescribed 2026-09-30 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[Encounter/ef5e136c-ff1e-0695-08ba-2471a16a6570] Encounter | 2026-09-30 | Emergency room admission (procedure) | class EMER | at APPLE VALLEY CENTER
[Encounter/ef5e136c-ff1e-0695-aea4-11055569fd51] Encounter | 2026-09-23 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/ef5e136c-ff1e-0695-4a41-6fca58c80cb7] Encounter | 2026-09-16 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Immunization/ef5e136c-ff1e-0695-6beb-93901776b619] Immunization | 2026-05-13 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Condition/ef5e136c-ff1e-0695-08d2-be5484c6a000] Condition | onset 2023-03-22 | Unemployed (finding) | clinical status resolved | resolved 2023-09-13 | SNOMED 73438004
[Condition/ef5e136c-ff1e-0695-0659-7182eb1d6004] Condition | onset 2026-07-15 | Stress (finding) | clinical status resolved | resolved 2026-07-29 | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-e041-99b1020df098] Condition | onset 2026-06-03 | Stress (finding) | clinical status resolved | resolved 2026-07-01 | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-692f-015054b9f312] Condition | onset 2026-06-17 | Social isolation (finding) | clinical status resolved | resolved 2026-07-01 | SNOMED 422650009
[Condition/ef5e136c-ff1e-0695-4933-cd2f72fdccfd] Condition | onset 2026-02-25 | Social isolation (finding) | clinical status resolved | resolved 2026-05-20 | SNOMED 422650009
[Condition/ef5e136c-ff1e-0695-015a-38b99f76c99a] Condition | onset 2026-07-15 | Medication review due (situation) | clinical status resolved | resolved 2026-09-23 | SNOMED 314529007
[Condition/ef5e136c-ff1e-0695-75e1-26880e235e23] Condition | onset 2026-06-24 | Medication review due (situation) | clinical status resolved | resolved 2026-07-08 | SNOMED 314529007
[Condition/ef5e136c-ff1e-0695-2f1a-03ff86dc5f30] Condition | onset 2022-06-22 | Gingivitis (disorder) | clinical status resolved | resolved 2022-07-06 | SNOMED 66383009
[Condition/ef5e136c-ff1e-0695-dbf4-8f4d3ac1dc0d] Condition | onset 2021-04-28 | Gingivitis (disorder) | clinical status resolved | resolved 2021-05-12 | SNOMED 66383009
[Device/ef5e136c-ff1e-0695-a6bd-061655f25eb7] Device | Manual wheelchair (physical object) | status active | manufactured 2019-10-04 | SNOMED 228869008
```

</details>

label: s
note: Anemia, gingivitis (2023-04-19) and chronic sinusitis cards are all active. Every other active disorder in the record is a kidney or metabolic diagnosis already named in the previous sentence, so the list of 'other' disorders is complete.

## 48. `lay-a-sinus-infection:e56a8cde#0#1`

Question: Has the patient ever been diagnosed with a sinus infection? If so, when?

Answer: Yes, the patient has been diagnosed with viral sinusitis on two occasions. **The first episode had onset 2017-12-07 at a symptom encounter at DANA FARBER CANCER INSTITUTE and resolved 2018-01-02.** The second episode had onset 2020-03-01, was treated with amoxicillin 250 mg / clavulanate 125 mg oral tablet, and resolved 2020-03-18.

Cards this sentence cites:

- `[Condition/e56a8cde-8395-a37d-448b-343ff0888a14]` Condition | onset 2017-12-07 | Viral sinusitis (disorder) | clinical status resolved | resolved 2018-01-02 | SNOMED 444814009
- `[Encounter/e56a8cde-8395-a37d-7593-7148468dba47]` Encounter | 2017-12-07 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at DANA FARBER CANCER INSTITUTE
- `[DocumentReference/e9da819c-9abe-a548-8fa2-b345f1f0bd0f#1]` Clinical note | 2017-12-07 | part 1 of 1 | 2017-12-07 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 72 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), sprain (morphologic abnormality), medication review due (situation), full-time employment (finding), sprain of wrist (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; acetaminophen 325 mg oral tablet; simvastatin 10 mg oral tablet; acetaminophen 325 mg oral tablet [tylenol]; alendronic acid 10 mg oral tablet # Assessment and Plan Patient is presenting with viral sinusitis (disorder). ## Plan

<details><summary>Everything the model saw (56 cards)</summary>

```text
[Condition/e56a8cde-8395-a37d-f7ae-15d35f13e9f0] Condition | onset 2025-12-25 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/e56a8cde-8395-a37d-80d3-3984f14d8bb3] Condition | onset 2025-12-25 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/e56a8cde-8395-a37d-5c7c-75429c6f1e56] Condition | onset 2025-12-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/e56a8cde-8395-a37d-354e-df92238c35a7] Condition | onset 2025-12-25 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/e56a8cde-8395-a37d-6690-7ef5746552bd] Condition | onset 2017-11-09 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/e56a8cde-8395-a37d-922a-d32061194c0b] Condition | onset 2016-11-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/e56a8cde-8395-a37d-e775-23849ffbe97b] Condition | onset 2014-02-01 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/e56a8cde-8395-a37d-a82c-6129bc784139] Condition | onset 2014-02-01 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/e56a8cde-8395-a37d-64b8-86023f198a46] Condition | onset 2014-02-01 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/e56a8cde-8395-a37d-e547-8e085bacfa8e] Condition | onset 2007-09-13 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/e56a8cde-8395-a37d-37b4-500cf9e797e9] Condition | onset 2005-09-01 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/e56a8cde-8395-a37d-d5cb-6239a28a0055] Condition | onset 2003-12-16 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/e56a8cde-8395-a37d-4d5f-670d3e1632bc] Condition | onset 2003-12-16 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/e56a8cde-8395-a37d-1853-568436ee1ea2] Condition | onset 2001-08-20 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/e56a8cde-8395-a37d-810b-643d651149ba] Condition | onset 2001-08-18 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/e56a8cde-8395-a37d-2761-7d0bfc799087] Condition | onset 2001-08-09 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/e56a8cde-8395-a37d-ed31-c4144dbefb9e] Condition | onset 1996-05-17 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
[Condition/e56a8cde-8395-a37d-333f-0835bee4de98] Condition | onset 1991-06-13 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/e56a8cde-8395-a37d-30cd-5f4f9de67da3] Condition | onset 1967-07-27 | Lack of access to transportation (finding) | clinical status active | SNOMED 713458007
[Condition/e56a8cde-8395-a37d-ac70-0b466edf16a1] Condition | onset 1963-07-18 | Transport problem (finding) | clinical status active | SNOMED 266934004
[Condition/e56a8cde-8395-a37d-99e6-93fe1e3f6036] Condition | onset 1963-07-18 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/e56a8cde-8395-a37d-0c1b-7da0b396a0c4] MedicationRequest | prescribed 2026-01-01 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/e56a8cde-8395-a37d-f153-06ed5ef5b40a] MedicationRequest | prescribed 2025-12-25 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/e56a8cde-8395-a37d-b70b-d6ff9e66fb91] MedicationRequest | prescribed 2025-12-25 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/e56a8cde-8395-a37d-1cff-386c29158923] MedicationRequest | prescribed 2025-12-25 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/e56a8cde-8395-a37d-f778-f1044e9a8316] MedicationRequest | prescribed 2003-12-16 | atorvastatin 10 MG Oral Tablet | status active | RxNorm 617312
[MedicationRequest/e56a8cde-8395-a37d-e36e-ab680e0ad841] MedicationRequest | prescribed 2003-12-16 | hydrochlorothiazide 25 MG / lisinopril 20 MG Oral Tablet | status active | RxNorm 197887
[MedicationRequest/e56a8cde-8395-a37d-d237-6e376bbcb9a6] MedicationRequest | prescribed 2003-12-16 | metoprolol tartrate 25 MG Oral Tablet | status active | RxNorm 866924
[MedicationRequest/e56a8cde-8395-a37d-2fb4-edeac8b69b00] MedicationRequest | prescribed 2003-12-16 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/e56a8cde-8395-a37d-228f-f6135c165caa] MedicationRequest | prescribed 2003-12-16 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/e56a8cde-8395-a37d-eee1-8d05287f0e29] MedicationRequest | prescribed 2001-08-16 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/e56a8cde-8395-a37d-d36b-2e3fc9df975e] MedicationRequest | prescribed 2001-08-16 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/e56a8cde-8395-a37d-a8c0-f9ed9ed3ea83] MedicationRequest | prescribed 2001-08-16 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/e56a8cde-8395-a37d-321f-ecd1d25263ad] MedicationRequest | prescribed 2001-08-16 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/e56a8cde-8395-a37d-9456-c58ec0c7de32] MedicationRequest | prescribed 1949-01-17 | diphenhydrAMINE Hydrochloride 25 MG Oral Tablet | status active | RxNorm 1049630
[AllergyIntolerance/e56a8cde-8395-a37d-b318-8f34a7d6b5f7] AllergyIntolerance | recorded 1946-06-09 | Animal dander (substance) | allergy, category environment, criticality low | clinical status active | reactions: Eruption of skin (disorder); Rhinoconjunctivitis (disorder) | SNOMED 264287008
[AllergyIntolerance/e56a8cde-8395-a37d-a098-9831a40ac85b] AllergyIntolerance | recorded 1946-06-09 | Mold (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 84489001
[AllergyIntolerance/e56a8cde-8395-a37d-85d4-fe7519012219] AllergyIntolerance | recorded 1946-06-09 | House dust mite (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 260147004
[AllergyIntolerance/e56a8cde-8395-a37d-60c2-b75e4a4d4513] AllergyIntolerance | recorded 1946-06-09 | Tree pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 782576004
[AllergyIntolerance/e56a8cde-8395-a37d-5834-224d1127b6f9] AllergyIntolerance | recorded 1946-06-09 | Grass pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 256277009
[AllergyIntolerance/e56a8cde-8395-a37d-2daa-dbe0dbcf6ecf] AllergyIntolerance | recorded 1946-06-09 | Shellfish (substance) | allergy, category food, criticality low | clinical status active | reactions: Dyspnea (finding); Allergic angioedema (disorder); Itching (finding); Cough (finding); Diarrhea (finding) | SNOMED 735029006
[AllergyIntolerance/e56a8cde-8395-a37d-1508-bdb84bdc4c5d] AllergyIntolerance | recorded 1946-06-09 | Allergic disposition (finding) | allergy, category environment, criticality low | clinical status active | SNOMED 609328004
[Encounter/e56a8cde-8395-a37d-9f47-5b69723a8690] Encounter | 2026-01-01 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Encounter/e56a8cde-8395-a37d-2450-250d53d64dc7] Encounter | 2025-12-25 | General examination of patient (procedure) | class AMB | at SOUTH SHORE PRIMARY CARE PC
[Encounter/e56a8cde-8395-a37d-20eb-f707e34a4164] Encounter | 2024-12-20 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Immunization/e56a8cde-8395-a37d-7cd1-bb3bac5572f3] Immunization | 2025-12-25 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Condition/e56a8cde-8395-a37d-f660-3a080ceb9c43] Condition | onset 2020-03-01 | Viral sinusitis (disorder) | clinical status resolved | resolved 2020-03-18 | SNOMED 444814009
[Condition/e56a8cde-8395-a37d-448b-343ff0888a14] Condition | onset 2017-12-07 | Viral sinusitis (disorder) | clinical status resolved | resolved 2018-01-02 | SNOMED 444814009
[DocumentReference/53edf378-3bfc-fc8b-b070-0e0daf1e78f5#1] Clinical note | 2018-11-29 | part 1 of 1 | 2018-11-29 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 73 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), sprain (morphologic abnormality), medication review due (situation), full-time employment (finding), sprain of wrist (disorder), viral sinusitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; acetaminophen 325 mg oral tablet; simvastatin 10 mg oral tablet; acetaminophen 325 mg oral tablet [tylenol]; alendronic acid 10 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - extraction, erupted tooth or exposed root (elevation and/or forceps removal)
[Encounter/e56a8cde-8395-a37d-a174-6f2b8b9d9601] Encounter | 2020-03-01 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at DANA FARBER CANCER INSTITUTE
[DocumentReference/42753ae1-81eb-b0aa-5a3b-e0a9b39507dc#1] Clinical note | 2020-03-01 | part 1 of 1 | 2020-03-01 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 74 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), sprain (morphologic abnormality), medication review due (situation), unhealthy alcohol drinking behavior (finding), full-time employment (finding), sprain of wrist (disorder), viral sinusitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; acetaminophen 325 mg oral tablet; simvastatin 10 mg oral tablet; acetaminophen 325 mg oral tablet [tylenol]; alendronic acid 10 mg oral tablet # Assessment and Plan Patient is presenting with viral sinusitis (disorder). ## Plan The patient was prescribed the following medications: - amoxicillin 250 mg / clavulanate 125 mg oral tablet
[DocumentReference/e9da819c-9abe-a548-8fa2-b345f1f0bd0f#1] Clinical note | 2017-12-07 | part 1 of 1 | 2017-12-07 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 72 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), sprain (morphologic abnormality), medication review due (situation), full-time employment (finding), sprain of wrist (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; acetaminophen 325 mg oral tablet; simvastatin 10 mg oral tablet; acetaminophen 325 mg oral tablet [tylenol]; alendronic acid 10 mg oral tablet # Assessment and Plan Patient is presenting with viral sinusitis (disorder). ## Plan
[DocumentReference/a1179c6e-edc7-a264-ebd1-2d2d22f5e3f1#1] Clinical note | 2021-02-18 | part 1 of 1 | 2021-02-18 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 75 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), sprain (morphologic abnormality), medication review due (situation), unhealthy alcohol drinking behavior (finding), full-time employment (finding), sprain of wrist (disorder), viral sinusitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; acetaminophen 325 mg oral tablet; simvastatin 10 mg oral tablet; acetaminophen 325 mg oral tablet [tylenol]; alendronic acid 10 mg oral tablet; amoxicillin 250 mg / clavulanate 125 mg oral tablet # Assessment and Plan Patient is presenting with acute infective cystitis (disorder). ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 100 mcg/0.5ml dose or 50 mcg/0.25ml dose.
[DocumentReference/b3013519-3000-7f68-7b32-de706218460e#1] Clinical note | 2018-11-15 | part 1 of 2 | 2018-11-15 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 73 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), sprain (morphologic abnormality), medication review due (situation), full-time employment (finding), sprain of wrist (disorder), viral sinusitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; acetaminophen 325 mg oral tablet; simvastatin 10 mg oral tablet; acetaminophen 325 mg oral tablet [tylenol]; alendronic acid 10 mg oral tablet
[Encounter/e56a8cde-8395-a37d-7593-7148468dba47] Encounter | 2017-12-07 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at DANA FARBER CANCER INSTITUTE
[DocumentReference/54e6f2f3-53b3-4254-8474-3e83b705f0b8#1] Clinical note | 2019-11-21 | part 1 of 2 | 2019-11-21 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 74 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), sprain (morphologic abnormality), medication review due (situation), full-time employment (finding), sprain of wrist (disorder), viral sinusitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; acetaminophen 325 mg oral tablet; simvastatin 10 mg oral tablet; acetaminophen 325 mg oral tablet [tylenol]; alendronic acid 10 mg oral tablet
```

</details>

label: s
note: The viral sinusitis card has onset 2017-12-07 and resolved 2018-01-02. The same-day symptom encounter at DANA FARBER CANCER INSTITUTE has reason viral sinusitis. It is the earlier of the record's two sinusitis episodes (the other is 2020-03-01), so 'first' holds.

## 49. `lay-high-blood-pressure:e56a8cde#0#0`

Question: Has the patient ever been diagnosed with high blood pressure? If so, when?

Answer: **Yes, the patient has essential hypertension with onset 1991-06-13, and its clinical status is active.** A clinical note dated 1991-06-13 documents the patient presenting with essential hypertension. The patient was placed on a careplan of lifestyle education regarding hypertension. Lisinopril 10 MG Oral Tablet, prescribed 2025-12-25, is active with the reason listed as essential hypertension. The most recent blood pressure, on 2025-12-25, was Systolic 106 mm[Hg] and Diastolic 75 mm[Hg].

Cards this sentence cites:

- `[Condition/e56a8cde-8395-a37d-333f-0835bee4de98]` Condition | onset 1991-06-13 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000

<details><summary>Everything the model saw (56 cards)</summary>

```text
[Condition/e56a8cde-8395-a37d-f7ae-15d35f13e9f0] Condition | onset 2025-12-25 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/e56a8cde-8395-a37d-80d3-3984f14d8bb3] Condition | onset 2025-12-25 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/e56a8cde-8395-a37d-5c7c-75429c6f1e56] Condition | onset 2025-12-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/e56a8cde-8395-a37d-354e-df92238c35a7] Condition | onset 2025-12-25 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/e56a8cde-8395-a37d-6690-7ef5746552bd] Condition | onset 2017-11-09 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/e56a8cde-8395-a37d-922a-d32061194c0b] Condition | onset 2016-11-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/e56a8cde-8395-a37d-e775-23849ffbe97b] Condition | onset 2014-02-01 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/e56a8cde-8395-a37d-a82c-6129bc784139] Condition | onset 2014-02-01 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/e56a8cde-8395-a37d-64b8-86023f198a46] Condition | onset 2014-02-01 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/e56a8cde-8395-a37d-e547-8e085bacfa8e] Condition | onset 2007-09-13 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/e56a8cde-8395-a37d-37b4-500cf9e797e9] Condition | onset 2005-09-01 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/e56a8cde-8395-a37d-d5cb-6239a28a0055] Condition | onset 2003-12-16 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/e56a8cde-8395-a37d-4d5f-670d3e1632bc] Condition | onset 2003-12-16 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/e56a8cde-8395-a37d-1853-568436ee1ea2] Condition | onset 2001-08-20 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/e56a8cde-8395-a37d-810b-643d651149ba] Condition | onset 2001-08-18 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/e56a8cde-8395-a37d-2761-7d0bfc799087] Condition | onset 2001-08-09 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/e56a8cde-8395-a37d-ed31-c4144dbefb9e] Condition | onset 1996-05-17 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
[Condition/e56a8cde-8395-a37d-333f-0835bee4de98] Condition | onset 1991-06-13 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/e56a8cde-8395-a37d-30cd-5f4f9de67da3] Condition | onset 1967-07-27 | Lack of access to transportation (finding) | clinical status active | SNOMED 713458007
[Condition/e56a8cde-8395-a37d-ac70-0b466edf16a1] Condition | onset 1963-07-18 | Transport problem (finding) | clinical status active | SNOMED 266934004
[Condition/e56a8cde-8395-a37d-99e6-93fe1e3f6036] Condition | onset 1963-07-18 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/e56a8cde-8395-a37d-0c1b-7da0b396a0c4] MedicationRequest | prescribed 2026-01-01 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/e56a8cde-8395-a37d-f153-06ed5ef5b40a] MedicationRequest | prescribed 2025-12-25 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/e56a8cde-8395-a37d-b70b-d6ff9e66fb91] MedicationRequest | prescribed 2025-12-25 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/e56a8cde-8395-a37d-1cff-386c29158923] MedicationRequest | prescribed 2025-12-25 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/e56a8cde-8395-a37d-f778-f1044e9a8316] MedicationRequest | prescribed 2003-12-16 | atorvastatin 10 MG Oral Tablet | status active | RxNorm 617312
[MedicationRequest/e56a8cde-8395-a37d-e36e-ab680e0ad841] MedicationRequest | prescribed 2003-12-16 | hydrochlorothiazide 25 MG / lisinopril 20 MG Oral Tablet | status active | RxNorm 197887
[MedicationRequest/e56a8cde-8395-a37d-d237-6e376bbcb9a6] MedicationRequest | prescribed 2003-12-16 | metoprolol tartrate 25 MG Oral Tablet | status active | RxNorm 866924
[MedicationRequest/e56a8cde-8395-a37d-2fb4-edeac8b69b00] MedicationRequest | prescribed 2003-12-16 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/e56a8cde-8395-a37d-228f-f6135c165caa] MedicationRequest | prescribed 2003-12-16 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/e56a8cde-8395-a37d-eee1-8d05287f0e29] MedicationRequest | prescribed 2001-08-16 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/e56a8cde-8395-a37d-d36b-2e3fc9df975e] MedicationRequest | prescribed 2001-08-16 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/e56a8cde-8395-a37d-a8c0-f9ed9ed3ea83] MedicationRequest | prescribed 2001-08-16 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/e56a8cde-8395-a37d-321f-ecd1d25263ad] MedicationRequest | prescribed 2001-08-16 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/e56a8cde-8395-a37d-9456-c58ec0c7de32] MedicationRequest | prescribed 1949-01-17 | diphenhydrAMINE Hydrochloride 25 MG Oral Tablet | status active | RxNorm 1049630
[AllergyIntolerance/e56a8cde-8395-a37d-b318-8f34a7d6b5f7] AllergyIntolerance | recorded 1946-06-09 | Animal dander (substance) | allergy, category environment, criticality low | clinical status active | reactions: Eruption of skin (disorder); Rhinoconjunctivitis (disorder) | SNOMED 264287008
[AllergyIntolerance/e56a8cde-8395-a37d-a098-9831a40ac85b] AllergyIntolerance | recorded 1946-06-09 | Mold (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 84489001
[AllergyIntolerance/e56a8cde-8395-a37d-85d4-fe7519012219] AllergyIntolerance | recorded 1946-06-09 | House dust mite (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 260147004
[AllergyIntolerance/e56a8cde-8395-a37d-60c2-b75e4a4d4513] AllergyIntolerance | recorded 1946-06-09 | Tree pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 782576004
[AllergyIntolerance/e56a8cde-8395-a37d-5834-224d1127b6f9] AllergyIntolerance | recorded 1946-06-09 | Grass pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 256277009
[AllergyIntolerance/e56a8cde-8395-a37d-2daa-dbe0dbcf6ecf] AllergyIntolerance | recorded 1946-06-09 | Shellfish (substance) | allergy, category food, criticality low | clinical status active | reactions: Dyspnea (finding); Allergic angioedema (disorder); Itching (finding); Cough (finding); Diarrhea (finding) | SNOMED 735029006
[AllergyIntolerance/e56a8cde-8395-a37d-1508-bdb84bdc4c5d] AllergyIntolerance | recorded 1946-06-09 | Allergic disposition (finding) | allergy, category environment, criticality low | clinical status active | SNOMED 609328004
[Encounter/e56a8cde-8395-a37d-9f47-5b69723a8690] Encounter | 2026-01-01 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Encounter/e56a8cde-8395-a37d-2450-250d53d64dc7] Encounter | 2025-12-25 | General examination of patient (procedure) | class AMB | at SOUTH SHORE PRIMARY CARE PC
[Encounter/e56a8cde-8395-a37d-20eb-f707e34a4164] Encounter | 2024-12-20 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Immunization/e56a8cde-8395-a37d-7cd1-bb3bac5572f3] Immunization | 2025-12-25 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/e56a8cde-8395-a37d-cd94-ac1e06ff3aac] Observation (vital-signs) | 2021-12-02 | Blood pressure panel with all children optional = Diastolic Blood Pressure 73 mm[Hg]; Systolic Blood Pressure 116 mm[Hg] | status final | LOINC 85354-9
[Observation/e56a8cde-8395-a37d-c7f1-f8947e6d7810] Observation (vital-signs) | 2025-12-25 | Blood pressure panel with all children optional = Diastolic Blood Pressure 75 mm[Hg]; Systolic Blood Pressure 106 mm[Hg] | status final | LOINC 85354-9
[Observation/e56a8cde-8395-a37d-9a08-8f6c538f4d3d] Observation (vital-signs) | 2024-12-19 | Blood pressure panel with all children optional = Diastolic Blood Pressure 74 mm[Hg]; Systolic Blood Pressure 108 mm[Hg] | status final | LOINC 85354-9
[Observation/e56a8cde-8395-a37d-17dd-076107990533] Observation (vital-signs) | 2023-12-14 | Blood pressure panel with all children optional = Diastolic Blood Pressure 71 mm[Hg]; Systolic Blood Pressure 112 mm[Hg] | status final | LOINC 85354-9
[DocumentReference/7504f1c0-58e2-6285-f81f-87337a5ecce1#1] Clinical note | 1991-06-13 | part 1 of 1 | 1991-06-13 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 46 year-old nonhispanic white male. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicaid. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with essential hypertension (disorder). ## Plan The patient was placed on a careplan: - lifestyle education regarding hypertension (procedure)
[Condition/e56a8cde-8395-a37d-1815-01a34059f1ca] Condition | onset 2022-12-08 | Stress (finding) | clinical status resolved | resolved 2023-12-14 | SNOMED 73595000
[Condition/e56a8cde-8395-a37d-8f9a-508090a4ffda] Condition | onset 2017-11-09 | Stress (finding) | clinical status resolved | resolved 2018-11-15 | SNOMED 73595000
[DiagnosticReport/e56a8cde-8395-a37d-3f4f-0347df4d9217] DiagnosticReport | 2021-12-02 | CBC panel - Blood by Automated count | results: Leukocytes [#/volume] in Blood by Automated count 4.7251 10*3/uL; Erythrocytes [#/volume] in Blood by Automated count 5.3883 10*6/uL; Hemoglobin [Mass/volume] in Blood 12.046 g/dL; Hematocrit [Volume Fraction] of Blood by Automated count 39.229 %; MCV [Entitic mean volume] in Red Blood Cells by Automated count 80.875 fL; MCH [Entitic mass] by Automated count 32.2 pg; MCHC [Entitic Mass/volume] in Red Blood Cells by Automated count 33.52 g/dL; Erythrocyte [DistWidth] in Blood by Automated count 43.265 fL; Platelets [#/volume] in Blood by Automated count 379.77 10*3/uL; Platelet distribution width [Entitic volume] in Blood by Automated count 472.58 fL; Platelet [Entitic mean volume] in Blood by Automated count 11.132 fL | LOINC 58410-2
[DiagnosticReport/e56a8cde-8395-a37d-4ba2-972e3d1ff301] DiagnosticReport | 2016-11-03 | CBC panel - Blood by Automated count | results: Leukocytes [#/volume] in Blood by Automated count 4.7152 10*3/uL; Erythrocytes [#/volume] in Blood by Automated count 5.4279 10*6/uL; Hemoglobin [Mass/volume] in Blood 17.444 g/dL; Hematocrit [Volume Fraction] of Blood by Automated count 35.356 %; MCV [Entitic mean volume] in Red Blood Cells by Automated count 81.833 fL; MCH [Entitic mass] by Automated count 28.393 pg; MCHC [Entitic Mass/volume] in Red Blood Cells by Automated count 33.537 g/dL; Erythrocyte [DistWidth] in Blood by Automated count 44.311 fL; Platelets [#/volume] in Blood by Automated count 156.23 10*3/uL; Platelet distribution width [Entitic volume] in Blood by Automated count 311.85 fL; Platelet [Entitic mean volume] in Blood by Automated count 9.4606 fL | LOINC 58410-2
[Condition/e56a8cde-8395-a37d-e08a-eebe5956bc62] Condition | onset 2007-09-13 | Medication review due (situation) | clinical status resolved | resolved 2018-11-15 | SNOMED 314529007
```

</details>

label: s
note: The cited Condition card shows essential hypertension, onset 1991-06-13, clinical status active.

## 50. `current-meds:3ab4eeae#0#0`

Question: What medications is the patient currently prescribed?

Answer: **The patient's active prescriptions, all prescribed 2023-11-04, are 24 HR metoprolol succinate 25 MG Extended Release Oral Tablet, prasugrel 10 MG Oral Tablet, ezetimibe 10 MG / simvastatin 20 MG Oral Tablet, aspirin 81 MG Oral Tablet, and valsartan 160 MG Oral Tablet.**

Cards this sentence cites:

- `[MedicationRequest/3ab4eeae-f5cd-e604-f51c-a09297670cbb]` MedicationRequest | prescribed 2023-11-04 | 24 HR metoprolol succinate 25 MG Extended Release Oral Tablet | status active | RxNorm 866427
- `[MedicationRequest/3ab4eeae-f5cd-e604-7682-8d945b9c6ac0]` MedicationRequest | prescribed 2023-11-04 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
- `[MedicationRequest/3ab4eeae-f5cd-e604-6d5d-e301c1432339]` MedicationRequest | prescribed 2023-11-04 | ezetimibe 10 MG / simvastatin 20 MG Oral Tablet | status active | RxNorm 476349
- `[MedicationRequest/3ab4eeae-f5cd-e604-38be-3e404ac22c76]` MedicationRequest | prescribed 2023-11-04 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
- `[MedicationRequest/3ab4eeae-f5cd-e604-255b-436f33da6d88]` MedicationRequest | prescribed 2023-11-04 | valsartan 160 MG Oral Tablet | status active | RxNorm 349201

<details><summary>Everything the model saw (35 cards)</summary>

```text
[Condition/3ab4eeae-f5cd-e604-7094-18aeb6eeb508] Condition | onset 2025-10-22 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/3ab4eeae-f5cd-e604-7e58-38c37ebb189c] Condition | onset 2023-11-04 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/3ab4eeae-f5cd-e604-0ae7-81d0657d905f] Condition | onset 2023-11-04 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/3ab4eeae-f5cd-e604-65c2-1ca7d1082fc0] Condition | onset 2023-10-11 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/3ab4eeae-f5cd-e604-59b6-1ca110c880ca] Condition | onset 2023-10-11 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/3ab4eeae-f5cd-e604-5f9d-d583345bfe9c] Condition | onset 2022-10-05 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/3ab4eeae-f5cd-e604-b46f-a9d976941725] Condition | onset 2000-07-25 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/3ab4eeae-f5cd-e604-94f9-fed37e65d36d] Condition | onset 1994-06-15 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/3ab4eeae-f5cd-e604-5875-2449d8ccb675] Condition | onset 1991-01-31 | Impacted molars (disorder) | clinical status active | SNOMED 196416002
[Condition/3ab4eeae-f5cd-e604-2991-ef6fdcd56f57] Condition | onset 1990-12-25 | Chronic intractable migraine without aura (disorder) | clinical status active | SNOMED 124171000119105
[Condition/3ab4eeae-f5cd-e604-caad-28bccbbd0084] Condition | onset 1990-03-04 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/3ab4eeae-f5cd-e604-1a00-e509439f1432] Condition | onset 1990-02-28 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/3ab4eeae-f5cd-e604-d496-97e5f86853bb] Condition | onset 1988-08-24 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/3ab4eeae-f5cd-e604-ee66-1e23e18aed73] Condition | onset 1986-01-16 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/3ab4eeae-f5cd-e604-014e-3e684daf5feb] Condition | onset 1976-08-11 | Lack of access to transportation (finding) | clinical status active | SNOMED 713458007
[Condition/3ab4eeae-f5cd-e604-4cf1-bd79da7c4690] Condition | onset 1972-08-02 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[Condition/3ab4eeae-f5cd-e604-06de-0b7cfd57e8f2] Condition | onset 1972-08-02 | Transport problem (finding) | clinical status active | SNOMED 266934004
[MedicationRequest/3ab4eeae-f5cd-e604-f51c-a09297670cbb] MedicationRequest | prescribed 2023-11-04 | 24 HR metoprolol succinate 25 MG Extended Release Oral Tablet | status active | RxNorm 866427
[MedicationRequest/3ab4eeae-f5cd-e604-7682-8d945b9c6ac0] MedicationRequest | prescribed 2023-11-04 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/3ab4eeae-f5cd-e604-6d5d-e301c1432339] MedicationRequest | prescribed 2023-11-04 | ezetimibe 10 MG / simvastatin 20 MG Oral Tablet | status active | RxNorm 476349
[MedicationRequest/3ab4eeae-f5cd-e604-38be-3e404ac22c76] MedicationRequest | prescribed 2023-11-04 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/3ab4eeae-f5cd-e604-255b-436f33da6d88] MedicationRequest | prescribed 2023-11-04 | valsartan 160 MG Oral Tablet | status active | RxNorm 349201
[Encounter/3ab4eeae-f5cd-e604-2d40-f0532e1c8497] Encounter | 2026-02-17 | Encounter for problem (procedure) | class AMB | reason: Dependent drug abuse (disorder) | at TUFTS MEDICAL CENTER, INC
[Encounter/3ab4eeae-f5cd-e604-1043-95240162a32a] Encounter | 2026-01-18 | Encounter for problem (procedure) | class AMB | reason: Dependent drug abuse (disorder) | at TUFTS MEDICAL CENTER, INC
[Encounter/3ab4eeae-f5cd-e604-65a4-9d7267e25c97] Encounter | 2025-12-19 | Encounter for problem (procedure) | class AMB | reason: Dependent drug abuse (disorder) | at TUFTS MEDICAL CENTER, INC
[MedicationRequest/3ab4eeae-f5cd-e604-155d-0ad6f41697a1] MedicationRequest | prescribed 2023-11-04 | status completed
[MedicationRequest/3ab4eeae-f5cd-e604-2af2-0511bae54e0b] MedicationRequest | prescribed 2023-11-04 | status completed
[MedicationRequest/3ab4eeae-f5cd-e604-8f9d-ad7bf11733be] MedicationRequest | prescribed 2023-11-04 | status completed
[MedicationRequest/3ab4eeae-f5cd-e604-9e77-463fed159608] MedicationRequest | prescribed 2023-11-04 | status completed
[MedicationRequest/3ab4eeae-f5cd-e604-ce68-06dbfa74f4da] MedicationRequest | prescribed 2023-11-04 | status completed
[MedicationRequest/3ab4eeae-f5cd-e604-cd00-ebbb5618890c] MedicationRequest | prescribed 2025-04-04 | Acetaminophen 325 MG Oral Tablet | status completed | RxNorm 313782
[MedicationRequest/3ab4eeae-f5cd-e604-aa68-64fa11ab5566] MedicationRequest | prescribed 2025-05-30 | Acetaminophen 325 MG Oral Tablet | status completed | reason: Acute bronchitis (disorder) | RxNorm 313782
[DocumentReference/1f4a4f20-dc03-f400-97f3-b14afd4a373f#2] Clinical note | 2025-04-04 | part 2 of 2 | # Assessment and Plan Patient is presenting with sprain (morphologic abnormality), sprain of ankle (disorder). ## Plan The patient was prescribed the following medications: - acetaminophen 325 mg oral tablet The patient was placed on a careplan: - physiotherapy care plan (record artifact)
[DocumentReference/4699b8e8-7b24-6b05-0aed-fb7501a35c58#1] Clinical note | 2013-05-12 | part 1 of 1 | 2013-05-12 # Chief Complaint No complaints. # History of Present Illness Nelia669 is a 58 year-old nonhispanic white female. Patient has a history of dental caries on smooth surface penetrating into dentin, periodontal disease, social isolation (finding). # Social History Patient is single. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a low socioeconomic background. Patient did not finish high school. Patient currently has Medicaid. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with rheumatoid arthritis (disorder). ## Plan The patient was prescribed the following medications: - naproxen 500 mg oral tablet - methotrexate 2.5 mg oral tablet The patient was placed on a careplan: - musculoskeletal care (regime/therapy)
[MedicationRequest/3ab4eeae-f5cd-e604-6a8a-c29cc4405ef1] MedicationRequest | prescribed 2013-05-12 | Methotrexate 2.5 MG Oral Tablet | status completed | reason: Rheumatoid arthritis (disorder) | RxNorm 105585
```

</details>

label: s
note: All five cited cards are status active and dated 2023-11-04, with names and doses matching. These are the only active MedicationRequests in the record, so 'all' and the full list hold.

