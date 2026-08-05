# Confidence Rules

Judge confidence before presenting conclusions.

## High confidence

Use when:

- timestamps look fresh
- summary and supporting endpoints are directionally consistent
- records are not dominated by null values
- duplicates are minimal or explainable

Language pattern:

- "The MCP shows..."
- "This week's summary indicates..."

## Mixed confidence

Use when:

- one endpoint looks fresh but another disagrees
- the counts reconcile only partially
- there are some null-heavy or duplicate-like rows

Language pattern:

- "The best available MCP summary shows..."
- "Supporting endpoints are inconsistent, so treat this as the strongest available view rather than a fully reconciled total."

## Low confidence

Use when:

- timestamps look stale
- endpoints materially conflict
- records are dominated by null or suspicious values
- the user asked for precision the MCP cannot currently support

Language pattern:

- "The MCP data is not consistent enough to support a precise conclusion."
- "Here is a provisional summary based on the least noisy source."

## What to do when confidence drops

- say which source you trusted most
- explain why
- avoid exact claims if unsupported
- keep insights conservative
