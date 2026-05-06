# CXRaide Data Pipeline

End-to-end data engineering portfolio project for CXRaide, a chest X-ray annotation and AI-assisted analysis system.

This repository is organized to demonstrate a production-style pipeline:

- Ingest NIH and VinBig chest X-ray datasets from Kaggle.
- Store raw files outside Git and track dataset lineage.
- Validate metadata, labels, image manifests, and train/validation/test splits.
- Transform analytical tables with dbt.
- Train and evaluate a deep learning model with MLflow tracking.
- Serve model predictions through a lightweight API.

## Pipeline Stages

1. Ingestion: download and register Kaggle datasets.
2. Data preparation: extract metadata, normalize labels, preprocess images, and create dataset splits.
3. Validation: run Great Expectations checks before downstream processing.
4. Transformation: use dbt models for clean analytical tables.
5. Machine learning: train, evaluate, and track models.
6. Deployment: expose model inference through FastAPI and Docker.

## Local-First Stack

- Python for pipeline code
- DuckDB for local analytics storage
- dbt Core for SQL transformations
- Great Expectations GX Core for validation
- Prefect for beginner-friendly orchestration
- MLflow for experiment tracking
- FastAPI for inference serving

## Data Notice

Raw NIH and VinBig image files are not committed to this repository. See [data/README.md](data/README.md) for the expected local layout.

