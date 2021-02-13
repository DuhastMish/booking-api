import pytest  # noqa : D100

from api_site import app


@pytest.fixture
def mock_app():
    """Create a DataRoom for testing."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
