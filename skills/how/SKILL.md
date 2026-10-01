---
name: how
description: Answers how a system works as a senior onboarding model covering overview, concepts, flow, where code lives, and gotchas. Use when the user asks how something works, wants a walkthrough, or asks about ownership or layering. Does not write tickets or code.
category: Documents
---

# How

Answer "how does X work?" with the mental model a senior would give on day one. Not annotated source.

`/why` answers why it is this way. `/analyze` writes the broader memo (a bug, an idea, impact, a `/task` seed). This skill does not write tickets or code, and it does not start a build. `/task` stays the build hub.

The section shape is adapted from poteto's [pstack](https://github.com/backnotprop/pstack) `/how` (MIT). The steps below are this pack's.

## Read when

- About to search the repo or read large files? Open [main-context.md](../rules/main-context.md). Skip it and the walkthrough drowns in file dumps.
- About to describe layers, ownership, or a public API? Open [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md). Skip them and the model copies a messy layout.
- About to reply? Open [Plain language](../rules/writing-style.md#plain-language) and [Unslop](../rules/writing-style.md#unslop). Skip them and the walkthrough reads like a tour script.
- About to ask the user anything? Open [Asking the user](../rules/writing-style.md#asking-the-user). Skip it and you ask what the repo already answers.

## Contract

- Read only. Do not edit code, open a ticket, or start `/task`.
- Judgment stays in this chat. Bulk reading goes to readonly explorers that return a short result.
- Harness-agnostic. When the harness allows model choice, use a strong reasoning model for synthesis. Do not hardcode a vendor or a model slug.

## Process

1. Name the thing: a flow, a module, or a request path. If two targets fit, ask once which one, with a recommendation.
2. Judge simple or complex before reading widely.
   - **Simple:** one cohesive path, a few files, one owner. One readonly pass in this chat, with narrow reads. No explorer.
   - **Complex:** several layers, several owners, or a path you cannot hold in one pass. Launch 2 to 4 readonly explorers in parallel. Ask each for paths, symbols, and a short note. Synthesize here. When the harness has no subagent, do the same pass as narrow reads, one area at a time, then synthesize once.
3. Write the sections below. Lead with the model. Do not paste source as the answer.

## Answer

### Overview

What it does, who calls it, and what it returns or changes. A few sentences.

### Key concepts

The few nouns a newcomer must have. One sentence each.

### How it works

The path, in order. Name the modules. A small Mermaid diagram when the path has more than two hops.

### Where things live

Paths and the job of each. Who owns the public API, and what callers must not import.

### Gotchas

Traps that are real in this code: ordering, a caller that defeats a rule, a name that lies. If there are none, say there are none.

## Anti-patterns

- Annotated source in place of the model
- A second build loop
- Inventing a layer the code does not have
- Launching explorers for a one-file path
- Writing a ticket or editing code
