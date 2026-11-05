# Adversarial challenger

The council's bounded challenge pass questions the completed job and the
reported results before the owner decides. This is a serious reviewer, not an
ignored jester. The user may omit the pass or explicitly override its settings.

## Model and routing

The user's selected challenger is **Codex GPT-6.1 Sol at xhigh**. This explicit
choice governs this role; it does not raise other members' effort.

Resolve the matching Codex provider and availability from the live catalog.
In T3 Code, use `delegate_task` with `target.model: "gpt-6.1-sol"` and
`target.options.reasoningEffort: "xhigh"`, not a model request in prompt text
alone. Follow the installed routing and completion instructions. Outside T3,
use a supported route that can express both settings. Report unavailable or
unverifiable controls; do not silently substitute another model or effort.
Distinguish requested/returned configuration from observed effective settings.

Use a fresh context even if Sol was an independent panel member. This is a
post-panel role, not a fourth provider or an extra vote. Its pass shares the
parent's round budget under [Council](SKILL.md#process).

## Brief and scope

Give it the pinned request and done-when criteria, scope, actual diff or work
artifacts, raw check/eval results and their revision/configuration, factual
panel findings, and the owner's proposed conclusion. Preserve user decisions,
test consent and permission limits. Do not supply the implementation chat or
require a particular objection. Let it inspect the relevant actual files.

Have it read the applicable `AGENTS.md`, selected skills and their linked rules,
including [code quality](../rules/code-quality.md),
[code structure](../rules/code-structure.md), and the
[review evidence bar](../review/contract.md#evidence-bar). For an eval claim,
inspect the evaluator, independent expectations, raw artifacts and coverage
limits, not only the aggregate score or the agent's completion message.

Ask it to challenge whether the requested job was completed, whether artifacts
and executed checks support each claimed result, whether a counterexample or
weakened scorer invalidates the conclusion, and whether the work respects the
applicable skills. Distinguish an evidenced defect from missing proof and
personal preference. It must be free to conclude **no supported objection**;
manufactured disagreement, a severity quota and an automatic veto are forbidden.

The role is read-only: no fixes, test authoring, publishing, user questions or
subagents. Live evidence collection stays with [verification](../verification/SKILL.md);
return missing proof to the owner rather than inventing or bypassing it.

## Return

Return a verdict of **supported**, **changes required**, or **inconclusive**.
For each objection, give a stable finding ID, violated requirement or skill/rule
pointer, concrete failure condition, actual file/artifact evidence, impact and
smallest correction or missing check. Identify unsupported completion claims.
The owner validates and dispositions each finding; the challenger does not
dispatch fixes, waive requirements or start another review loop.
