import pandas as pd
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

def test_filter_empty_result():
    """Filter returning no rows should produce empty DataFrame."""
    df = pd.read_csv(FIXTURE_PATH)
    filtered = df[df["price"] > 999999]
    assert len(filtered) == 0
    assert list(filtered.columns) == ["name", "price", "category"]


def test_filter_all_rows_match():
    """Filter matching all rows should return full DataFrame."""
    df = pd.read_csv(FIXTURE_PATH)
    filtered = df[df["price"] > 0]
    assert len(filtered) == len(df)


def test_filter_on_string_column():
    """Filter on string column should return correct subset."""
    df = pd.read_csv(FIXTURE_PATH)
    filtered = df[df["category"] == "electronics"]
    assert all(filtered["category"] == "electronics")
    assert len(filtered) == 2
