"""Module contains fixture for tests."""
import pytest

from booking_api.app import app


@pytest.fixture
def mock_app():
    """Create a DataRoom for testing."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
