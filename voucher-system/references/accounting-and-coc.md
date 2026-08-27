# Accounting And COC Rules

This reference supports voucher preparation; it does not replace the user's accountant, tax adviser, company policy, or the COC in the supplied workbook.

## Voucher roles

- Journal Voucher records the accounting entry for the underlying transaction, such as recognizing inventory and input tax against Accounts Payable.
- Payment Voucher documents settlement by bank transfer or another non-check payment method.
- Check Voucher documents settlement through a check or PDC. The current master workbook's Check Voucher sheet has a Check Voucher form on the left and a Journal Voucher form on the right; preserve that layout and label.

## Current company rule

For a purchase supported by the sample PO pattern:

- Journal Voucher: debit the appropriate purchase, inventory, or expense account; debit `Input Tax` when supported by the source and applicable tax documentation; credit `600 Accounts Payable`.
- Bank transfer: Payment Voucher debits `600 Accounts Payable` and credits the confirmed bank/cash account.
- PDC/check: Check Voucher debits `600 Accounts Payable` and credits the confirmed bank/cash account, subject to the user's posting policy for issued checks.

Do not copy the Journal Voucher's inventory/input-tax debits into Payment or Check Vouchers. Those settlement vouchers use the Accounts Payable debit rule supplied by Accounting.

## COC control

Use the `COC` sheet in the supplied template as the authoritative code/name pair. Match by exact code/name where possible and use fuzzy matching only to propose a candidate. Confirm ambiguous candidates with the user. Do not invent codes from internet research.

Relevant entries observed in the current master workbook include:

- `140 Inventory Control` — Current Asset
- `Input Tax` — listed in the COC
- `600 Accounts Payable` — Accounts Payable; outstanding supplier invoices not yet paid at balance date
- `100 Security Bank - PHP` — Bank

## External reference boundaries

These sources support general principles, not the company's specific COC or payment policy:

- IFRS IAS 2 Inventories: https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/
- IFRS Conceptual Framework: https://www.ifrs.org/issued-standards/list-of-standards/conceptual-framework/
- Philippine BIR RMO 23-2023 Annex F, input-tax verification: https://bir-cdn.bir.gov.ph/BIR/pdf/RMO%2023-2023%20Annex%20F.pdf
- Utah Division of Finance journal-voucher policy: https://finance.utah.gov/state-agency-resources/policy/02-05_00/

Internet research must not override the user's COC, Accounting-approved account mappings, source evidence, or explicit payment-method confirmation.
