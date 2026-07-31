from financial_tools.assistant.prompt import (
    FINANCIAL_SYSTEM_PROMPT
)


def test_prompt_contains_context():

    assert "{context}" in FINANCIAL_SYSTEM_PROMPT
    assert "{question}" in FINANCIAL_SYSTEM_PROMPT