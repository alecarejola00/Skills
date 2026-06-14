---
name: quotable-knowledge
description: Use when user mentions Quotable, Quotable Knowledge, or BRD. Combine BRD evidence, codebase reality, and explicit dev request; warn and reconfirm on material conflicts.
---

# Quotable Knowledge

Use this skill ONLY when the task is about Quotable and BRD-informed implementation or validation.

## Trigger conditions

Activate when user input includes any of:

- `Quotable`
- `Quotable Knowledge`
- `BRD`

## Decision model

Use this precedence when deciding how to execute:

1. Explicit dev/user task request (execution intent)
2. Verified codebase/runtime reality (technical constraints)
3. BRD evidence (guidance and business context)

BRD is important guidance, but not absolute truth.

## Operating mode

1. Ground work in both BRD evidence and codebase facts.
2. Keep implementation tightly scoped to the requested dev task.
3. Warn and reconfirm before proceeding on material conflicts.

## Required workflow

### Phase 1: Capture task intent and scope

- Extract the explicit dev/user objective and requested boundaries first.
- Identify expected outputs and success criteria from the request.
- If scope is unclear, ask exactly one targeted question.

### Phase 2: Evidence retrieval (BRD + codebase)

- Prefer calling MCP BRD validation tool early (`brd_validate_context`) with:
  - `retrieval_mode="hybrid"`
  - `include_trace=true`
- In parallel, verify codebase reality (existing modules, data model, interfaces, constraints).
- Extract and compare:
  - in-scope requirements and constraints
  - dependencies and integration impacts
  - current implementation boundaries
  - potential scope/version conflicts

If evidence is insufficient, ask one targeted clarification question before coding.

### Phase 3: Conflict detection and reconfirmation

Detect and classify conflicts:

- dev request vs BRD evidence
- dev request vs codebase reality
- BRD evidence vs codebase reality

If conflict is material, do all of the following before implementation:

- state what conflicts
- state risk/impact of proceeding
- provide a recommended default path
- ask one targeted reconfirmation question

Proceed after reconfirmation.

### Phase 4: Architecture draft/check and implementation plan

- If user has no design, generate a preliminary architecture:
  - components
  - data flow
  - affected boundaries
  - dependency and risk notes
- If user has a design, run gap analysis:
  - BRD-supported parts
  - codebase-aligned parts
  - missing constraints
  - conflict points
  - concrete revisions
- Produce short, ordered implementation plan.
- Map each step to BRD evidence and codebase reality.
- Implement only after scope is confirmed.

## Response format preference

When producing analysis, include:

- Task intent (what user explicitly asked)
- BRD-supported decisions
- Codebase-supported decisions
- Architecture summary
- Gaps/conflicts
- Scoped file/directory plan
- Next coding steps

## Guardrails

- Do not invent BRD requirements or codebase facts.
- Do not treat BRD as a hard gate when codebase/user intent differs.
- Do not expand edits outside agreed task scope.
- When scope conflict is material, warn and reconfirm before proceeding.
