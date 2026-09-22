#!/usr/bin/env python3

"""Validate structural and provenance invariants in a research package."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


PACKAGE_STATUSES = {"working", "final", "blocked"}
MODES = {"quick", "standard", "pro", "ultra"}
BRANCH_STATUSES = {"open", "partial", "conflicting", "resolved", "missing", "blocked"}
CLAIM_TYPES = {"fact", "attributed_view", "synthesis", "estimate", "assumption"}
CLAIM_STATUSES = {
    "supported",
    "supported_by_synthesis",
    "partial",
    "conflicting",
    "unsupported",
    "not_verifiable",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path, help="Research package JSON file.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors.")
    return parser.parse_args()


def require(mapping: dict, field: str, context: str, errors: list[str]) -> object:
    value = mapping.get(field)
    if value is None or value == "" or value == []:
        errors.append(f"{context}: missing required field '{field}'")
    return value


def index_records(records: object, kind: str, errors: list[str]) -> dict[str, dict]:
    if not isinstance(records, list):
        errors.append(f"package: '{kind}' must be a list")
        return {}
    indexed: dict[str, dict] = {}
    for position, record in enumerate(records):
        context = f"{kind}[{position}]"
        if not isinstance(record, dict):
            errors.append(f"{context}: must be an object")
            continue
        record_id = require(record, "id", context, errors)
        if not isinstance(record_id, str) or not record_id:
            continue
        if record_id in indexed:
            errors.append(f"{context}: duplicate id '{record_id}'")
        indexed[record_id] = record
    return indexed


def validate(data: object) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(data, dict):
        return ["package root must be an object"], warnings

    require(data, "schema_version", "package", errors)
    status = require(data, "status", "package", errors)
    if status not in PACKAGE_STATUSES:
        errors.append(f"package: invalid status '{status}'")

    contract = data.get("research_contract")
    if not isinstance(contract, dict):
        errors.append("package: 'research_contract' must be an object")
        contract = {}
    for field in ("question", "mode", "as_of_date", "decision_context"):
        require(contract, field, "research_contract", errors)
    if contract.get("mode") not in MODES:
        errors.append(f"research_contract: invalid mode '{contract.get('mode')}'")
    try:
        date.fromisoformat(str(contract.get("as_of_date")))
    except ValueError:
        errors.append("research_contract: as_of_date must be YYYY-MM-DD")

    branches = index_records(data.get("branches"), "branches", errors)
    sources = index_records(data.get("sources"), "sources", errors)
    claims = index_records(data.get("claims"), "claims", errors)
    calculations = index_records(data.get("calculations", []), "calculations", errors)

    urls: dict[str, list[str]] = {}
    for source_id, source in sources.items():
        context = f"source {source_id}"
        for field in ("title", "url", "source_type", "accessed_at", "origin_id"):
            require(source, field, context, errors)
        url = source.get("url", "")
        if isinstance(url, str) and urlparse(url).scheme not in {"http", "https"}:
            warnings.append(f"{context}: URL is not http/https")
        if isinstance(url, str):
            urls.setdefault(url, []).append(source_id)
        origin_id = source.get("origin_id")
        if origin_id and origin_id not in sources:
            warnings.append(f"{context}: origin_id '{origin_id}' is not another source id")

    for url, source_ids in urls.items():
        origins = {sources[item].get("origin_id", item) for item in source_ids}
        if len(source_ids) > 1 and len(origins) > 1:
            warnings.append(
                f"sources {source_ids}: duplicate URL has inconsistent origin ids"
            )

    for claim_id, claim in claims.items():
        context = f"claim {claim_id}"
        for field in ("text", "claim_type", "status"):
            require(claim, field, context, errors)
        if claim.get("claim_type") not in CLAIM_TYPES:
            errors.append(f"{context}: invalid claim_type '{claim.get('claim_type')}'")
        if claim.get("status") not in CLAIM_STATUSES:
            errors.append(f"{context}: invalid status '{claim.get('status')}'")
        source_ids = claim.get("source_ids", [])
        if not isinstance(source_ids, list):
            errors.append(f"{context}: source_ids must be a list")
            source_ids = []
        unknown = [item for item in source_ids if item not in sources]
        if unknown:
            errors.append(f"{context}: unknown source ids {unknown}")
        if claim.get("critical") and claim.get("status") in {"supported", "supported_by_synthesis"} and not source_ids:
            errors.append(f"{context}: supported critical claim has no sources")
        if claim.get("claim_type") in {"synthesis", "estimate"} and not claim.get("reasoning"):
            warnings.append(f"{context}: synthesis/estimate has no reasoning")
        if claim.get("status") == "supported_by_synthesis":
            origins = {sources[item].get("origin_id", item) for item in source_ids if item in sources}
            if len(origins) < 2:
                warnings.append(f"{context}: synthesis uses fewer than two independent origins")

    unresolved_critical: list[str] = []
    for branch_id, branch in branches.items():
        context = f"branch {branch_id}"
        require(branch, "question", context, errors)
        branch_status = require(branch, "status", context, errors)
        if branch_status not in BRANCH_STATUSES:
            errors.append(f"{context}: invalid status '{branch_status}'")
        unknown = [item for item in branch.get("claim_ids", []) if item not in claims]
        if unknown:
            errors.append(f"{context}: unknown claim ids {unknown}")
        if status == "final" and branch.get("critical") and branch_status == "open":
            errors.append(f"{context}: final package has an open critical branch")
        if branch.get("critical") and branch_status in {
            "partial",
            "conflicting",
            "missing",
            "blocked",
        }:
            unresolved_critical.append(branch_id)

    for calculation_id, calculation in calculations.items():
        context = f"calculation {calculation_id}"
        for field in ("claim_id", "raw_inputs", "formula", "result", "result_unit", "status"):
            require(calculation, field, context, errors)
        if calculation.get("claim_id") not in claims:
            errors.append(f"{context}: unknown claim_id '{calculation.get('claim_id')}'")
        if calculation.get("status") not in {"passed", "needs_review"}:
            errors.append(f"{context}: invalid status '{calculation.get('status')}'")
        raw_inputs = calculation.get("raw_inputs", [])
        if isinstance(raw_inputs, list):
            unknown_sources = [
                item.get("source_id")
                for item in raw_inputs
                if isinstance(item, dict)
                and item.get("source_id")
                and item.get("source_id") not in sources
            ]
            if unknown_sources:
                errors.append(f"{context}: raw inputs use unknown sources {unknown_sources}")

    coverage = data.get("coverage", [])
    if not isinstance(coverage, list):
        errors.append("package: 'coverage' must be a list")
    else:
        for index, item in enumerate(coverage):
            context = f"coverage[{index}]"
            if not isinstance(item, dict):
                errors.append(f"{context}: must be an object")
                continue
            require(item, "dimension", context, errors)
            require(item, "status", context, errors)
            unknown = [source_id for source_id in item.get("source_ids", []) if source_id not in sources]
            if unknown:
                errors.append(f"{context}: unknown source ids {unknown}")

    retrieval_log = data.get("retrieval_log", [])
    if not isinstance(retrieval_log, list):
        errors.append("package: 'retrieval_log' must be a list")
    else:
        for index, item in enumerate(retrieval_log):
            context = f"retrieval_log[{index}]"
            if not isinstance(item, dict):
                errors.append(f"{context}: must be an object")
                continue
            branch_id = item.get("branch_id")
            if branch_id and branch_id not in branches:
                errors.append(f"{context}: unknown branch_id '{branch_id}'")
            unknown = [source_id for source_id in item.get("source_ids", []) if source_id not in sources]
            if unknown:
                errors.append(f"{context}: unknown source ids {unknown}")

    if status == "final":
        assessment = data.get("final_assessment")
        if not isinstance(assessment, dict):
            errors.append("final package: 'final_assessment' must be an object")
        else:
            for field in ("confidence", "bottom_line", "stopping_reason"):
                require(assessment, field, "final_assessment", errors)
            if assessment.get("confidence") not in {"high", "medium", "low"}:
                errors.append("final_assessment: confidence must be high, medium, or low")
            if unresolved_critical:
                disclosed = bool(assessment.get("critical_gaps")) or bool(
                    assessment.get("unresolved_conflicts")
                )
                if not disclosed:
                    errors.append(
                        "final_assessment: unresolved critical branches must be disclosed "
                        f"({unresolved_critical})"
                    )
                if assessment.get("confidence") == "high":
                    errors.append(
                        "final_assessment: confidence cannot be high with unresolved "
                        f"critical branches {unresolved_critical}"
                    )

    return errors, warnings


def main() -> int:
    args = parse_args()
    try:
        data = json.loads(args.package.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: unable to read package: {exc}", file=sys.stderr)
        return 2

    errors, warnings = validate(data)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    failed = bool(errors) or (args.strict and bool(warnings))
    if failed:
        print(f"Validation failed: {len(errors)} error(s), {len(warnings)} warning(s).", file=sys.stderr)
        return 1
    print(f"Research package is valid: {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
