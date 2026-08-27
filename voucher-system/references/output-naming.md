# Output Naming

Every generated output filename must match the source data as closely as possible, especially the source document identifier and the registered company or payee.

## Primary naming rule

When both are available, name the output:

`<primary-document-id> - <registered-company>.<ext>`

Examples:

- `PO-000123 - Example Supplier Inc.xlsx`
- `PO-000123 - Example Supplier Inc.pdf`

## Fallbacks

Use this order when one part is missing:

1. `<primary-document-id> - <registered-company>.<ext>`
2. `<registered-company> - voucher.<ext>`
3. `<input-filename-base> - voucher.<ext>`

## What counts as primary document ID

Prefer, in order:

1. PO number
2. invoice number
3. quote number when no stronger document number exists
4. another user-confirmed business identifier

## Company name selection

Prefer, in order:

1. the registered company or supplier name shown in the source
2. the payee selected by the user
3. a user-confirmed fallback label

## Preservation rule

If the input file already follows a strong business naming pattern such as:

`PO-000123 - Example Supplier Inc.pdf`

preserve that pattern in the output and change only the extension unless the user requests a different standard.

## Sanitization rule

Before saving:

- remove filesystem-invalid characters
- normalize repeated spaces
- keep periods that belong to company names when allowed by the filesystem
- avoid adding duplicate suffixes such as `- voucher - voucher`

## Batch rule

For multiple inputs:

- generate one filename per source
- ensure uniqueness
- when two outputs would collide, append a short deterministic suffix such as `- 2`
