"""
Synthetic Financial Data Generator

Generate realistic synthetic financial transactions
for analytics, machine learning, and AI applications.
"""

import random
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker


fake = Faker()


def generate_transactions(n_records=100):
    """
    Generate synthetic financial transactions.

    Parameters:
        n_records (int): Number of transactions

    Returns:
        pandas.DataFrame
    """

    transactions = []

    for i in range(n_records):

        amount = round(random.uniform(100, 500000), 2)

        transaction = {
            "transaction_id": f"TRX-{i+1:05d}",
            "date": fake.date_between(
                start_date="-2y",
                end_date="today"
            ),
            "customer": fake.company(),
            "category": random.choice(
                [
                    "Sales",
                    "Purchase",
                    "Service",
                    "Expense"
                ]
            ),
            "amount": amount,
            "currency": "IRR",
            "status": random.choice(
                [
                    "Paid",
                    "Pending",
                    "Cancelled"
                ]
            )
        }

        transactions.append(transaction)

    return pd.DataFrame(transactions)


if __name__ == "__main__":

    df = generate_transactions(20)

    print(df)

    df.to_csv(
        "data/synthetic/sample_transactions.csv",
        index=False
    )