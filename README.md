# CXRaide Machine Learning Project

Machine learning workspace for CXRaide, a chest X-ray annotation and AI-assisted analysis system.

This repository is organized around dataset preparation and model development:

- Prepare NIH and VinBig chest X-ray metadata and image labels for ML experiments.
- Keep raw image payloads outside Git while tracking lightweight CSV metadata.
- Train and evaluate a deep learning model with MLflow tracking.
- Serve model predictions through a lightweight API.

## Project Areas

- `notebooks/DataPreparation/`: dataset cleaning, merging, balancing, and exploratory preparation notebooks.
- `notebooks/ML/`: notebook-based model dataset export and ML experiments.
- `ml/`: model training, evaluation, inference, and experiment code.
- `api/`: FastAPI inference service.

## Local-First Stack

- Python for preparation and ML code
- MLflow for experiment tracking
- FastAPI for inference serving

## Data Notice

Raw NIH and VinBig image files are not committed to this repository. See [notebooks/README.md](notebooks/README.md) for the expected notebook data layout.

