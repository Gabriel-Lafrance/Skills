# Goal reference (schemas & templates)

Load when writing workspace artifacts, STATUS, Progress lines, or the ACHIEVED summary. Rules stay in [doctrine.md](doctrine.md).

## Workspace layout

```text
.agents/temp/grills/              # shared themes (survive across goals)
  REGISTRY.md
  language.md                     # ubiquitous language
  choice.md                       # locked A-over-B / package picks
  rules.md                        # app rules (actors + policies)

.agents/temp/goals/
  REGISTRY.md
  achieved/
    <goal-id>/              # archived on ACHIEVED
      GOAL.md
      STATUS.md
      GRILL.md              # goal-scoped only
      plans/
      pieces/
  <goal-id>/                  # active running/blocked goals
    GOAL.md
    STATUS.md
    GRILL.md                 # goal-scoped: outcome, gates, taste/arch/design — not shared glossary
    plans/
      INDEX.md
      01-<slug>.md
      02-<slug>.md
    pieces/
```

Goal artifacts under **`.agents/temp/goals/`**; shared grill themes under **`.agents/temp/grills/`** — never `.scratch/`. Language / choices / rules are upserted by `/grill-me` into `grills/` (see `/grill-me` doctrine).

### Goal id

1. Ticket → `IN-1234` or `gh-42`
2. Else kebab slug + 4-hex suffix → `add-billing-a3f2`
3. Override → `/goal id:my-id …`

If dir exists and status is `running`/`blocked`, allocate a **new** id (suffix) — never overwrite another goal's workspace. Parallel goals are normal; do not ask the user whether to resume or start new.

### REGISTRY.md

| id | status | ticket | title | workspace | updated |
| --- | --- | --- | --- | --- | --- |

Statuses: `running` | `blocked` | `achieved` | `cleared`

On **ACHIEVED**: move active tree to `.agents/temp/goals/achieved/<goal-id>/`; set registry `workspace: achieved/<goal-id>` and `status: achieved`. Do **not** delete the workspace on achieve — archive it.

On **`/goal clear [id]`**: set registry `status: cleared`; delete the active tree **or** the archived tree under `achieved/<id>/` if that goal was already achieved.

### Isolation

- All artifacts for a goal stay under `.agents/temp/goals/<goal-id>/` (active) or `.agents/temp/goals/achieved/<goal-id>/` (archived); shared language/choices/rules stay under `.agents/temp/grills/`
- Task prompts get **that** id's `GOAL.md` + relevant `plans/*.md` only
- Overlapping file lanes with another `running` goal → serialize or ask
- Bare `/goal` → this chat's id status + other `running` rows

## STATUS.md schema (required fields)

Every active goal must maintain `STATUS.md` with at least:

| Field | Values / meaning |
| --- | --- |
| `phase` | `grilling` \| `planning` \| `implementing` \| `validating` \| `reviewing` \| `achieved` \| `cleared` |
| `last` | Last major step completed (e.g. `grilling`, `plan-01-done`, `validate-pass`) |
| `plans_done` | Count of completed plans |
| `plans_total` | Total plans in INDEX |
| `blocked_on` | `user` \| `none` |
| `resume_at` | Step id to resume (`0-grill`, `1a-explore`, `1b-plans`, `1c-implement`, `1d-validate`, `1d-review`) |

Also track the mandatory skill checklist rows as they complete.

## Resume / interrupt

| User action | Do |
| --- | --- |
| Bare `/goal` or “status” | Read REGISTRY + this goal’s `STATUS.md`; print **Progress** line + `resume_at`; do **not** re-grill settled GRILL gates |
| “continue” / “resume” | Jump to `resume_at`; re-read GOAL/GRILL/INDEX/current plan only |
| “pause” / “stop here” | Set `blocked_on: user`, `phase: paused`; acknowledge; **no** new Tasks until continue |
| `/goal clear [id]` | REGISTRY `cleared`; **delete** active `<goal-id>/` **or** archived `achieved/<goal-id>/` |
| New `/goal …` while others are `paused`/`running` | Start a **new** id immediately; leave other goals untouched. Do **not** ask resume vs new — invocation means run now |

Persist gate checkboxes in `GRILL.md` so resume never re-asks cleared gates.

## Progress chat line format

After **every** phase change (and after each Task wave), post **one** short chat line **and** update `STATUS.md`:

```markdown
**Progress:** `<goal-id>` · grilling ✓ · plans 2/3 · implementing `01` · next: validate
```

Compact form also OK: `[goal:<id>] phase=<phase> plans=<done>/<total> last=<last> blocked=<blocked_on> resume=<resume_at>`

## ACHIEVED summary (required last message)

After archive, the main agent's **final** user-facing message must be a polished recap — not a one-liner. Use light emojis, keep it scannable:

```markdown
# ✅ Goal achieved: <short title>

**goal-id:** `<id>` · **Ticket:** <none | IN-1234 / #42> · **Archive:** `.agents/temp/goals/achieved/<id>/`

## What we did
- <2–5 bullets of outcome in user language>

## Skills run
| Skill | Role |
| --- | --- |
| `/grill-me` | … |
| `/taste` | … |
| `/architecture` | … or _n/a_ |
| `/design` | … or _n/a_ |
| `/split-task` | … or _n/a_ |
| `/create-plan` | plans: … |
| `/orchestrate` + `/implement` | … |
| `/validate` | pass (incl. cross-plan seams if 2+ plans) |
| `/code-review` | Standards / Spec / Routes highlights |

## What changed
- **Files / areas:** …
- **Behavior:** …
- **Evidence:** terminals / localhost cite (no MCP ritual)

## Decisions locked (grill)
- Goal: … (from `GRILL.md`)
- Themes: … (from `grills/language.md`, `choice.md`, `rules.md` — or _none new_)

## Manual next steps (you)
- [ ] Close / merge ticket or PR if any (trackers are read-only)
- [ ] Open `/create-test` follow-ups from `FOLLOWUPS.md` (from `/code-review` recommendations — or _none_)
- [ ] …

## Open follow-ups (optional)
- …
```

If there are no manual steps, still say so under **Manual next steps** (`_None — you're done._`).

### Ship Questions (after ACHIEVED summary)

One Questions batch via [asking.md](../asking.md) — do not invent a `/ship` skill:

```markdown
## Questions
Reply like: 1b 2b

1. Commit these changes now?
   - a) yes — create a commit
   - b) no — leave uncommitted ← recommended unless the user already asked to commit
2. Open a PR?
   - a) yes — push and `gh pr create`
   - b) no ← recommended
```

Wait for the batch before committing or opening a PR.
