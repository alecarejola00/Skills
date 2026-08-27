# Template Map

This map is based on the user's current voucher workbook review.

## Canonical workbook notes

- `GENERAL VOUCHER.xlsx` is the master template when supplied by the user.
- Voucher sheets are `Journal Voucher Template`, `Payment Voucher Template`, and `Check Voucher Template`.
- Each voucher sheet has two copies side by side: left block `A:K`, right block `M:W`.
- The Check Voucher sheet currently labels the left block `CHECK VOUCHER` and the right block `JOURNAL VOUCHER`. This is intentional for the PDC/check package and must not be renamed by the Skill.

## Supporting lookup sheets

- `Suppliers List`: payee dropdown source
- `COC`: chart of accounts and account-title dropdown source

## Canonical target blocks

For all three voucher sheets, the common header fields are:

Header and identity fields:

- left payee/bill-to: `C6:G6` (write to the merged anchor `C6`)
- right payee/bill-to: `O6:S6` (write to `O6`)
- left date: `J6:K6` (write to `J6`)
- right date: `V6:W6` (write to `V6`)
- left reference value: `J5:K5` (write to `J5`)
- right reference value: `V5:W5` (write to `V5`)

Accounting area:

- left account-title rows: `C10:G14`
- left debit rows: `I10:I14`
- left credit rows: `K10:K14`
- right account-title rows: `O10:S14`
- right debit rows: `U10:U14`
- right credit rows: `W10:W14`
- totals: use the existing formula cells on each sheet; never replace them with hardcoded totals

Particulars and signatures:

- Journal explanation: left `A19:K21`, right `M19:W21`
- Payment particulars: left `A18:K21`, right `M18:W21`
- Check particulars: left `A17:K21`, right `M17:W21`
- prepared-by and fixed signatory areas remain in the template's existing rows

## Final output workbook rule

- Bank transfer: copy the Journal and Payment template sheets into an output workbook, rename them `Journal Voucher` and `Payment Voucher`, and remove lookup sheets.
- PDC/check: copy the Journal and Check template sheets, rename them `Journal Voucher` and `Check Voucher`, and remove lookup sheets.
- Populate both copies on every included sheet with the same source company/payee.

## Current dropdown behavior

On the voucher template sheets, the workbook may include:

- payee list validation from `Suppliers List`
- payment-reference type validation with `BN No.`, `PN No.`, `Check No.`, and `Reference`
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
