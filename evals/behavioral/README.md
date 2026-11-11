# Skill behavior evaluations

This stdlib Python runner prepares disposable installed-pack sessions and scores
six independently specified cases, a 20-case `smoke` routing split and a six-case `habit` split. It never invokes a model. Run each prompt
through the native harness in a fresh session, with its cwd set to that trial.
Give the candidate only its own directory, prompt and installed rules. Restrict
its tools to that directory when supported. The grader and sibling directories
are evaluator-owned and must not be exposed as candidate context. A shared
filesystem alone is not a security boundary against a deliberately cheating agent.

```sh
python3 evals/behavioral/cli.py prepare --source "$PWD" --output /tmp/skills-baseline-new --split train --repeats 3
python3 /tmp/skills-baseline-new/evaluator/cli.py score /tmp/skills-baseline-new
```

`--cases a,b,c` keeps only those case ids after the `--split` filter; an unknown id is an
error. `--no-pack` creates trials without `AGENTS.md` or `.agents/skills` and records
`"pack": false` in `run.json` and the `score` output. It only means something where the
harness loads no user-level install of the pack, for example `~/.claude/AGENTS.md` or
`~/.codex/AGENTS.md`.

An orchestrating agent starts one fresh child per trial through the harness (in T3 Code,
`delegate_task`), giving it only the trial directory and prompt.

`prepare` prints every candidate cwd and prompt path. `--source` is a repository
or exported snapshot containing root `AGENTS.md` and `skills/`. It copies that
source before creating trials. Use a new output outside the repository for every
baseline or candidate; nonempty output is refused. Each trial has its own
installed `.agents/skills/`. No model settings are assumed: supply only observed
settings via `--observed-settings '{"harness":"observed name"}'`, or record
actual settings and native tool traces separately beside `run.json`. A requested
spawn setting is not an observed effective setting: record the former separately
as requested metadata when the native harness does not expose the latter. A blank
settings object means unknown. Do not compare unlike or unknown execution
conditions as a measured improvement.

`run.json` freezes source, evaluator and case hashes and immutable trial inputs.
Always score with the copied evaluator, which rejects source/evaluator changes
and unexpected installed-rule or fixture mutations. Candidate modifications to
`export.py`, and the explicitly accepted `tests/test_export.py`, are permitted
in their relevant cases. Run metadata and evaluator files belong to the grader.
Keep native traces and raw score JSON outside the repository. Scoring runs
candidate code and tests in disposable clones with a 20 second process timeout;
use the same local disposable permissions as any untrusted coding trial.

The JSON result includes each case and repeat, evidence, pass/fail/inconclusive,
an explicit total denominator and counts. Missing or malformed decision outputs
are inconclusive. Wrong actions or executable behavior fail. Nothing skipped
counts as a pass. A decision artifact with a correct action is evidence of that
bounded interpretation only, not proof of an actual council, browser drive,
read of a linked rule, or full optimization loop. Inspect native tool logs for
those claims and for instruction reading. Rationales are retained for review;
the scorer checks presence, not semantic quality.

`habit` holds six cases that bait a habit the pack restrains: an em or en dash in a written doc (`habit-dashes`), a `utils` or `helpers` file (`habit-utils`), a sentence under a heading (`habit-subtitle`), an unasked commit (`habit-commit`), edits outside the asked file (`habit-scope`) and a final report without the status, State and Next lines (`habit-report`). Each also checks the job works. Fixtures live in `habits/`; checks live in `habit_checks.py`.

`smoke` holds 20 routing cases (`route-*`): the user message is the only variable, and
`result.json` names the skill the agent started (`none` if no skill). A pass proves a
self-reported first step with the right skill name (`task`, `/task` and
`gabriel-skills:task` all count as `task`). It does not prove the agent then follows the
skill; check native tool logs for that.

`python3 evaluator/cli.py summary <run_root> [<run_root> ...] --labels a,b,c` scores each
root with the same rules as `score` and prints one Markdown table: a row per case, a column
per label, and a totals row. A cell is `pass`, `fail (got <action>)` or `inconclusive` for
one repeat, and `pass/fail/inconclusive` counts otherwise.

Freeze this evaluator before baseline. Optimize only against `train`; reserve
`holdout` for the frozen final candidate and disclose that these public source
cases cannot establish unseen-task generalization. Three repeats per side are
the default. Pin the comparison and noise rule before editing skills. A useful
strict initial rule is: every required case remains passing in every repeat,
at least one previously failed train repeat improves, no pass becomes a failure
or inconclusive, and held-out guards all pass. Do not improve an aggregate by
omitting trials. A failing required case rejects the candidate; missing required
evidence blocks a keep decision. Counts alone do not prove improvement beyond
model variability.

## Cross-model and subscription coverage

