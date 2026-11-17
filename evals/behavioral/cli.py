#!/usr/bin/env python3
"""Prepare candidate workspaces or score their artifacts. No model invocation."""
import argparse
import json
from pathlib import Path
import sys

from run_store import prepare
from scoring import score
from summary import summarize


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prep = commands.add_parser("prepare")
    prep.add_argument("--source", type=Path, required=True)
    prep.add_argument("--output", type=Path, required=True)
    prep.add_argument("--split", choices=("train", "holdout", "smoke", "habit", "all"), default="train")
    prep.add_argument("--cases", type=lambda text: text.split(","),
                      help="comma-separated case ids, applied after --split")
    prep.add_argument("--no-pack", action="store_true",
                      help="trials get no AGENTS.md and no .agents/skills")
    prep.add_argument("--repeats", type=int, default=3)
    prep.add_argument("--observed-settings", type=json.loads, default={},
                      help="JSON metadata backed by observed harness settings; default unknown")
    grade = commands.add_parser("score")
    grade.add_argument("run_root", type=Path)
    table = commands.add_parser("summary")
    table.add_argument("run_roots", type=Path, nargs="+")
    table.add_argument("--labels", type=lambda text: text.split(","), required=True)
    args = parser.parse_args()
    try:
        if args.command == "summary":
            print(summarize(args.run_roots, args.labels))
            return 0
        result = (prepare(args.source, args.output, args.split, args.repeats,
                          args.observed_settings, args.cases, not args.no_pack)
                  if args.command == "prepare" else score(args.run_root))
        print(json.dumps(result, indent=2))
    except (OSError, ValueError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
