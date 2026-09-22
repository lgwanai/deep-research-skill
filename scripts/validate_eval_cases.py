#!/usr/bin/env python3

"""Validate the behavioral evaluation case catalog."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


VALID_MODES = {"quick", "standard", "pro", "ultra"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", type=Path)
    args = parser.parse_args()

    try:
        data = json.loads(args.catalog.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    errors: list[str] = []
    if data.get("schema_version") != "1.0":
        errors.append("schema_version must be '1.0'")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        errors.append("cases must be a non-empty list")
        cases = []

    seen: set[str] = set()
    for index, case in enumerate(cases):
        context = f"cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{context} must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"{context}.id is required")
        elif case_id in seen:
            errors.append(f"{context}.id duplicates '{case_id}'")
        else:
            seen.add(case_id)
        if not case.get("prompt"):
            errors.append(f"{context}.prompt is required")
        if case.get("expected_mode") not in VALID_MODES:
            errors.append(f"{context}.expected_mode is invalid")
        for field in ("expected_experts", "must", "must_not"):
            if not isinstance(case.get(field), list):
                errors.append(f"{context}.{field} must be a list")

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"Evaluation catalog validation failed: {len(errors)} error(s).", file=sys.stderr)
        return 1
    print(f"Evaluation catalog is valid: {len(cases)} case(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
