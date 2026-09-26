# Testing

Changing code is not a reason to add a test.

Do not create or extend a test for a small tweak, copy change, rename, comment, type-only edit, wiring change, formatter, UI chrome, generated code, or a one-line fix. Do not add a test to chase coverage, to restate the implementation (`expect(add(1, 2)).toBe(3)`), or because the suite should cover this.

Running tests that already exist is fine. Fix an existing assertion only when this change made that assertion lie. Do not add a new case next to it.

Write a test only when the user has accepted that lock:

- they explicitly asked for it, or
- they answered yes on a `/task` behavior-lock brief after grill Locked (each brief cites a grilled rule; every brief has a no; silence and a parent taking `recommended` are not acceptance), or
- they started `/create-test` after `/review` recommended one for a complex public surface (authorization, ownership, safe-to-retry, a domain rule that can silently drift).

Then write it by following `/create-test`. Do not start `/create-test` without one of those acceptances. If the target is trivial, say so and stop.

This binds every skill, including `/task` build slices and `/design`.
