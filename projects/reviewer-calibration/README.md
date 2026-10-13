# Reviewer Calibration & Self-Correction

## Goal

Show how I review my own earlier annotations, catch drift, and record corrections in a way that another reviewer could audit. Calibration is the part of annotation work that is easy to skip and expensive to skip.

**Data note:** The cases below are synthetic and were written for this portfolio. They are not a record of a real client project or a real quality review cycle.

## Why this project exists

Anyone can produce a clean final label. The more useful skill is noticing when an earlier label was wrong, understanding why, and writing the correction down so the same mistake does not recur. This project demonstrates that habit.

## Calibration workflow

1. Re-read a batch of earlier judgements after a gap of at least a day.
2. Score each one again without looking at the original label.
3. Compare the two scores.
4. For any disagreement, write down which score is right and why.
5. If the disagreement comes from an unclear guideline, propose a guideline change instead of just fixing the single record.

## Case 1: Over-flagging ambiguity

**Task:** Text annotation.
**Original label:** `needs_context=true` with note "the reference is unclear."

**Text:** "Send it over when you get a chance."

**Why the original label was wrong:** The sentence is informal, but it is not ambiguous in the way the schema means. The action ("send it over") is clear. Only the referent of "it" is missing, and for a single-turn annotation task that is normal, not a flag. The `needs_context` label is meant for cases where the *intent* cannot be judged, not where a pronoun lacks a referent.

**Corrected label:** `needs_context=false`, intent `request`, tone `neutral`.

**Lesson:** The schema needs a separate field for "unresolved referent," or the `needs_context` definition needs to say explicitly that unresolved pronouns alone do not qualify. I noted this as a guideline change rather than a one-off fix.

## Case 2: Drift toward the stricter score

**Task:** LLM response evaluation.
**Original decision:** Response B wins on a prompt asking for a simple explanation.

**Why the original decision was wrong:** On a second read, Response A and Response B were both correct and both simple. The reason I picked B the first time was that it was slightly longer and I had unconsciously treated length as thoroughness. In a pairwise task, length is not a dimension on the rubric. I was applying a preference that was not in the guidelines.

**Corrected decision:** Tie, with the same evidence as before.

**Lesson:** On re-review, I now check whether my winner is winning on a rubric dimension or on an unstated preference. If it is the latter, I revert to a tie.

## Case 3: Missing a tone failure because the content was correct

**Task:** Linguistic error analysis.
**Original label:** `meaning_distortion` on a response that changed a date.

**Why the original label was wrong:** The label was technically defensible — the response did change a date — but the more useful label was `instruction_not_followed`, because the user had asked for a direct quote and the model paraphrased with an altered date. The dominant failure was instruction-following, not distortion of the original text. Choosing the narrower label would have hidden the more important problem.

**Corrected label:** `instruction_not_followed` (primary), with `meaning_distortion` recorded as a secondary note.

**Lesson:** When two labels are plausible, record the primary failure and the secondary one instead of collapsing to one. This preserves information for the next reviewer.

## What I took from these reviews

- Ambiguity flags should be reserved for *intent* ambiguity, not missing referents.
- Pairwise winners need a rubric dimension behind them, not a preference.
- When two labels are plausible, the primary label should reflect the *dominant* failure mode, and the secondary should be noted.
- Guideline gaps should be logged as proposals, not patched silently in a single record.

## Quality checks

- Re-scored without looking at the original label.
- Wrote down the reason for every change, not just the new label.
- Distinguished "I was wrong" from "the guideline is unclear."
- Proposed guideline changes where the same problem would recur.

## Limitations

These are three illustrative cases, not a measured calibration study. A real calibration process would involve multiple reviewers, blind re-scoring, and agreement statistics. This project shows the habit and the reasoning, not a statistical result.
