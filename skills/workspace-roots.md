# Workspace roots

Goal and analysis paths are runtime context, not a function of an id alone. A parent wave may place them under its own workspace. Every flow must resolve and preserve this context instead of reconstructing pack-global paths.

## Fields

Persist these on an active goal's `STATUS.md`:

```markdown
**goals_container:** .agents/temp/goals
**goal_root:** .agents/temp/goals/<goal-id>
**parent_wave:** none
```

When a parent owns the goal, its values replace the defaults:

```markdown
**goals_container:** .agents/temp/just-do-it/<jdi-id>/goals
**goal_root:** .agents/temp/just-do-it/<jdi-id>/goals/<goal-id>
**parent_wave:** just-do-it:<jdi-id>
```

An analysis may also receive:

```markdown
**analyses_container:** .agents/temp/analyses
**analysis_root:** .agents/temp/analyses/<analysis-id>
```

`/just-do-it` changes both containers. Shared grill themes remain under `.agents/temp/grills/`.

## Resolve once

1. Use `goal_root`, `goals_container`, `analysis_root`, or `analyses_container` supplied by the caller.
2. Otherwise read the target workspace `STATUS.md` when it already exists.
3. Only then use the standalone defaults above.
4. Persist resolved values before invoking a child flow or Task worker.

Never infer a path from `goal-id` or `analysis-id` alone when a caller supplied root context.

## Propagate

- `/goal` creates and records the default root unless its caller supplies one.
- Parent waves create their own container registries and pass the resolved roots to `/analyze`, `/goal`, and every child flow.
- `/orchestrate` includes the resolved roots and exact artifact paths in every Task prompt.
- Goal archives stay inside `goals_container`: `<goals_container>/achieved/<goal-id>/`.
- Analysis promotion creates its goal under the supplied `goals_container` and writes the goal root fields before handing off.

## Anti-patterns

- Writing nested work to `.agents/temp/goals/` or `.agents/temp/analyses/`.
- Updating the wrong `REGISTRY.md`.
- Sending a Task only `goal-id` while omitting its resolved paths.
- Moving an achieved nested goal outside its parent wave.
