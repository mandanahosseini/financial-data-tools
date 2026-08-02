from financial_tools.llm.factory import get_llm

from financial_tools.rag.retriever import (
    FinancialRetriever
)

from financial_tools.assistant.financial_assistant import (
    FinancialAssistant
)


class AssistantService:


    def __init__(self):

        self.retriever = FinancialRetriever()


        documents = [

            """
            Invoice ID: INV-1001
            Customer: ABC Company
            Category: Software License
            Amount: 500000 IRR
            Date: 2026-01-15
            Status: Paid
            """,


            """
            Invoice ID: INV-1002
            Customer: XYZ Company
            Category: ERP Support
            Amount: 900000 IRR
            Date: 2026-02-20
            Status: Pending
            """
        ]


        self.retriever.build(
            documents
        )


        llm = get_llm()


        self.assistant = FinancialAssistant(
            self.retriever,
            llm
        )


    def ask(
        self,
        question
    ):

        return self.assistant.answer(
            question
        )