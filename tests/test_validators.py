from persian_fiscal_tools.validators import validate_national_code, validate_postal_code

def test_national_code():
    assert validate_national_code("1111111111") == False

def test_postal_code():
    assert validate_postal_code("1234567890") == True
    assert validate_postal_code("123") == False
