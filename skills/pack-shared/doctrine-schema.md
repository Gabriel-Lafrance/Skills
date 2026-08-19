# Doctrine schema

Every `skills/*/doctrine.md` uses **these H2s, in this order, with these names**.
Do not invent `## Ownership`, `## Core rules`, or `## Process` in doctrine.

| Order | H2 | What goes here |
| --- | --- | --- |
| 1 | **Job** | One sentence. What this file is for. |
| 2 | **Owns** | What this skill decides. |
| 3 | **Does not own** | What it must not decide, plus a link to the file that does. |
| 4 | **Cite keys** | `skill:slug` to heading. If none: `none (uses taste:* and architecture:*)`. |
| 5 | **Bars** | Canonical definitions only. Tables. No numbered how-to. |
| 6 | **Output** | Artifact to emit, or `none (see process.md)`. |
| 7 | **Apply** | When this changes the work. When to load and keep the existing shape. |
| 8 | **Anti-patterns** | What this skill must not do. |

## Author rules

1. Extra detail goes under **Bars** as `###` subheads, or to `examples.md` / `reference.md`.
2. Numbered process steps belong in `process.md`, not doctrine.
3. Do not restate another skill’s Bars. Cite the key (`taste:keep-jobs-apart`).
4. Omit a section only with an explicit `none` line so a reader does not think the file was cut off.
5. Heading text must match this list exactly.

Contracts in this folder (`review-contract.md`, `asking.md`, …) are not `doctrine.md`. They still keep Job / Owns / Output when they define a return shape.
