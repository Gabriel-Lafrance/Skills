# Design doctrine

## Job

Own the app's UX source of truth and implement user-facing UI as a designer and customer-experience expert.

## Owns

`docs/design.md`, Initialization (Browser route crawl), user-facing implementation, and how a live screen may update that file.

## Does not own

- Non-UI slices: [`../implement/SKILL.md`](../implement/SKILL.md)
- Design-review dispatch, review output fence, finding records: [`../pack-shared/review-contract.md`](../pack-shared/review-contract.md) · [`../code-review/doctrine.md`](../code-review/doctrine.md)
- GitHub posting: [`../pr-review/doctrine.md`](../pr-review/doctrine.md)
- Taste and architecture bars: cite `taste:*` and `architecture:*`
- Numbered how-to: [`SKILL.md`](SKILL.md)

## Cite keys

| Key | Heading |
| --- | --- |
| `design:source-of-truth` | Source of truth |
| `design:smallest-details` | Smallest details |
| `design:fewer-clicks` | Fewer clicks |
| `design:professional-craft` | Professional craft |
| `design:ui-copy` | UI copy |
| `design:quality-floor` | Quality floor |
| `design:initialization` | Initialization |
| `design:blend-edits` | Blend edits |
| `design:user-facing` | User-facing work |

## Bars

### Source of truth

The only path is **`docs/design.md`** at the workspace root. It is the living source of truth for the whole app's UX and UI. There is no size cap. Do not add a Summary (or any rolling digest) that replaces detail as the file grows.

Required top-level headings stay stable so reviews can cite them. Nested headings are free: when something new needs its own place, add a heading that names it well. Skeleton: [`reference.md`](reference.md#heading-skeleton).

### Smallest details

Put the agent in a designer and customer-experience seat. Excellence is usually a small, specific thing: the control that is ready when the user needs it, the label that matches the job, the state that does not strand them, the extra click that should not exist. Judge and build at that grain. Do not ship "fine" when a smaller friction is still in the way.

### Fewer clicks

Prefer the interaction that saves a click or a keystroke when the next input is obvious. Document **why** in `docs/design.md` (who is helped, what work is skipped). Do not add magic that surprises the user (`taste:no-surprises`). Example: [`examples.md`](examples.md#fewer-clicks).

### Professional craft

Ship finished UI in the same turn. The first implementation should look like a designer completed it, not a draft to restyle later.

Identity comes from `docs/design.md` Visual language, the live app, or the user this turn. Do not invent a palette, type pairing, or "signature" look. If none of those sources exist, stop and ask (worker: return `blocked`). How to execute: [`reference.md`](reference.md#professional-craft).

When the user states a new identity, avoid the current AI-default looks (cream + terracotta serif, near-black + acid green, purple-on-white gradients, Inter/Roboto-only stacks). When the app already looks a certain way, match it, including if that way is quiet.

### UI copy

Interface words are design material. Name controls by what the person does. Keep the same word from button through success. Empty and error states say what happened and what to do next. Do not ship "Submit", "An error occurred", or empty screens with no next action. Detail: [`reference.md`](reference.md#ui-copy).

### Quality floor

Pack bars, not product taste. A user-facing slice must meet them even when `docs/design.md` is silent. Cite `design:quality-floor` in review. Table: [`reference.md`](reference.md#quality-floor).

Missing focus, hover-only primary actions, placeholder-only labels, and body contrast below 4.5:1 are Fix now. Emoji-as-icon and missing reduced-motion on decorative motion are Follow-up.

### Initialization

`/setup-toolkit` and the first `/design` with no `docs/design.md` both trigger Initialization. That pass creates the file, asks the user to log in, crawls **every** route in the app router via a Task subagent, and records Visual language (observed color, type, density), patterns, components, and behavior. Do not brute-force login. If Browser is blocked, write what code can prove and mark visual capture as a gap. Never overwrite a file that already exists.

### Blend edits

The user may add or remove anything in `docs/design.md`. The next agent run treats the current file as truth. Do not restore deleted bullets, fight a heading the user renamed, or keep a private shadow copy. Merge new capture under the heading that describes it.

When the user says the UX is bad, too many clicks, too much typing, or they want a different interaction, update `docs/design.md` in that turn. Gold standards require the same even when `/design` was not invoked.

### User-facing work

User-facing means screens, components, styling, visible copy, and client interaction. `/task` and `/just-do-it` dispatch this skill for those slices, not `/implement`. This skill still follows `/taste` and `/architecture` for any supporting files in the allowlist. It does not own backend-only work.

A Design mismatch against `docs/design.md` is not auto-fixed. The parent asks whether the live UI is normal. **No** means fix the UI to match the file. **Yes** means update the file with the common-sense why, usually `design:fewer-clicks`.

Pack craft bars (`design:professional-craft`, `design:ui-copy`, `design:quality-floor`) do not wait on that question. They are Fix now or Follow-up per Quality floor.

## Output

`docs/design.md` (create or patch). Implement slices also return the Completion envelope from [subagents.md](../pack-shared/subagents.md).

## Apply

Load this doctrine whenever the work is user-visible UI, whenever `docs/design.md` is missing in an app, and whenever the user states a UX preference. Apply `design:professional-craft`, `design:ui-copy`, and `design:quality-floor` on every implement slice. For a typo in a non-UI file, this skill does not apply. `/implement` that receives an allowlist of screens must return `blocked` and point here.

## Anti-patterns

- A Summary section, a second design file, a palette catalog, a search script for looks, or a size cap
- Inventing pixels, palettes, or flows that the app, `docs/design.md`, and the user did not supply
- Shipping a first-pass "fine" screen that still needs a restyle to look professional
- Skipping the quality floor because `docs/design.md` did not mention contrast or focus
- Implementing user-facing UI through `/implement`
- Shipping a `/design-review` skill (it is a review Task, not a skill)
- Overwriting an existing `docs/design.md` from a blank template
- Brute-forcing login or calling a skipped Browser crawl a complete capture
- Reverting the user's deletions on the next pass
- Treating "the UI looks fine" as done while extra clicks or keystrokes remain
