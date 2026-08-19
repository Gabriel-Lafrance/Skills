# Unslop examples

Concrete good vs bad. Prefer matching **good**.

## Content tells

**Puffery (bad):** This release is a pivotal moment and a testament to
our evolving landscape.

**Puffery (good):** `/unslop` is now a pack skill. Agents Read it before
user-facing chat.

**Hollow -ing (bad):** The change improves reliability, ensuring teams
can ship with confidence.

**Hollow -ing (good):** Public writes call `requireUser` before the
patch. A missing identity throws.

**Vague attribution (bad):** Experts believe this pattern does not
scale.

**Vague attribution (good):** Unbounded `.collect()` on `events` timed
out in production at ~50k rows.

## Language tells

**AI vocabulary (bad):** This section delves into the intricate
interplay of taste and architecture.

**AI vocabulary (good):** Taste is how a unit reads. Architecture is
where it lives.

**Not just X, but Y (bad):** This is not just a linter, but a full
writing discipline.

**Not just X, but Y (good):** Unslop cuts AI tells. It is not a linter.

**Synonym cycling (bad):** The protagonist (the main character, our
central figure) calls the helper.

**Synonym cycling (good):** `checkout` calls `billing.makeUserPay`.

## Style tells

**Mid-sentence colon crutch (bad):** If you're coming from User Rules:
instead of pasting gold standards, install the plugin.

**Mid-sentence colon crutch (good):** Install the plugin. Do not paste
gold standards into User Rules.

**Inline-header restatement (bad):**

- **Performance:** Performance improved after the index.

**Inline-header restatement (good):**

- **Schema in TypeScript.** Tables live in one file.

**Title Case (bad):** `## What The Plugin Ships`

**Title Case (good):** `## What the plugin ships`

## Chat tells

**Chatbot closing (bad):** I hope this helps! Let me know if you want
me to apply it.

**Chatbot closing (good):** `/unslop` is in the Guide catalog. Say
`/unslop` on a file when you want a rewrite.

**Sycophancy (bad):** Great question! You're absolutely right to want
this.

**Sycophancy (good):** Apply it two ways: always-on via standards, and
`/unslop` when you name a file.

## Filler and plain speech

**Filler (bad):** It is important to note that, in order to unslop, we
need to scan for tells.

**Filler (good):** Scan for tells, then rewrite.

**Mood instead of mechanism (bad):** Types that follow your schema, SQL
you can read, a database that stays close at hand.

**Mood instead of mechanism (good):** A column rename fails the build.
`.toSQL()` returns the string sent to the database.

**Could-be-any-repo (bad):** We take quality seriously and ship with
confidence.

**Could-be-any-repo (good):** Installed skills must Read `/taste` and
`/architecture` on every run.

## Scope (do not "fix")

**Wrong (strip parentheses):** Gold standards (plugin rule) force the
Reads.

**Right (parentheses stay):** Gold standards (plugin rule) force the
Reads.

**Wrong (rewrite doctrine terms):** "Reuse the existing one-job helper
inside the deep public API." in `architecture/doctrine.md`

**Right (doctrine keeps cite keys; chat uses ordinary words):** Doctrine
says `architecture:primitives`. Chat says "reuse the existing one-job
helper."
