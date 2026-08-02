import ollama

from .base import BaseLLM



class OllamaLLM(BaseLLM):


    def __init__(
        self,
        model="llama3.2"
    ):

        self.model = model



    def generate(
        self,
        prompt
    ):


        response = ollama.chat(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )


        return response["message"]["content"]