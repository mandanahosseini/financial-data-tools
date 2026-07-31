from financial_tools.invoice.text_processing import (
    clean_invoice_text
)


def test_clean_text():

    text = "Invoice #123 !!!"

    result = clean_invoice_text(text)

    assert "invoice" in result
    assert "#" not in result