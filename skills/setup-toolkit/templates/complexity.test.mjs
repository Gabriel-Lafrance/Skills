/**
 * Quality gate: each function stays at or under cyclomatic complexity 5.
 * Split extra branches into named helpers. This is not a behavior test.
 */

import assert from "node:assert/strict";
import { relative } from "node:path";
import { test } from "node:test";
import { ESLint } from "eslint";

import { maxCyclomaticComplexity } from "./cyclomatic-cap.mjs";

test("each function stays at or under cyclomatic complexity 5", async () => {
  const eslint = new ESLint({
    overrideConfigFile: true,
    overrideConfig: [
      {
        ignores: [
          "**/node_modules/**",
          "**/dist/**",
          "**/build/**",
          "**/.next/**",
          "**/coverage/**",
          "**/convex/_generated/**",
        ],
      },
      {
        rules: {
          complexity: ["error", maxCyclomaticComplexity],
        },
      },
    ],
  });

  const results = await eslint.lintFiles([
    "**/*.{js,mjs,cjs,jsx,ts,tsx}",
  ]);

  const failures = results.flatMap((result) =>
    result.messages
      .filter((message) => message.ruleId === "complexity")
      .map((message) => {
        const file = relative(process.cwd(), result.filePath);
        return `${file}:${message.line} ${message.message}`;
      }),
  );

  assert.equal(
    failures.length,
    0,
    [
      `Cyclomatic complexity (McCabe) must stay at or under ${maxCyclomaticComplexity}.`,
      "Split extra branches into named helpers. Do not raise the cap.",
      ...failures,
    ].join("\n"),
  );
});
