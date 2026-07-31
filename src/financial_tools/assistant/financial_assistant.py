from .prompt import FINANCIAL_SYSTEM_PROMPT


class FinancialAssistant:


    def __init__(self, retriever, llm):

        self.retriever = retriever
        self.llm = llm


    def answer(self, question):

        documents = self.retriever.retrieve(
            question
        )


        context = "\n\n".join(
            documents
        )


        prompt = FINANCIAL_SYSTEM_PROMPT.format(
            context=context,
            question=question
        )


        response = self.llm.generate(
            prompt
        )


        return response