from financial_tools.rag.chunker import (
    split_text
)

from src.financial_tools.rag.embeddings import (
    FinancialEmbedding
)


document = """
Invoice INV-1001.
Customer ABC Company.
Total amount 500000 IRR.
Payment status paid.
"""


chunks = split_text(
    document,
    5
)


print(chunks)


embedding = FinancialEmbedding()

vectors = embedding.encode(
    chunks
)


print(vectors)