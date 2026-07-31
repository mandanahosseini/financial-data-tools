from financial_tools.data_generator.synthetic_finance import (
    generate_transactions
)


def test_generate_transactions():

    df = generate_transactions(10)

    assert len(df) == 10


def test_required_columns():

    df = generate_transactions(5)

    expected_columns = [
        "transaction_id",
        "date",
        "customer",
        "category",
        "amount",
        "currency",
        "status"
    ]

    for column in expected_columns:
        assert column in df.columns