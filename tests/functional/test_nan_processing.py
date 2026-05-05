import pandas as pd
import numpy as np

def test_dropna_functionality():
    df = pd.DataFrame({"name": ["Alice", None], "age": [25, np.nan]})
    cleaned = df.dropna()
    assert cleaned.isnull().sum().sum() == 0
    assert len(cleaned) == 1