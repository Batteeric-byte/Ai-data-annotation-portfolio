# Search Relevance Review

## Goal

Judge search results against the likely intent of a query, not just whether they share keywords with it.

**Data note:** All queries and result descriptions below are synthetic examples. They are not taken from a live search engine.

## Relevance scale

- **3 — Highly relevant:** Directly satisfies the main intent.
- **2 — Partly relevant:** Useful, but misses a meaningful part of the intent.
- **1 — Marginally relevant:** Shares a topic or keyword but is unlikely to satisfy the need.
- **0 — Not relevant:** Does not help with the query.

## Sample judgments

| Query | Result | Score | Reason |
|---|---|---:|---|
| "how to keep 4c hair moisturised between wash days" | A guide on refreshing tightly coiled hair with water-based leave-in products | 3 | Directly addresses the hair type and between-wash routine. |
| "how to keep 4c hair moisturised between wash days" | A product page for a straightening iron | 0 | The product does not answer the moisture-maintenance question. |
| "difference between semantics and pragmatics" | An introductory linguistics page comparing literal meaning and meaning in context | 3 | Direct match for the comparison requested. |
| "difference between semantics and pragmatics" | A page listing general English grammar exercises | 1 | Related to language learning, but does not explain the requested distinction. |
| "free beginner spreadsheet course" | A course page with beginner spreadsheet lessons and no paid prerequisite | 3 | Matches the skill level and cost constraint described in the query. |
| "free beginner spreadsheet course" | An advanced data engineering bootcamp with a tuition fee | 0 | Conflicts with both beginner level and free access. |

## Ambiguous queries

Some queries cannot be scored confidently from the wording alone. In those cases the useful move is to state the interpretation you are assuming, score against that interpretation, and mark the record for review.

### Query: "python error"

This query has no stated goal. The user could be asking for:
- an explanation of a specific error message they have not pasted,
- a general tutorial on Python exceptions,
- a fix for a bug in their own code,
- documentation for a library error.

| Result | Score under stated assumption | Reason |
|---|---:|---|
| A general "Common Python errors and how to read them" tutorial | 2 | Reasonable if the user wants orientation, but not enough if they have a specific error. |
| A Stack Overflow thread about `ModuleNotFoundError` | 1 | Useful only if the user's error happens to match; the query does not establish that. |
| A page explaining how to interpret a Python traceback | 2 | Helps the user diagnose their own error, but assumes they can share the traceback. |

**Assumption used:** "user wants general guidance on reading Python errors." Score is conditional on that. Flagged: `needs_clarification=true`.

### Query: "best phone 2026"

This query is under-specified across multiple dimensions: budget, operating system, region, and use case (camera, battery, gaming).

| Result | Score under stated assumption | Reason |
|---|---:|---|
| A 2026 flagship comparison article covering iOS and Android | 2 | Relevant to the general topic but assumes the user wants flagships, not mid-range or budget phones. |
| A budget Android buying guide | 2 | Relevant if budget is the constraint, but the query does not say so. |
| A single-carrier promotional page | 1 | Too narrow relative to the open phrasing of the query. |

**Assumption used:** "user wants a general 2026 comparison, no budget or OS preference." Flagged: `needs_clarification=true`.

## A case where two reviewers could reasonably disagree

**Query:** "how to stop my cat scratching furniture"

**Result:** A page titled "Why cats scratch — understanding natural behaviour" that explains scratching as territory marking and stress relief but does not include a step-by-step solution.

| Reviewer | Score | Reasoning |
|---|---:|---|
| Reviewer A | 1 | The user asked *how to stop* the behaviour. The page explains *why* it happens but offers no intervention. Marginal. |
| Reviewer B | 2 | The page is a prerequisite to solving the problem; understanding cause is often the first step toward a fix. Partly relevant. |

**What I would record:** Score 2, with a note that the page is a foundation rather than a solution, and that Reviewer A's score of 1 is defensible under a strict "did it answer the how-to question?" reading.

**Why this is included:** Disagreement is not a failure of the scale. It is a signal that the guideline should clarify whether "foundational context" counts as satisfying a how-to query. Recording the disagreement is more useful than forcing a number.

## Decision process

1. Identify the main task, topic, and constraints in the query.
2. Read the result description rather than matching a keyword alone.
3. Apply the same scale to every result.
4. Record the specific match or mismatch.
5. Mark a case for review if the query is too vague to judge confidently.
6. When two scores are defensible, state the assumption and keep the disagreement visible.

## Edge cases

A result can mention all the right words but still be irrelevant. For example, a page about buying hair tools may mention "4c hair" without giving advice on moisture. Similarly, a result about general language learning may not answer a specific semantics-versus-pragmatics question. Under-specified queries, such as "python error" or "best phone 2026," should be scored only against a stated interpretation.

## Quality checks

- The score is supported by a written reason.
- Query constraints such as "free" and "beginner" are treated as important, not optional.
- Relatedness is not confused with usefulness.
- Ambiguous cases are flagged instead of assigned false precision.
- Assumptions are written down so another reviewer can check the same interpretation.

## Limitations

These judgments illustrate a process; they do not measure a search engine's real-world ranking quality. A live evaluation would require actual result pages, a defined user population or intent assumptions, and reviewer calibration.
