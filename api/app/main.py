"""FastAPI application for CXRaide model inference."""

from fastapi import FastAPI

app = FastAPI(title="CXRaide Inference API")


@app.get("/health")
def health() -> dict[str, str]:
    """Return API health status."""
    return {"status": "ok"}

