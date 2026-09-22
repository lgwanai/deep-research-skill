#!/usr/bin/env python3

"""Filter the bundled structured source registry."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


DEFAULT_REGISTRY = Path(__file__).resolve().parent.parent / "references/source-registry.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--domain", help="Research domain, such as equity or macro.")
    parser.add_argument("--region", help="Region code or global.")
    parser.add_argument("--authority", help="Authority class, such as primary.")
    parser.add_argument("--role", help="Evidence role, such as filing or dataset.")
    parser.add_argument("--format", choices=("table", "json"), default="table")
    return parser.parse_args()


def matches(source: dict, args: argparse.Namespace) -> bool:
    checks = (
        (args.domain, source.get("research_domains", [])),
        (args.region, source.get("regions", [])),
        (args.role, source.get("evidence_roles", [])),
    )
    for requested, values in checks:
        if requested and requested.lower() not in {str(value).lower() for value in values}:
            return False
    if args.authority and args.authority.lower() != str(source.get("authority", "")).lower():
        return False
    return True


def main() -> int:
    args = parse_args()
    data = json.loads(args.registry.read_text(encoding="utf-8"))
    sources = [source for source in data.get("sources", []) if matches(source, args)]
    if args.format == "json":
        print(json.dumps({"sources": sources}, ensure_ascii=False, indent=2))
        return 0

    print("ID\tNAME\tAUTHORITY\tACCESS\tDOMAINS")
    for source in sources:
        print(
            "\t".join(
                [
                    source["id"],
                    source["name"],
                    source["authority"],
                    source["access"],
                    ",".join(source["domains"]),
                ]
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
