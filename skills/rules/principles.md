# Principles

**Open this when:** you are about to make a design, verification, or delegation judgment.
**Skip it and you will:** cite a principle with no owner, or relitigate one this pack already named.

This is a steering vocabulary. One line here, the detail in the file that owns it. Rows that point at [keep-it-simple.md](keep-it-simple.md), [strong-foundation.md](strong-foundation.md), and [main-context.md](main-context.md) are already hard rules in `AGENTS.md`. Do not restate them.

Adapted in part from poteto's [pstack](https://github.com/backnotprop/pstack) (MIT). This file does not vendor those skills.

## How to use

When a principle changes a decision, name the cite form and the decision it changed.

Example: "Prove it works (real artifact): the checkout check is a double-click in the running app, not a green typecheck."

Chat uses the cite form, plain name then the classic name in parentheses ([Plain language](writing-style.md#plain-language)).

## Vocabulary

| Cite in chat | One-line rule | Open when | Detail |
| --- | --- | --- | --- |
| **Prove it works** (real artifact) | Evidence must prove the claimed outcome. A compile or typecheck alone does not prove changed runtime behavior. | About to call work done | [Verification scope](execution.md#verification-scope) selects applicable proof; [verification](../verification/SKILL.md) owns live paths. An accepted test follows [testing.md](testing.md). |
| **Match proof to risk** (risk-based verification) | Check affected behavior and dependencies; broaden for shared risk, explicit requests, or mandatory repository requirements. A small diff is not evidence of low risk. | About to choose checks or reuse evidence | [Verification scope](execution.md#verification-scope); [Git sync only](execution.md#git-sync-only) stops after a clean operational sync. |
| **Fix the root cause** (repro first) | Reproduce the failure, then fix the cause. A patch on the symptom comes back. | About to fix a bug, or the same failure returned | This row |
| **Sequence the work** (verifiable units) | Split into units you can verify before the next one starts. The active execution skill owns the build. | About to plan more than one step | [Slice split](../task/reference.md#slice-split) |
| **Fail fast** (Fail Fast) | Reject bad input at the boundary. Inside, trust the type. | About to add a check, a cast, or a parse | [Fail fast](code-quality.md#fail-fast) |
| **Types tell the truth** (make illegal states unrepresentable) | The type cannot hold an illegal combination. | About to add an optional, an `any`, or a cast | [Types tell the truth](code-quality.md#types-tell-the-truth) |
| **Keep judgment in the main context** (main context) | Keep the decision in this chat. Hand the search, the large read, and the noisy log to a subagent. | About to search, read a large file, or bulk-edit | [main-context.md](main-context.md) |
| **Encode the lesson** (in the structure) | A repeated mistake becomes a lint, an accepted test, or a type. Another paragraph does not hold it. | About to add a warning for a mistake the tools can catch | [testing.md](testing.md) for an accepted regression. Types: [Types tell the truth](code-quality.md#types-tell-the-truth). |
| **Attack the premise** (same gate, new approach) | When the same gate fails after repeated fixes, question the approach. Another patch on the same idea is the loop. | Repeated fixes have failed the same gate | This row |
| **Keep this simple** (KISS) | Least code for the result. Subtract first. Light to read. | About to add a file, layer, or abstraction | [keep-it-simple.md](keep-it-simple.md). Do not rewrite it. |
| **Strong foundation** (model the domain) | Model the domain. A seam only where the next variant would otherwise be a rewrite. | About to grill, plan, or build a Feature | [strong-foundation.md](strong-foundation.md) |

Named code-quality checks that are not in this table (keep jobs apart, one altitude, and the rest) stay in [code-quality.md](code-quality.md#named-principles).
