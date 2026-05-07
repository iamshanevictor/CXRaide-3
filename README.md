# CXRaide 3.0 Machine Learning Project

Machine learning workspace for CXRaide 3.0, the next iteration of the CXRaide chest X-ray annotation and AI-assisted analysis system.

CXRaide 3.0 focuses on improving the model and data preparation strategy used in CXRaide 2.0. In the previous version, chest X-ray images were downscaled to 300x300 before training, which may have reduced small radiographic features that are important for localization and classification. This version will explore a higher-resolution object detection workflow centered on EfficientDet-D4, which can support 1024x1024 inputs.

## Direction

This repository is organized around a revised ML workflow:

- Prepare NIH and VinBig chest X-ray metadata and image labels for ML experiments.
- Keep raw image payloads outside Git while tracking lightweight CSV metadata.
- Preserve more image detail during preprocessing by targeting 1024x1024 model inputs.
- Train and evaluate EfficientDet-D4 as the primary detection model.
- Compare CXRaide 3.0 results against CXRaide 2.0 assumptions, especially the effect of image resolution on detection quality.
- Serve model predictions through a lightweight API.

## Roadmap

1. Rework data preparation for high-resolution training.
   - Standardize NIH and VinBig metadata.
   - Convert labels and bounding boxes into a consistent detection format.
   - Resize or pad images to 1024x1024 while preserving aspect ratio where possible.
   - Track how coordinate transforms affect bounding boxes.

2. Build the EfficientDet-D4 training workflow.
   - Define the dataset loader, augmentation policy, and training configuration.
   - Start with pretrained weights when available.
   - Track experiments, metrics, and artifacts with MLflow.

3. Evaluate model performance.
   - Measure detection quality using mAP, IoU-based metrics, precision, and recall.
   - Compare performance across image resolutions where useful.
   - Review failure cases visually, especially small findings and overlapping pathologies.

4. Prepare inference support.
   - Add local prediction scripts for trained checkpoints.
   - Keep the FastAPI app as an optional inference interface.
   - Document expected inputs, outputs, confidence thresholds, and model limitations.

5. Document research outcomes.
   - Update the data card with preprocessing decisions and dataset limitations.
   - Update the model card with architecture, training setup, evaluation results, and intended use.
   - Keep experiment notes under `ml/experiments/`.

## Project Areas

- `notebooks/DataPreparation/`: dataset cleaning, merging, balancing, and exploratory preparation notebooks.
- `notebooks/ML/`: notebook-based model dataset export and ML experiments.
- `ml/`: model training, evaluation, inference, and experiment code.
- `api/`: FastAPI inference service.

## Local-First Stack

- Python for preparation and ML code
- PyTorch for model training
- EfficientDet-D4 for high-resolution chest X-ray object detection
- MLflow for experiment tracking
- FastAPI for inference serving

## Data Notice

Raw NIH and VinBig image files are not committed to this repository. See [notebooks/README.md](notebooks/README.md) for the expected notebook data layout.

## Research Note

CXRaide 3.0 is a research and development project. Model outputs should be treated as experimental and not as clinical decisions.

