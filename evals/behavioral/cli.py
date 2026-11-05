#!/usr/bin/env python3
"""Prepare candidate workspaces or score their artifacts. No model invocation."""
import argparse
import json
from pathlib import Path
import sys

from run_store import prepare
from scoring import score


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prep = commands.add_parser("prepare")
    prep.add_argument("--source", type=Path, required=True)
    prep.add_argument("--output", type=Path, required=True)
    prep.add_argument("--split", choices=("train", "holdout", "all"), default="train")
    prep.add_argument("--repeats", type=int, default=3)
    prep.add_argument("--observed-settings", type=json.loads, default={},
                      help="JSON metadata backed by observed harness settings; default unknown")
    grade = commands.add_parser("score")
    grade.add_argument("run_root", type=Path)
    args = parser.parse_args()
    try:
        result = (prepare(args.source, args.output, args.split, args.repeats, args.observed_settings)
                  if args.command == "prepare" else score(args.run_root))
        print(json.dumps(result, indent=2))
    except (OSError, ValueError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
