# UI and experience variant

A [hillclimb](../SKILL.md) variant. The shared loop, budget and ownership stay
in the skill; this file only says what to judge and what counts as better.

## Picks it

The goal is how a scoped journey looks or feels to use: alignment, spacing,
hierarchy, clutter, friction, too many clicks or steps, transitions, and
loading, empty or error states. The user will judge it by using or looking at
the rendered flow.

## Read when

- Every run: [user experience](../../rules/user-experience.md) and existing
  `docs/design.md`. Reuse components/tokens, brand and interaction constraints,
  including the
  [no-obvious-copy rule](../../rules/user-experience.md#dont-tell-the-obvious):
  do not add unnecessary heading subtitles.
- A correction that needs `docs/design.md` or blends into existing screens:
  [design initialization/blending](../../rules/user-experience.md#initialization).

## Roles

- Reviewer: the shared `reviewer` role, judging rendered evidence as a
  **visual-and-experience reviewer**.
- Implementer: the shared `designer` role for UI code.

## Evidence

- The reviewer inspects rendered views or captured images alongside
  action/result observations; text-only summaries do not establish visual
  polish.
- Comparable means the same data, viewport, build and meaningful states.
  Candidate evidence covers touched keyboard/focus, responsive,
  loading/empty/error, cancel/retry and continuation paths.
- A reviewer may give a subjective rating under the judgment method below.
  Never present it as measured UX, real-user preference or conversion evidence.

### Subjective judgment

No programmatic score is required. Compare the baseline and candidate on the
named task: which is better, why, and what regressed? A requested
[council](../../council/SKILL.md) supplies independent judgments of the same
rendered evidence. If ratings out of 10 are used, freeze the rubric and report
the reasons and each member's rating; do not average away a required defect.

Pin any user-supplied reference designs and keep them unchanged across rounds.
Match comparable tasks and states; references inform quality, not permission
to replace the product's identity. Show baseline and candidate without winner
labels, randomize presentation order where practical, and withhold previous
ratings and target scores from fresh reviewers. Preserve essential context,
constraints and factual finding records needed for a focused rereview.

An unchanged reference receiving different ratings is evidence of judgment
drift. Recheck borderline gains against the same anchors; if the claimed
improvement depends only on shifting numbers, mark it inconclusive. A rating
target never overrides the rendered task evidence or regression guards below.

## Lens

Judge a premium, sleek, comfortable result within the product's own identity:

- Alignment, consistent spacing/padding, typography and hierarchy: cite the
  affected rendered state and task impact rather than imposing a new aesthetic.
- Restrained surfaces and grouping: flag nested-card clutter without deleting
  meaningful structure or expert capability.
- No new modals unless the user asks. Flag friction in existing modals and scope
  any change; preserve necessary confirmation/recovery flows.
- Clean transitions and icon-state changes that explain state. Preserve
  responsiveness and reduced motion; avoid decorative animation overload.
- Comfortable keyboard/focus, readable states, overflow and responsive layouts;
  preserve data and continuity through loading, error, empty, cancel and retry.
- Preserve meaningful behavior, accessibility and developer/agent experience.

## Keep or reject

Keep a candidate when the rendered comparison shows the named friction resolved
and every guard holds. Reject it when it:

- Weakens keyboard/focus, accessibility, reduced motion, or data and state
  continuity through loading, error, empty, cancel or retry.
- Adds a modal nobody asked for, a heading subtitle, or copy that repeats what
  the screen shows.
- Removes meaningful structure, a necessary confirmation, or expert capability.

A prettier screenshot does not excuse a harder task or a hidden regression.
