from financial_tools.rag.retriever import (
    FinancialRetriever
)

from financial_tools.assistant.financial_assistant import (
    FinancialAssistant
)

from financial_tools.llm.openai_llm import OpenAILLM

import os

class AssistantService:


    def __init__(self):

        self.retriever = FinancialRetriever()

        documents = [

            """
            Invoice INV-1001.
            Customer ABC Company.
            Amount 500000 IRR.
            Status Paid.
            """,

            """
            Invoice INV-1002.
            Customer XYZ Company.
            Amount 900000 IRR.
            Status Pending.
            """
        ]


        self.retriever.build(
            documents
        )


        llm = OpenAILLM(
            os.getenv("OPENAI_API_KEY")
        )


        self.assistant = FinancialAssistant(
             self.retriever,
             llm
        )

    def ask(self, question):

        return self.assistant.answer(
            question
        )