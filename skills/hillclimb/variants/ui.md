# UI and experience variant

A [hillclimb](../SKILL.md) variant.

## Picks it

The goal is how a scoped journey looks or feels to use: alignment, spacing,
hierarchy, clutter, friction, too many clicks or steps, transitions, and
loading, empty or error states. The user will judge it by using or looking at
the rendered flow.

## Read when

- Every run: existing `docs/design.md`; reuse its components, tokens, brand and
  interaction constraints.
- A correction that needs `docs/design.md` or blends into existing screens:
  [design initialization/blending](../../rules/user-experience.md#initialization).

## Roles

- Reviewer: the shared `reviewer` role, judging rendered evidence as a
  **visual-and-experience reviewer**.
- Implementer: the shared `designer` role for UI code, done by the parent by
  default.

## Evidence

- The reviewer inspects rendered views or captured images alongside
  action/result observations; text-only summaries do not establish visual
  polish.
- Comparable means the same data, viewport, build and meaningful states.
  Candidate evidence covers touched keyboard/focus, responsive,
  loading/empty/error, cancel/retry and continuation paths.
- A rating is subjective. Never present it as measured UX, real-user
  preference or conversion evidence.

### Subjective judgment

Compare the baseline and candidate on the named task: which is better, why,
and what regressed?

Pin any user-supplied reference designs and keep them unchanged across rounds.
Match comparable tasks and states; references inform quality, not permission
to replace the product's identity. Show baseline and candidate without winner
labels, randomize presentation order where practical, and withhold previous
ratings and target scores from fresh reviewers. Preserve essential context,
constraints and factual finding records needed for a focused rereview.

An unchanged reference receiving different ratings is judgment drift. Recheck
borderline gains against the same anchors; if the claimed improvement depends
only on shifting numbers, mark it inconclusive.

## Lens

Judge a premium, sleek, comfortable result within the product's own identity:

- Alignment, consistent spacing/padding, typography and hierarchy: cite the
  affected rendered state and task impact. Keep the brand and design tokens.
- Restrained surfaces and grouping: flag nested-card clutter without deleting
  meaningful structure or expert capability.
- Flag friction in existing modals and scope
  any change; preserve necessary confirmation/recovery flows.
- Clean transitions and icon-state changes that explain state. Preserve
  responsiveness and reduced motion; avoid decorative animation overload.
- Comfortable keyboard/focus, readable states, overflow and responsive layouts;
  preserve data and continuity through loading, error, empty, cancel and retry.

## Keep or reject

Keep a numbered change when the rendered comparison shows its named friction
resolved and every guard holds. Fix or drop it when it:

- Weakens keyboard/focus, accessibility, reduced motion, or data and state
  continuity through loading, error, empty, cancel or retry.
- Adds a modal nobody asked for, a heading subtitle, or copy that repeats what
  the screen shows.
- Removes meaningful structure, a necessary confirmation, or expert capability.

A prettier screenshot does not excuse a harder task or a hidden regression.

## Report

Each kept round and the final report show baseline and candidate side by side
with numbered highlights on every changed region, and one line per number
saying what changed and why.
