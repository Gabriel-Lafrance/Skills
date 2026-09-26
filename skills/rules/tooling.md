# Tooling

Do **not** paste a style guide into chat. If this repo already has ESLint or Prettier, **follow those configs**.

- Add or change lint/format tooling with `/setup-toolkit` after the user says yes to that phase. Do not invent a parallel config.
- The toolkit ESLint baseline includes `no-emdash/no-emdash` (em dash, en dash, horizontal bar). Keep that rule on. Do not disable it to "make the prose look fancy."
- The toolkit also installs `test:quality` (complexity cap 5, principle gates, plus `knip.test.mjs` for dead code) and `test:mutants` (Stryker: flipped operators must fail the suite). Keep them. Do not raise the cap, skip a gate, delete a gate, or lower the mutant break threshold to go green. Split the function, type the value, throw at the boundary, check identity, remove dead code, or strengthen the lock instead. Gate failures use plain (Classic), for example fail fast (Fail Fast).
- Editor workspace files live in `.vscode/extensions.json` and `.vscode/settings.json`. Do not add a parallel `.cursor/extensions.json`.
- Do **not** ritual-run `eslint`, `tsc`, or full suites after every slice. CI and the user's running terminals own that loop (`taste` Verify).
- **Before a push that opens or updates a PR:** run the CI mirror in `pack-shared/pr-ship.md` in this environment, then push once. A local commit with no open PR and no push does not run that suite. Skip `test:mutants` unless the pull_request workflow runs it. If there is no workflow and no lint or test script, say so. Never `git commit --no-verify` unless the user asked.
- Run lint or format when the user asked, when a named review finding requires it, or when you just added the config and need one smoke check.
- Do not reformat the whole tree as a drive-by. Format only files you already had to touch, unless the user asked for a repo-wide format.
- Never overwrite an existing `eslint.config.*`, Prettier config, or `.vscode/settings.json` without asking.
