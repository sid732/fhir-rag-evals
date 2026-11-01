# Evals

How the evaluation harness works, what each number means, and what hasn't been measured yet.

## The question set

`evals/questions/questions.jsonl` holds 275 questions over the 15 patients, built by `make questions`. Each question has a patient, a category, gold evidence, optional key facts, a source, and a split.

| Category | Dev | Test | Examples |
|---|---:|---:|---|
| fact_lookup | 34 | 23 | current medications, active diagnoses, allergies, smoking status, vaccines in the last year |
| values_dates | 60 | 40 | latest lab result and date, latest blood pressure, latest lipid panel, last flu shot, last visit, last colonoscopy |
| lay_terms | 18 | 12 | "Has the patient ever been diagnosed with high blood pressure?" |
| multi_step | 31 | 19 | medications prescribed for a condition, HbA1c trend over three results, reason for the last ER visit |
| not_in_record | 23 | 15 | labs never measured, conditions never diagnosed, tests Synthea never generates (blood type, HIV viral load), colonoscopy never done |

**Gold labels are computed from the raw bundles** by `src/fhir_rag/evals/templates.py`, which parses FHIR with plain dict access and shares nothing with the service except the bundle loader. A parsing bug in the service's views or cards can't hide in the labels too. `build_questions` checks that every gold ref exists in that patient's record and that every "not in record" question has no gold.

**Gold evidence is a list of groups.** Each group holds interchangeable refs: retrieving or citing any one of them counts for the group. "Latest HbA1c" has one group with one ref, the newest result. "What was prescribed for hypertension?" has one group per drug, holding every prescription of that drug for that reason. Recall counts groups, not refs.

**The split** was fixed before any tuning: the first build sent 60% of each category to dev by ranking hashes of the question ids. After that a question keeps its split, and a new question goes to dev when its id's hash falls in the first 60% of the hash range, so adding questions never moves others. (Ranking did move them: when the label fixes below added two questions, one dev question would have gone to test. That's how the bug was found, and `build_questions` now reads the existing splits before assigning new ones.) Design decisions were made on dev; test was scored after.

**Hand-written questions** go in `evals/questions/drafted.jsonl` (same format, `source: "human"`), and `make questions` merges them in. None exist yet.

## Retrieval metrics

`make eval-retrieval` (no API key, deterministic). For answerable questions:

- **hit@k**: some gold group has a member in the context.
- **recall@k**: share of gold groups with a member in the context.
- **MRR@k**: 1 / rank of the first gold card among the *ranked* cards. The pinned summary isn't ranked, so it's left out of MRR.
- **Leaked cards**: retrieved cards that belong to another patient. Checked on every question; CI fails on any.

"Context" is everything the model would see: the pinned summary (when on) plus the first k ranked cards. Summary cards don't count against k, so the report also gives the average context size and a no-summary configuration at the same budget.

Intervals are 95% cluster-bootstrap CIs that resample patients rather than questions, because questions about one patient are correlated.

## Answer metrics

`make eval-answers` runs the real pipeline. For answered, answerable cases:

- **Citation validity**: share of the model's citations that name a card it was shown. Measured before invalid citations are removed. Undefined, and left out, when an answer cites nothing.
- **Citation precision and recall**: overlap of the valid citations with the gold groups. Precision undercounts when the model cites a relevant card that isn't gold, such as an older result in a trend answer; the judge covers that case.
- **Numbers and dates in cited cards**: of the sentences that state a number or date, the share whose numbers and dates all appear in the cards that sentence cites. Deterministic and free, and aimed at the most harmful error: a wrong value or date.
- **Key facts present**: for questions with key facts (values and dates), the share that appear in the answer. Numbers compare as numbers, so 6.80 matches 6.8.
- **Faithfulness**: share of sentences the judge (claude-sonnet-5-5) marks fully supported. Facts about specific entries (values, dates, statuses) must be in the cards the sentence cites. Claims about the record as a whole ("most recent", "only", counts, "no record of") are checked against the whole context the model saw, because no single card can show that nothing later exists. Partial support is reported separately.
- **Gold evidence in context**: whether retrieval gave the model what it needed. It separates retrieval misses from generation misses.

