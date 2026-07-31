from .embeddings import FinancialEmbedding
from .vector_store import FinancialVectorStore


class FinancialRetriever:


    def __init__(self):

        self.embedding = FinancialEmbedding()

        self.store = None


    def build(self, documents):

        vectors = self.embedding.encode(
            documents
        )

        dimension = vectors.shape[1]

        self.store = FinancialVectorStore(
            dimension
        )

        self.store.add(
            vectors,
            documents
        )


    def retrieve(self, question):

        query_vector = self.embedding.encode(
            [question]
        )[0]


        return self.store.search(
            query_vector
        )