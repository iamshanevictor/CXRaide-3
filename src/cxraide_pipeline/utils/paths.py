"""Path helpers for local pipeline execution."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]


def project_path(*parts: str) -> Path:
    """Build an absolute path from the repository root."""
    return PROJECT_ROOT.joinpath(*parts)

