# Performance variant

A [hillclimb](../SKILL.md) variant. The shared loop, budget and ownership stay
in the skill; this file only says what to measure and what counts as better.

## Picks it

The goal is the speed, size, or resource use of a named path: page load or Web
Vitals, endpoint or job latency, throughput, query time, bundle or binary size,
memory, CPU, cold start, or build or test time. The user will judge it by a
number from a repeatable measurement.

## Read when

- A cache, batch, memo or precomputed value that spans users, tenants, roles or
  permissions: [Authority](../../rules/code-structure.md#authority).
- A new committed benchmark or performance test:
  [no-unrequested-tests.md](../../rules/no-unrequested-tests.md). It needs the
  same consent as any new test; a throwaway measurement command does not.

## Roles

- Reviewer: the shared `reviewer` role, reading measurements and profiles as
  well as the diff.
- Implementer: the shared `implementer` role, or `designer` when the change is
  in user-facing UI code.

## Evidence

- Pin the measurement before the baseline: metric and unit, the command or
  tool, workload and data, environment (machine, build mode, warm or cold,
  concurrency), and run count. Prefer the repository's existing benchmark,
  profiler, load script or trace setup.
- Time production-like builds: no dev mode, debug flags or attached profiler
  during timed runs. Profile in separate runs.
- Run each side at least five times under the same conditions, unless the user
  sets another count or one run is costly; state the count. Report the median
  and the spread (minimum to maximum), never a single run.
- Guard against drift between batches (background load, thermal throttling, a
  warming cache). Interleave baseline and candidate runs when both builds can
  run side by side; otherwise rerun the baseline after the candidate. If the
  repeated baseline moved by more than its spread, the comparison is
  inconclusive.
- Profile before proposing a fix: a flame graph, trace, query plan, network
  waterfall or bundle analysis names where the time or bytes go. A finding
  with no measured hotspot is a hypothesis, not a finding.
- No claim of production impact, user-perceived speed or cost savings from a
  local measurement, and no carrying one machine's numbers to another.

## Lens

- The largest measured share first: the hotspot the profile names, not the code
  that looks slow.
- Repeated work: N+1 queries, repeated fetches or renders, recomputation an
  index or memo removes, work inside a loop that belongs outside it.
- Waiting: serial calls that can run together, blocking I/O on a hot path,
  request waterfalls, missing pagination or streaming.
- Bytes: oversized payloads, images, bundles, and code or dependencies loaded
  before they are needed.
- Algorithmic cost at realistic data sizes; skip micro-optimizations below the
  noise.
- Remove work before adding a cache. A cache needs an owner, a key, invalidation
  and a size bound.

## Keep or reject

Keep a candidate when the drift check passes, its median beats the baseline's
by more than the larger of the two spreads, or meets the target the user set,
and every guard holds.
Reject it when:

- Behavior changes: existing tests fail, outputs differ, errors are swallowed,
  or validation, authorization or ordering guarantees are dropped.
- Another pinned metric gets worse past its threshold (memory for latency,
  bundle size for runtime) and the user did not accept that trade.
- A cache can serve data past its stated freshness, or across users, tenants or
  permissions.
- The gain exists only for the measured input (special cases, a warm cache
  production lacks) or comes from lowering quality, limits or coverage outside
  the scope.
- The added complexity buys a gain inside the noise.
