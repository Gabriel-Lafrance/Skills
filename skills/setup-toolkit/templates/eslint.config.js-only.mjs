import js from "@eslint/js";
import prettier from "eslint-config-prettier";
import globals from "globals";

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
    languageOptions: {
      globals: { ...globals.node, ...globals.browser },
    },
    rules: {
      complexity: ["error", 5],
      "no-empty": ["error", { allowEmptyCatch: false }],
    },
  },
];
