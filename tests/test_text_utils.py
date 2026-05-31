from persian_fiscal_tools.text_utils import normalize_persian_text

def test_normalize():
    text = "كتاب"
    normalized = normalize_persian_text(text)
    assert "ك" not in normalized
