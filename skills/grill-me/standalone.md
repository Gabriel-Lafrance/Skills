# Grill Me standalone

Interview a one-off ask until shared understanding is clear. Read
[doctrine.md](doctrine.md), the shared
[execution context](../pack-shared/execution-context.md), and the
[asking contract](../pack-shared/asking.md).

## Process

1. Establish a compact in-chat execution context from the ask and rediscovered
   repository, ticket, PR, or diff facts.
2. Batch the doctrine's unsettled product, behavior, language, policy, taste,
   architecture, design, split, and lane questions.
3. Update the visible context with each user answer and applicable Active Rule.
   Announce the Locked closure when the material decisions are resolved.
4. Stop after shared understanding unless the user explicitly asks for the
   next step. `/goal` receives the inline context; `/write-ticket` may receive
   the relevant memo and decisions.

Do not create automatic files for language, choices, rules, progress, or the
interview. If the user wants a durable artifact, ask for or honor an approved
destination under the shared
[optional-persistence rule](../pack-shared/execution-context.md#optional-persistence).

## Hand-offs

- Structure needed → `/architecture`, then `/goal`.
- Ready to build → `/goal`.
