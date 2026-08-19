# Unslop doctrine

## Job

Cut AI tells from user-facing writing and keep a specific, human cadence.

## Owns

What counts as an AI tell, the rewrite bar, human voice (not literary
flourish), and which texts this skill may touch.

## Does not own

- Ordinary words, pack nicknames, and abbreviations: [`../pack-shared/plain-language.md`](../pack-shared/plain-language.md)
- Em dash, en dash, and horizontal bar characters: [`../../rules/no-emdash.mdc`](../../rules/no-emdash.mdc)
- How to ask the user (Questions / Locked-in templates): [`../pack-shared/asking.md`](../pack-shared/asking.md)
- Coding taste and structure: `taste:*`, `architecture:*`
- Numbered cleanup steps: [`SKILL.md`](SKILL.md)

## Cite keys

| Key | Heading |
| --- | --- |
| `unslop:scope` | Scope |
| `unslop:human-voice` | Human voice |
| `unslop:tells` | Tells |
| `unslop:self-audit` | Self-audit |

Snippets: [`examples.md`](examples.md).

## Bars

### Scope

**Always apply** to text the user will read: chat, tickets, PR titles and
bodies, README and skill descriptions, and comments you post.

**Do not apply** as a rewrite of:

| Leave alone | Why |
| --- | --- |
| Asking-contract and Locked-in templates | Shape is the contract (`asking.md`) |
| Doctrine cite-key terms in skill files (`primitive`, `surface`, …) | Internal names; user-facing chat still uses ordinary words |
| Code identifiers, paths, commands, and test names | Honesty of names is `/taste`, not prose style |
| Files you were not asked to touch | No drive-by unslop of the tree |

**Pack overrides of pstack `/unslop`:**

1. Parentheses stay allowed. The no-emdash rule already bans dash
   characters and lists parentheses as a valid substitute. Do not strip
   parentheses to "sound more human."
2. Do not "let mess in" to look human. Required templates, doctrine
   schema, and one-row `Reply like:` stay exact.
3. Do not invent metaphors, late-night atmosphere, or cute asides. Be
   specific about *this* repo.
4. Only `/ask-gabriel` may auto-invoke. This skill stays
   `disable-model-invocation: true`. Always-on happens because gold
   standards and [standards.md](../pack-shared/standards.md) **Read**
   this file, not because the model self-starts `/unslop`.

A sentence that could appear unchanged in another project's docs says
nothing about this one. Cut it or name a concrete fact here.

### Human voice

Removing tells is half the job. Flat, voiceless prose is still a tell.

| Do | Do not |
| --- | --- |
| Have a point of view. Recommend. React to the fact in front of you | Fake balance ("pros and cons") when you already have a pick |
| Mix short sentences with longer ones | Same-length paragraph stacks |
| Name the mechanism, path, or number | Mood: "the database stays close at hand" |
| Use "I" when reporting what you did | Sycophancy: "Great question! You're absolutely right!" |
| Keep required headings and templates | Literary flourish, invented metaphor, or "soul" that fights `unslop:scope` |

### Tells

Scan, then rewrite. Preserve meaning.

#### Content

1. **Puffery.** "pivotal moment", "testament to", "evolving landscape",
   "setting the stage", "indelible mark", "deeply rooted". State what
   happened.
2. **Name-dropping.** A list of outlets with no claim. Pick one and say
   what it said, or delete.
3. **Hollow -ing phrases.** "highlighting…", "ensuring…",
   "reflecting…", "showcasing…", "fostering…". Delete, or replace with
   a source or a fact.
4. **Promotional words.** "vibrant", "breathtaking", "groundbreaking",
   "renowned", "stunning", "must-visit", "nestled". Use a neutral
   description.
5. **Vague attributions.** "Experts believe", "Industry reports
   suggest", "Some critics argue". Name the source or delete.
6. **Formulaic bounce-back.** "Despite challenges… continues to
   thrive." Replace with the specific fact.

#### Language

7. **AI vocabulary.** Additionally, crucial, delve, enduring, enhance,
   fostering, garner, interplay, intricate, landscape (abstract),
   pivotal, showcase, tapestry (abstract), testament, underscore,
   vibrant. Use a plain word.
8. **Fancy "is".** "serves as", "stands as", "boasts", "features". Say
   "is" or "has".
