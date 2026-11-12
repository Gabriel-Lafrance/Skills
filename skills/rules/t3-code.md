# T3 Code

T3's installed instructions govern discovery refresh and route restrictions.

## Browser and preview

When the user asks to open, view, click through, record or screenshot a page, use T3's `preview_*` tools (load them first if deferred), not Playwright, the system browser or a screenshot script. Where T3's instructions forbid preview unasked, for example to check your own edit, that limit stands.

## Delegation

- When advertised, `orchestrator_capabilities` supplies models, option descriptors, and inherited settings.
- Prefer a native same-provider child for synchronous same-turn work when it supports the selected model and settings. Use `delegate_task` for cross-provider work, settings native tools cannot express, background work, or isolated worktrees.
- Use only advertised target fields and option IDs/values, with explicit selections where supported. Inspect inherited values; clearing options selects defaults, not necessarily low effort.
- Use the durable `taskId`, not the storage `childThreadId`, for status, wait and cancellation.
- When supported, a new review round or recheck uses a new `delegate_task` and fresh `clientRequestId`; a retry of the same uncertain request keeps that request identity and reconciles the original outcome first. A thread continuation does not reopen the original published review result.
- Before replacing a running reviewer, use `task_cancel` when exposed and verify its state. Do not interrupt a storage thread as a substitute.

## PR watch

Use T3's native PR watch when available and permitted, under [watch lifecycle](pr-lifecycle.md#watch-lifecycle).
