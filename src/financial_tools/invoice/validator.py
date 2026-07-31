def validate_invoice(invoice):

    errors = []

    if not invoice.invoice_id:
        errors.append("Invoice ID is required")

    if invoice.amount <= 0:
        errors.append("Amount must be positive")

    if not invoice.customer:
        errors.append("Customer is required")

    return errors