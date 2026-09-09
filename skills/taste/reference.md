# Taste reference

Load with [doctrine.md](doctrine.md) when verifying, touching UI, or naming an extension seam. Bars stay in doctrine. Snippets stay in [examples.md](examples.md).

## Verify (terminals first)

This author almost always has **frontend localhost** and **`npx convex dev`** already running. CI owns type/lint. **Do not** re-verify by poking Convex MCP, re-running `convex` CLI, or spamming status tools.

**Prefer, in order:**

1. **Read existing terminal output** (IDE terminals folder / running `convex dev` + frontend logs) for push success, compile errors, HMR, runtime stacks
2. Diff + structural checks for the change
3. Only if terminals are silent or missing: say so, then ask, or start the **minimal** command once

**Do not** by default (ritual anti-patterns):

- Call **Convex MCP** (`status`, `data`, `tables`, `logs`, `run`, `runOneoffQuery`, `insights`, `functionSpec`, env tools, and similar) just to verify
- Re-run `npx convex …`, deploy, or codegen after every slice when `convex dev` is already watching
- Run `eslint`, `tsc --noEmit`, `npm run lint`, full suites, or just-to-be-sure scripts
- Start a second frontend/Convex process when one is already up
- Dispatch a subagent whose only job is MCP verification

**Do use Convex MCP / deeper checks only when:**

- Terminals show an error you cannot diagnose from the log text alone
- You need a one-off data read the user asked for
- No Convex terminal exists and you said so first
- The user explicitly asks for MCP/dashboard/CLI verification

Evidence citations should look like: `terminals/3.txt: convex push ok` (terminal filename, then what it showed). Not a fresh MCP round-trip.

Cite `taste:verify-terminals-first`.

## React and UI

- **Mobile first**, then widen
- One component per file (`taste:one-export-per-file`); keep components thin. Complexity lives in a hook or class behind the entry
- When touching marketing/landing UI, avoid AI-default looks: purple-on-white gradients, cream+terracotta serif clichés, flat single-color voids, card-heavy heroes, pill clusters, emoji decoration
- App UI follows `/design` (`design:experience`, `design:first-glance`, `design:professional-craft`, `design:ui-copy`, `design:quality-floor`): match the product's identity, do the next input when it is obvious, show only what everyone needs at first glance, and ship finished, not a restyle draft
- Landing first viewport: brand + one headline + one line + CTA + one dominant image. Nothing else

## Patterns and SOLID

- Refactoring Guru style patterns are welcome when they suit a useful case (Strategy, Facade, Adapter, Observer, and similar)
- **Big features:** lay the foundation early (seam + first implementation) so adding the next variant does not reopen the core
- **Tiny glue / local helpers:** skip ceremony; a plain function or single class is enough (`taste:keep-it-simple`)
- **SOLID is guidance, not scripture.** Use it to keep foundations extendable and readable. Stop when it becomes interface theater (factory-of-factories, empty base classes, one-line impl files with no behavior)
- Never require a second production implementation *before* introducing the seam on a big feature. That is the opposite of this taste

## Futureproofing

When building a **non-trivial / big feature**, build a bulletproof foundation from day one so growth is additive, not a rewrite every time something is added. Still apply `taste:keep-it-simple` to everything that is not the named seam:

- **Open to extension:** new behavior lands via new collaborators, strategies, or narrow hooks, not by rewriting call sites
- **Closed to breaking edits:** stable entry-point signatures; avoid forcing callers to change when internals grow
- **Put the seam in first:** interfaces / strategy slots / composition points belong in the initial design when the domain will grow (payments, notifiers, providers, channels). Do **not** wait for a second implementation before shaping the foundation. That causes perma re-editing
- Ship **one real implementation** behind that seam on day one; the seam is the foundation, not unused dead code
- Do **not** future-proof tiny one-off glue with empty hierarchies or config for imaginary products (`taste:keep-it-simple`)

Plans and structure cards **must** name the extension seam for big features.
