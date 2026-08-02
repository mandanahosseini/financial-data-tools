from pydantic import BaseModel


class InvoiceResponse(BaseModel):

    invoice_id: str

    customer: str

    amount: str

    status: str

    explanation: str