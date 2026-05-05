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



def test_read_csv_performance():
    """Reading a 100k row CSV file should complete in under 3 seconds."""
    with tempfile.TemporaryDirectory() as tmpdir:
        csv_path = os.path.join(tmpdir, "large_data.csv")
        generate_large_csv(csv_path)

        start = time.perf_counter()
        df = pd.read_csv(csv_path)
        elapsed = time.perf_counter() - start

        print(f"\n[PERF] read_csv on 100k rows: {elapsed:.4f}s")
        assert elapsed < 3.0, f"read_csv too slow: {elapsed:.4f}s"
        assert len(df) == 100_000