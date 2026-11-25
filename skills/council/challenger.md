# Adversarial challenger

## Model and routing

Use **Codex Astra 6.2 at xhigh**, the
[review affinity](../rules/main-context.md#task-affinity). Resolve it from the
live catalog under the [panel selection rules](SKILL.md#panel); never
substitute Sol. The user may omit this pass or override its settings.

In T3 Code, pass the resolved ID as `target.model` and set
`target.options.reasoningEffort: "xhigh"` through `delegate_task`.
Elsewhere use a route that supports both controls. Record requested and
observable effective settings. Report unavailable controls. Use a fresh context.

## Brief and scope

Give it the pinned request and done-when criteria, scope, actual diff or work
artifacts, raw check/eval results and their revision/configuration, factual
panel findings, and the owner's proposed conclusion. Preserve user decisions,
test consent and permission limits. Do not supply the implementation chat or
require a particular objection.

Have it read the applicable `AGENTS.md`, selected skills and their linked rules,
including [code quality](../rules/code-quality.md),
[code structure](../rules/code-structure.md), and the
[review evidence bar](../review/contract.md#evidence-bar). For an eval claim,
it inspects the evaluator, independent expectations, raw artifacts and
coverage limits, not only the aggregate score or the agent's completion
message.

Ask it to challenge whether the requested job was completed, whether artifacts
and executed checks support each claimed result, whether a counterexample or
weakened scorer invalidates the conclusion, and whether the work respects the
applicable skills. It separates an evidenced defect from missing proof and
personal preference. It may conclude **no supported objection**; manufactured
disagreement, a severity quota and an automatic veto are forbidden.

The role is read-only: no fixes, test authoring, publishing, user questions or
subagents. Live evidence collection stays with [verification](../verification/SKILL.md);
it returns missing proof to the owner instead of inventing or bypassing it.

## Return

Return a verdict of **supported**, **changes required**, or **inconclusive**.
For each objection, give a stable finding ID, violated requirement or skill/rule
pointer, concrete failure condition, actual file/artifact evidence, impact and
smallest correction or missing check. Identify unsupported completion claims.
