# Grill Me

Interview until you and the user share understanding (standalone variant).

**Read:** [doctrine.md](doctrine.md) · **Ask style:** [../asking.md](../asking.md)

Follow doctrine Rules + Closing. Batch every known question in one message per asking.md. Do not write `plans/*` or implement until closing gates pass when aiming at a goal.

## Themes (required when locked)

Upsert under **`.agents/temp/grills/`** (create dir + `REGISTRY.md` if missing):

| Lock | File |
| --- | --- |
| Domain terms / aliases / named events | `language.md` |
| Package / vendor / storage picks | `choice.md` |
| Actors + business policies | `rules.md` |

One phrase per line. Append/update — do not wipe unrelated entries. Announce paths after write. Themes are **project-wide**; do **not** put them in a goal `GRILL.md`.

## Process

1. Read existing `grills/language.md`, `choice.md`, `rules.md` when present (reuse; do not re-ask settled terms).
2. Batch interview per doctrine (include language / choices / rules when fuzzy).
3. On lock → upsert matching theme file(s) + REGISTRY.
4. If the user later starts `/goal`, seed goal `GRILL.md` with **outcome / gates / taste / arch / design** from this interview only — themes already live in `grills/`.

## Hand-offs

- Structure needed → `/architecture`, then `/goal`
- Ready to build → `/goal`
