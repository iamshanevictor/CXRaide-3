"""End-to-end Prefect flow for the CXRaide pipeline."""

from prefect import flow


@flow(name="cxraide-full-pipeline")
def full_pipeline() -> None:
    """Run ingestion, preparation, validation, transformations, and training."""
    raise NotImplementedError("Compose the stage flows once each stage is implemented.")


if __name__ == "__main__":
    full_pipeline()

