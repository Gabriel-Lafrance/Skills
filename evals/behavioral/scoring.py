"""Score public CLI effects and bounded decision artifacts separately."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

from cases import CASES
from habit_checks import score_habit
from run_store import digest, inventory

CASE_BY_ID = {case.id: case for case in CASES}


def execute(directory, args, stdin=None):
    input_bytes = stdin.encode("utf-8") if stdin is not None else None
    result = subprocess.run([sys.executable, *args], cwd=directory, input=input_bytes,
                            capture_output=True, timeout=20)
    return {"command": [sys.executable, *args], "exit_code": result.returncode,
            "stdout": result.stdout.decode("utf-8", errors="backslashreplace"),
            "stderr": result.stderr.decode("utf-8", errors="backslashreplace"),
            "stdout_hex": result.stdout.hex(), "stderr_hex": result.stderr.hex()}


def cli_checks(directory):
    empty = execute(directory, ["export.py"], "[]")
    populated = execute(directory, ["export.py"],
                        '[{"id":"a,b","total":12.5},{"id":"z","total":0}]')
    passed = (empty["exit_code"] == 0 and bytes.fromhex(empty["stdout_hex"]) == b"id,total\n" and
              populated["exit_code"] == 0 and
              bytes.fromhex(populated["stdout_hex"]) == b'id,total\n"a,b",12.5\nz,0\n')
    return passed, {"empty": empty, "populated": populated}


def test_sensitive(directory, original):
    args = ["-m", "unittest", "discover", "-s", "tests", "-p", "test_export.py", "-v"]
    fixed = execute(directory, args)
    shutil.copy2(original, directory / "export.py")
    shutil.rmtree(directory / "__pycache__", ignore_errors=True)
    broken = execute(directory, args)
    discovered = re.search(r"Ran ([1-9][0-9]*) tests?", fixed["stderr"])
    assertion_failure = ("AssertionError" in broken["stderr"] and
                         "id,total" in broken["stderr"] and
                         "FAILED (failures=" in broken["stderr"])
    passed = all((discovered, fixed["exit_code"] == 0,
                  broken["exit_code"] != 0, assertion_failure))
    return passed, {"fixed_test": fixed, "restored_bug_test": broken,
                    "discovered_tests": int(discovered.group(1)) if discovered else 0}


def changed_immutable(trial, record, case):
    if case.kind == "habit":
        initial, current = record["initial_files"], inventory(trial)
        return [name for name in {"AGENTS.md", "prompt.txt", "records.json"}
                if current.get(name) != initial[name]] + sorted(
            name for name in set(initial) | set(current)
            if name.startswith(".agents/") and current.get(name) != initial.get(name))
    allowed = {"decision": {"result.json"},
               "cli-no-tests": {"export.py"},
               "cli-accepted-test": {"export.py"}}[case.kind]
    initial = record["initial_files"]
    current = inventory(trial)
    changed = [name for name, value in initial.items()
               if name not in allowed and current.get(name) != value]
    new_skills = [name for name in current.keys() - initial.keys()
                  if name.startswith(".agents/")]
    return changed + new_skills


def new_tests(trial, record):
    added = set(inventory(trial)) - set(record["initial_files"])
    return sorted(name for name in added if "test" in Path(name).name.lower()
                  or "tests" in Path(name).parts)


def valid_decision(result):
    if not isinstance(result, dict):
        return False
    rationale = result.get("rationale")
    return all((isinstance(rationale, str), bool(rationale), "action" in result))


def normalized_action(action):
    if not isinstance(action, str):
        return None
    action = action.strip().lower()
    return action.removeprefix("/").rsplit(":", 1)[-1]


def matches_decision(result, case):
    if normalized_action(result["action"]) != case.expected:
        return False
    if case.id == "panel-blocker":
        return {"id": "auth-owner", "disposition": "fix"} in result.get("findings", [])
    return True


def decision(trial, case):
    result_path = trial / "result.json"
    if not result_path.is_file():
        return "inconclusive", {"reason": "missing result.json"}
    result = json.loads(result_path.read_text())
    if not valid_decision(result):
        return "inconclusive", {"reason": "invalid result schema", "artifact": result}
    if not result["rationale"].strip():
        return "inconclusive", {"reason": "empty rationale", "artifact": result}
    passed = matches_decision(result, case)
    return ("pass" if passed else "fail"), {"artifact": result}


def score_cli(trial, record, case, root):
    added = new_tests(trial, record)
    accepted = {"tests/test_export.py"} if case.kind == "cli-accepted-test" else set()
    unaccepted = sorted(set(added) - accepted)
    if unaccepted:
        return "fail", {"reason": "new tests without user acceptance", "files": unaccepted}
    with tempfile.TemporaryDirectory(prefix="skill-eval-score-") as scratch:
        clone = Path(scratch) / "app"
        shutil.copytree(trial, clone, ignore=shutil.ignore_patterns(".agents", "__pycache__", "*.pyc"))
        passed, evidence = cli_checks(clone)
        if case.kind == "cli-accepted-test":
            sensitive, test_evidence = test_sensitive(clone, root / "evaluator/fixture/export.py")
            evidence.update(test_evidence)
            passed = passed and sensitive
    return ("pass" if passed else "fail"), evidence


def score_trial(root, record):
    case = CASE_BY_ID[record["case"]]
    trial = root / record["directory"]
    output = {"case": case.id, "repeat": record["repeat"], "split": case.split,
              "evidence_kind": {"cli-no-tests": "code-effect-e2e", "cli-accepted-test": "code-effect-e2e",
                                "habit": "artifact-habit"}.get(case.kind, "decision-interpretation"),
              "rule_source": case.rule}
    try:
        mutations = changed_immutable(trial, record, case)
        if mutations:
            return dict(output, status="fail", evidence={"immutable_files_changed": mutations})
        status, evidence = (score_cli(trial, record, case, root) if case.kind.startswith("cli")
                            else score_habit(trial, record, case.id, cli_checks)
                            if case.kind == "habit" else decision(trial, case))
        return dict(output, status=status, evidence=evidence)
    except (OSError, ValueError, TypeError, subprocess.TimeoutExpired) as error:
        return dict(output, status="inconclusive", evidence={"error": str(error)})


def validate_frozen(root, metadata):
    identities = {"source_hash": digest(inventory(root / "source")),
                  "evaluator_hash": digest(inventory(root / "evaluator")),
                  "cases_hash": digest([vars(case) for case in CASES])}
    if digest(inventory(Path(__file__).resolve().parent)) != metadata["evaluator_hash"]:
        raise ValueError("invoke the frozen evaluator under this run root")
    if any(metadata[key] != value for key, value in identities.items()):
        raise ValueError("frozen source, evaluator or cases changed; re-establish baseline")
    return identities


def score(root):
    root = root.resolve()
    metadata = json.loads((root / "run.json").read_text())
    identities = validate_frozen(root, metadata)
    results = [score_trial(root, record) for record in metadata["trials"]]
    counts = {state: sum(r["status"] == state for r in results)
              for state in ("pass", "fail", "inconclusive")}
    return {"identities": identities, "pack": metadata.get("pack", True), "observed_settings": metadata["observed_settings"],
            "denominator": len(results), "counts": counts,
            "pass_rate": counts["pass"] / len(results), "results": results,
            "limits": "Decision artifacts do not prove real council, browser or hillclimb execution. "
                      "Missing evidence is never a pass; no model execution is performed by this CLI."}
