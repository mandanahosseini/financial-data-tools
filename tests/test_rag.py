from financial_tools.rag.chunker import (
    split_text
)


def test_chunking():

    text = "one two three four five six"

    chunks = split_text(
        text,
        3
    )

    assert len(chunks) == 2