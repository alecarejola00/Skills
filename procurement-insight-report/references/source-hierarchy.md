# Source Hierarchy

Use the Procurement MCP endpoint that best matches the user's requested level of summary.

## Preferred order

1. `weekly_quote_report`
Use for weekly counts, status mix, and top-level weekly procurement summaries.

2. `quote_details`
Use for a single quote deep dive or for validating a specific quote mentioned by the user.

3. `search_quotes`
Use for filtering, searching, exploring subsets, and supporting evidence around a weekly or operational summary.

4. `pending_quotes`
Use for backlog context, operational follow-up, aging review, and unresolved work. Do not assume it is the source of truth for all totals.

5. `search_procurement`
Use for assignee lookup and person matching.

## Conflict rule

If endpoints disagree:

- prefer the endpoint that most directly answers the user's requested task
- state the disagreement clearly
- reduce confidence
- avoid claiming precision that the MCP does not support

## Typical examples

- Weekly report request: prefer `weekly_quote_report`
- "What happened to quote X?": prefer `quote_details`
- "Show all July quotes for customer Y": prefer `search_quotes`
- "Who has the oldest open items?": prefer `pending_quotes`
