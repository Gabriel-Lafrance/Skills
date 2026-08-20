# Plain language

Humans must understand every message without decoding jargon, nicknames, or abbreviations.

This contract is for **what the user reads**. Internal worker notes may keep short labels. If the user will see a line, write it in ordinary words.

## Rules

1. Write like a teammate explaining the work, not like a spec.
2. Prefer short common words. One idea per sentence.
3. Do not use an abbreviation unless you already spelled it out in **this** message, or the user already used it (examples that are fine: API, PR, URL, Git, ID, UI).
4. Do not teach the user pack nicknames. Say the meaning.
5. Skill names like `/task` are fine when recommending a next step.
6. A finding ID or rule ID may appear for tracking. The same bullet must still include a plain sentence of what is wrong and what to do.

## Say this, not that

| Do not say to the user | Say |
| --- | --- |
| SoC / SLAP / CQS / PoLA / DRY | Keep jobs apart / this function is doing two jobs / this read also writes / this name surprises people / write this idea in one place |
| entropy | Don’t copy the old messy layout |
| primitive | Reuse the existing one-job helper |
| hard-apply / Hard apply | Must follow taste and architecture |
| INV-1 (alone) | Rule 1 — payments must not charge twice |
| Active Rules | Rules that must stay true |
| Worker Brief | (don’t say this; it is internal) |
| n/a | none / does not apply |
| AC / DoD | what “done” means |
| CR1 / CR2 | first review / second review |

KISS is allowed only as **keep it simple**. If you say KISS, expand it in the same sentence the first time.

## AI tells

Ordinary words are not enough if the sentence still sounds generated.
Chat replies follow the unslop plugin rule
([`../../rules/unslop.mdc`](../../rules/unslop.mdc)) when the plugin or
pinned rules are installed. This file owns jargon and nicknames. That
rule owns puffery, chatbot closings, fake cadence, and drafting the
reply clean. `npx skills` does not install plugin rules; pin them with
`/setup-toolkit` if you need them without the plugin.

## Questions and announcements

Follow [asking.md](asking.md). Question text and Locked-in text must be readable without this pack’s vocabulary. Options describe the real choice, not an internal process name.

## Anti-patterns

- Dumping principle acronyms into chat (“SoC + SLAP violation”)
- Using a nickname the user has not used
- A review comment that is only a rule slug
- Explaining a decision in words only an author of this pack would know
