import re


def extract_invoice_entities(text):

    entities = {}

    invoice_number = re.search(
        r"invoice\s*#?\s*(\d+)",
        text,
        re.IGNORECASE
    )

    if invoice_number:
        entities["invoice_id"] = (
            invoice_number.group(1)
        )

    amount = re.search(
        r"amount\s*[:]\s*(\d+)",
        text,
        re.IGNORECASE
    )

    if amount:
        entities["amount"] = float(
            amount.group(1)
        )

    return entities