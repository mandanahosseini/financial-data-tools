from fastapi import FastAPI

from .schemas import (
    QuestionRequest,
    AnswerResponse
)


app = FastAPI(
    title="Financial AI Assistant API",
    description="RAG based financial assistant",
    version="1.0"
)


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

    # Later connected to real RAG pipeline

    answer = (
        "Received question: "
        + request.question
    )

    return AnswerResponse(
        answer=answer
    )