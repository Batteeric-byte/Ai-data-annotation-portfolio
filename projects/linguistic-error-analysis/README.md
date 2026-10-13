# Linguistic Error Analysis in Model Responses

## Goal

Use semantics and pragmatics to identify answers that may be grammatically fluent but still misunderstand a request or the situation.

**Data note:** These prompts and responses are synthetic examples written for demonstration.

## Case 1: Technically true, wrong implication

**User:** "Can I submit the form after 5 pm?"

**Model:** "The office closes at 5 pm."

**Issue:** The response gives related information but does not answer whether after-hours submission is possible. The user may be asking about an online form, a physical office, or a deadline.

**Label:** `intent_not_resolved`

**Better response:** "I can't tell from that information alone. Is this an online form or one that must be handed in at the office?"

**Reasoning:** The answer should not infer that submission is impossible solely from the office closing time.

## Case 2: Ambiguous pronoun reference

**User:** "Amina spoke to Grace after she finished the review. Who finished the review?"

**Model:** "Amina finished the review."

**Issue:** The pronoun "she" could refer to Amina or Grace. The sentence does not provide enough information to decide.

**Label:** `unsupported_resolution`

**Better response:** "The sentence is ambiguous; 'she' could refer to either Amina or Grace."

**Reasoning:** A model should recognize when the wording does not uniquely identify the referent.

## Case 3: Tone and implied intent

**User:** "Could you explain this more simply? I'm new to the topic."

**Model:** "As already stated, the process is straightforward."

**Issue:** The response sounds dismissive and does not simplify the explanation. "As already stated" can imply that the user should already understand.

**Label:** `tone_mismatch` and `instruction_not_followed`

**Better response:** "Of course. Here's the simple version: …"

**Reasoning:** The user asked for simpler wording and signalled that they are a beginner. The response should adjust its explanation rather than imply the user has missed something obvious.

## Annotation labels

| Label | Use when |
|---|---|
| `intent_not_resolved` | The response does not answer the user's main question. |
| `unsupported_resolution` | The response chooses an interpretation that the context does not establish. |
| `tone_mismatch` | The wording conflicts with the requested or appropriate tone. |
| `instruction_not_followed` | The response misses an explicit instruction. |
| `meaning_distortion` | The response changes the meaning of the original content. |

## Reviewer checklist

- What did the user actually ask for?
- What does the wording support, and what remains uncertain?
- Is the issue factual, semantic, pragmatic, or tonal?
- Does the proposed correction preserve the user's meaning?
- Could another reviewer apply the label using the same evidence?

## Limitations

These are illustrative cases, not a benchmark. Real evaluation should include multiple reviewers, agreed label definitions, disagreement tracking, and examples from the target domain.
