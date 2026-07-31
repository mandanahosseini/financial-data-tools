from financial_tools.rag.retriever import (
    FinancialRetriever
)


documents = [

"""
Invoice INV-1001
Customer ABC Company
Amount 500000 IRR
Status Paid
""",

"""
Invoice INV-1002
Customer XYZ Company
Amount 900000 IRR
Status Pending
""",

"""
Supplier payment
Amount 300000 IRR
Category Purchase
"""
]


retriever = FinancialRetriever()


retriever.build(
    documents
)


question = """
Which invoice has pending payment?
"""


results = retriever.retrieve(
    question
)


for r in results:

    print("----------------")

    print(r)