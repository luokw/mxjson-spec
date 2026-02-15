#!/usr/bin/env python3
"""Validate MxJSON examples against schema and key business rules."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "mxjson.schema.json"
EXAMPLES = [
    ROOT / "examples" / "contract-review" / "contract-review.mxjson",
    ROOT / "examples" / "translator" / "translator.mxjson",
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_with_jsonschema(schema, doc, path: Path):
    try:
        import jsonschema  # type: ignore
    except ModuleNotFoundError:
        print("[WARN] jsonschema is not installed; running structural fallback checks only.")
        return False

    jsonschema.validate(doc, schema)
    print(f"[OK] schema validation passed: {path.relative_to(ROOT)}")
    return True


def fallback_checks(schema, doc, path: Path):
    """Minimal checks when jsonschema isn't available."""
    required_top = schema.get("required", [])
    for field in required_top:
        if field not in doc:
            raise ValueError(f"missing required top-level field '{field}' in {path}")

    cap = doc.get("capability", {})
    ctype = cap.get("type")
    if ctype == "prompt" and "prompt" not in cap:
        raise ValueError(f"prompt capability missing 'prompt' in {path}")
    if ctype == "workflow" and "steps" not in cap:
        raise ValueError(f"workflow capability missing 'steps' in {path}")

    for step in cap.get("steps", []):
        nxt = step.get("next")
        if isinstance(nxt, dict) and not nxt:
            raise ValueError(f"step.next object cannot be empty in {path}")

    print(f"[OK] fallback checks passed: {path.relative_to(ROOT)}")


def main() -> int:
    schema = load_json(SCHEMA_PATH)

    validated_by_jsonschema = False
    for example in EXAMPLES:
        doc = load_json(example)
        try:
            used = validate_with_jsonschema(schema, doc, example)
            validated_by_jsonschema = validated_by_jsonschema or used
            if not used:
                fallback_checks(schema, doc, example)
        except Exception as exc:  # explicit fail path for CI
            print(f"[ERROR] validation failed for {example.relative_to(ROOT)}: {exc}")
            return 1

    if validated_by_jsonschema:
        print("[DONE] all examples validated with JSON Schema.")
    else:
        print("[DONE] all examples validated with fallback checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
