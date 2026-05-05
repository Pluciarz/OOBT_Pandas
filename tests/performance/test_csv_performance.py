import pandas as pd
import numpy as np
import time
import os
import tempfile

def generate_large_csv(path: str, rows: int = 100_000):
    """Generate a large CSV file for performance testing."""
    rng = np.random.default_rng(42)
    df = pd.DataFrame({
        "id": range(rows),
        "name": [f"User_{i}" for i in range(rows)],
        "age": rng.integers(18, 80, size=rows),
        "salary": rng.integers(3000, 20000, size=rows),
        "city": rng.choice(["Warsaw", "Krakow", "Gdansk", "Poznan"], size=rows)
    })
    df.to_csv(path, index=False)