# Design examples

Concrete good vs bad. Prefer matching **good**. Stop at “good,” not S-tier gold-plating.

## Depth fixes boring UI

**Bad** — one flat surface, hard border, one muddy shadow:

```css
.card {
  background: #fff;
  border: 1px solid #ddd;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
}
```

**Good** — layered surfaces + light-from-above shadow pair:

```css
:root {
  --bg-dark: hsl(0 0% 94%);
  --bg: hsl(0 0% 98%);
  --bg-light: hsl(0 0% 100%);
  --highlight: hsl(0 0% 100% / 0.8);
  --shadow-tight: 0 1px 0 var(--highlight) inset, 0 1px 2px hsl(0 0% 0% / 0.08);
  --shadow-soft: 0 1px 0 var(--highlight) inset, 0 8px 24px hsl(0 0% 0% / 0.08);
}

.page { background: var(--bg-dark); }
.card {
  background: var(--bg-light);
  border: 1px solid hsl(0 0% 0% / 0.06);
  box-shadow: var(--shadow-tight);
}
.card:hover { box-shadow: var(--shadow-soft); }
```

Raise what matters (lighter + shadow); recess secondary (darker / inset). Drop borders when layers already separate surfaces.

## Hierarchy

**Bad** — spreadsheet energy: same size/weight for title, meta, and price.

**Good** — important = bigger / higher / louder:

- Title large + strong
- Price accent color, top-right or near CTA
- Meta smaller + muted
- Icon pairs instead of verbose labels when scanning is the job

## Color system (neutrals + primary + semantic)

**Bad** — random hexes; decorative rainbow; pure `#fff` text on near-black (harsh).

**Good** — HSL/OKLCH shades:

| Role | Idea |
| --- | --- |
| Surfaces | 3 lightness steps (`bg-dark` / `bg` / `bg-light`) |
| Text | strong heading + muted body (still legible) |
| Primary | brand for main actions only |
| Semantic | green/red/yellow for success/danger/warning — meaning, not decoration |

Name by role so light/dark themes stay sane (`bg-light` is always the raised surface).

## States & signifiers

**Bad** — button with only a default style; selected nav looks identical to idle.

**Good** — every control teaches itself:

- Button: default / hover / active / disabled (+ loading when async)
- Input: focus / error (+ warning when useful)
- Nav: clear selected surface (lighter layer or primary tint)

## Seamless list UX (also scales)

**Bad** — “Page 1 2 3” with full remount; blank white flash; fetch all rows.

**Good:**

- Cursor pages + infinite / near-bottom load
- Skeleton rows while next page loads
- Append items; keep scroll position
- Prefetch when ~80% down the list
- Virtualize if the DOM gets huge

## Forms & onboarding psychology (ethical)

**Bad** — five empty fields; progress at 0%; “Sign up to see your results” hostage wall.

**Good:**

- Smart defaults pre-filled (scan & adjust)
- Progress starts > 0% (credit something already done)
- Real value before hard signup (reciprocity)
- Let users choose/build something first (endowment) — then Continue

Never fake urgency, scarcity, progress, or reviews.

## Overlays on images

**Bad** — full black scrim that kills the photo and the text.

**Good** — gradient (optional progressive blur) into a readable text band; image still visible.

## Landing first viewport

**Bad** — hero with stats strip, schedule, address, three CTAs, pill clusters, emoji.

**Good** — brand + one headline + one line + one CTA group + one dominant visual. Mobile first.

## Design card (standalone create / design-flow)

**Good** — written before coding pixels:

```markdown
## Design
**Job of this screen:** Choose a plan and continue checkout
**Primary action:** Continue with Pro
**Hierarchy:** plan name + price loud; feature list quiet
**Surfaces:** page bg-dark; plan cards bg-light; selected card raised
**Depth:** selected = tighter top highlight + soft shadow; others flat
**States:** Continue default/hover/disabled; billing toggle
**Psychology:** Pro pre-selected (smart default); no fake countdown
**Out of scope visually:** marketing illustrations
```
