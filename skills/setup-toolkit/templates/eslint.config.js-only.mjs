import js from "@eslint/js";
import prettier from "eslint-config-prettier";

import { maxCyclomaticComplexity } from "./cyclomatic-cap.mjs";
import { noEmdashConfig } from "./eslint-plugin-no-emdash.mjs";

export default [
  {
    ignores: [
      "**/node_modules/**",
      "**/dist/**",
      "**/build/**",
      "**/.next/**",
      "**/coverage/**",
    ],
  },
  js.configs.recommended,
  prettier,
  noEmdashConfig,
  {
    rules: {
      complexity: ["error", maxCyclomaticComplexity],
    },
  },
];
