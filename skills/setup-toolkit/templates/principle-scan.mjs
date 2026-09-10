/**
 * Scanners for principle-gate.test.mjs.
 * Each function stays under the cyclomatic cap. Do not add a UI import denylist.
 */

import { existsSync, readdirSync, readFileSync } from "node:fs";
import { basename, extname, join, relative } from "node:path";

const SKIP_DIRS = new Set([
  "node_modules",
  "dist",
  "build",
  ".next",
  "coverage",
  "_generated",
]);

const CODE_EXT = new Set([".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx"]);

const GATE_FILES = new Set([
  "complexity.test.mjs",
  "principle-gate.test.mjs",
  "principle-scan.mjs",
  "cyclomatic-cap.mjs",
  "knip.test.mjs",
]);

const AUTH_EXEMPT = new Set([
  "http.ts",
  "http.js",
  "httpActions.ts",
  "httpActions.js",
  "crons.ts",
  "crons.js",
]);

export function hasConvex(root) {
  return existsSync(join(root, "convex"));
}

function hasTsconfig(root) {
  return existsSync(join(root, "tsconfig.json"));
}

export function formatHits(hits, principle, fix) {
  const lines = hits.map((hit) => `${hit.file}:${hit.line} ${principle}. ${fix}`);
  return [principle, fix, ...lines].join("\n");
}

export function scanIllegalTypes(root) {
  const scanTsAny = hasTsconfig(root);
  const hits = [];
  for (const file of appCodeFiles(root)) {
    collectTypeHits(root, file, scanTsAny, hits);
  }
  return hits;
}

export function scanFailFast(root) {
  const hits = [];
  for (const file of appCodeFiles(root)) {
    collectFailFastHits(root, file, hits);
  }
  return hits;
}

export function scanUntrustedWrites(root) {
  if (!hasConvex(root)) return [];
  const hits = [];
  for (const file of convexCodeFiles(root)) {
    collectUntrustedHits(root, file, hits);
  }
  return hits;
}

export function scanClockInQueries(root) {
  if (!hasConvex(root)) return [];
  const hits = [];
  for (const file of convexCodeFiles(root)) {
    collectClockHits(root, file, hits);
  }
  return hits;
}

function appCodeFiles(root) {
  const out = [];
  collectFiles(root, root, out);
  return out;
}

function convexCodeFiles(root) {
  const out = [];
  collectFiles(join(root, "convex"), join(root, "convex"), out);
  return out;
}

function collectFiles(root, dir, out) {
  let entries;
  try {
    entries = readdirSync(dir, { withFileTypes: true });
  } catch {
    return;
  }
  for (const entry of entries) {
    handleEntry(root, dir, entry, out);
  }
}

function handleEntry(root, dir, entry, out) {
  const full = join(dir, entry.name);
  if (entry.isDirectory()) {
    addDir(root, full, entry.name, out);
    return;
  }
  addFile(full, entry.name, out);
}

function addDir(root, full, name, out) {
  if (SKIP_DIRS.has(name)) return;
  if (name.startsWith(".")) return;
  collectFiles(root, full, out);
}

function addFile(full, name, out) {
  if (GATE_FILES.has(name)) return;
  if (!CODE_EXT.has(extname(name))) return;
  out.push(full);
}

function collectTypeHits(root, file, scanTsAny, hits) {
  const lines = readFileSync(file, "utf8").split("\n");
  for (let i = 0; i < lines.length; i++) {
    pushTypeHit(root, file, lines[i], i + 1, scanTsAny, hits);
  }
}

function pushTypeHit(root, file, line, lineNo, scanTsAny, hits) {
  if (lineIsComment(line)) return;
  if (!typeLineIsIllegal(line, scanTsAny)) return;
  hits.push({ file: relative(root, file), line: lineNo });
}

function typeLineIsIllegal(line, scanTsAny) {
  if (vAnyPattern().test(line)) return true;
  return scanTsAny && tsAnyPattern().test(line);
}