For every case: a confusion matrix of answered vs "not in record" against answerable vs not, with precision and recall for "not in record". Cost comes from recorded usage and list prices (`src/fhir_rag/llm/pricing.py`); latency is reported at p50 and p95.

## Harness checks

- `make eval-selftest` runs **oracle** answers (built from the gold labels) and **null** answers ("I don't know", no citations) through the whole pipeline. On dev, the oracle gets key facts 1.000, precision 0.951 and recall 0.951 (the same as the context recall, its true ceiling), and abstains correctly on every "not in record" question. Null gets 0 on precision, recall and key facts, and never abstains. Two bugs were caught this way and fixed: precision and recall were counting citations that had already been removed, and two metrics passed empty answers vacuously.
- Failed attempts (timeouts, API errors, refusals, unparseable output) go to `errors.jsonl` with a failure class and are never scored as wrong answers. Every case is written as it finishes, and an interrupted run resumes.
- The model that served each answer is recorded. If a refusal fallback answered instead of the requested model, the row is flagged.
- Each report records the commit, cohort hash, card version, models, effort and retrieval settings.

## Judge calibration

The faithfulness number means little until the judge is checked against independent labels:

```bash
uv run python -m fhir_rag.evals.calibrate sample --run <run-name> --n 50 [--set NAME]
# write s, p or n on every `label:` line of evals/labels/NAME.md
uv run python -m fhir_rag.evals.calibrate score [--set NAME] [--run <run-name>]
```

`sample` writes a sheet with each sentence inside its whole answer, the cards it cites, and everything the model saw, and keeps the judge's verdicts in `NAME.verdicts.jsonl` so labeling is blind. The judge flags few sentences, so a random sample would hold almost none: up to half the sample is flagged sentences, the rest are drawn from those the judge passed, and each carries a weight that maps its stratum back to the run. Sentences already in another set are skipped, so a new set is held out from the old ones. A `?` after a label marks a case the labeler finds unclear.

`score` prints agreement on the sample and on clear cases, agreement and the share of supported sentences weighted back to the run (by the labels and by the judge), Cohen's kappa, and a confusion table. `--run` scores another run's verdicts on the same labels, which is how a revised judge is compared with the old one; the weights still hold, because they come from how the set was drawn. The target is at least 90% agreement on clear cases. `make eval-rejudge FROM=<run> RUN=<new-run>` re-grades a finished run's answers with the current judge, so a prompt change costs only judge calls (about $2 for dev).

## Judge v1 and v2

The first full dev run ([report](../evals/reports/answers-dev-1.md)) used judge v1, which saw only the cards each sentence cited. It scored faithfulness 0.635 while every deterministic check was near perfect. Of the 85 sentences it didn't mark supported, 74 were flagged only for a claim about the whole record, such as "the most recent reading was ..." with one reading cited. v1 couldn't check those claims, because the evidence for "most recent" is the absence of anything later. Key facts were 1.000 against gold computed from the raw bundles, so those claims were right.

Judge v2 (`prompts/judge_v2.txt`) checks such claims against the whole context, and it also judges sentences that cite nothing (one answer said, correctly, that no low red cell count diagnosis was recorded). The same 290 sentences, re-judged ([report](../evals/reports/answers-dev-1-judge2.md)):

| v1 verdict | v2: supported | v2: partially supported |
|---|---:|---:|
| supported | 201 | 4 |
| partially supported | 80 | 4 |
| not supported | 1 | 0 |

Faithfulness went from 0.635 to 0.976 [0.960, 0.991], for $1.97 of judge calls ($0.014 per answer; v2 reads about 6,200 input tokens, v1 about 1,400). Whether v2 was right is the next section.

## Checking the judge against blind reference labels

Two label sets, 50 sentences each, were labeled on 2026-10-30 by Claude Opus 5.5, a stronger model than the judge, in batches of 10 sentences. Each batch saw the rubric and its own items, never a judge's verdicts, and gave a reason for every label. Every factual claim in a reason that decided a disagreement was checked against the cards, and all of them held.

