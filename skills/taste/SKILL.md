---
name: taste
description: >-
  Author coding taste — futureproofing, pragmatic OOP/SOLID, DRY, smart
  responsibility, naming, errors, React/UI, Convex. Shared contract for plan,
  architecture, implement, validate, and code-review. Use when writing or
  reviewing code in this author's style, or when other pack skills say to
  follow /taste.
disable-model-invocation: true
---

# Taste

Shared style contract for this pack. **Other skills must read this before planning or writing code** — not only when `/taste` is invoked alone.

For good vs bad snippets, see [examples.md](examples.md).

## Non-negotiables

1. **Never-nest** — flatten control flow; extract early instead of deep `if`/`try` pyramids
2. **DRY** — one concept, one place; no copy-paste twins
3. **Throw + try/catch** at boundaries — never `{ success: false }` / Result bags for expected failure control flow
4. **One component (or main export) per file**
5. **No dynamic `import()`** — static imports only
6. **Comments only** to summarize big/complex functions — no narrating obvious code
7. **Cite a sibling** — before inventing shape, mirror one nearby feature in the repo
8. **Smart responsibility** — a unit does one job well (a logger only logs; it does not format emails or hit the DB)
9. **Easy to follow** — a reader can walk the happy path without branching into unrelated concerns
10. **Don't spam lint/typecheck** — verification comes from running local servers first (see below)

## Verify (local servers first)

This author almost always has **frontend localhost** and **`npx convex dev`** (or equivalent) already running. Typecheck/lint are covered by **CI** — do not re-run them as a ritual.

**Prefer, in order:**

1. Read the IDE **terminals** folder / running process output for the frontend and Convex (errors, HMR, deploy/push failures)
2. Hit or inspect the running app behavior when the change is user-visible
3. Read the diff + Convex function results / logs for backend changes

**Do not** by default:

- Run `eslint`, `tsc --noEmit`, `npm run lint`, full test suites, or “just to be sure” verify scripts after every slice
- Start a second dev server when one is already up

**Do run deeper checks only when:**

- Local servers are throwing errors related to this change
- The user asks for lint/typecheck/tests
- No local servers are running and you cannot get signal another way (say so, then ask or run the minimal command)

CI remains the safety net for type and lint. Agent time is for shape, behavior, and fixing what the running stack actually reports.

## Futureproofing (open to extend, closed to break)

When building a **non-trivial / big feature**, build a **bulletproof foundation from day one** so growth is additive — not a rewrite every time something is added:

- **Open to extension** — new behavior lands via new collaborators, strategies, or narrow hooks — not by rewriting call sites
- **Closed to breaking edits** — stable entry-point signatures; avoid forcing callers to change when internals grow
- **Put the seam in first** — interfaces / strategy slots / composition points belong in the initial design when the domain will grow (payments, notifiers, providers, channels, etc.). Do **not** wait for a “second implementation” before shaping the foundation — that causes perma re-editing
- Ship **one real implementation** behind that seam on day one; the seam is the foundation, not unused dead code
- Do **not** future-proof tiny one-off glue with empty hierarchies or config for imaginary products

Plans and structure cards **must** name the extension seam for big features.

## Shape (with `/architecture`)

- Prefer **OOP** (class / abstract class) for stateful domain behavior and shared lifecycle
- Prefer **hooks** for React state/effects; **facades** for multi-step I/O workflows
- Call sites import the **simple entry point** only — hide collaborators
- Prefer over-splitting files inside a feature folder over god files

### OOP depth cap

Keep inheritance / interface stacks **shallow**:

- At most **two** levels of class or interface nesting in a chain (e.g. `PaymentMethod` ← `CardPayment` — stop there)
- Prefer composition over a third layer
- If you need depth 3+, the design is wrong for this taste — flatten or compose

### Patterns & SOLID (pragmatic)

- **Refactoring Guru–style patterns** are welcome when they suit a useful case (Strategy, Facade, Adapter, Observer, etc.)
- **Big features:** lay the foundation early — seam + first implementation — so adding the next variant does not reopen the core
- **Tiny glue / local helpers:** skip ceremony; a plain function or single class is enough
- **SOLID is guidance, not scripture** — use it to keep foundations extendable and readable; stop when it becomes interface theater (factory-of-factories, empty base classes, one-line “impl” files with no behavior)
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
- **Visual craft** → follow **`/design`** (hierarchy, color shades, depth, states, ethical UX psychology)
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

When `/create-plan` or a ticket-driven `/goal` writes acceptance criteria, include **taste-relevant** checks when the change touches structure/UI — e.g. entry point exists, folder map followed, extension seam named (if big feature), no Result bags, Convex names legal, responsibilities not mixed.

Plans must not propose shapes that violate this file (including SOLID-maximalist boilerplate or class trees deeper than two).

## Implement self-check (required each slice)

- [ ] Sibling pattern cited (or explicitly "greenfield")
- [ ] Entry point + folder match `/architecture` card
- [ ] Naming rules above (especially Convex)
- [ ] No nesting pyramids / no dynamic import / no `success: false`
- [ ] One main export per new file
- [ ] Each new type has one clear responsibility (no logger-that-also-sends-mail)
- [ ] Class/interface chain ≤ 2 deep; composition if more is needed
- [ ] Big feature: foundation seam + first impl shipped together (no “wait for second impl”); entry signature stays stable
- [ ] Did not ritual-run lint/typecheck; checked running server/Convex output instead (unless servers errored)

Fail any box → fix before `/validate`.

## Review

`/code-review` Standards axis treats violations of this file as **hard** unless the repo's own `AGENTS.md` / `.cursor/rules` contradict (repo wins on conflict).