function collectFailFastHits(root, file, hits) {
  const source = readFileSync(file, "utf8");
  pushPatternHits(root, file, source, emptyCatchPattern(), hits);
  pushPatternHits(root, file, source, resultBagPattern(), hits);
}

function pushPatternHits(root, file, source, pattern, hits) {
  const global = new RegExp(pattern.source, "g");
  let match = global.exec(source);
  while (match) {
    hits.push({
      file: relative(root, file),
      line: lineNumberAt(source, match.index),
    });
    match = global.exec(source);
  }
}

function collectUntrustedHits(root, file, hits) {
  if (AUTH_EXEMPT.has(basename(file))) return;
  const source = readFileSync(file, "utf8");
  for (const chunk of chunksFromSource(source)) {
    pushUntrustedHit(root, file, source, chunk, hits);
  }
}

function pushUntrustedHit(root, file, source, chunk, hits) {
  if (!isPublicWrite(chunk.text)) return;
  if (hasIdentityHelper(chunk.text)) return;
  hits.push({
    file: relative(root, file),
    line: lineNumberAt(source, chunk.start),
  });
}

function collectClockHits(root, file, hits) {
  const source = readFileSync(file, "utf8");
  for (const chunk of chunksFromSource(source)) {
    pushClockHit(root, file, source, chunk, hits);
  }
}

function pushClockHit(root, file, source, chunk, hits) {
  if (!hasQueryWrapper(chunk.text)) return;
  const match = clockPattern().exec(chunk.text);
  if (!match) return;
  hits.push({
    file: relative(root, file),
    line: lineNumberAt(source, chunk.start + match.index),
  });
}

function chunksFromSource(source) {
  const starts = exportStarts(source);
  const chunks = [];
  for (let i = 0; i < starts.length; i++) {
    chunks.push({
      start: starts[i],
      text: source.slice(starts[i], nextStart(starts, i, source.length)),
    });
  }
  return chunks;
}

function exportStarts(source) {
  const starts = [];
  const pattern = /^export const /gm;
  let match = pattern.exec(source);
  while (match) {
    starts.push(match.index);
    match = pattern.exec(source);
  }
  return starts;
}

function nextStart(starts, index, fallback) {
  if (index + 1 < starts.length) return starts[index + 1];
  return fallback;
}

function isPublicWrite(text) {
  if (isInternalWrite(text)) return false;
  return hasMutationWrapper(text) || hasActionWrapper(text);
}

function isInternalWrite(text) {
  return (
    /\binternalMutation\s*\(\s*\{/.test(text) ||
    /\binternalAction\s*\(\s*\{/.test(text)
  );
}

function hasMutationWrapper(text) {
  return /\bmutation\s*\(\s*\{/.test(text);
}

function hasActionWrapper(text) {
  return /\baction\s*\(\s*\{/.test(text);
}

function hasQueryWrapper(text) {
  return /\b(?:internalQuery|query)\s*\(\s*\{/.test(text);
}

function hasIdentityHelper(text) {
  return /requireUser|getUserIdentity|getAuthUserId|auth\.getUserId/.test(text);
}

function lineIsComment(line) {
  const trimmed = line.trimStart();
  if (trimmed.startsWith("//")) return true;
  if (trimmed.startsWith("*")) return true;
  return trimmed.startsWith("/*");
}

function lineNumberAt(source, index) {
  return source.slice(0, index).split("\n").length;
}

function tsAnyPattern() {
  return /(?::\s*any\b|\bas any\b|<any>)/;
}

function vAnyPattern() {
  return new RegExp("\\bv" + "\\.any\\s*\\(");
}

function emptyCatchPattern() {
  return /catch\s*(?:\([^)]*\))?\s*\{\s*\}/;
}

function resultBagPattern() {
  return new RegExp("\\{\\s*success:\\s*(?:true|false)\\b");
}

function clockPattern() {
  return new RegExp(
    [
      "Date\\.now\\s*\\(",
      "new Date\\s*\\(",
      "Math\\.random\\s*\\(",
      "crypto\\.randomUUID\\s*\\(",
    ].join("|"),
  );
}
