from financial_tools.config.settings import DEFAULT_LLM
from financial_tools.config.settings import DEFAULT_MODEL

from .ollama import OllamaLLM
from .openai import OpenAILLM



def get_llm():


    if DEFAULT_LLM == "ollama":

        return OllamaLLM(
            DEFAULT_MODEL
        )


    if DEFAULT_LLM == "openai":

        return OpenAILLM()


    raise ValueError(
        "Unsupported LLM"
    )