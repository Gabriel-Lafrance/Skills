---
name: create-formal-verification-skill
description: Use only when the user asks for /create-formal-verification-skill, to model-check a race, retry, state machine, parser, or unsafe code, or to prove an invariant that tests cannot reach.
category: Code
disable-model-invocation: true
---

# Create a formal verification skill

A test checks the cases someone thought to write. Formal verification checks every case in a stated scope: every order of steps in a model, every input up to a bound, or every input. This skill finds the part of the repo where that matters most, verifies one property of it, and leaves a project-local skill that lets the next agent check a change against that property. Write that skill for an agent who reads it cold, mid-change, and has never seen your work. The user must be able to trust the result and act on it without learning the verification language.

Adapted from pstack's [create-formal-verification-skill](https://github.com/cursor/plugins/tree/b4a4f6151b8e77f8d71045f09f553a733cf0ed37/pstack/skills/create-formal-verification-skill) (MIT).

## Read when

- Every run, before judging targets or writing verification code: [code-quality.md](../rules/code-quality.md), [code-structure.md](../rules/code-structure.md).
- Before asking the user anything: [asking the user](../rules/writing-style.md#asking-the-user).
- Writing the hand-off: [plain language](../rules/writing-style.md#plain-language).

## Process

1. **Choose the target from the code.** Answer from the codebase, and ask the user only what you cannot observe. If the user named an area or a bug, start there. A good target is a promise the code makes, where a break harms users and tests rarely reach the case that breaks it. Choose the strongest such target in the repo, not the one that is easiest to verify.
2. **Let the question choose the tool.** Use a small TLA+ model for ordering or a code verifier for properties such as overflow or data-structure invariants. A property at every size may require a proof assistant. Prefer a tool the repo's developers can install and run. If no verifier fits, report the limit. Probe the real code with generated inputs in scratch or propose a persistent test through [verification](../verification/SKILL.md), which writes only [accepted tests](../rules/no-unrequested-tests.md). Report sampled results as sampled, and stop before generating a formal skill if no formal check can run.
3. **Hold the bars.**
   - **True to the code.** Every part of the model or proof points to code a reviewer can open. What the verification treats as one indivisible step is one indivisible step in the code. Names come from this repo.
   - **Able to fail.** Show each property failing after a scratch change that removes a guard or reorders a step. For a standalone model, translate the same change into the model and replay its counterexample against the broken code.
   - **Findings stay findings.** When the current code breaks the property, report it with the counterexample in the code's terms. Do not weaken the property or the model until it passes, and do not change product code unless the user asks.
   - **Honest about scope.** Say what is verified, under which bounds and assumptions, and what is left out. A pass covers the model or the bound, not the whole system.
   - **Readable without the tool.** State the property and the harm in one plain sentence each. Tell a counterexample as a short sequence of steps in the code's words.
   - **Cheap to rerun.** One command, a reproducible tool version, and a run short enough that the next agent will use it on every relevant change.
   - **Kept in step with the code.** Record which files and functions each check covers, and the commit at which you last confirmed the verification describes them. When covered code changes after that commit, the next agent can see the verification needs another look.
4. **Generate the verify skill.** Write it in the project's existing skill root, with frontmatter that names the area and when to use it. Name the covered code, commands, bounds, and how to distinguish a code bug from a modeling error. Record the commit matching the checked code when one exists. If covered code is uncommitted, record the checked revision and diff, leaving the sync commit unset until confirmed on committed code. For TLA+ results, point to [`/statechart`](../statechart/SKILL.md) by name in the generated skill. It provides counterexamples and draws the chart within its chart budget. Keep its internal paths and options out of the generated skill.
5. **Prove it before you hand off.** Run the generated skill as written on the scratch variant from step 3. It must catch the break. Drop the scratch code and model changes and confirm the original result returns. If a step misses the break or cannot run, fix the skill or verification before handoff.
6. **Hand off.** Tell the user what you verified, which tool you used and why, the bounds, what the check found in plain words, how to run it, and what it does not cover. Suggest a second target only if you found a close one. Point the user at [`/maintain-formal-verification-skill`](../maintain-formal-verification-skill/SKILL.md) for bringing the verification back in line after changes that did not recheck it.

## Anti-patterns

- Choosing the target that is easiest to verify instead of the promise whose break costs most
- Hand-modeling a function in a checker language when no verifier runs on the code, instead of testing the real code with generated inputs
- Weakening the property or the model until the current code passes
- Handing off a generated skill that was never run end to end
