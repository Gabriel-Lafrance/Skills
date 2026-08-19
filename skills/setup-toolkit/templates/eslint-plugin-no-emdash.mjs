/** Ban em dash, en dash, and horizontal bar in linted source. */

const forbiddenPattern = /[\u2013\u2014\u2015]/g;

export const noEmdashPlugin = {
  meta: {
    name: "no-emdash",
    version: "1.0.0",
  },
  rules: {
    "no-emdash": {
      meta: {
        type: "problem",
        docs: {
          description:
            "Disallow em dashes, en dashes, and horizontal bars. Use a comma, colon, period, or hyphen.",
        },
        schema: [],
        messages: {
          forbidden:
            "Do not use {{name}} ({{ch}}). Use a comma, colon, period, or hyphen.",
        },
      },
      create(context) {
        const sourceCode = context.sourceCode;

        return {
          Program() {
            const text = sourceCode.getText();
            forbiddenPattern.lastIndex = 0;
            let match = forbiddenPattern.exec(text);
            while (match !== null) {
              const ch = match[0];
              const name =
                ch === "\u2014"
                  ? "em dash"
                  : ch === "\u2013"
                    ? "en dash"
                    : "horizontal bar";
              const start = match.index;
              const end = start + ch.length;
              context.report({
                loc: {
                  start: sourceCode.getLocFromIndex(start),
                  end: sourceCode.getLocFromIndex(end),
                },
                messageId: "forbidden",
                data: { ch, name },
              });
              match = forbiddenPattern.exec(text);
            }
          },
        };
      },
    },
  },
};

export const noEmdashConfig = {
  plugins: {
    "no-emdash": noEmdashPlugin,
  },
  rules: {
    "no-emdash/no-emdash": "error",
  },
};
