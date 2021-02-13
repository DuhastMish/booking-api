from pathlib import Path


class LocalStorage():
    def _get_path_for_api_documentation(self) -> Path:
        """Return path for API documentation yaml."""
        return Path(__file__).parents[1] / 'api_documentation.yaml'

    def get_api_documentation(self) -> bytes:
        """Return API documentation yaml content."""
        return self._get_path_for_api_documentation().read_bytes()
