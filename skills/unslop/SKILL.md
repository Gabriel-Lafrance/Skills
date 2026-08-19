---
name: unslop
description: >-
  Cut AI tells from the agent's reply in this discussion. Must always
  apply to chat. Use when the user says unslop, that sounded like
  ChatGPT, rewrite that reply, or tighten the last message. Not for
  README, ticket, or PR-body file cleanup.
disable-model-invocation: true
---

# Unslop

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md).
This skill *is* discussion voice; still Read `/taste` and `/architecture`
doctrines this turn. Do not skip.

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

**Read:** [doctrine.md](doctrine.md) (Job through Bars) ·
[examples.md](examples.md) ·
[../pack-shared/plain-language.md](../pack-shared/plain-language.md)

The prose surface is **the reply in this discussion**. Write it clean as
you draft it. Do not generate slop and strip it afterward. That cleanup
pass fails.

Cite keys live in doctrine. Ordinary words live in
[plain-language.md](../pack-shared/plain-language.md). Em dash characters
live in the no-emdash plugin rule.

Parents load this doctrine so every chat reply is unslopped. Gold-standards
loads it even for `/ask-gabriel`. This skill stays
`disable-model-invocation: true` (only `/ask-gabriel` may auto-invoke).
Always-on is that Read, not a self-start.

Adapted from [pstack `/unslop`](https://github.com/backnotprop/pstack)
(MIT). Pstack sends docs and PR bodies to a separate technical-writing
skill. This pack does the same split: unslop is discussion text
(`unslop:scope`).

### If this skill is already loaded (every reply)

1. Read doctrine + examples.
2. Draft the reply clean (`unslop:draft`). Scan with `unslop:tells` while
   writing, not after.
3. Keep asking-contract and Locked-in templates intact (`unslop:scope`).
4. Self-audit (`unslop:self-audit`) before the user sees the message.
5. Do not edit files. Do not rewrite a README, ticket, or PR body as
   this skill's job.

### If the user asks to unslop a reply

The last assistant message in this discussion landed sloppy.

1. Take that chat message (or the paste they pointed at in chat). Not a
   file lane.
2. Rewrite it in the next reply. Preserve meaning. Match the intended
   tone.
3. Self-audit. Send the rewritten message. Do not open a diff unless
   they also asked to change code.

Hand-offs: coding style → `/taste`. Structure → `/architecture`. Build
end-to-end → `/goal`.
