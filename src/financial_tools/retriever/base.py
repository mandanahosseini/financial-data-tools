from abc import ABC, abstractmethod


class BaseRetriever(ABC):

    @abstractmethod
    def retrieve(self, question: str) -> list[str]:
        """
        Retrieve relevant documents.
        """
        pass