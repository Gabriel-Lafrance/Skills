# Attribution

PR lifecycle and harness refinements use original wording informed by
[t3dotgg/tstack at 7de017b](https://github.com/t3dotgg/tstack/tree/7de017b3fc9d50c03cf3ecb98fb71e0ca65a78bd/skills),
checked on 2026-10-26: `babysit-pr` (parent-owned watch and cleanup), `sol-loop`
(finite review rounds), `modernize` (intent before branch refresh), `takeover`
(authorship and current relevance), and `file-pr` (problem and outcome first).
The pack retains its own review, permissions, no-force-push and draft shipping
contracts. No upstream orchestration script or full skill is vendored. The
upstream [MIT license notice](third-party/tstack-LICENSE.txt) is retained
separately from runtime instructions.

T3 adaptation facts were checked against
[orchestration instructions](https://github.com/pingdotgg/t3code/blob/e762f09e265b31607261ead2b4517c467ff59c28/packages/provider-core/src/server/orchestrationInstructions.ts),
[MCP lifecycle documentation](https://github.com/pingdotgg/t3code/blob/e762f09e265b31607261ead2b4517c467ff59c28/docs/orchestration-v2/orchestrator-mcp-server.md),
and [source-control watch documentation](https://github.com/pingdotgg/t3code/blob/e762f09e265b31607261ead2b4517c467ff59c28/docs/user/source-control.md)
at `e762f09`, checked on 2026-10-26. These are provenance, not frozen tool
schemas: the installed live harness instructions, capabilities and permissions
govern. No T3 source code is copied.

Architecture and navigation refinements use original wording informed by [Matt Pocock's architecture investigation](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md) (friction, deep public boundaries, and change locality; [MIT](https://github.com/mattpocock/skills/blob/main/LICENSE), copyright 2026 Matt Pocock) and [Aider's repository map documentation](https://aider.chat/docs/repomap.html) (relevant paths, symbols, and signatures before implementation detail), checked on 2026-10-05. No upstream text, automatic map, report workflow, or tooling dependency is vendored; this pack uses its existing scoped chat handoffs and authorization rules.

Grill guidance uses original wording informed by [Matt Pocock's grilling skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md), checked on 2026-10-05: prerequisite-aware rounds, environment fact lookup, recommendations, and recomputing dependent choices after replies. [MIT](https://github.com/mattpocock/skills/blob/main/LICENSE), copyright 2026 Matt Pocock. No upstream text or tool-specific workflow is vendored. This pack retains its existing announce-only lock, test permissions, and user control over stopping or deferring.

Ticket and working-output guidance uses original wording informed by these methods, checked on 2026-10-05. No upstream template or workflow is vendored; runtime rules are self-contained.

- [Superpowers writing-plans](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md): specify affected files, interfaces, fixed values, and observable verification instead of leaving consequential choices implicit.
- [spec-kit tasks template](https://github.com/github/spec-kit/blob/main/templates/tasks-template.md): group work by outcome and use item IDs to make dependencies readable.
- [GSD summary template](https://github.com/gsd-build/get-shit-done/blob/main/get-shit-done/templates/summary.md): lead summaries with delivered outcomes, evidence, decisions, and remaining work.

Provenance for maintainers, not agent workflow instructions. The UX integration uses original wording and selectively synthesizes the ideas below; no upstream skill, checklist, or implementation is vendored. Sources were checked on 2026-10-03.

- [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/477bcb28c9812b385cb51a4605ddf30d7b2266e2/.claude/skills/ui-ux-pro-max/SKILL.md) and [UX guidelines](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/477bcb28c9812b385cb51a4605ddf30d7b2266e2/src/ui-ux-pro-max/data/ux-guidelines.csv): scoped retrieval, redundant entry, control semantics, and feedback. [MIT](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/477bcb28c9812b385cb51a4605ddf30d7b2266e2/LICENSE), copyright 2024 Next Level Builder.
- [Impeccable references](https://github.com/pbakaus/impeccable/tree/e103efe779e2dd01274dabae83531fef00bf2563/skill/reference) (`distill`, `critique`, `operate`, `new-work`, `harden`): purposeful actions, familiar operational UI, reuse, and recovery. [Apache 2.0](https://github.com/pbakaus/impeccable/blob/e103efe779e2dd01274dabae83531fef00bf2563/LICENSE), copyright 2025 Paul Bakaus.
- [Vercel Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines/blob/e3d624baaf29dc1fc645aff3e38f03e564d2d6b1/command.md): state, navigation, keyboard, and focus checks. [MIT](https://github.com/vercel-labs/web-interface-guidelines/blob/e3d624baaf29dc1fc645aff3e38f03e564d2d6b1/LICENSE), copyright 2025 Vercel Labs.
- [Anthropic frontend-design](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/frontend-design/SKILL.md): brief, visual hierarchy, type, spacing, and rendered critique. [Apache 2.0](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/frontend-design/LICENSE.txt).
