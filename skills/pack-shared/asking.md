# Asking the user

Every pack skill that needs a decision follows this contract. Link here instead
of restating it inline.

## Rules

1. Batch every known decision into one message.
2. Number items and provide lettered options when the choice is discrete.
3. Mark one recommended option with `← recommended`.
4. Keep `Reply like:` to one row of codes only, such as `1a 2b 3c`.
5. Wait for decisions before acting. Do not re-ask settled decisions.
6. Look up repository and tool facts instead of asking the user for them.
7. Ask only when an action or choice is needed; list settled facts outside Questions.
8. **Never put a Locked section in the same message as Questions.** While
   Questions remain, send **Questions only**. Record agent-owned conclusions in
   the [execution context](execution-context.md); do not dump a
   `## Locked (correct if wrong)` block above the ask.
9. After material Questions are settled (or when the turn is announce-only),
   announce agent-owned conclusions in a separate **Locked (correct if wrong)**
   message. Ask only open product, UX, architecture, taste, or policy choices.

## Locked decisions

Keep non-goals, plan split, shared understanding, relevant Active Rules, and
user overrides visible in the current [execution context](execution-context.md).
Do not write them to an agent-owned runtime file. Save them only when the user
requests a durable artifact and approves its destination.

## Skill exception

`/write-ticket` uses numbered freeform questions for its open grill. Its type
and metadata choices use the normal lettered contract.

## Batch template (Questions)

When asking the user, use this shape only — no Locked heading:

```markdown
## Questions
Reply like: 1a 2c

1. <open choice>?
   - a) <recommended> ← recommended
   - b) <alternative>
   - c) Other — say what you want
```

Yes/no choices use the same shape; freeform items keep a number but omit
letters.

## Locked template (announce-only)

Use only when there are **no** Questions in the message (grill closed, or a
pure announce such as branch/type/split with nothing left to ask):

```markdown
## Locked (correct if wrong)
**Non-goals:** …
**Plans:** 1. … · 2. …
**Shared understanding:** …
**Active Rules:** `INV-1` … · `INV-2` … (or _none_)
```

Omit Locked when nothing is announced. Omit Questions when every remaining item
is announce-only. Never combine both templates in one message.

## Anti-patterns

- Putting `## Locked (correct if wrong)` above or beside a Questions batch
- Dripping known questions one at a time
- Optioned choices without a recommendation
- `Reply like:` with descriptions, invalid letters, commas, or multiple rows
- Asking about a fact the repository or tools can answer
- Asking yes/no for non-goals, plan split, or shared understanding
- Persisting agent process notes without an explicit user request
