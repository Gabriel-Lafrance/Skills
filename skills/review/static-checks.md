# Static checks

Report what you ran and what it said.

## Knip (no dead code)

1. Inspect changed exports, dependencies, and their reachability first; an unrelated root scan is optional.
2. Use the repository's existing Knip script, scoped when adequate, or its full command for broad reachability or dependency impact or a required gate. If tooling is absent, inspect the entry and import graph and report what remains unproven; never silently install a new checker for a small review.

**Clean** means Knip exits 0 and prints no issues.

Fix a finding instead of adding an ignore entry to go green.

## Cyclomatic complexity (cap of 6)

1. If the repo's ESLint config already sets `complexity` to 6 (or lower), run the repo lint script on the changed files.
2. Otherwise, if ESLint is already installed and configured, run its local binary once with the rule forced (do not use a command that fetches missing tooling):

   ```bash
   ./node_modules/.bin/eslint --rule '{"complexity":["error",6]}' <changed files>
   ```

   If TypeScript files fail to parse under the repo config, count by hand.
3. With no usable installed ESLint/config, count McCabe complexity of changed functions by hand and disclose the tool gap. Above 6 is a finding.

Only report functions the diff added or changed. The fix is to extract a named helper, not to raise the cap.

## Other languages

Use the language's usual tool for unused code and complexity (for example `vulture` and `radon cc` for Python, `staticcheck` and `gocyclo` for Go), or count by hand with the rule above. Say which one you used in the review output.
