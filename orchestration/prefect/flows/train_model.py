"""Prefect flow for model training."""

from prefect import flow


@flow(name="cxraide-train-model")
def train_model() -> None:
    """Train and evaluate the CXRaide model."""
    raise NotImplementedError("Wire this flow to ml/training/train.py.")


if __name__ == "__main__":
    train_model()

