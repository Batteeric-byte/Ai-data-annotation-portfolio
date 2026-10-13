"""Basic validation for the synthetic portfolio annotation CSV."""
import csv
from pathlib import Path

DATA_FILE = Path(__file__).with_name("annotations.csv")
ALLOWED_INTENTS = {"question", "request", "complaint", "other"}
ALLOWED_TONES = {"neutral", "positive", "frustrated", "uncertain"}
ALLOWED_CONTEXT = {"true", "false"}

def validate(path=DATA_FILE):
    errors = []
    seen_ids = set()

    with open(path, newline="", encoding="utf-8") as f:
        rows = csv.DictReader(f)
        required = {"text_id", "text", "intent", "tone", "needs_context", "review_note"}
        if not required.issubset(set(rows.fieldnames or [])):
            return [f"Missing columns: {sorted(required - set(rows.fieldnames or []))}"]

        for line_no, row in enumerate(rows, start=2):
            record_id = row["text_id"].strip()
            if not record_id:
                errors.append(f"Line {line_no}: text_id is empty")
            elif record_id in seen_ids:
                errors.append(f"Line {line_no}: duplicate text_id {record_id}")
            seen_ids.add(record_id)

            if not row["text"].strip():
                errors.append(f"Line {line_no}: text is empty")
            if row["intent"] not in ALLOWED_INTENTS:
                errors.append(f"Line {line_no}: invalid intent {row['intent']!r}")
            if row["tone"] not in ALLOWED_TONES:
                errors.append(f"Line {line_no}: invalid tone {row['tone']!r}")
            if row["needs_context"] not in ALLOWED_CONTEXT:
                errors.append(f"Line {line_no}: needs_context must be true/false")
            if not row["review_note"].strip():
                errors.append(f"Line {line_no}: review_note is empty")

    return errors

if __name__ == "__main__":
    problems = validate()
    if problems:
        print("Validation failed:")
        print("\n".join(f"- {p}" for p in problems))
        raise SystemExit(1)
    print("Validation passed.")
