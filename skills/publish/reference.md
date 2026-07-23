# Publish Reference

Load this when locking type/ticket, naming a branch, drafting a PR, or publishing.

## Change types and branch names

| Type | Branch prefix | Use when |
| --- | --- | --- |
| Feature | `feature/` | New capability or intentional enhancement |
| Tweak | `tweak/` | Small bounded intentional adjustment, not a defect or standalone capability |
| Bug | `bug/` | Defect fix |
| Refactor | `refactor/` | Structural change with no intended product behavior change |

```text
{type}/{ticket}-{slug}
```

- `ticket`: Linear ID, GitHub issue number, or `no-ticket` only after the user explicitly chooses it.
- `slug`: lowercase kebab-case verb phrase.
- No spaces or colons; keep below roughly 60 characters when practical.

Examples: `bug/IN-1234-fix-checkout-total`, `tweak/IN-1234-adjust-empty-state-copy`, `feature/ENG-99-add-invite-flow`, `refactor/42-extract-billing-service`.

## Type and ticket questions

```markdown
## Questions
Reply like: 1a 2a

1. Change type?
   - a) Feature ← recommended when this adds or enhances a capability
   - b) Tweak ← recommended when this is a small intentional adjustment, not a defect or standalone capability
   - c) Bug ← recommended when this fixes broken or wrong behavior
   - d) Refactor ← recommended when this moves or cleans up debt without new behavior
2. Ticket?
   - a) <detected IN-#### / #N> ← recommended when present
   - b) Other — paste a Linear ID, GitHub issue, or URL
```

## Branch announcement

```markdown
## Locked (correct if wrong)
**Type:** Bug
**Ticket:** IN-1234
**Branch:** `bug/IN-1234-fix-checkout-total`
**Base:** `main`
**Push:** yes
```

## Draft and publish questions

```markdown
## Questions
Reply like: 1a

1. Draft a PR and publish it?
   - a) yes — show draft first, then publish ← recommended
   - b) no — stop after branch and push
   - c) draft only — show in chat, do not create
```

```markdown
## Questions
Reply like: 1a

1. Publish this PR as shown?
   - a) yes ← recommended
   - b) no — say what to edit
```

## Create command

```bash
gh pr create --title "<title>" --base <base> --body "$(cat <<'EOF'
<approved body>
EOF
)"
```

Title shape: `[IN-1234] Short imperative summary` or `[#42] Short imperative summary`.

## PR body templates

### Feature

```markdown
## Type
Feature

## Ticket
<Linear URL or `IN-1234` · GitHub `#N`>

## What changed
- …

## How to QA
1. …
2. …
- [ ] Expected: …

## Notes
- … (omit section if none)
```

### Tweak

```markdown
## Type
Tweak

## Ticket
<Linear URL or `IN-1234` · GitHub `#N`>

## What changed
- Adjusted: …

## How to QA
1. …
2. Confirm the intended adjustment: …
- [ ] Adjacent behavior remains unchanged

## Notes
- … (omit section if none)
```

### Bug

```markdown
## Type
Bug

## Ticket
<Linear URL or `IN-1234` · GitHub `#N`>

## What changed
- Fixed: …
- Root cause (if known): …

## How to QA
1. Repro steps that used to fail: …
2. Confirm expected behavior: …
- [ ] Bug no longer reproduces
- [ ] No obvious regression in adjacent flow

## Notes
- … (omit section if none)
```

### Refactor

```markdown
## Type
Refactor

## Ticket
<Linear URL or `IN-1234` · GitHub `#N`>

## What changed
- Moved or reshaped: …
- What must not change: …

## How to QA
1. …
2. …
- [ ] Behavior still holds
- [ ] No new product behavior landed with this PR

## Notes
- … (omit section if none)
```
