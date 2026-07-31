from datetime import date

from financial_tools.invoice.models import Invoice


def test_invoice_tax():

    invoice = Invoice(
        invoice_id="1",
        customer="Test",
        invoice_date=date.today(),
        amount=1000
    )

    assert invoice.tax_amount == 90


def test_invoice_total():

    invoice = Invoice(
        invoice_id="1",
        customer="Test",
        invoice_date=date.today(),
        amount=1000
    )

    assert invoice.total_amount == 1090