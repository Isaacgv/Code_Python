"""Teste temperature."""
# from main import get_temperature
import main
import pytest

_resp_ap = {'currently': {'temperature': 62}}


class ResponseMock:
    """Mock response."""

    def json(self):
        """Mock json."""
        return _resp_ap


def get_mock(url):
    """Mock get."""
    return ResponseMock()


@pytest.fixture
def mock_request_get():
    """Mock request.get."""
    get = main.requests.get
    main.requests.get = get_mock
    yield get_mock
    # Tear down
    main.requests.get = get


def test_get_temperature_by_lat_lng(mock_request_get):
    """Test temperature convertion."""
    lat = -14.235004
    lng = -51.92528

    assert main.get_temperature(lat, lng) == 16