9. **"Not just X, but Y."** State the point once.
10. **Forced groups of three.** Use the natural number of items.
11. **Synonym cycling.** One name per thing. Repeat it.
12. **False ranges.** "from X to Y" when X and Y are not on a scale.
    List the topics.

#### Style

13. **Dash characters.** Never write an em dash, en dash, or horizontal
    bar. Follow the no-emdash rule: comma, colon, period, parentheses,
    or hyphen. Colon is fine before a list or example, not as a
    mid-sentence crutch that frames a comparison.
14. **Boldface overuse.** Bold only the few words that matter. Do not
    bold every proper noun.
15. **Inline-header lists.** A bold label plus colon that restates the
    line ("**Performance:** Performance improved…") is a tell. Convert
    to prose. A bold lead-in that names the item and adds new detail
    is fine.
16. **Title Case headings.** Use sentence case for headings you author.
17. **Decorative emojis.** Remove from headings and bullets.
18. **Curly quotes.** Use straight quotes.

#### Chat

19. **Chatbot closings.** "I hope this helps!", "Let me know if…",
    "Of course!", "Certainly!", "Found the smoking gun!" Delete.
20. **Cutoff disclaimers.** "While specific details are limited…"
    Find the source or remove.
21. **Sycophantic tone.** Answer the question.

#### Filler

22. **Filler.** "In order to" → "To". "Due to the fact that" →
    "Because". Delete "It is important to note that".
23. **Stacked hedges.** "could potentially possibly be argued that it
    might" → "may".
24. **Generic endings.** "The future looks bright." State the next
    concrete step or fact.

#### Jargon and plain speech

25. **Abstract metaphor nouns** in user-facing text: substrate, wedge,
    vector, locus, vantage, nexus, harness (metaphor), bedrock,
    scaffolding (metaphor), modality, paradigm, gold-plating, ratchet
    (metaphor), evacuate (for moving code), endgame, north star,
    flywheel. Pick the concrete word. In **this pack's doctrines**,
    `primitive` and `surface` stay; in chat, say "one-job helper" and
    "public API" ([plain-language.md](../pack-shared/plain-language.md)).
26. **Say what it does.** If you cannot restate the sentence as an
    instruction, fact, or number, cut it.
27. **Shorten or split.** One idea per sentence when the reader would
    backtrack.
28. **Active voice.** Name the actor. Passive is fine when the actor is
    unknown or does not matter.
29. **Cut adverbs, or use a stronger verb.** "significantly improves"
    becomes the measured delta.
30. **Prefer the plain word.** "utilize" / "leverage" → "use".
    "facilitate" → "help". "in the event that" → "if".

### Self-audit

After the rewrite, ask: **What makes this obviously generated?** Fix
those tells before the user sees the text. Passing a spellcheck is not
the bar.

## Output

User one-off: the rewritten passage or a diff in the named lane.

Always-on: no extra artifact. The message, ticket, or PR body *is* the
output.

Self-check before the user sees the text:

- [ ] `unslop:scope` (did not break templates, code names, or doctrine terms)
- [ ] `unslop:tells` (no remaining scan hits that still read as generated)
- [ ] `unslop:human-voice` (specific, recommended, mixed rhythm; no fake soul)
- [ ] `unslop:self-audit`
- [ ] `taste:plain-language` for jargon ([plain-language.md](../pack-shared/plain-language.md))
- [ ] No em dash / en dash / horizontal bar (no-emdash rule)

Fail any box → rewrite before sending.

## Apply

Load this doctrine whenever the user will read what you write, including
`/ask-gabriel` replies (gold-standards Read) and every other pack skill
run ([standards.md](../pack-shared/standards.md)).

Run the numbered cleanup in [`SKILL.md`](SKILL.md) when the user names
`/unslop` or asks to tighten existing prose.

For a typo-only edit, still avoid introducing tells. Do not restyle
untouched files.

## Anti-patterns

- Auto-invoking this skill (router stays `/ask-gabriel`)
- Stripping parentheses because pstack did
- Breaking Questions / Locked-in / doctrine schema to "sound human"
- Rewriting `primitive` / `surface` out of doctrines
- Sweeping the repo to unslop files nobody asked for
- Chatbot closings, puffery, or "Great question!"
- Invented metaphor presented as warmth
- A sentence that would fit any other repo's README unchanged
