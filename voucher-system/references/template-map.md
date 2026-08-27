# Template Map

This map is based on the user's current voucher workbook review.

## Canonical workbook notes

- The workbook contains historical filled examples plus lookup sheets.
- The cleanest reusable block today is on sheet `FIXED VOUCHERS`.
- The bottom voucher block is the best current candidate for automation because its editable cells are largely blank while the formulas and labels remain in place.
- The historical template pattern also uses two voucher copies side by side on a single sheet. Preserve that side-by-side layout when generating the final output workbook, while still reducing the final workbook to one sheet tab unless the user asks otherwise.

## Supporting lookup sheets

- `Suppliers List`: payee dropdown source
- `COC`: chart of accounts and account-title dropdown source

## Canonical blank target block

Sheet: `FIXED VOUCHERS`

Header and identity fields:

- voucher type: `A116:K116` and `M116:W116`
- company/TIN/address header: rows `117:118`
- payment-reference label/value area: `I119:K119` and `U119:W119`
- payee: `C120:G120` and `O120:S120`
- date: `J120:K120` and `V120:W120`

Accounting area:

- account-title rows, left voucher: `C123:E128`
- debit rows, left voucher: `I123:I128`
- credit rows, left voucher: `K123:K128`
- account-title rows, right voucher: `O123:Q128`
- debit rows, right voucher: `U123:U128`
- credit rows, right voucher: `W123:W128`
- totals: row `129`

Particulars and signatures:

- particulars label: `A130` and `M130`
- particulars content: `A131:K134` and `M131:W134`
- signature section starts at row `138`

## Final output workbook rule

- Keep the voucher content on a single output sheet tab by default.
- If the template contains two side-by-side voucher copies on that sheet, populate both copies.
- For one input source, both copies should represent the same supplier or company unless the user explicitly requests a different arrangement.

## Current dropdown behavior

On `FIXED VOUCHERS`, the workbook already includes:

- payee list validation from `Suppliers List`
- payment-reference type validation with `BN No.`, `PN No.`, `Check No.`, and `Reference`
- voucher type validation with `PAYMENT VOUCHER` and `CHECK VOUCHER`
- account-title validation from `COC`

## Known sample mapping from the reviewed PO

For a typical PO-to-voucher case, the sample voucher logic may be:

- payee: supplier or registered company from the source
- source date from PO: the PO or invoice date shown in the source
- voucher date: the final payment or voucher date, usually user-supplied when absent from the source
- debit `Inventory Control`: source subtotal when inventory purchases apply
- debit `Input Tax`: source VAT amount when applicable
- credit bank or liability account: full source total
- particulars pattern: payment text referencing the internal PO number, the source PO number, and quote reference

## Important open rule

The sample particulars include an additional internal PO identifier that does not appear directly in the reviewed source PO. Treat that field as user-supplied or process-derived until a reliable rule is defined.
