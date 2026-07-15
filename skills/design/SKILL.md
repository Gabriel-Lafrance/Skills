---
name: design
description: >-
  UI/UX craft for screens that feel clear, deep, and usable. Fix or polish the
  current UI, or shape hierarchy, color, depth, states, and ethical psychology
  when creating UI outside a goal. Agents may auto-invoke. Use when the user
  says /design, fix this UI, polish the UI, or when creating user-facing
  interface without an active /goal. Under /goal use /design-flow instead.
---

# Design

Visual + interaction craft for this pack: **signifiers, hierarchy, color as shades, depth that sells light, and ethical psychology that makes the next step feel easy.**

Also respect `/taste` (mobile-first, anti–AI-default looks, one component per file). Design owns **how it looks and feels**; taste/architecture own code shape.

For good vs bad pairs, see [examples.md](examples.md).

Inside a `/goal` workspace, use **`/design-flow`** instead of this skill.

## Standalone — fix or create UI

User wants the **existing** screen improved, or is creating UI **outside** `/goal`. Do not invent new product scope on a polish pass.

1. Identify the target (path, component, or “what’s on localhost”).
2. Read the current UI code + running frontend if useful (`/taste` Verify).
3. Diagnose with the **checklist** below (boring flat, weak hierarchy, missing states, decision fatigue, etc.).
4. When **creating** UI: write a tiny **Design card** first, then implement against it (mobile first).

```markdown
## Design
**Job of this screen:** one sentence
**Primary action:** …
**Hierarchy:** what is top / mid / background
**Surfaces:** bg-dark / bg / bg-light (or token names)
**Depth:** which elements raise vs recess
**States:** buttons/inputs that need default·hover·active·disabled (+ loading/error if relevant)
**Psychology (if flow):** defaults / progress / reciprocity / endowment — ethical only
**Out of scope visually:** …
```

5. Apply the **smallest depth/color/hierarchy/psychology fixes** that move average → good. Prefer CSS/token changes over structural rewrites when polishing.
6. Show a short before→after intent list; then edit.
7. Re-check running localhost — no ritual lint.

Stop at “good” (depth + hierarchy + clear next action). Do not gold-plate to S-tier polish unless asked.

## Doctrine

### 1. Signifiers & feedback

People should understand what the UI can do **without instructions**.

- Selected, disabled, hover, and focus states are how the interface “talks”
- Group related controls visually so belonging is obvious (proximity = meaning)
- Every user action gets a response: buttons need default / hover / active / disabled (+ loading when async)
- Inputs need focus, error (and warning when useful)
- Icons and labels can replace long copy when the meaning is already conventional

### 2. Hierarchy

Hierarchy is contrast: **size, position, and color** — not more chrome.

- Important = larger, higher, higher contrast / color; secondary = smaller, quieter
- Lead with what the user came for (title, primary value, primary action); metadata stays below and smaller
- Images/icons when they speed scanning
- One clear primary action per view when possible
- Price / key metric: often top-right or otherwise visually distinct so it doesn’t blend into timestamps and labels

### 3. Space & type

- White space matters more than rigid 12-column grids for most product UI; grids help repeating galleries/blogs, not every custom screen
- Let things breathe; group related items (proximity = hierarchy)
- Prefer a **4-point** spacing scale (multiples of 4)
- Prefer **one** sans family; large titles: slightly tighter tracking (~−2–3%) and line-height ~1.1–1.2
- Dashboards: keep type denser (avoid huge display sizes)

### 4. Color (think in shades, not random hex)

You need roughly three jobs:

- **Neutrals** — backgrounds, text, borders (shades via lightness)
- **Primary / brand** — main actions + character
- **Semantic** — success / danger / warning / info — for meaning, not decoration

Practical recipe:

- Prefer **HSL or OKLCH** so lightness steps are intentional (hex/RGB make shade ladders opaque)
- Build neutrals with saturation ≈ 0; vary **lightness** for a harmonic surface ladder
- **3 surface shades**: page base darker; raised cards/surfaces step lighter toward the user — lighter = closer = more important
- **2 text shades**: strong for headings; muted but legible for body — avoid pure 100% white on dark (harsh)
- Name surfaces by role (`bg-dark` / `bg` / `bg-light`) so light and dark themes stay sane
- Light mode starting point: flip lightness (~100 − L), then fix by eye — light comes from above, so top/raised surfaces should be **lighter**, not darker
- Borders: visible but quiet; often a top **highlight** + soft border beats a harsh outline
- Gradients: subtle, light-from-above; full blast on hover if idle is too loud

### 5. Depth (fix boring flat UI)

Flat “one surface + one muddy drop-shadow” reads as average. Fix with a **two-step** depth process:

1. **3–4 shades** of the same surface color; put the lighter shade on important / raised layers (same hue family, stepped lightness)
2. **Realistic shadows** — light edge/glow or inset highlight on **top** + softer darker shadow **below** (combined soft + dark beats one generic `box-shadow`)

Then:

- Raise what matters; recess what doesn’t (inset / darker for “deeper”)
- Selected cards/tabs: lighter fill + the small dual shadow so they feel closer to the user
- Remove redundant borders once layers already separate surfaces
- Stronger shadow for overlays/popovers than for resting cards; bump shadow slightly on hover when it sells elevation
- If the shadow is the first thing you notice, it’s too strong — pick the smallest natural option
- Never ignore **light mode** — depth reads especially well there; most users live there

### 6. Psychology (flows) — ethical only

Use when designing onboarding, forms, pricing, signup, empty states. Goal: make the next action feel obvious and worth completing — **not** manipulative.

| Principle | Do | Why |
| --- | --- | --- |
| Smart defaults | Pre-fill common choices; reduce blank-form fields | Blank forms create decision fatigue |
| Goal gradient | Never start progress at 0% — credit something already done | Early progress motivates finishing |
| Reciprocity | Give real value before a hard signup wall | Trust beats hostage gates |
| Endowment / IKEA | Let users make/own something before “Sign up” | Ownership increases commitment |
| Loss aversion | Frame what’s at stake clearly without faking threats | Loss weighs heavier than abstract gains |
| Contrast | Price/value feel relative — frame against a reference | Same number feels cheap or expensive by context |

**Never:** fake urgency, fake scarcity, fake progress, fake reviews, or other dark patterns.

### 7. Overlays on imagery

Prefer gradient (and optional progressive blur) into a readable text region over a flat dim that kills the photo.

## Anti-patterns

- Flat single-surface UI with one hard border and one opacity shadow
- Decorative color with no semantic job
- Missing hover/focus/disabled/error states
- Blank forms / 0% progress / hostage “sign up to see results”
- AI-default purple gradients, pill spam, emoji decoration (see `/taste`)
- Rewriting architecture when a depth/token pass would fix “boring”
- Naming surfaces `gray-1` / `gray-2` without role names that survive light/dark

## Hand-offs

- Structure / folders → `/architecture` + `/taste`
- Behavior Done when → `/validate` (localhost evidence)
- Standalone fix done → stop (or `/validate` if user wants a gate)
- Inside `/goal` → `/design-flow`
