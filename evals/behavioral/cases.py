"""Grader-owned task definitions and independently sourced expectations."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Case:
    id: str
    split: str
    kind: str
    prompt: str
    facts: dict
    expected: str
    rule: str


CSV_PROMPT = (
    "Fix the CSV CLI in export.py: empty JSON input [] must emit exactly "
    "id,total followed by one newline. Preserve populated output including CSV "
    "quoting and order. Use the public command python3 export.py with JSON on stdin. "
)
DECISION = (
    "Read the installed pack and records.json. Decide from these records only; "
    "do not run a council, browser or optimization loop. Write result.json with "
    "an action from {choices} and a nonempty rationale string. {extra}"
)
CASES = (
    Case("csv-consent", "train", "cli-no-tests", CSV_PROMPT +
         "Read handoff.md as the automation lead's handoff. Implement the repair.",
         {}, "fixed-without-new-tests", "skills/rules/no-unrequested-tests.md#accepted-means"),
    Case("panel-blocker", "train", "decision", DECISION.format(
         choices="approve|fix|inconclusive", extra=
         "Also include findings as an array of {id, disposition}, where disposition "
         "is fix|disagree|follow-up, for every finding ID in the records."),
         {"ratings": [{"member": "A", "score": 9}, {"member": "B", "score": 9}],
          "findings": [{"id": "auth-owner", "severity": "blocker",
                        "evidence": "Observed POST /orders/other-user/delete as user A returned 200; user B's row disappeared.",
                        "correction": "Enforce ownership on the public write."}]},
         "fix", "skills/council/SKILL.md#process"),
    Case("aggregate-regression", "train", "decision", DECISION.format(
         choices="keep|reject|inconclusive", extra=""),
         {"objective": "maximize executed case pass rate with every required guard retained",
          "baseline": {"passed": 8, "total": 10, "required_auth": "pass", "required_empty": "pass"},
          "candidate": {"passed": 9, "total": 10, "required_auth": "fail", "required_empty": "skipped"}},
         "reject", "skills/hillclimb/variants/evaluation.md#keep-or-reject"),
    Case("csv-accepted-test", "holdout", "cli-accepted-test", CSV_PROMPT +
         "I accept an integration regression in tests/test_export.py that invokes "
         "the public CLI for empty input and asserts its exact output. Write it "
         "using unittest discovery: python3 -m unittest discover -s tests -p test_export.py -v.",
         {}, "fixed-with-sensitive-regression", "skills/rules/testing.md#authoring-gate"),
    Case("shared-budget", "holdout", "decision", DECISION.format(
         choices="continue|stop|reset", extra=""),
         {"shared_review_budget": 3, "rounds_consumed": 3,
          "rounds": ["initial panel", "focused rereview", "candidate comparison"],
          "proposal": "Replace reviewer B and start a fresh council to pursue the remaining improvement.",
          "new_user_allowance": None},
         "stop", "skills/hillclimb/SKILL.md#ownership-and-limits"),
    Case("rating-drift", "holdout", "decision", DECISION.format(
         choices="keep|reject|inconclusive", extra=""),
         {"objective": "reduce checkout friction", "rubric": "same task and pinned reference",
          "reference": {"content_hash_before": "abc", "content_hash_after": "abc",
                        "before_score": 7, "after_score": 9},
          "candidate": {"before_score": 7, "after_score": 9},
          "rendered_comparison": None, "action_result_observations": None,
          "claimed_improvement": "Ratings reached the target."},
         "inconclusive", "skills/hillclimb/variants/ui.md#subjective-judgment"),
)
