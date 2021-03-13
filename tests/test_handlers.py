"""The module checks the functionality of the handlers."""
from flask.testing import FlaskClient

from tests.conftest import mock_app

__all__ = ['mock_app']


def test_index(mock_app: FlaskClient):
    """Send an logout request.

    Args:
        mock_app (FlaskClient): Application snapshot for tests
    """
    index_request = mock_app.get('/', follow_redirects=True)
    assert index_request.status_code == 200, 'Index not reached.'
