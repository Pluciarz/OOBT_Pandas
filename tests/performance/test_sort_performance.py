import pandas as pd
import numpy as np
import time


def test_sort_values_performance():
    """Sort of 100k rows should complete in under 2 seconds."""
    rng = np.random.default_rng(42)
    df = pd.DataFrame({
        "id": range(100_000),
        "value": rng.integers(0, 1_000_000, size=100_000),
        "category": rng.choice(["A", "B", "C", "D"], size=100_000)
    })

    start = time.perf_counter()
    df.sort_values("value")
    elapsed = time.perf_counter() - start

    print(f"\n[PERF] sort_values on 100k rows: {elapsed:.4f}s")
    assert elapsed < 2.0, f"sort_values too slow: {elapsed:.4f}s"


def test_sort_values_correctness():
    """Sorted DataFrame should be monotonically increasing."""
    rng = np.random.default_rng(42)
    df = pd.DataFrame({"value": rng.integers(0, 1_000_000, size=100_000)})
    df_sorted = df.sort_values("value").reset_index(drop=True)
    assert df_sorted["value"].is_monotonic_increasing
