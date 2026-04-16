pythonimport pandas as pd
import os

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "..", "fixtures", "products.csv")


def test_filter_returns_correct_rows():
    """Only rows with price > 100 should be returned."""
    df = pd.read_csv(FIXTURE_PATH)
    filtered = df[df["price"] > 100]
    assert len(filtered) == 4


def test_filter_min_price():
    """Minimum price in filtered DataFrame should be greater than 100."""
    df = pd.read_csv(FIXTURE_PATH)
    filtered = df[df["price"] > 100]
    assert filtered["price"].min() > 100


def test_filter_excludes_cheap_items():
    """Items with price <= 100 should not appear in filtered result."""
    df = pd.read_csv(FIXTURE_PATH)
    filtered = df[df["price"] > 100]
    assert "Apple" not in filtered["name"].values
    assert "Banana" not in filtered["name"].values
