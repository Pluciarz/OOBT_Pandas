import pandas as pd
import os

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "..", "fixtures", "products.csv")


def test_groupby_returns_correct_categories():
    """Grouped result should contain all unique categories."""
    df = pd.read_csv(FIXTURE_PATH)
    result = df.groupby("category")["price"].sum()
    assert set(result.index) == {"fruit", "electronics", "furniture"}


def test_groupby_sum_matches_total():
    """Sum of all group totals should equal total sum of price column."""
    df = pd.read_csv(FIXTURE_PATH)
    result = df.groupby("category")["price"].sum()
    assert result.sum() == df["price"].sum()


def test_groupby_electronics_sum():
    """Electronics category total should equal sum of Laptop and Phone prices."""
    df = pd.read_csv(FIXTURE_PATH)
    result = df.groupby("category")["price"].sum()
    assert result["electronics"] == 3700
