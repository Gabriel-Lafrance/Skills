# Taste Flow Doctrine

Shared style contract for this pack. **Other pack skills must read this before planning or writing code.**

For good vs bad snippets, see [examples.md](examples.md).

## Bad code = complexity and entropy

**Bad code** is whatever **increases complexity** or **entropy**. **Good code** is deep where it matters (simple surface, rich inside), orthogonal by service, and leaves the touched lane cleaner or no dirtier than before.

| Term | Meaning |
| --- | --- |
| **Complexity** | Change amplification, cognitive load, unknown unknowns — hard to understand or change safely. Prefer fewer concepts at the call site; put richness behind a **deep** entry (`/architecture` deep public surface). |
| **Entropy** | Local disorder that spreads when copied or left untouched in a lane you edit (broken windows). Touching a dirty lane without a **behavior-preserving cleanup** when you can preserve behavior **increases** entropy. |

**Operational tests** (apply before shipping a slice):

1. **Call-site** — Does the caller need internals / order / edge cases? → shallow / complex.
2. **Change** — Would a small product change touch many files for one concept? → complexity (amplification).
3. **Window** — Are we copying or extending a known-wrong shape? → entropy.
4. **Judo** — Is there a behavior-preserving delete/move that removes a whole branch or layer? → do it (build or review).

Non-negotiables below are **consequences** of this definition (never-nest, DRY, cite good sibling / move debt, smart responsibility, easy happy path). Architecture applies it to structure; `/code-review` blocks regressions.

## Non-negotiables

1. **Never-nest** — flatten control flow; extract early instead of deep `if`/`try` pyramids (reduces cognitive load)
2. **DRY** — one concept, one place; no copy-paste twins (stops entropy + change amplification)
3. **Throw + try/catch** at boundaries — never `{ success: false }` / Result bags for expected failure control flow
4. **One component (or main export) per file**
5. **No dynamic `import()`** — static imports only
6. **Comments only** to summarize big/complex functions — no narrating obvious code
7. **Cite a sibling** — before inventing shape, mirror a **good** nearby feature **or existing service** that matches this taste + `/architecture`. Bad nearby code is a **debt / entropy signal**, not a template — when you touch that lane, prefer a **behavior-preserving move** (see `/architecture` §3 Prior mistakes; same spirit as `/code-review` judo while building)
8. **Smart responsibility** — a unit does one job well (a logger only logs; it does not format emails or hit the DB)
9. **Easy to follow** — a reader can walk the happy path without branching into unrelated concerns
10. **Don't spam verify** — read existing terminals first; no ritual lint/typecheck/Convex MCP (see Verify)

## Verify (terminals first — not MCP)

This author almost always has **frontend localhost** and **`npx convex dev`** already running. CI owns type/lint. **Do not** re-verify by poking Convex MCP, re-running `convex` CLI, or spamming status tools.

**Prefer, in order:**

1. **Read existing terminal output** (IDE terminals folder / running `convex dev` + frontend logs) for push success, compile errors, HMR, runtime stacks
2. Diff + structural checks for the change
3. Only if terminals are silent/missing: say so — then ask, or start the **minimal** command once

**Do not** by default (ritual anti-patterns):

- Call **Convex MCP** (`status`, `data`, `tables`, `logs`, `run`, `runOneoffQuery`, `insights`, `functionSpec`, env tools, etc.) "just to verify"
- Re-run `npx convex …`, deploy, or codegen after every slice when `convex dev` is already watching
- Run `eslint`, `tsc --noEmit`, `npm run lint`, full suites, or "just to be sure" scripts
- Start a second frontend/Convex process when one is already up
- Dispatch a subagent whose only job is MCP verification

**Do use Convex MCP / deeper checks only when:**

- Terminals show an error you cannot diagnose from the log text alone
- You need a one-off data read the user asked for
- No Convex terminal exists and you said so first
- The user explicitly asks for MCP/dashboard/CLI verification

Evidence citations should look like: `terminals/3.txt — convex push ok` — not a fresh MCP round-trip.

## Futureproofing (open to extend, closed to break)

When building a **non-trivial / big feature**, build a **bulletproof foundation from day one** so growth is additive — not a rewrite every time something is added:

- **Open to extension** — new behavior lands via new collaborators, strategies, or narrow hooks — not by rewriting call sites
- **Closed to breaking edits** — stable entry-point signatures; avoid forcing callers to change when internals grow
- **Put the seam in first** — interfaces / strategy slots / composition points belong in the initial design when the domain will grow (payments, notifiers, providers, channels, etc.). Do **not** wait for a "second implementation" before shaping the foundation — that causes perma re-editing
- Ship **one real implementation** behind that seam on day one; the seam is the foundation, not unused dead code
- Do **not** future-proof tiny one-off glue with empty hierarchies or config for imaginary products

