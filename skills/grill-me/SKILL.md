---
name: grill-me
description: >-
  Relentless interview to sharpen a plan or design. Use when the user wants to
  stress-test thinking before coding, or says grill me / interview me.
disable-model-invocation: true
---

# Grill Me

Interview the user relentlessly about every aspect of the idea until you share understanding.

## Rules

1. Walk each branch of the decision tree. Resolve dependencies one by one.
2. For every question, give your **recommended answer** first so they can accept in one word.
3. Ask **one question at a time**. Wait for the answer.
4. If a *fact* is in the repo or tools, look it up — do not ask.
5. *Decisions* belong to the user — put each to them and wait.
6. Do **not** implement feature code until they confirm shared understanding. Then `/create-plan` (disk plan) or `/goal` may proceed — no Plan mode.

## After shared understanding

If the work is multi-file / extraction / UI state, ask **one** shape question (recommended answer first): hook vs class vs facade — default from `/taste` + nearby siblings.

Recommend next step:

- Multi-file / extraction / UI state → `/architecture` (with `/taste`), then `/create-plan` or `/goal`
- Verifiable long-running outcome → `/goal`
- Otherwise → `/create-plan`, or stop if they only wanted clarity