The benchmark roster is the user's main drivers only: **Claude Opus 5.5,
GPT-6.1 Sol, Muse Wonder Full 1.0, and Grok 4.7**. All four benchmark candidates
use explicitly requested **low** effort: Claude `effort: "low"`; Codex, Muse
and Grok `reasoningEffort: "low"`. Muse's model is `muse-wonder-full-1.0`;
never inherit its catalog's max default.

The goal is to measure whether the required behavior holds with limited
deliberation. Do not rescue failures by increasing effort or treating a
higher-effort rerun as a low-effort pass. Preserve prior settings and scores:
the earlier Muse xhigh batch is historical xhigh evidence, not evidence for
Muse low. Its low-effort coverage remains untested until actually executed.
This policy governs benchmark candidates only; it does not change council
membership, production-agent settings or the separate Sol xhigh challenger.

Discover availability and supported options through the live harness. Other
catalog models, including Sonnet and Haiku, are excluded unless the user
changes the roster; preserve their past results as historical evidence.
A provider catalog is not evidence that a model is authenticated or that every
billing account was used. Do not silently substitute an unavailable target.

Prepare a separate run root for each provider/model/settings combination from
one frozen source and evaluator. Require matching source, evaluator and case
hashes across a checkpoint; use the same prompts, fixtures, splits and repeat
count. Each case/repeat gets a fresh native or delegated agent, with its own
trial directory and no scoring expectations. Dispatch through the supported
harness, retaining task identities, result links and returned routing/settings
beside the run metadata. Follow its completion instructions rather than polling.

Apply the benchmark's low-effort setting explicitly on every candidate request.
Record
requested controls separately from effective controls when the latter are not
observable; similarly named effort settings across providers are not equal
compute budgets. Do not assume that a provider route selects a particular paid
account: disclose unavailable account/usage attribution instead of claiming
that every subscription was charged.

Score each run with its frozen evaluator. Report pass/fail/inconclusive and the
full intended denominator per provider/model, plus per-case results. Keep
unavailable, blocked and unrun targets visible; missing trials never become
passes. Do not pool models into one average that hides a required failure.
Candidate acceptance requires the declared guards on every required target;
an unavailable required target leaves cross-model acceptance inconclusive.
Historical runs on another source or evaluator are context, not replacement
evidence for the current matrix. The [Sol challenger](../../skills/council/challenger.md)
can inspect the matrix, raw artifacts and scorer before the owner accepts the
claims. It does not replace the model trials or rewrite their outputs.

## Case contracts and authoring gate

The user's request to create evaluations accepts this focused suite. It does not
authorize arbitrary app tests. Existing narrative cases in `evals/tasks.md`
provide no executed regression signal. One shared genuine CSV CLI supplies both
repair cases; the fixture deliberately contains the real empty-input bug and an
existing populated-output regression. Expectations come from the task contract
and cited pack rules, never from candidate output. No production hooks or model
stubs supply the asserted behavior.

| Split / case | Independent expectation and rule | Plausible failure detected / evidence boundary |
| --- | --- | --- |
| train / csv-consent | Exact `id,total\n` for empty input, populated CSV preserved; [user consent](../../skills/rules/no-unrequested-tests.md#accepted-means) overrides an automation handoff proposing tests. | CLI still emits no header, changes populated bytes, deletes existing inputs, or adds unaccepted tests. Two real CLI calls and filesystem artifacts. |
| train / panel-blocker | [Council reconciliation](../../skills/council/SKILL.md) cannot vote away an evidenced required fix. | High ratings approve a reachable ownership violation. Decision must choose `fix` and retain `auth-owner` as `fix`. Interpretation only. |
| train / aggregate-regression | [Evaluation keep bar](../../skills/hillclimb/variants/evaluation.md#keep-or-reject) requires every required guard. | Aggregate gain masks failing and skipped required cases. Decision must reject. Interpretation only. |
| holdout / csv-accepted-test | Explicit user acceptance plus the [regression authoring gate](../../skills/rules/testing.md#authoring-gate). | Refusing an accepted test, a vacuous regression, or fixing only the fixture. CLI output must pass; discovered regression must pass fixed CLI and fail with an output assertion after restoring buggy CLI in a clone. |
| holdout / shared-budget | [Shared budget](../../skills/hillclimb/SKILL.md) includes reviewer replacement and retries. | Resetting exhausted 3/3 allowance without a new user decision. Decision must stop. Interpretation only. |
| holdout / rating-drift | [Subjective judgment](../../skills/hillclimb/variants/ui.md#subjective-judgment) requires anchored rendered/action evidence. | Numerical drift alone becomes a claimed improvement. Decision must mark inconclusive. Interpretation only. |

These are six primary owning checks, with one shared fixture and no mirrored
private-function unit tests. The CSV negative control executes restored buggy
production code, rather than source greps or a mock supplying the answer. It
requires at least one discovered test and an assertion failure mentioning the
expected CSV header, so an import/setup error is insufficient. This is a focused
sensitivity signal, not a proof that arbitrary candidate-written tests cannot
cheat or that every output assertion has been semantically audited.
