---
name: voucher-system
description: "Create or update payment/general voucher outputs from local files or exact cloud-source links, using the user's voucher workbook template and asking only for missing accounting or payment fields."
---

# Voucher System

Use this skill when the user wants to turn purchase orders, invoices, quotes, images, spreadsheets, or Google Drive-hosted files into voucher outputs based on a user-supplied voucher workbook template.

## Scope

- Create one voucher output per source input.
- Always ask for both the input source file and the output template file.
- Support local files and exact user-supplied cloud links such as Google Drive, Google Docs, and Google Sheets.
- Recommend `.xlsx` by default when missing fields still need manual completion.
- Export `.pdf` only after the required fields are complete or the user explicitly wants a fixed output.

## First step

Always identify the source before doing extraction:

- Ask the user for the input file and the output template file first.
- Ask whether the source is a local file, Google Drive link, Google Doc/Sheet link, or a mixed batch.
- For cloud sources, ask the user for the exact link instead of searching or guessing.
- If access to the linked source is unavailable, stop and ask for an export or uploaded file.

## What to extract vs. what to ask

Extract whatever is explicit in the source, such as:

- supplier or registered company name
- document identifier such as PO number or invoice number
- document date
- line item descriptions
- subtotal, VAT, and total
- quote or reference identifiers shown in the source

Ask the user for fields that are missing, ambiguous, or process-specific, such as:

- voucher date
- payment reference type and value such as `BN No.`, `PN No.`, `Check No.`, or `Reference`
- account-title overrides when the accounting treatment is uncertain
- missing particulars wording when the source is insufficient
- confirmation when the template layout and the requested output behavior conflict
- output format when the task is ready to generate

If payee, totals, tax split, or account mapping is uncertain, ask instead of inferring.

## Template and accounting behavior

- Keep the workbook layout separate from the accounting rules.
- Treat the user-chosen output template file as the main working workbook for the run.
- Reuse the chosen voucher workbook and its lookup sheets rather than rebuilding the layout each time.
- Final workbook outputs should contain only one sheet tab unless the user explicitly asks for more.
- If the chosen template uses two voucher copies side by side on one sheet, preserve that single-sheet visual layout in the output.
- For a single input source, keep both side-by-side voucher copies tied to the same company or payee unless the user explicitly requests a different pairing.
- Follow the exact cell and range map in [references/template-map.md](references/template-map.md) when populating the workbook.
- Follow the intake and routing rules in [references/source-intake-and-workflow.md](references/source-intake-and-workflow.md).
- Follow the output naming rules in [references/output-naming.md](references/output-naming.md).
- Follow the process-memory and continuous-improvement rules in [references/process-memory.md](references/process-memory.md).

## Batch behavior

- Accept multiple inputs in one run.
- Process each source independently.
- Create one output workbook per input source unless the user explicitly asks to combine them.
- Do not let one failed or ambiguous source block the entire batch unless the user asks for all-or-nothing behavior.

## Decision boundary

- Use this skill for voucher-generation workflow, field mapping, source extraction, naming, and process capture.
- Do not use this skill for unrelated bookkeeping, tax advice, or broad finance policy questions that are outside the voucher workflow.
