---
name: maintain-formal-verification-skill
description: Use only when the user asks for /maintain-formal-verification-skill, asks whether a formal model is still true to the code, or after merges and refactors touched verified code without rechecking it.
category: Code
disable-model-invocation: true
---

# Maintain a formal verification skill

A formal check proves a property of what it describes. When the code changes and the verification does not, the check can keep passing while it describes code that no longer exists. That pass is the dangerous case, because it looks like a proof. This skill is the upkeep loop for a verify skill that [`/create-formal-verification-skill`](../create-formal-verification-skill/SKILL.md) generated, or for any project-local skill that runs a model checker, prover, or code-level verifier against named code. The project-local skill handles a change an agent makes while it uses that skill. This skill handles the changes that skipped it: merges, edits made without the skill, and drift that builds up across many commits.

Adapted from pstack's [maintain-formal-verification-skill](https://github.com/cursor/plugins/tree/b4a4f6151b8e77f8d71045f09f553a733cf0ed37/pstack/skills/maintain-formal-verification-skill) (MIT).

## Read when

- Every run, before judging whether covered code changed shape: [code-quality.md](../rules/code-quality.md), [code-structure.md](../rules/code-structure.md).
- Writing the report: [plain language](../rules/writing-style.md#plain-language).

## Outcomes

Give each check one outcome, and say which:

- **in sync**: no change since the last sync alters what the check describes, and the check passes.
- **updated**: the verification changed to match current code, and the check passes.
- **bug**: the verification describes the current code, and the code breaks the property. This is a finding about the code. It is not drift.
- **blocked**: the check could not be brought back in line or could not run. Say exactly why.

If an update exposes a bug, report **bug** and describe the update.

Edit only the verification: models, harnesses, property files, and the verify skill itself. Never edit product code during a run, unless the user asks. When a property fails on the current code, do not weaken the property or the model to make it pass. Report the failure. Put the verification updates in a change of their own, separate from any product fix.

## Process

1. **Find the checks.** A verify skill has no fixed name, so find it by what it does: a project skill that runs a model checker, a prover, or another verifier against named code. Read each one you find, or the one the user named. For each check, collect the property, the code it covers, the bounds and assumptions, the command that runs it, and the commit where it was last confirmed to describe the code. If no verify skill exists, stop and point at [`/create-formal-verification-skill`](../create-formal-verification-skill/SKILL.md). If the skill does not record a sync commit, use the last commit that changed the verification files, and say you did.
2. **Run it as it is.** Run each check once before you change anything, and record the result. A pass here does not tell you the code is correct; it tells you the old description still holds. A failure here can be drift or a bug. Do not decide which until step 5.
3. **Read every change to covered code.** Diff the covered files from the sync commit to the current commit, and read each commit message. Also look for code that moved: a covered function renamed, split, or moved to another file is still covered code. Also look for new code that touches the state a check guards, such as a new function that writes the same fields. For each change, decide which of these it is:
   - **No effect.** The change alters nothing the verification describes, such as formatting, comments, or code paths the verification does not cover. Check this against the model or harness, not against the commit message.
   - **The verification no longer describes the code.** A step that was one indivisible action is now two, a branch was added or removed, a check moved, a new path reaches the guarded state, or a value now has a different range. The model or harness must change.
   - **The promise changed on purpose.** The change alters what the code promises, and evidence in the change says that is intended: the doc comment, the tests, the changelog, or the commit message. The property must change, and you must cite that evidence.
   - **The promise may be broken.** The code changed, and no evidence says the promise changed. Treat a failure that follows as a bug candidate.
4. **Update from the code, not from the result.** Change the model or harness so each changed part again points to code a reviewer can open, and keep one indivisible step in the code as one step in the verification. Write the update from the code before you rerun; do not shape it by what makes the check pass. Change a property only for a promise that changed on purpose. Write down the old wording, the new wording, and the evidence. Keep the bounds unless the change makes them wrong. If you must reduce a bound, say so in the report.
5. **Rerun and judge each result.**
   - **Pass:** use a scratch code mutation to show the check still catches the guarded failure. For standalone models, model the same mutation and replay its counterexample against the broken code. Then drop the scratch changes.
   - **Fail:** replay the counterexample against the real code, step by step. If a step cannot happen in the code, the verification is wrong. Fix the verification, and say what was wrong. If every step can happen, it is a bug. Name the commit that introduced it, tell the counterexample as a sequence of steps in the code's own words, and state the harm in one sentence. If a cheap test or reproduction against the real code shows the bug, add it to the report as evidence; do not commit it to the product code. For a TLA+ check, read the result with [`/statechart`](../statechart/SKILL.md).
6. **Update the verify skill.** Update coverage, commands, bounds, and assumptions. Follow the verify skill once on the final code and verification snapshot. Advance the sync commit only for a completed check whose covered code matches that commit. For blocked checks or uncommitted changes to covered code, keep the previous sync commit and report why.
7. **Report.** For each check: the outcome and the commits you read; what changed in the verification and why, with a short reason per change (the code changed shape, or the promise changed on purpose, with the evidence); the rerun result and the break you used to show the updated check can still fail; each bug in plain words, with the counterexample as steps in the code's words, the harm, and the commit that introduced it; and what the verification still does not cover, including new code it should cover and does not. Say outright which failures were drift in the verification and which were bugs in the code. For a check that passed before you updated it and fails after, say that the old pass was on a stale description.

## Anti-patterns

- Treating a pass on a stale description as proof the code is correct
- Updating the model from what makes the check pass instead of from the code
- Moving the sync commit forward for a blocked check
- Editing product code, or folding a product fix into the verification update
