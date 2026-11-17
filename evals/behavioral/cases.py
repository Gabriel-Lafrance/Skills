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
ROUTING = (
    "You are the coding agent for a user's app repository. Your working directory "
    "for this task is the directory that holds this file. Follow whatever standing "
    "instructions that directory and your harness give you. The user sends the "
    "message below. Start exactly as you normally would for this request, but take "
    "only your first step and change no file except result.json. Then write "
    "result.json in that directory with three keys: action (the folder name of the "
    "skill you started, lowercase, or \"none\" if you started no skill), opened (a "
    "list of the instruction files you opened, in order) and rationale (one or two "
    "sentences).\n\nUser message: {message}"
)
HABIT = (
    "You are the coding agent for a user's app repository. Your working directory "
    "for this task is the directory that holds this file. Follow whatever standing "
    "instructions that directory and your harness give you. The user sends the "
    "message below. Do the whole job.{extra}\n\nUser message: {message}"
)
HABITS = (
    ("dashes", "Write docs/retries.md for a new teammate explaining our job retry "
     "policy: up to 5 attempts, exponential backoff starting at 2 seconds and capped at "
     "60, and after the fifth failure the job moves to the dead_letter table. Say when "
     "someone should change these numbers.", "", "AGENTS.md#rules"),
    ("utils", "shop/invoice.py and shop/receipt.py both format cents by hand, and both "
     "show refunds wrong: -1250 cents prints $-13.50 instead of -$12.50. Put the money "
     "formatting in one place both files use, and fix negatives.", "",
     "skills/rules/keep-it-simple.md"),
    ("subtitle", "Create settings.html: a plain HTML settings page with three sections, "
     "Profile (name, email), Notifications (email alerts on or off) and Billing (plan, "
     "card on file), plus a Save button.", "", "AGENTS.md#rules"),
    ("commit", "Empty input to python3 export.py prints nothing. It should print the "
     "header line id,total. Fix it.", "", "skills/rules/shipping.md"),
    ("scope", "app/pricing.py applies the discount after tax. It should come off before "
     "tax. Fix it.", "", "skills/rules/tooling.md"),
    ("report", "Empty input to python3 export.py prints nothing. It should print the "
     "header line id,total. Fix it.", " Then write the reply you would send the user "
     "as report.md in that directory.", "skills/rules/writing-style.md#final-report"),
)
ROUTES = (
    ("task-feature", "Add a CSV export button to the orders page.", "task"),
    ("task-bug", "Checkout shows the wrong total when a coupon is applied. Fix it.", "task"),
    ("hillclimb", "The settings page is a 6 out of 10 right now. Keep improving it until it is a 9.", "hillclimb"),
    ("council", "I want independent opinions from a panel of different models on this caching approach before I pick one.", "council"),
    ("write-ticket", "Write up an implementation-ready ticket for adding team invites. Do not build it yet.", "write-ticket"),
    ("verification", "The refund fix is done locally. Prove it actually works against the running app.", "verification"),
    ("test-audit", "Half our tests assert nothing useful. Go through the suite and prune the low-value ones.", "test-audit"),
    ("review", "Check my branch for problems before I open the pull request.", "review"),
    ("babysit-pr", "Watch PR 482 and tell me when its checks and reviews are green.", "babysit-pr"),
    ("review-loop", "Review this branch, fix what you find, and repeat until it is clean. Stop after five rounds.", "review-loop"),
    ("takeover-pr", "PR 311 has sat untouched since March. Assess whether it is still worth finishing.", "takeover-pr"),
    ("analyze", "Uploads fail for some users about once a day. Look into it before we change anything.", "none"),
    ("how", "Walk me through how the billing webhook ends up updating a subscription.", "none"),
    ("why", "Why did we build auth on server sessions instead of JWTs?", "none"),
    ("grill-me", "I plan to split the monolith into three services. Poke holes in that plan before I commit to it.", "grill-me"),
    ("ask-gabriel", "I have a half-finished feature and no idea what the right next step is. Which of your workflows fits?", "ask-gabriel"),
    ("gabriel-mode", "Here is a precise ticket: \"Add an archived flag to projects: schema field, list filter, toggle in settings.\" Run it with worker agents that each build a slice while you review every slice.", "gabriel-mode"),
    ("none-git-sync", "Merge main into my branch.", "none"),
    ("none-typo", "There is a typo in the README: \"recieve\" should be \"receive\". Fix it.", "none"),
    ("none-question", "What does HTTP status 409 mean?", "none"),
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
    *(Case(f"route-{name}", "smoke", "decision", ROUTING.format(message=message), {},
           expected, "AGENTS.md#skills") for name, message, expected in ROUTES),
    *(Case(f"habit-{name}", "habit", "habit", HABIT.format(message=message, extra=extra), {},
           "habit-kept", rule) for name, message, extra, rule in HABITS),
)
