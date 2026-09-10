/**
 * Quality gate: no dead code (Knip).
 * Remove the unused file, export, or dependency. Do not weaken this test to go green.
 */

import assert from "node:assert/strict";
import { execFile } from "node:child_process";
import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { test } from "node:test";
import { promisify } from "node:util";

const runFile = promisify(execFile);

const KNIP_CONFIGS = [
  "knip.json",
  "knip.jsonc",
  ".knip.json",
  ".knip.jsonc",
  "knip.ts",
  "knip.js",
  "knip.config.ts",
  "knip.config.js",
];

const PRINCIPLE = "no dead code (Knip)";
const FIX =
  "Remove the unused file, export, or dependency. If Knip is wrong, narrow entry and project in knip.json.";

test("no dead code (Knip)", async (t) => {
  const root = process.cwd();
  if (!hasKnipConfig(root)) {
    t.skip("no knip config");
    return;
  }
  const bin = knipBin(root);
  if (!existsSync(bin)) {
    t.skip("knip is not installed");
    return;
  }
  const stdout = await knipJson(bin, root);
  const hits = parseKnipIssues(stdout);
  assert.equal(hits.length, 0, formatKnipHits(hits));
});

function hasKnipConfig(root) {
  for (const name of KNIP_CONFIGS) {
    if (existsSync(join(root, name))) return true;
  }
  return hasPackageJsonKnip(root);
}

function hasPackageJsonKnip(root) {
  try {
    const pkg = JSON.parse(readFileSync(join(root, "package.json"), "utf8"));
    return pkg.knip !== undefined && pkg.knip !== null;
  } catch {
    return false;
  }
}

function knipBin(root) {
  const name = process.platform === "win32" ? "knip.cmd" : "knip";
  return join(root, "node_modules", ".bin", name);
}

async function knipJson(bin, root) {
  try {
    const { stdout } = await runFile(bin, ["--reporter", "json"], { cwd: root });
    return stdout;
  } catch (error) {
    return stdoutFromKnipError(error);
  }
}

function stdoutFromKnipError(error) {
  if (isExecError(error) && error.code === 1 && typeof error.stdout === "string") {
    return error.stdout;
  }
  throw new Error(`Knip did not run. ${stderrOf(error)}`, { cause: error });
}

function isExecError(error) {
  return typeof error === "object" && error !== null && "code" in error;
}

function stderrOf(error) {
  if (typeof error === "object" && error !== null && "stderr" in error) {
    return String(error.stderr).trim();
  }
  return String(error);
}

function parseKnipIssues(stdout) {
  let parsed;
  try {
    parsed = JSON.parse(extractJson(stdout));
  } catch {
    throw new Error(
      `Knip returned output this test cannot read. Run npx knip and read its report.\n${stdout}`,
    );
  }
  const issues = Array.isArray(parsed.issues) ? parsed.issues : [];
  return issues.flatMap(knipHitsForFile);
}

function extractJson(stdout) {
  const start = stdout.indexOf("{");
  const end = stdout.lastIndexOf("}");
  if (start === -1 || end === -1 || end < start) return stdout;
  return stdout.slice(start, end + 1);
}

function knipHitsForFile(group) {
  const hits = [];
  for (const [issueType, entries] of Object.entries(group)) {
    collectKnipHits(group.file, issueType, entries, hits);
  }
  return hits;
}

function collectKnipHits(file, issueType, entries, hits) {
  if (isReportMeta(issueType)) return;
  if (!Array.isArray(entries)) return;
  for (const entry of entries) {
    hits.push(knipHit(file, issueType, entry));
  }
}

function isReportMeta(issueType) {
  return issueType === "file" || issueType === "owners";
}

function knipHit(file, issueType, entry) {
  const line = entryLine(entry);
  const location = line === null ? String(file) : `${file}:${line}`;
  return `${location} ${knipSubject(issueType, entry)}`;
}

function entryLine(entry) {
  if (typeof entry === "object" && entry !== null && Number.isInteger(entry.line)) {
    return entry.line;
  }
  return null;
}

function knipSubject(issueType, entry) {
  return `${issueType} ${entryName(entry)}`.trim();
}

function entryName(entry) {
  if (typeof entry === "object" && entry !== null && typeof entry.name === "string") {
    return entry.name;
  }
  return "issue";
}

function formatKnipHits(hits) {
  return [PRINCIPLE, FIX, ...hits].join("\n");
}
