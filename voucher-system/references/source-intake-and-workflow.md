# Source Intake And Workflow

## Intake order

Start every run by confirming the source type:

1. Local file
2. Google Drive link
3. Google Docs or Google Sheets link
4. Mixed batch

For cloud sources, require the exact link from the user. Do not browse folders or guess which file the user means.

Also require the output template file for the run. Treat that template as the main working workbook.

## Supported source types

- purchase order PDFs
- invoice PDFs
- quote PDFs
- scans or screenshots
- spreadsheets
- Google Drive-hosted exports
- Google Sheets or Google Docs links when the user explicitly provides them

## Standard run flow

1. Identify the source location and document type.
2. Confirm the output template file that should receive the voucher data.
3. Read the source and extract structured fields.
4. Compare the extracted fields with the voucher template requirements.
5. Fill whatever is confidently supported by the source.
6. Ask for missing or ambiguous values.
7. Confirm the payment method. If not stated, ask the user; offer authorized email lookup by exact source identifier as an optional path.
8. Select the voucher package:
   - bank transfer: Journal Voucher + Payment Voucher
   - PDC/check preparation: Journal Voucher + Check Voucher
9. Confirm the desired output format.
10. Generate one `.xlsx` or `.pdf` package per source.
11. Present a short audit summary of:
   - source file or link
   - output template file used
   - extracted fields
   - user-supplied fields
   - accounting rules used
   - payment-method evidence and confirmation status

## Confidence gate

Do not silently infer:

- the payment date
- the payment reference number
- the payment reference type
- the correct debit or credit accounts when more than one treatment is plausible
- the payment method when it is not in the source and email access was not explicitly authorized
- whether the voucher should be labeled payment voucher vs. general voucher if the process rule is unclear

Ask the user instead.

## Output format rule

Recommend `.xlsx` when:

- any required field is still missing
- the user may need to adjust account mapping
- the particulars text still needs review

Allow `.pdf` when:

- the source is complete
- the user has supplied all missing fields
- the user wants a fixed, shareable copy

## Workbook structure rule

- Include only the sheets required by the confirmed package; exclude `Suppliers List` and `COC`.
- Bank transfer output: Journal Voucher and Payment Voucher sheets.
- PDC/check output: Journal Voucher and Check Voucher sheets.
- Preserve each included sheet's side-by-side two-copy layout. For one source, both copies represent the same company/payee.
- Keep the Check Voucher sheet's current workbook labels unchanged, including its right-side `JOURNAL VOUCHER` label.
- A PDF package is one PDF with one page per included voucher sheet.

## Batch rule

For multiple inputs:

- keep one extraction record per source
- keep one output workbook per source
- preserve the input-to-output pairing
- report failures separately so successful outputs can still be delivered
