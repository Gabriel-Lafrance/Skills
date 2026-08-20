/**
 * Quality gate: mechanical cores of named principles.
 * Fix the code. Do not skip, delete, or weaken this test to go green.
 */

import assert from "node:assert/strict";
import { test } from "node:test";

import {
  formatHits,
  hasConvex,
  scanClockInQueries,
  scanFailFast,
  scanIllegalTypes,
  scanUntrustedWrites,
} from "./principle-scan.mjs";

const root = process.cwd();

test("types tell the truth (make illegal states unrepresentable)", () => {
  assertClean(
    scanIllegalTypes(root),
    "types tell the truth (make illegal states unrepresentable)",
    "Replace any and Convex v.any with a real type or validator.",
  );
});

test("fail fast (Fail Fast)", () => {
  assertClean(
    scanFailFast(root),
    "fail fast (Fail Fast)",
    "Throw at the boundary. Do not swallow errors or return a success-flag bag.",
  );
});

test("trust the server (never trust the client)", (t) => {
  if (skipWithoutConvex(t)) return;
  assertClean(
    scanUntrustedWrites(root),
    "trust the server (never trust the client)",
    "Check identity on public mutations and actions.",
  );
});

test("deterministic queries (no clock in queries)", (t) => {
  if (skipWithoutConvex(t)) return;
  assertClean(
    scanClockInQueries(root),
    "deterministic queries (no clock in queries)",
    "Pass time in as an argument. Do not read the clock or randomness inside a query.",
  );
});

function skipWithoutConvex(t) {
  if (hasConvex(root)) return false;
  t.skip("no convex/ directory");
  return true;
}

function assertClean(hits, principle, fix) {
  assert.equal(hits.length, 0, formatHits(hits, principle, fix));
}
