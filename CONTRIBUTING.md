# Contributing

## Add a skill

1. Create `skills/<skill-name>/SKILL.md` (lowercase, hyphens).
2. Frontmatter must include `name` and `description` (third person, WHAT + WHEN).
3. Keep `SKILL.md` under ~500 lines. Put long examples in `examples.md`.
4. Wire it into the flow if needed: update [`ask-gabriel`](./skills/ask-gabriel/SKILL.md), [`goal`](./skills/goal/SKILL.md), and this repo’s [README](./README.md) catalog.
5. Local check:

```bash
npx skills@latest add . --list
```

## Conventions

- Cursor-native: Plan mode, CreatePlan, Task subagents, validate gates.
- Prefer one skill = one job.
- No YouTube (or other video) links in skill bodies — teach the principle in prose.
- Do not put secrets in skills.

## License

By contributing, you agree your changes are MIT-licensed like the rest of the repo.
