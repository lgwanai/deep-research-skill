#!/usr/bin/env python3

"""Score manually or independently graded behavioral evaluation results."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


WEIGHTS = {
    "coverage": 20,
    "citation_support": 20,
    "source_quality_independence": 15,
    "freshness_point_in_time": 10,
    "numerical_consistency": 10,
    "tool_routing_resilience": 10,
    "decision_usefulness": 10,
    "uncertainty_discipline": 5,
}
RELEASE_BLOCKERS = {"citation_support", "numerical_consistency"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results", type=Path)
    parser.add_argument("--cases", type=Path, default=Path("evals/cases.json"))
    args = parser.parse_args()

    try:
        case_data = load_json(args.cases)
        result_data = load_json(args.results)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    case_ids = {case.get("id") for case in case_data.get("cases", [])}
    errors: list[str] = []
    totals: list[float] = []
    blocked = False

    for index, result in enumerate(result_data.get("results", [])):
        context = f"results[{index}]"
        case_id = result.get("case_id")
        if case_id not in case_ids:
            errors.append(f"{context}: unknown case_id '{case_id}'")
            continue
        scores = result.get("scores", {})
        total = 0.0
        for dimension, weight in WEIGHTS.items():
            score = scores.get(dimension)
            if not isinstance(score, (int, float)) or not 0 <= score <= 5:
                errors.append(f"{context}: {dimension} must be a number from 0 to 5")
                continue
            total += (float(score) / 5.0) * weight
            if dimension in RELEASE_BLOCKERS and score < 3:
                blocked = True
        failures = result.get("critical_failures", [])
        if not isinstance(failures, list):
            errors.append(f"{context}: critical_failures must be a list")
        elif failures:
            blocked = True
        totals.append(total)
        print(f"{case_id}: {total:.1f}/100")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if not totals:
        print("ERROR: no results to score", file=sys.stderr)
        return 1

    print(f"Mean: {sum(totals) / len(totals):.1f}/100 across {len(totals)} case(s)")
    print(f"Release gate: {'BLOCKED' if blocked else 'PASS'}")
    return 1 if blocked else 0


if __name__ == "__main__":
    raise SystemExit(main())
