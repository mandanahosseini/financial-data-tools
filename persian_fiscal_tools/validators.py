def validate_national_code(code: str) -> bool:
    if not code or not code.isdigit() or len(code) != 10:
        return False
    if len(set(code)) == 1:
        return False
    check = int(code[9])
    total = sum(int(code[i]) * (10 - i) for i in range(9))
    remainder = total % 11
    if remainder < 2:
        return check == remainder
    return check == (11 - remainder)

def validate_postal_code(code: str) -> bool:
    return bool(code) and code.isdigit() and len(code) == 10
