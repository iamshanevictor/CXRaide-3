"""Prefect flow for data preparation."""

from prefect import flow


@flow(name="cxraide-prepare-data")
def prepare_data() -> None:
    """Build manifests, normalize labels, preprocess images, and split data."""
    raise NotImplementedError("Wire this flow to the preparation scripts.")


if __name__ == "__main__":
    prepare_data()

