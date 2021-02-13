"""The module checks the functionality of the handlers."""
from flask.testing import FlaskClient
from flask.wrappers import Response

from . import mock_app

__all__ = ['mock_app', ]


def test_index(mock_app: FlaskClient) -> Response:
    """Send an logout request."""
    index_request = mock_app.get('/', follow_redirects=True)
    assert index_request.status_code == 200, 'Index not reached.'