- **Set 1** ([sheet](../evals/labels/judge_calibration.md)): v2's 8 flags plus 42 of its 282 passes, weighted to all 290 sentences.
- **Set 2** ([sheet](../evals/labels/judge_calibration_2.md)): drawn after v3 existed, from the 240 sentences not in set 1: v3's one flag there plus 49 of its passes. v3 was written after reading set 1, so set 2 is the held-out check.

| Judge | Set 1, clear cases | Set 1, weighted | Set 2, clear cases | Set 2, weighted | Sentences supported, set 1 / set 2 |
|---|---:|---:|---:|---:|---:|
| Labels | | | | | 0.970 / 0.980 |
| v1 | 0.659 | 0.669 | 0.688 | 0.675 | 0.685 / 0.695 |
| v2 | 0.909 | 0.956 | 1.000 | 0.980 | 0.972 / 1.000 |
| v3 | 1.000 | 0.977 | 0.979 | 0.976 | 0.993 / 0.996 |

"Clear cases" is agreement on the sample, leaving out the items labelers marked unclear (6 in set 1, 2 in set 2). "Weighted" is agreement estimated for the whole run. The last column is the share of sentences supported, per sentence; the reports' faithfulness is a mean over answers.

**What v2 got wrong.** Its passes held up (41 of 42 in set 1), its flags didn't. The labels confirm 2 of its 8 flags: a prescription tied to a visit only by a matching date, and a "stated reason" that comes from cards the sentence doesn't cite. A third ("at that visit" for a same-day flu shot) could go either way. The other five are judge errors: a list the next sentence completes, a reason that calls the sentence supported, a "most recent" date that is the latest one shown, an "only medication" that is the only one with that reason, and a "prior panel" that is the one before. Two of the five came from guessing about entries it wasn't shown. Cohen's kappa on set 1 is 0.30.

**Judge v3** (`prompts/judge_v3.txt`, [report](../evals/reports/answers-dev-1-judge3.md)) reads each sentence as part of the whole answer, repeats that only the excerpts count, says entries can appear in clinical notes, and writes its reason before its verdict, so the verdict comes after the reasoning instead of before it. On set 1 it fixed all five errors, kept both correct flags, and passed "at that visit"; kappa 0.79. Re-judging cost $2.07, and faithfulness is 0.993 [0.985, 1.000].

**On held-out data v3 is no better than v2.** Both pass nearly everything in set 2. v3's one flag there ("metformin has been prescribed since 2021-11-21") is wrong by the labels. So v3's gain is shown only on the set it was designed from; the fresh set says it is no worse, not that it is better. Set 2 has too few flags for kappa to mean anything.

**Blind spot.** Both v2 and v3 missed 2 of 2 omissions: answers that listed past entries and skipped ones that appear only in clinical notes (a flu shot in a 2018 note; four Humulin prescriptions in notes). The answers share the weakness, and the judge reports about two points too high because of it: 0.993 to 0.996 of sentences supported by v3, 0.970 to 0.980 by the labels. A faithfulness of about 0.97 to 0.98 is the better headline.

## The test split

The first run on the test questions ([test-1](../evals/reports/answers-test-1.md), 2026-10-31) used the same models, prompts, retrieval settings and judge v3 as dev, through the CLI backend described below. All 110 cases were graded; none failed. Reading every miss against the raw bundles turned up four wrong labels. The fixes went into the templates, so they apply to every patient in both splits, not just to those four questions:

- `last_er_visit` took the latest emergency encounter *that has a reasonCode*, so when the latest one had no reason, gold pointed at an older visit. That was true for 3 of the 5 test patients with the question and none of the 7 dev patients. In all three the model named the true latest visit and said it had no recorded reason, and twice it also gave the older visit and its reason. Gold is now the latest emergency encounter, and two dev patients whose emergency visits all lack a reason now get the question too.
- `missing_lab` and `latest_labs` looked under one LOINC code per lab, but Synthea records glucose, creatinine, potassium and sodium under a whole-blood code and a serum-or-plasma code. One patient was asked for "potassium" as an unanswerable question while the record has it under 2823-3 rather than 6298-4, and the model reported that result. Both templates now look under every code (`SAME_LAB`). The potassium question is gone, and one dev glucose question's gold group gained the same-day serum result.

