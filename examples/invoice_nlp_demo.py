from financial_tools.invoice.text_processing import (
    clean_invoice_text
)

from financial_tools.invoice.entity_extraction import (
    extract_invoice_entities
)


text = """
Invoice #2025

Customer: ABC Company

Amount: 450000
"""


clean_text = clean_invoice_text(text)

print(clean_text)


entities = extract_invoice_entities(
    text
)

print(entities)