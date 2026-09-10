# Plain language

Humans must understand every message. Named principles use a **plain name plus the classic name** so people can read them and models still retrieve KISS, SoC, and Boy Scout.

This contract is for **what the user reads**. Internal worker notes may keep cite keys (`taste:keep-it-simple`). If the user will see a line, write it in ordinary words, then the classic name in parentheses.

## Rules

1. Write like a teammate explaining the work, not like a spec.
2. Prefer short common words. One idea per sentence.
3. Cite a named principle as **plain (Classic)** in the same sentence. Example: `We need to keep this simple (KISS).` Never acronym-only. Never plain-only for a named principle.
4. Other abbreviations (API, PR, URL, Git, ID, UI) are fine. Do not use INV-1, Worker Brief, or pack nicknames without the plain sentence.
5. Do not teach pack cite keys (`taste:keep-jobs-apart`) as the user-facing name.
6. Skill names like `/task` are fine when recommending a next step.
7. A finding ID or rule ID may appear for tracking. The same bullet must still include the plain (Classic) sentence of what is wrong and what to do.

The canonical map lives in [`../taste/doctrine.md`](../taste/doctrine.md) (named principles and mechanical rules).

## Say this, not that

| Do not say to the user | Say |
| --- | --- |
| `SoC violation` / `keep jobs apart` alone | Keep jobs apart (SoC) |
| `KISS` alone / `keep it simple` alone | Keep this simple (KISS) |
| `Boy Scout` alone / `leave it cleaner` alone | Leave it cleaner (Boy Scout Rule) |
| entropy | Don’t copy the old messy layout |
| primitive | Reuse the existing one-job helper |
| hard-apply / Hard apply | Must follow taste and architecture |
| INV-1 (alone) | Rule 1 — payments must not charge twice |
| Active Rules | Rules that must stay true |
| Worker Brief | (don’t say this; it is internal) |
| n/a | none / does not apply |
| AC / DoD | what “done” means |
| CR1 / CR2 | first review / second review |

## AI tells

Ordinary words are not enough if the sentence still sounds generated.
Chat replies follow the unslop plugin rule
([`../../rules/unslop.mdc`](../../rules/unslop.mdc)) when the plugin or
pinned rules are installed. This file owns jargon and nicknames. That
rule owns puffery, chatbot closings, fake cadence, and drafting the
reply clean. `npx skills` does not install plugin rules; pin them with
`/setup-toolkit` if you need them without the plugin.

## Questions and announcements

Follow [asking.md](asking.md). Question text and Locked-in text must be readable without this pack’s vocabulary. Options describe the real choice, not an internal process name. Principle names in questions still use `plain (Classic)`.

## Anti-patterns

- Dumping principle acronyms into chat (“SoC + SLAP violation”)
- Using a plain principle name with no classic name (“keep it simple”)
- Using a nickname the user has not used for anything other than these classic principle names
- A review comment that is only a rule slug
- Explaining a decision in words only an author of this pack would know
