# Data Layout

This folder is intentionally excluded from Git for raw and generated data.

Expected local layout:

```text
data/
  raw/         # Original Kaggle downloads and extracted archives
  interim/     # Temporary extraction and preprocessing outputs
  processed/   # Clean manifests, splits, parquet/csv outputs, local DuckDB files
  external/    # Optional external lookup tables
```

Recommended rule: never edit files in `data/raw/`. Treat them as immutable source data.

