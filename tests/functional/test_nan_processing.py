import pandas as pd
import numpy as np

def test_dropna_functionality():
    df = pd.DataFrame({"name": ["Alice", None], "age": [25, np.nan]})
    cleaned = df.dropna()
    assert cleaned.isnull().sum().sum() == 0
    assert len(cleaned) == 1


def test_merge_logic_simple():
        df1 = pd.DataFrame({"id": [1, 2], "val": ["A", "B"]})
        df2 = pd.DataFrame({"id": [1, 3], "val": ["X", "Y"]})
        result = pd.merge(df1, df2, on="id", how="inner")
        assert len(result) == 1
        assert result.loc[0, "id"] == 1