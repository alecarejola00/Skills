---
name: voucher-system
description: "Create Journal, Payment, and Check voucher packages from source documents using the user's voucher workbook and COC, with payment-method confirmation and optional authorized email lookup."
---

# Voucher System

Use this skill when the user wants to turn purchase orders, invoices, quotes, images, spreadsheets, or Google Drive-hosted files into voucher outputs based on a user-supplied voucher workbook template.

## Scope

- Create one voucher package per source input.
- Always ask for both the input source file and the output template file.
- Support local files and exact user-supplied cloud links such as Google Drive, Google Docs, and Google Sheets.
- Recommend `.xlsx` by default when missing fields still need manual completion.
- Export `.pdf` only after the required fields are complete or the user explicitly wants a fixed output. A PDF package is one page per generated voucher form.

## First step

Always identify the source before doing extraction:

- Ask the user for the input file and the output template file first.
- Ask whether the source is a local file, Google Drive link, Google Doc/Sheet link, or a mixed batch.
- For cloud sources, ask the user for the exact link instead of searching or guessing.
- If access to the linked source is unavailable, stop and ask for an export or uploaded file.

## Payment-method decision gate

The source document may not state how payment will be made. Do not infer the method from a purchase order, supplier, amount, or wording.

Ask the user to choose or confirm one of:

- `Bank transfer`: generate Journal Voucher and Payment Voucher.
- `PDC/check preparation`: generate Journal Voucher and Check Voucher.

If the user explicitly authorizes email access and an email connector or signed-in mail source is available, search for the exact source identifier (for example, `PO-021517`) and inspect only relevant messages for payment terms or method. Report the message/date used and ask the user to confirm the result before generating. If email access is unavailable, ask the user for the payment method or an exported email; never guess and never claim email evidence that was not accessed.

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
- payment method when it is not explicit in the source or confirmed by authorized email lookup
- account-title overrides when the accounting treatment is uncertain
- missing particulars wording when the source is insufficient
- confirmation when the template layout and the requested output behavior conflict
- output format when the task is ready to generate

If payee, totals, tax split, or account mapping is uncertain, ask instead of inferring.

## Template and accounting behavior

- Keep the workbook layout separate from the accounting rules.
- Treat the user-chosen output template file as the main working workbook for the run.
- Reuse the chosen voucher workbook and its lookup sheets rather than rebuilding the layout each time.
- Treat `GENERAL VOUCHER.xlsx` as the user's master template when supplied. Preserve its labels, formulas, formatting, and side-by-side layout; do not rename a form because its neighboring form has a different business role.
- Final workbook packages contain only the voucher sheets required by the confirmed payment method. Exclude `Suppliers List` and `COC` from delivered outputs.
- Bank transfer package: output `Journal Voucher` and `Payment Voucher` sheets.
- PDC/check package: output `Journal Voucher` and `Check Voucher` sheets. The current Check Voucher sheet intentionally contains `CHECK VOUCHER` on the left and `JOURNAL VOUCHER` on the right; preserve those workbook labels.
- Populate both side-by-side copies on every included sheet with the same source company/payee unless the user requests another arrangement.
- For PDF, render the included sheets in package order as one PDF, one page per voucher sheet.
- Follow the exact cell and range map in [references/template-map.md](references/template-map.md) when populating the workbook.
- Follow the intake and routing rules in [references/source-intake-and-workflow.md](references/source-intake-and-workflow.md).
- Follow the output naming rules in [references/output-naming.md](references/output-naming.md).
- Follow the process-memory and continuous-improvement rules in [references/process-memory.md](references/process-memory.md).
- Follow the accounting and COC rules in [references/accounting-and-coc.md](references/accounting-and-coc.md).

## Batch behavior

- Accept multiple inputs in one run.
- Process each source independently.
- Create one output workbook per input source unless the user explicitly asks to combine them.
- Do not let one failed or ambiguous source block the entire batch unless the user asks for all-or-nothing behavior.

## Decision boundary

- Use this skill for voucher-generation workflow, field mapping, source extraction, naming, and process capture.
- Do not use this skill for unrelated bookkeeping, tax advice, or broad finance policy questions that are outside the voucher workflow.
