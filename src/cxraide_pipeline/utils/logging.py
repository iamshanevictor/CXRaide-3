"""Logging helpers for pipeline scripts."""

import logging


def get_logger(name: str) -> logging.Logger:
    """Return a console logger with a consistent format."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )
    return logging.getLogger(name)

