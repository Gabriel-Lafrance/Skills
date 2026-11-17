# Statechart reference

## Reading the report

- A state that breaks a rule has the class `breaks`. When only some model states behind it break the rule, it has the class `mayBreak`. The Legend names the rules of each mark. When two rules break on one mark, the Legend names both, so say in the hand-off which state breaks which rule. In a regions chart, a state gets a mark when each combination of region states that includes it can break a rule; when a combination can break a rule and none of its states has a mark, each state in that combination gets one.
- TLC goes past a state that breaks a rule, so the chart shows the states after a bug. Because of that, a model with no limit on its states can run without end. Keep the constants small, or add a CONSTRAINT.
- With a VIEW or a SYMMETRY, TLC counts states it treats as the same as one state, and the chart draws that one state. An arrow can lead to it rather than to the state the step reaches; the report says so.
- TLC checks the rules in each state past a CONSTRAINT or an ACTION_CONSTRAINT, but does not explore that state or check it for deadlock. When TLC's shortest path for a rule ends in such a state, the chart draws it and the report gives that path; other states past the bound are not drawn, and a deadlock there does not show. TLC also checks the rules after each step an ACTION_CONSTRAINT excludes, even when it reaches the next state another way; a shortest path ending with such a step is drawn.
- The command checks the rules with TLC on the config as written, with one worker. When a rule breaks, it removes that rule and runs TLC again, until no rule breaks. After the first break, each run stops at 100,000 distinct states. When a run reaches that bound or stops on an error, the report lists the unchecked rules under "Rules not checked" and the chart does not mark them. An unchecked rule can hold or break; to check it, remove the rules that break from the config, or make the model smaller. The bound adds a module that changes TLC's order of the variables, so for a property TLC can find a different counterexample than a run without the bound.
- `tlc.out` is what TLC printed on the config as written. When the chart does not show the bug path of a rule that breaks, `tlc-RULE.out` is what TLC printed for the run that found it. When TLC repeats its first warning, plain TLC prints it twice but `tlc.out` shows it once, since TLC leaves the second copy out of the output this command reads. That happens only when Java runs with `-XX:+UseParallelGC`.
- The chart has a budget of 500 states, counted by TLC on the config as written. Above that, the chart draws only the paths to the rules that break, and when no rule breaks, the command writes no `chart.mmd`. It still checks each rule, and the report gives the state count and each bug path. To see the whole graph, make the model smaller.

## Render a chart as an image

Render each `.mmd` file you show with the npm package `pele@1.9.0`, and give the user the SVG. Install Pele once, outside the repo. Write each SVG next to its `.mmd` file, with the same name. Pass `{ limit: 1_000_000, outputLimit: 8_000_000, maxEdges: 10_000 }` as the options of `render`; Pele's defaults are smaller than a chart of 500 states can be. When Pele throws a `PeleError`, show the user the Mermaid text and the error.

Pele ignores Mermaid `theme` and `themeVariables`; set its `--pele-*` CSS variables on `.pele`. The command gives each state the color class of its group, marks each bad state with `breaks` or `mayBreak`, each state on the shortest path to a bug with `bugPath`, and each state a PROPERTY counterexample repeats forever with `repeats`. The `.mmd` file has a `classDef` line for `breaks` and `mayBreak`, so any Mermaid viewer shows the bug marks. Pele writes each `classDef` color as a `style` attribute, and a `style` attribute wins over a normal CSS rule, so the mark rules below use `!important`. Put the mark rules after the group colors, so a mark shows over the group color. Put these colors in a `<style>` element at the start of each SVG, so each SVG follows the light or dark setting of the viewer.

```css
.pele {
  --pele-bg: #ffffff;
  --pele-fg: #1c1c1c;
  --pele-muted: #656565;
  --pele-line: #808080;
  --pele-surface: #fcfcfc;
  --pele-surface-alt: #f1f1f1;
  --pele-border: #c9c9c9;
}
.pele .blue rect { fill: #c3e0ff; }
.pele .orange rect { fill: #f0d3bf; }
.pele .purple rect { fill: #e3d5ff; }
.pele .yellow rect { fill: #f0dcbf; }
.pele .teal rect { fill: #bfe3df; }
.pele .tan rect { fill: #e5d9ce; }
.pele .pink rect { fill: #ffcbe6; }
.pele .breaks rect {
  fill: #ffecee !important;
  stroke: #e72e3b !important;
  stroke-width: 2.5px !important;
}
.pele .breaks text { fill: #cd2834 !important; }
.pele .mayBreak rect {
  fill: #fff3e6 !important;
  stroke: #e8730c !important;
  stroke-width: 2.5px !important;
}
.pele .mayBreak text { fill: #b85a06 !important; }
.pele .bugPath rect {
  stroke: #1680f3 !important;
  stroke-width: 2.5px !important;
}
.pele .repeats rect {
  stroke: #9b35d6 !important;
  stroke-width: 2.5px !important;
  stroke-dasharray: 6 3;
}
@media (prefers-color-scheme: dark) {
  .pele {
    --pele-bg: #1f1f1f;
    --pele-fg: #f5f5f5;
    --pele-muted: #acacac;
    --pele-line: #939393;
    --pele-surface: #121212;
    --pele-surface-alt: #2c2c2c;
    --pele-border: #4e4e4e;
  }
  .pele .blue rect { fill: #1b3857; }
  .pele .orange rect { fill: #573117; }
  .pele .purple rect { fill: #3c2e57; }
  .pele .yellow rect { fill: #573d17; }
  .pele .teal rect { fill: #174641; }
  .pele .tan rect { fill: #3d3127; }
  .pele .pink rect { fill: #57233e; }
  .pele .breaks rect {
    fill: #2e2021 !important;
    stroke: #cf2b35 !important;
  }
  .pele .breaks text { fill: #ff6463 !important; }
  .pele .mayBreak rect {
    fill: #2e2619 !important;
    stroke: #d0700f !important;
  }
  .pele .mayBreak text { fill: #ffa257 !important; }
  .pele .bugPath rect { stroke: #116dd2 !important; }
  .pele .repeats rect { stroke: #9a3fcf !important; }
}
```

## Provenance and updating the engine

The engine in `scripts/` is a verbatim copy of pstack's statechart scripts at commit `b4a4f6151b8e77f8d71045f09f553a733cf0ed37` (MIT, copyright Lauren Tan). Keep [LICENSE.txt](LICENSE.txt) with the skill so it travels with standalone installs. The upstream test corpus under `scripts/test/` (377 files, about 3.6 MB of TLA+ fixtures and golden outputs) is not vendored, so installs stay small; the corpus would also fail this pack's link, dash, and word-budget checks.

Treat `scripts/` as upstream code. To update it:

1. Clone `cursor/plugins` and check out the new commit to pin.
2. In that scratch clone, install dev dependencies and run `npm test` from `pstack/skills/statechart/scripts`. Set `TLA2TOOLS` and `JAVA` to include the real-TLC cases. Record failures and skips.
3. Copy only tracked files under `scripts/` at the pin, excluding `scripts/test/`. Keep the `statechart` launcher executable.
4. Run one small model end to end with the vendored copy and confirm the chart and report look right.
5. Update the pinned commit in this section, in [SKILL.md](SKILL.md), and in the pack's ATTRIBUTIONS.md. If a local edit to the engine is ever unavoidable, record it in ATTRIBUTIONS.md in the same change; an unrecorded edit makes the next update a guess.
