from datetime import date

from financial_tools.invoice.models import Invoice
from financial_tools.invoice.validator import validate_invoice

invoice = Invoice(
    invoice_id="INV-1001",
    customer="Demo Corporation",
    invoice_date=date.today(),
    amount=500000
)


print("Total:", invoice.total_amount)


errors = validate_invoice(invoice)

if errors:
    print(errors)
else:
    print("Invoice is valid")