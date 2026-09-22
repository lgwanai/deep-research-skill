#!/usr/bin/env python3

"""Report local retrieval capability signals without network access or secrets."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


CLI_GROUPS = {
    "search_or_mcp": ["agent-reach", "mcporter", "brave", "tavily", "exa"],
    "browser_rendering": ["lightpanda", "playwright", "browserless"],
    "crawl_extract": ["firecrawl", "curl", "wget"],
    "platform_social": ["opencli", "twitter", "bird", "rdt", "bili"],
    "video_audio": ["yt-dlp", "ffmpeg"],
    "developer": ["gh"],
}

SKILL_CANDIDATES = {
    "agent-reach": [
        Path.home() / ".agents/skills/agent-reach/SKILL.md",
        Path.home() / ".codex/skills/agent-reach/SKILL.md",
    ],
    "ego-browser": [
        Path.home() / ".agents/skills/ego-browser/SKILL.md",
        Path.home() / ".codex/skills/ego-browser/SKILL.md",
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Detect local CLI and skill signals for retrieval planning."
    )
    parser.add_argument(
        "--compact", action="store_true", help="Emit compact JSON instead of indented JSON."
    )
    return parser.parse_args()


def detect_clis() -> dict[str, dict[str, str]]:
    groups: dict[str, dict[str, str]] = {}
    for group, commands in CLI_GROUPS.items():
        groups[group] = {}
        for command in commands:
            path = shutil.which(command)
            groups[group][command] = path or "unavailable"
    return groups


def detect_skills() -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for name, candidates in SKILL_CANDIDATES.items():
        matches = [str(path) for path in candidates if path.is_file()]
        result[name] = {"available": bool(matches), "paths": matches}
    return result


def main() -> int:
    args = parse_args()
    result = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "network_requests_made": False,
        "local_cli": detect_clis(),
        "local_skills": detect_skills(),
        "host_discovery_required": [
            "built-in search and fetch tools",
            "MCP/app/plugin tools not represented by local executables",
            "authenticated browser sessions",
            "finance and market-data tools",
        ],
        "interpretation": (
            "Use this as one input to the pre-search audit. A missing executable does "
            "not prove that the host lacks the equivalent capability."
        ),
    }
    indent = None if args.compact else 2
    print(json.dumps(result, ensure_ascii=True, indent=indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
