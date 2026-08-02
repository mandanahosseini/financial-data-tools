from .base import BaseLLM


class OllamaLLM(BaseLLM):

    def __init__(
        self,
        model="llama3.2"
    ):

        self.model = model


    def generate(
        self,
        prompt: str
    ):

        # کد واقعی Ollama بعداً اینجا منتقل می‌شود

        return ""