from dataclasses import dataclass
from datetime import date


@dataclass
class Invoice:

    invoice_id: str
    customer: str
    invoice_date: date
    amount: float
    tax_rate: float = 0.09

    @property
    def tax_amount(self):
        return self.amount * self.tax_rate

    @property
    def total_amount(self):
        return self.amount + self.tax_amount