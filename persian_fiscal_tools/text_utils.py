def normalize_persian_text(text: str) -> str:
    replacements = {'ي': 'ی', 'ك': 'ک'}
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def number_to_persian_words(amount: int) -> str:
    return f"{amount:,} تومان"