The second run ([test-2](../evals/reports/answers-test-2.md)) keeps test-1's answers for the 106 test questions whose labels didn't change, and asked the three ER questions again; all three were answered correctly again.

| Metric | Dev (API) | Test-1, old labels | Test-2 |
|---|---:|---:|---:|
| "Not in record" precision / recall | 0.958 / 1.000 | 0.938 / 0.938 | 0.938 / 1.000 |
| Citation recall | 0.957 | 0.914 | 0.925 |
| Gold evidence in context | 0.957 | 0.914 | 0.925 |
| Numbers and dates in cited cards | 0.979 | 0.968 | 0.968 |
| Key facts present | 1.000 | 0.984 | 1.000 |
| Faithfulness, judge v3 | 0.993 | 0.986 | 0.986 |

What's left on test:

- **One retrieval miss.** The latest lipid panel of one patient wasn't in the context, and the model said it found notes mentioning a lipid panel but no values. That's the one answerable question it declined.
- **One wrong comparison, caught by the judge.** An answer called a lipid panel's values higher than the next day's when HDL was lower.
- **One judge flag on conflicting record data.** "The only active prescription is ferrous sulfate" matches the medication statuses, but a 2025 note still lists norethindrone and an IUD among current medications, and the judge marked the sentence partially supported.
- **Numbers and dates.** Three of the four sentences flagged state the record's as-of date (2026-10-01), which is in the prompt but in no card; the fourth gives a date in a sentence that cites nothing.
- **Smoking status** accounts for most of the lower citation recall in `fact_lookup`, as on dev: answers cite the notes that say "never smoked", while gold is the structured smoking-status Observation, which retrieval misses (BM25 has no stemming).

Labels were fixed after test had been scored, so test-1 is kept as it was scored, and the table shows both. Test also differs from dev in two ways at once, the questions and the backend, so the small drops can't be put down to either one. Cost per question was $0.050 at list price (nothing was billed), against $0.040 on dev, from the CLI's extra input and output tokens, and latency was higher for the reasons below.

## Running on a Claude subscription

`FHIR_RAG_LLM_BACKEND=cli` sends every generator and judge call through the Claude Code CLI (`claude -p`) on a logged-in Claude subscription instead of the API, so a run uses the plan's limits instead of API credits. `FHIR_RAG_CLAUDE_CONFIG_DIR` picks the login. `ClaudeCodeLLM` (`llm/client.py`) replaces Claude Code's system prompt with ours, turns off tools, settings files (hooks, plugins, CLAUDE.md), MCP servers and prompt caching, runs in an empty directory, and removes `ANTHROPIC_API_KEY` from the CLI's environment so a call can't bill the API.

It is close to the API path, not the same:

- Claude Code still adds a line before the system prompt, an environment block with today's date, and an account reminder. With the tool it uses for structured output, that's about 1,000 extra input tokens per call. The prompts give the record's as-of date, which is what "most recent" and "last year" are judged against.
- Structured output takes an extra model turn, so model calls are slower: 8.0 s and 16.2 s through the CLI against 4.3 s and 4.4 s through the API, on the same two dev questions.
- There is no refusal fallback; Claude Code retries rate limits and server errors itself.

On those two questions the CLI answers stated the same values and dates as the API answers, and the judge (also through the CLI) marked every sentence supported. A CLI run's cost is the list price of its tokens, though nothing is billed, and its latency isn't the API's. In the README, dev's cost and latency come from an API run and test's from the CLI.

## Not measured yet

- Judge agreement with clinician labels.
- Run-to-run noise: three repetitions of the dev answer eval (`--reps 3`). The answer-eval CI gate waits on this number.
- Whether a whole run through the CLI backend scores the same as one through the API.
