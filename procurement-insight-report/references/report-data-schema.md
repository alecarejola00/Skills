# Report Data Schema

Use a normalized JSON payload before rendering HTML or DOCX.

## Top-level shape

```json
{
  "title": "Weekly Quote Report",
  "subtitle": "Procurement MCP summary",
  "reporting_window": "July 30, 2026 to August 5, 2026",
  "confidence": "mixed",
  "summary": [
    "214 quotes were recorded in the last 7 days.",
    "Quoted volume remains strong, but a large share is still on going."
  ],
  "kpis": [
    {"label": "Total Quotes", "value": "214"},
    {"label": "Quoted", "value": "104"},
    {"label": "Won", "value": "10"},
    {"label": "On Going / Unknown", "value": "95"}
  ],
  "charts": [
    {
      "title": "Status Breakdown",
      "type": "bar",
      "series": [
        {"label": "Quoted", "value": 104},
        {"label": "Won", "value": 10},
        {"label": "Cancelled", "value": 5},
        {"label": "Unknown", "value": 95}
      ]
    }
  ],
  "facts": [
    "The weekly summary endpoint returned fresh data timestamped 2026-08-05.",
    "Lower-level search filters were inconsistent with the weekly rollup."
  ],
  "insights": [
    "A large unknown/on-going share suggests active pipeline load and possible follow-up risk."
  ],
  "recommended_actions": [
    "Review aging on unknown/on-going items by assignee.",
    "Use the weekly summary endpoint as the primary weekly source until search filters are rebuilt."
  ],
  "caveats": [
    "Search endpoints returned 0 results for the same date window.",
    "Confidence is mixed because endpoint reconciliation is incomplete."
  ],
  "sources": [
    "Procurement MCP weekly_quote_report",
    "Procurement MCP search_quotes",
    "Procurement MCP pending_quotes"
  ]
}
```

## Required fields

- `title`
- `reporting_window`
- `confidence`

## Recommended fields

- `summary`
- `kpis`
- `charts`
- `facts`
- `insights`
- `recommended_actions`
- `caveats`

## Confidence values

Use one of:

- `high`
- `mixed`
- `low`

## Chart types

Current renderer support:

- `bar`
- `line`

If the data does not fit those forms cleanly, omit the chart rather than forcing it.