Plans and structure cards **must** name the extension seam for big features.

## Shape (with `/architecture`)

- **Services** own domain concerns (billing, auth, …) with a small public API — features call them; never reimplement per feature
- Prefer **OOP** (class / abstract class) for stateful domain behavior and shared lifecycle (often *is* the service)
- Prefer **hooks** for React state/effects; **services** (module/class/facade) for shared domain I/O
- Call sites import the **simple entry point / service public API** only — hide collaborators
- Prefer over-splitting files inside a service or feature folder over god files
- Cite a **good** sibling feature **or existing service** when one exists — do not copy debt; move/correct when touching that lane (`/architecture` prior-mistakes)

### OOP depth cap

Keep inheritance / interface stacks **shallow**:

- At most **two** levels of class or interface nesting in a chain (e.g. `PaymentMethod` ← `CardPayment` — stop there)
- Prefer composition over a third layer
- If you need depth 3+, the design is wrong for this taste — flatten or compose

### Patterns & SOLID (pragmatic)

- **Refactoring Guru–style patterns** are welcome when they suit a useful case (Strategy, Facade, Adapter, Observer, etc.)
- **Big features:** lay the foundation early — seam + first implementation — so adding the next variant does not reopen the core
- **Tiny glue / local helpers:** skip ceremony; a plain function or single class is enough
- **SOLID is guidance, not scripture** — use it to keep foundations extendable and readable; stop when it becomes interface theater (factory-of-factories, empty base classes, one-line "impl" files with no behavior)
- Never require a second production implementation *before* introducing the seam on a big feature — that is the opposite of this taste

## Naming & files

| Area | Rule |
| --- | --- |
| App / UI / general TS | `lowercase-with-hyphens` (`use-checkout.ts`, `order-summary.tsx`) |
| **Convex** `convex/**` | **No `-` or `_` in filenames** (`orders.ts`, `orderActions.ts`) |
| Folders | Feature/domain folders before flat dumps; no anonymous `utils` / `helpers` bags |

## React & UI

- **Mobile first**, then widen
- One component per file; keep components thin — complexity in hook/class behind the entry
- **Visual craft** → follow **`/design-flow`** (hierarchy, color shades, depth, states, ethical UX psychology)
- When touching marketing/landing UI, avoid AI-default looks: purple-on-white gradients, cream+terracotta serif clichés, flat single-color voids, card-heavy heroes, pill clusters, emoji decoration
- Landing first viewport: brand + one headline + one line + CTA + one dominant image — nothing else

## Errors

```typescript
// Good
try {
  await charge(order);
} catch (error) {
  throw new Error("Payment failed", { cause: error });
}

// Bad
return { success: false, error: "Payment failed" };
```

## Planning & spec (how other skills use this)

When `/create-plan-flow` or a ticket-driven `/goal` writes acceptance criteria, include **taste-relevant** checks when the change touches structure/UI — e.g. entry point exists, folder map followed, extension seam named (if big feature), no Result bags, Convex names legal, responsibilities not mixed. When structure is in play, AC may include: **callers stay thin; complexity behind service X** (deep surface; no entropy growth in the touched lane).

Plans must not propose shapes that violate this file (including SOLID-maximalist boilerplate or class trees deeper than two).

## Implement self-check (required each slice)

- [ ] Sibling pattern cited is a **good** one (or explicitly "greenfield" / correcting debt)
- [ ] Entry point + folder match `/architecture` card (including **Moves / corrections**)
- [ ] Did not copy a bad sibling — moved/corrected when the lane had prior mistakes
- [ ] Change **reduces or holds complexity** at call sites (deep entry, not shallower)
- [ ] Touched lane: **no entropy growth** (did not copy/extend known-wrong shape without a move)
- [ ] Naming rules above (especially Convex)
- [ ] No nesting pyramids / no dynamic import / no `success: false`
- [ ] One main export per new file
- [ ] Each new type has one clear responsibility (no logger-that-also-sends-mail)
- [ ] Class/interface chain ≤ 2 deep; composition if more is needed
- [ ] Big feature: foundation seam + first impl shipped together (no "wait for second impl"); entry signature stays stable
- [ ] Did not ritual-run lint/typecheck **or Convex MCP**; checked existing terminal output instead (unless terminals errored / user asked)

Fail any box → fix before `/validate-flow`.

## Review

`/code-review` Standards axis treats violations of this file as **hard** unless the repo's own `AGENTS.md` / `.cursor/rules` contradict (repo wins on conflict).
