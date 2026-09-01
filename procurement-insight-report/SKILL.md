---
name: procurement-insight-report
description: Turn Procurement MCP quote and assignee data into factual answers, decision-oriented insights, and visual reports. Use when Codex needs to answer procurement questions, analyze quote activity, summarize weekly quote performance, explain pending or on-going quote status, create chart-based HTML reports, export publishable procurement reports such as DOCX on request, or identify repeat procurement workflows that should become Skill improvements.
---

# Procurement Insight Report

Interpret the user's request first. Decide whether the task is primarily an answer, an analysis, a report, or an improvement opportunity. Combine modes when needed.

## Use this workflow

1. Identify the reporting question, audience, and time window.
2. Pull Procurement MCP data using the best endpoint for that task.
3. Reconcile timestamp freshness, endpoint disagreements, and obvious anomalies before drawing conclusions.
4. Present findings as facts first, then insights, then recommended actions.
5. Use visuals when they improve comprehension. Prefer HTML for visual reports.
6. Create `.docx` only when the user asks for a publishable artifact or specifies that format.
7. If you notice a repeated procurement workflow, ask whether it should be added to or formalized in the Skill.

## Choose the mode

Use `Answer` for short factual replies.

Use `Analyze` when the user wants patterns, interpretation, operational bottlenecks, or recommendations.

Use `Report` when the user wants a formal summary, charts, dashboard-style output, HTML, or a publishable artifact.

Use `Improve` when you see a repeatable procurement workflow that should become part of the Skill.

Use `Quote Performance` when the user asks for quote SLA performance, on-time quote fulfillment, quote performance scoring, or the Quote Performance KPI.

### Quote Performance

This mode measures the SLA criterion: `eligible quotes sent within the applicable SLA / eligible quote requests`, weighted at 20%.

1. If the user does not provide a reporting date, month, or range, ask for it before retrieving data. For a monthly request, obtain both the year and month; do not assume the current month.
2. Prefer `procurement_mcp.quote_performance` (exposed as `mcp__procurement_mcp__quote_performance`) for the exact requested month or range. Use its native eligibility set, SLA buckets, on-time counts, and exclusions as the source of truth.
3. For a monthly call, pass the requested `year` and numeric `month` (1–12). Do not substitute generic summary endpoints when the dedicated endpoint is available.
4. Treat the endpoint's measurement convention as authoritative. If it reports tracker `DAYS QUOTED` in calendar days, do not recalculate using business days or replace its values with date arithmetic.
5. Report, at minimum: on-time percentage, on-time count / eligible count, KPI points out of 20, total deduplicated quotes, status breakdown, excluded quote count and reason categories, SLA-bucket breakdown, measurement convention, data freshness, and confidence.
6. Calculate weighted KPI points as `on_time_rate * 20`, rounded for presentation only. Keep the underlying numerator and denominator visible so the score is auditable.
7. Separate facts from insights. Insights may identify the largest SLA bucket, quantify its contribution to the result, and flag excluded or late-volume concentration, but must not infer causes unless the source provides evidence.
8. If the dedicated endpoint is unavailable, say so explicitly and label any fallback reconstruction as provisional. A fallback must not be presented as the native Quote Performance KPI.

The standard concise output is:

```plaintext
Quote Performance — [period]
On-time fulfillment: [percent]% ([on-time] / [eligible])
KPI score: [points] / 20
Total deduplicated quotes: [count]
Status mix: [breakdown]
SLA buckets: [bucket breakdown]
Excluded from KPI: [count] ([reasons])
Convention: [calendar/business days and source field]
Insights: [largest driver and key exception]
Confidence / caveats: [freshness, coverage, limitations]
```

## Use source hierarchy

Use this initial endpoint preference unless the task clearly requires otherwise:

1. `quote_performance` for the dedicated Quote Performance KPI and SLA scoring
2. `weekly_quote_report` for weekly summary counts and headline metrics
3. `quote_details` for quote-level drill-down
4. `search_quotes` for scoped search and supporting retrieval
5. `pending_quotes` for backlog and operational context
6. `search_procurement` for assignee lookup

Read [references/source-hierarchy.md](references/source-hierarchy.md) when choosing between endpoints or when endpoint results disagree.

## Reconcile before concluding

Before giving conclusions, check for:

- `generated_at` freshness
- duplicate-like rows
- null-heavy records
- conflicting counts
- status fields that do not align with status categories

Assign a confidence level internally and communicate it when useful:

- `high`: fresh and consistent
- `mixed`: useful but conflicted or partially noisy
- `low`: materially inconsistent or stale

Read [references/confidence-rules.md](references/confidence-rules.md) when the data quality looks questionable.

If confidence is `mixed` or `low`, do not overstate precision.

## Separate facts from insight

Always separate:

- `Facts`
- `Insights`
- `Recommended Actions`
- `Confidence / Caveats`

Facts must stay anchored to MCP output.
Insights may interpret bottlenecks, workload patterns, cancellation themes, and turnaround implications, but must not invent unsupported causes.

Read [references/insight-patterns.md](references/insight-patterns.md) when the user asks for decisions, trends, root themes, or what the data implies operationally.

## Prefer visual reports

When creating a report, prefer HTML first and include only charts supported by the data:

- status breakdown
- quote volume trend
- assignee activity or workload
- cancellation reason breakdown
- aging buckets for pending or on-going work

Use [assets/report-template.html](assets/report-template.html) as the layout starting point.
Use `scripts/render_report_html.py` to turn a normalized report JSON payload into a shareable HTML report.
Use `scripts/export_report_docx.py` to turn the same normalized report JSON payload into a publishable DOCX when the user requests that format.
Read [references/report-data-schema.md](references/report-data-schema.md) before preparing the payload for either script.

Default report order:

1. reporting window
2. executive summary
3. KPI summary
4. charts
5. findings
6. insights
7. recommended actions
8. confidence notes

Read [references/report-patterns.md](references/report-patterns.md) when choosing structure, chart types, or audience tone.

## Handle audience

If the user does not specify an audience, default to an executive-plus-operations style:

- concise summary first
- actions and operational implications included

If the audience is executive, compress detail and emphasize KPIs and decisions.
If the audience is analyst, include more methodology and caveats.

## Improve the workflow

When the same procurement pattern repeats, ask:

"This looks like a repeatable procurement workflow. Do you want me to add it to the Procurement Skill?"

Examples:

- repeated weekly report layout
- repeated endpoint-reconciliation logic
- repeated assignee scorecard requests
- repeated export formatting or publishing flow

Read [references/improvement-loop.md](references/improvement-loop.md) when deciding whether a repeated process should become a Skill update.

## Guardrails

Do not:

- present interpretation as if it were raw fact
- hide endpoint conflicts
- invent precise totals when MCP sources disagree
- default to plain text when visuals would materially improve clarity

If the data is too inconsistent for a trustworthy conclusion, say so clearly and provide the best provisional summary available.
