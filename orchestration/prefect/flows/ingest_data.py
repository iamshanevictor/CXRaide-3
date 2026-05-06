"""Prefect flow for dataset ingestion."""

from prefect import flow


@flow(name="cxraide-ingest-data")
def ingest_data() -> None:
    """Download and register source datasets."""
    raise NotImplementedError("Wire this flow to the ingestion scripts.")


if __name__ == "__main__":
    ingest_data()

