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
7. Confirm the desired output format.
8. Generate one `.xlsx` or `.pdf` per source.
9. Present a short audit summary of:
   - source file or link
   - output template file used
   - extracted fields
   - user-supplied fields
   - accounting rules used

## Confidence gate

Do not silently infer:

- the payment date
- the payment reference number
- the payment reference type
- the correct debit or credit accounts when more than one treatment is plausible
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

- The output workbook should normally contain only one sheet tab.
- Preserve the template's layout inside that one sheet when possible.
- If the template shows two voucher copies side by side on one sheet, keep that layout in the final output.
- For a single-source run, both side-by-side copies should correspond to the same source company or payee unless the user says otherwise.
- If the chosen template requires multiple sheets for a legitimate process reason, ask before keeping them.

## Batch rule

For multiple inputs:

- keep one extraction record per source
- keep one output workbook per source
- preserve the input-to-output pairing
- report failures separately so successful outputs can still be delivered
