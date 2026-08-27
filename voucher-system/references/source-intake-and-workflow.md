# Source Intake And Workflow

## Intake order

Start every run by confirming the source type:

1. Local file
2. Google Drive link
3. Google Docs or Google Sheets link
4. Mixed batch

For cloud sources, require the exact link from the user. Do not browse folders or guess which file the user means.

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
2. Read the source and extract structured fields.
3. Compare the extracted fields with the voucher template requirements.
4. Fill whatever is confidently supported by the source.
5. Ask for missing or ambiguous values.
6. Confirm the desired output format.
7. Generate one `.xlsx` or `.pdf` per source.
8. Present a short audit summary of:
   - source file or link
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

## Batch rule

For multiple inputs:

- keep one extraction record per source
- keep one output per source
- preserve the input-to-output pairing
- report failures separately so successful outputs can still be delivered
