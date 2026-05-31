from persian_fiscal_tools.dates import shamsi_to_gregorian

def test_shamsi_to_gregorian():
    result = shamsi_to_gregorian("1403/01/01")
    assert result.year == 2024
    assert result.month == 3
    assert result.day == 20
