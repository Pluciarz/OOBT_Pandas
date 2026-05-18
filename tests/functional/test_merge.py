import pandas as pd
import os

# Sciezki do plikow csv stworzonych w kroku 1
EMPLOYEES_PATH = os.path.join(os.path.dirname(__file__), "..", "fixtures", "employees.csv")
DEPARTMENTS_PATH = os.path.join(os.path.dirname(__file__), "..", "fixtures", "departments.csv")

def test_merge_contains_all_columns():
    """Merged DataFrame should contain columns from both input DataFrames."""
    employees = pd.read_csv(EMPLOYEES_PATH)
    departments = pd.read_csv(DEPARTMENTS_PATH)
    merged = pd.merge(employees, departments, on="id")
    assert "name" in merged.columns
    assert "department" in merged.columns

def test_inner_merge_row_count():
    """Inner merge should return only rows with matching IDs in both DataFrames."""
    employees = pd.read_csv(EMPLOYEES_PATH)
    departments = pd.read_csv(DEPARTMENTS_PATH)
    merged = pd.merge(employees, departments, on="id", how="inner")
    assert len(merged) == 3

def test_merge_excludes_unmatched_ids():
    """ID present only in one DataFrame should not appear in inner merge result."""
    employees = pd.read_csv(EMPLOYEES_PATH)
    departments = pd.read_csv(DEPARTMENTS_PATH)
    merged = pd.merge(employees, departments, on="id", how="inner")
    assert 4 not in merged["id"].values
    assert 5 not in merged["id"].values


def test_left_merge_keeps_all_left_rows():
    """Left merge should keep all rows from left DataFrame."""
    employees = pd.read_csv(EMPLOYEES_PATH)
    departments = pd.read_csv(DEPARTMENTS_PATH)
    merged = pd.merge(employees, departments, on="id", how="left")
    assert len(merged) == len(employees)


def test_merge_no_common_ids_returns_empty():
    """Inner merge with no common IDs should return empty DataFrame."""
    df1 = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
    df2 = pd.DataFrame({"id": [9, 10], "department": ["HR", "IT"]})
    merged = pd.merge(df1, df2, on="id", how="inner")
    assert len(merged) == 0