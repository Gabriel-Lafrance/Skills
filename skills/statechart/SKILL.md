---
name: statechart
description: Use only when the user asks for /statechart, to model-check or draw a flow, protocol, service, or state machine as a checked statechart, or to show a bug as a path through states.
category: Code
disable-model-invocation: true
---

# Statechart

Check a TLA+ model of a system that moves between states and draw it as a Mermaid statechart in the reader's words. The checker tries every order of steps up to a bound, marks each state that breaks a rule, and gives the shortest path to each one. The reader, the person who owns the behavior, decides whether the behavior is right.

Adapted from pstack's [statechart](https://github.com/cursor/plugins/tree/b4a4f6151b8e77f8d71045f09f553a733cf0ed37/pstack/skills/statechart) (MIT). The chart engine in `scripts/` is vendored verbatim; see [provenance](reference.md#provenance-and-updating-the-engine).

## Read when

- Every run, before judging the model against the code it describes: [code-quality.md](../rules/code-quality.md), [code-structure.md](../rules/code-structure.md).
- Reading the report, rendering an image, or updating the engine: [reference.md](reference.md).
- Writing the hand-off: [plain language](../rules/writing-style.md#plain-language).

## Process

1. **Set up.** Work in a scratch folder outside the repo. The command is `scripts/statechart SPEC.tla [--config FILE] [--view FILE] [--out DIR]` from this skill's folder. It is TypeScript, so it needs Node 22.18 to 22.x, Node 23.6 or later, Bun 1.1.5 or later, or Deno 2.0 or later. The first run installs TLC and Java with `mise` and needs the network; or set `TLA2TOOLS` to a `tla2tools.jar` path and `JAVA` to a Java 11 or later binary.
2. **Write the spec and config.** Create an adjacent `SPEC.cfg` or pass a config with `--config`. Set `INIT` and `NEXT` or `SPECIFICATION`, and list each agreed invariant with `INVARIANT`. Add variables when a rule needs them. Never weaken a rule to make it hold. Write `Next` as a disjunction of named actions so TLC can name each step. Give intended terminal states a no-op action, such as `Done == phase \in {"paid", "failed"} /\ UNCHANGED vars`, to avoid a spurious deadlock.
3. **Pick the chart.** The judgment is yours: the words on each state and arrow, the phases and their colors, the title, and the report to the reader. Put it in a view module and pass it with `--view`. The view exports `state(vars)`: a string gives a flat chart (`v.paid ? "Paid" : "Paying"`), an array gives parent states (`v.main.split(".")`), and an object gives one parallel region per key (`{ Playback: v.playback, Volume: v.volume }`). Label each state with what the reader can see or cares about; keep variable names out of labels. A TLA+ sequence arrives as an object with keys from 1, and a set as an array.
4. **Label the arrows.** The view can export `step(action, from, to)`, returning the arrow label as the user sees it happen, such as "you press play" or "the connect fails". Never name the code or the TLA+ action. Two actions that end the same get the same label, so they share one arrow. End a label with its condition in brackets when a step happens only sometimes, such as `you press play [while the file loads]`; in a regions chart skip brackets for conditions on other regions, since the command writes those itself. When a hidden value decides where a step goes, name the result instead, such as "the roster read fails". The view can also export `group(vars)` for phase colors, `colors`, and `title`. Each function runs at most once per model state or step, so make it depend only on its arguments.
5. **Keep it readable.** Aim for about 20 arrows or fewer. Start with coarser `state()` labels: one label for values that act the same, and leave out detail the reader does not need. Keep every state on a bug path and every mark. Never merge two states that break different rules. Still too busy: return `null` from `step()` for steps the reader does not need, keeping every state reachable from a start state, at least one arrow out of each state that has one in the model, and all or none of the steps behind one arrow. Say in the hand-off which steps the chart hides. A step that stays inside one label is not drawn; split the label when the reader must see it.
6. **Run and read.** Run the command, then read the report with [reading the report](reference.md#reading-the-report): `breaks` and `mayBreak` marks, the Legend, rules not checked, and the 500-state chart budget all have fine print that changes what a result means.
7. **Show the result.** If the command wrote `chart.mmd`, show it as a `mermaid` code block. Otherwise give the report and explain the chart limit. Render SVG on request or when the chart is too large to read as text, following [render a chart](reference.md#render-a-chart-as-an-image).
8. **Hand off.** Give each chart and its Mermaid text to the person who must decide. Add one line per bug: the rule, the reader's sentence for that rule, and the path as the report numbers it. Say what the model leaves out, and give the command that makes the files again with a new `--out` folder. When the model describes code, replay each bug path against the real code, as a test or a live repro, one step per action. If a bug does not occur there, treat the model as wrong until you show it is not.

## If a parent already owns the next step

A project-local formal verification skill may name `/statechart` to read its results. Return the chart, the report findings, and what the model leaves out. The parent owns any fix. This skill never edits product code and never weakens a rule to reach a pass.

## Anti-patterns

- Weakening an invariant, shrinking the model, or merging states until the marks go away
- Labels that name variables, code, or TLA+ actions instead of what the reader sees
- Reporting a bug path that was never replayed against the real code it claims to describe
- Editing the vendored engine in `scripts/` to change a verdict
