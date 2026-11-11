# Convex

**Open this when:** the repo has a `convex/` folder and you are about to name, place, query, validate, or verify Convex code.

## Naming and files

- `convex/**` file names use **no `-` or `_`** (`orders.ts`, `orderActions.ts`; `billing.ts`, not `billing-actions.ts`).
- A Convex file exposes a small set of queries, mutations and actions. Only the owning Convex file holds Stripe or auth logic.

## Folders

A one-file concern may stay `convex/billing.ts` if that is the repo pattern. A second file moves the cluster into `convex/billing/` (no root `billingStripe.ts`), and `convex/billing.ts` and `convex/billing/` never coexist.

## Queries and validators

| Don't | Do |
| --- | --- |
| `.filter` scans, or `collect()` then reduce | `.withIndex` on filter and sort fields |
| Unbounded `.collect()` on a growing table | Paginate or aggregate |

Argument and return validators use specific types, never `v.any()`.

## Terminals

`npx convex dev` may already be running. Read its terminal for push success before any Convex check. By default, read terminals instead of running:

- Convex MCP (`status`, `data`, `tables`, `logs`, `run`, `runOneoffQuery`, `insights`, `functionSpec`, env tools) just to verify.
- `npx convex`, deploy, or codegen after every slice while `convex dev` is watching.
- A second Convex process when one is already up.

Use Convex MCP only under the conditions in [Verify terminals first](tooling.md#verify-terminals-first). Cite evidence as `terminals/3.txt: convex push ok`, not a fresh MCP round-trip.
