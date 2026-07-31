from financial_tools.rag.retriever import (
    FinancialRetriever
)

from financial_tools.assistant.financial_assistant import (
    FinancialAssistant
)

from financial_tools.assistant.mock_llm import (
    MockLLM
)


documents = [

"""
Invoice INV-1001
Customer: ABC Company
Amount: 500000 IRR
Status: Paid
""",

"""
Invoice INV-1002
Customer: XYZ Company
Amount: 900000 IRR
Status: Pending
"""
]


retriever = FinancialRetriever()

retriever.build(
    documents
)


assistant = FinancialAssistant(
    retriever,
    MockLLM()
)


answer = assistant.answer(
    "Which invoice is pending?"
)


print(answer)