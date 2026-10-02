# Shipping templates

Question, announcement, and pull request body templates for [shipping.md](shipping.md). The rules and steps that use them live there.

## Questions and announcements

Shapes follow [Asking the user](writing-style.md#asking-the-user).

Type and ticket:

```markdown
## Questions
Reply like: 1a 2a

1. Change type?
   - a) Feature ← recommended when this adds or enhances a capability
   - b) Tweak ← recommended when this is a small intentional adjustment, not a defect or standalone capability
   - c) Bug ← recommended when this fixes broken or wrong behavior, including an urgent production defect
   - d) Refactor ← recommended when this moves or cleans up debt without new behavior
   - e) Chore ← recommended when this is non-product maintenance (deps, CI, tooling, docs)
2. Ticket?
   - a) <detected IN-#### / #N> ← recommended when present
   - b) Other: paste a Linear ID, GitHub issue, or URL
   - c) no-ticket (you said there is none)
```

Branch announcement (sent as a Locked in message):

```markdown
## Locked in (tell me if this is wrong)
**Type:** Bug
**Ticket:** IN-1234
**Branch:** `bug/IN-1234-fix-checkout-total`
**Base:** `main`
**Push:** yes
```

Draft and publish:

```markdown
## Questions
Reply like: 1a

1. Draft a PR and publish it?
   - a) yes: show draft first, then publish ← recommended
   - b) no: stop after branch and push
   - c) draft only: show in chat, do not create
```

```markdown
## Questions
Reply like: 1a

1. Publish this PR as shown?
   - a) yes ← recommended
   - b) no: say what to edit
```

## PR title and body

Title shape: `[IN-1234] Short imperative summary` or `[#42] Short imperative summary`.

### Change diagram

Every PR body has a **high-level** Mermaid diagram of what changed: modules, actors, and request/data flow, not every function or file.

| Shape of work | Diagrams |
| --- | --- |
| **New** (new capability, net-new path, additive tweak/chore) | One diagram under `## Change diagram` |
| **Rework** (refactor, structural move, bug that changes the flow) | `### Before` and `### After` under `## Change diagram` |

- Omit the section only when the diff is truly diagram-hostile (typo-only) and say why in Notes.
- Keep node labels short. Use `flowchart`, `sequenceDiagram`, or `graph`, whichever is clearest.
- Name real modules, services, or routes from the diff, and only those.
- For Before/After, keep the same node ids so the delta is obvious.
- Put the diagram after **What changed** and before **How to QA**.

Rework example:

````markdown
## Change diagram

### Before

```mermaid
flowchart LR
  UI[Checkout UI] --> Stripe[Stripe]
  UI --> DB[(orders)]
```

### After

```mermaid
flowchart LR
  UI[Checkout UI] --> Billing[billing.makeUserPay]
  Billing --> Stripe[Stripe]
  Billing --> DB[(orders)]
```
````

### Blast radius and merge danger

End every new or updated PR description with `## Blast radius and merge danger`, after Notes and any stack or verification details. Use it for every publication tool, the repository template, and each PR in a stack. Assess the actual delta against that PR's base and the current checked result; refresh the assessment when either changes.

Adapted from the door and blast-radius framing in [Matt Pocock's pinned PR skill](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/pr/SKILL.md). Keep this pack's existing body, test-approval, verification, and shipping gates.

- **Blast radius:** Name affected surfaces, users or callers, and meaningful dependencies. Explain relevant behavior, data, security, or rollout consequences. File count alone is not impact; do not invent unrelated hazards.
- **Door:** Choose two-way, one-way, mixed, or unknown from the actual rollback path and its limits. A code revert does not necessarily restore deleted data, undo external effects, clear persistent state, or recover older consumers.
- **Evidence and remaining checks:** State what was actually verified and its limits, referring to How to QA or Notes without copying logs. Identify residual unknowns and required rollout or human checks, with an owner when known. Planned checks are not passes.
- **Merge danger:** Give a concise judgment with the evidence and conditions that justify it. Green CI alone does not establish low danger or operational readiness. Avoid unsupported safe/none boilerplate. This assessment never grants merge permission or replaces existing gates.

Scale detail to the change. A scoped copy fix may need one short sentence per field; a destructive migration needs its actual compatibility, recovery, and rollout limits. When evidence is missing, say what is unknown instead of guessing.

### Body template

Start from the base template, then apply the row for the locked type. A row's checkboxes replace the base `- [ ] Expected: …` line.

````markdown
## Type
<Feature | Tweak | Bug | Refactor | Chore>

## Ticket
<Linear URL or `IN-1234` · GitHub `#N`>

## What changed
- …

## Change diagram

```mermaid
flowchart LR
  A[Entrypoint] --> B[Changed path]
```

## How to QA
1. …
2. …
- [ ] Expected: …

## Notes
- … (omit section if none)

## Blast radius and merge danger
- **Blast radius:** <affected surfaces, users/callers, dependencies, and relevant consequences>
- **Door:** <two-way | one-way | mixed | unknown; actual rollback path and limits>
- **Evidence and remaining checks:** <actual verification and limits; unknowns or required checks>
- **Merge danger:** <grounded assessment, reasons, and conditions; never merge permission>
````

| Type | What changed bullets | Change diagram | How to QA |
| --- | --- | --- | --- |
| Feature | `- …` | One diagram: `A[Entrypoint] --> B[New capability]` | Base steps; `- [ ] Expected: …` |
| Tweak | `- Adjusted: …` | One diagram: `A[Existing surface] --> B[Adjusted behavior]` | Step 2 `Confirm the intended adjustment: …`; `- [ ] Adjacent behavior remains unchanged` |
| Bug | `- Fixed: …` and `- Root cause (if known): …` | Before/After: `A[Trigger] --> B[Broken path]`, then `A[Trigger] --> B[Correct path]` | Step 1 `Repro steps that used to fail: …`; step 2 `Confirm expected behavior: …`; `- [ ] Bug no longer reproduces`; `- [ ] No obvious regression in adjacent flow` |
| Refactor | `- Moved or reshaped: …` and `- What must not change: …` | Before/After: `Caller --> OldShape[Old module/layout]`, then `Caller --> NewShape[New module/layout]` | Base steps; `- [ ] Behavior still holds`; `- [ ] No new product behavior landed with this PR` |
| Chore | `- Maintained: …` | One diagram: `Tooling[CI / deps / docs] --> Outcome[Maintenance outcome]` | Step 2 `Confirm maintenance outcome: …`; `- [ ] Intended maintenance landed`; `- [ ] No unintended product behavior change` |

