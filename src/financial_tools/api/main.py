from fastapi import FastAPI
import json

from .schemas import QuestionRequest
from financial_tools.services.assistant_service import AssistantService
from financial_tools.models.financial_response import InvoiceResponse

app = FastAPI(
    title="Financial AI Assistant API",
    version="1.0"
)

assistant_service = AssistantService()


@app.get("/")
def root():
    return {
        "message": "Financial AI Assistant API"
    }


@app.post(
    "/ask",
    response_model=InvoiceResponse
)
def ask_question(request: QuestionRequest):

    answer = assistant_service.ask(request.question)

    try:

        data = json.loads(answer)

        return InvoiceResponse(
            invoice_id=data.get("invoice_id", ""),
            customer=data.get("customer", ""),
            amount=data.get("amount", ""),
            status=data.get("status", ""),
            explanation=data.get("explanation", "")
        )

    except json.JSONDecodeError:

        return InvoiceResponse(
            invoice_id="",
            customer="",
            amount="",
            status="",
            explanation="The model returned invalid JSON."
        )