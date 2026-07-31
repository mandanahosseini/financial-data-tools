from fastapi import FastAPI

from .schemas import (
    QuestionRequest,
    AnswerResponse
)

from financial_tools.services.assistant_service import (
    AssistantService
)


app = FastAPI(
    title="Financial AI Assistant API",
    version="1.0"
)


assistant_service = AssistantService()



@app.get("/")
def root():

    return {
        "message":
        "Financial AI Assistant API"
    }



@app.post(
    "/ask",
    response_model=AnswerResponse
)
def ask_question(
    request: QuestionRequest
):

    answer = assistant_service.ask(
        request.question
    )

    return AnswerResponse(
        answer=answer
    )