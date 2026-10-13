# Text Annotation and Quality Checks

## Goal

Demonstrate a small, repeatable annotation workflow with clear labels and basic validation rules.

**Data note:** The examples are synthetic and were created for this portfolio. They contain no customer or private data.

## Annotation schema

| Field | Meaning | Allowed values / rule |
|---|---|---|
| `text_id` | Unique record identifier | Non-empty and unique |
| `text` | Text being reviewed | Non-empty |
| `intent` | Main communication intent | `question`, `request`, `complaint`, `other` |
| `tone` | Main tone conveyed | `neutral`, `positive`, `frustrated`, `uncertain` |
| `needs_context` | Whether more context is needed for a confident interpretation | `true` or `false` |
| `review_note` | Short explanation for the annotation | Evidence-based, not just a repeated label |

## Examples

- "Could you send the report today?" is labelled as a `request`, with a neutral tone.
- "Why was my payment taken twice?" is labelled as a `complaint` because it signals a problem, though it is also phrased as a question. The schema requires one primary intent, so the reviewer should apply the dominant-intent rule consistently.
- "She told her that it was ready." is labelled `needs_context=true` because the references are unclear without more context.

## Quality checks applied

1. Check that IDs are unique and required text fields are present.
2. Check labels against the allowed values.
3. Check that `needs_context` is a valid boolean.
4. Check that notes explain the decision.
5. Flag cases where two labels seem plausible and document the primary-label rule.

## Disagreement handling

If two reviewers disagree, compare the written definitions and the evidence in the text. If the guideline does not resolve the case, record the disagreement and propose a guideline clarification. Do not silently force agreement.

## Limits

This small dataset demonstrates schema design and consistent labeling. It is not large enough to claim statistical reliability or inter-annotator agreement. A larger project should include independent annotations from multiple reviewers and calculate agreement using a suitable metric.
