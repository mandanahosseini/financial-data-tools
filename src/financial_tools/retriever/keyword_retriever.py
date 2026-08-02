from .base import BaseRetriever


class KeywordRetriever(BaseRetriever):

    def __init__(self):
        self.documents = [
            "Invoice INV-1001 has been paid.",
            "Invoice INV-1002 is pending.",
            "Customer XYZ Company owes 900000 IRR."
        ]

    def retrieve(self, question: str):

        return self.documents