"""This module works with local storage."""
from pathlib import Path


class LocalStorage():
    """Class for working with local files."""

    def get_api_documentation(self) -> bytes:
        """Return API documentation yaml content."""
        return self._get_path_for_api_documentation().read_bytes()

    def _get_path_for_api_documentation(self) -> Path:
        """Return path for API documentation yaml."""
        return Path(__file__).parents[1] / 'api_documentation.yaml'
