---
name: unslop
description: >-
  Cut AI tells from writing and keep a human voice. Always apply to
  user-facing chat, tickets, PRs, and docs you author. Use when the user
  says unslop, tighten prose, sounds like ChatGPT, cut slop, make this
  sound human, or asks to clean a README, ticket, or PR body.
disable-model-invocation: true
---

# Unslop

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md).
This skill *is* writing discipline; still Read `/taste` and `/architecture`
doctrines this turn. Do not skip.

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

**Read:** [doctrine.md](doctrine.md) (Job through Bars) ·
[examples.md](examples.md) ·
[../pack-shared/plain-language.md](../pack-shared/plain-language.md)

Cite keys live in doctrine. Ordinary words live in
[plain-language.md](../pack-shared/plain-language.md). Em dash characters
live in the no-emdash plugin rule. This skill owns AI tells and cadence.

Parents load this doctrine on every skill run via standards, next to
plain language. `/ask-gabriel` stays a thin router and does not run this
skill; gold-standards still requires the doctrine before user-facing
writing.

Adapted from [pstack `/unslop`](https://github.com/backnotprop/pstack)
(MIT). Pack overrides are in doctrine (`unslop:scope`).

### If this is a user one-off (clean named writing)

Use when the user asks to unslop, tighten, or humanize a message, file,
ticket, or PR body.

1. Identify the lane (paths, paste, or the last assistant message).
2. Read doctrine + examples. Scan with `unslop:tells`.
3. Rewrite in place. Preserve meaning and the intended tone. Do not
   change code behavior, identifiers, or required templates
   (`unslop:scope`).
4. Add a human voice (`unslop:human-voice`): specific to this repo,
   recommended next step, mixed sentence length. Do not invent metaphors
   or literary flourish.
5. Self-audit (`unslop:self-audit`): "What makes this obviously
   generated?" Fix remaining tells. Show the rewritten text or diff.
6. Do not sweep unrelated files. Do not invent a parent wave, write
   tests, or start `/create-test`.

Hand-offs: coding style → `/taste`. Structure → `/architecture`. Build
end-to-end → `/goal`.

### If this skill is already loaded inside a build

1. Load unslop doctrine before any user-facing message (chat, ticket,
   PR title/body, README, review comment).
2. Apply `unslop:tells` and `unslop:human-voice` to text the user will
   read. Keep asking-contract and Locked-in templates intact.
3. Run the doctrine Output self-check before sending that text.
4. Do not rewrite pack doctrines to erase cite-key terms such as
   primitive or surface. User-facing chat still uses ordinary words
   ([plain-language.md](../pack-shared/plain-language.md)).
