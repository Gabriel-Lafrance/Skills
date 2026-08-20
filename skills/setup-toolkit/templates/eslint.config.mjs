import js from "@eslint/js";
import prettier from "eslint-config-prettier";
import tseslint from "typescript-eslint";

import { maxCyclomaticComplexity } from "./cyclomatic-cap.mjs";
import { noEmdashConfig } from "./eslint-plugin-no-emdash.mjs";

export default tseslint.config(
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
  js.configs.recommended,
  tseslint.configs.recommended,
  prettier,
  noEmdashConfig,
  {
    rules: {
      complexity: ["error", maxCyclomaticComplexity],
      "no-empty": ["error", { allowEmptyCatch: false }],
    },
  },
  {
    files: ["**/*.ts", "**/*.tsx"],
    rules: {
      "@typescript-eslint/no-explicit-any": "error",
      "@typescript-eslint/no-unused-vars": [
        "error",
        { argsIgnorePattern: "^_", varsIgnorePattern: "^_" },
      ],
    },
  },
);
