from financial_tools.rag.retriever import (
    FinancialRetriever
)

from financial_tools.assistant.financial_assistant import (
    FinancialAssistant
)

from financial_tools.assistant.mock_llm import (
    MockLLM
)


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


        self.assistant = FinancialAssistant(
            self.retriever,
            MockLLM()
        )


    def ask(self, question):

        return self.assistant.answer(
            question
        )