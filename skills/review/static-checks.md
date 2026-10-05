# Static checks

How to check the two mechanical Standards rules in a review: no dead code (Knip) and the cyclomatic cap of 5. Report what you ran and what it said.

## Knip (no dead code)

1. Select dead-code checks under [verification scope](../rules/execution.md#verification-scope). Inspect changed exports/dependencies and affected reachability first; an unrelated root scan is not mandatory on every review.
2. Use the repository's existing Knip script/installation with supported scope when adequate, or its full command for broad reachability/dependency impact or a required gate. Reuse valid evidence. If tooling is absent, inspect the relevant entry/import graph and report what remains unproven; do not silently install a new checker for a small review.

**Clean** means Knip exits 0 and prints no issues.

Knip groups its output by kind:

- **Unused files:** files no entry point reaches. Delete them.
- **Unused dependencies / devDependencies:** packages in `package.json` nothing imports. Remove them.
- **Unlisted dependencies:** imports of packages missing from `package.json`. Add them.
- **Unused exports / types:** exported names no other file imports. Drop the `export` or delete the code.

A finding is **Fix now** when the diff introduced it (a new file, export, or dependency, or an edit that orphaned one). A finding in code the diff did not touch is a Follow-up. Fix the finding instead of adding an ignore entry to go green.

## Cyclomatic complexity (cap of 5)

1. If the repo's ESLint config already sets `complexity` to 5 (or lower), run the repo lint script on the changed files.
2. Otherwise, if ESLint is already installed and configured, run its local binary once with the rule forced (do not use a command that fetches missing tooling):

   ```bash
   ./node_modules/.bin/eslint --rule '{"complexity":["error",5]}' <changed files>
   ```

   This uses the repo's ESLint config, so TypeScript files parse only when that config sets up the TypeScript parser. If they fail to parse, count by hand.
3. With no usable installed ESLint/config, count changed functions by hand and disclose the tool gap. A function starts at 1. Each `if`, `else if`, loop (`for`, `while`, `do`), `catch`, `case`, ternary `?:`, `&&`, `||`, and `??` adds one. Above 5 is a finding.

Only report functions the diff added or changed. The fix is to extract a named helper, not to raise the cap.

## Other languages

Use the language's usual tool for unused code and complexity (for example `vulture` and `radon cc` for Python, `staticcheck` and `gocyclo` for Go), or count by hand with the rule above. Say which one you used in the review output.
