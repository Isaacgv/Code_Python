"""Teste api temperature."""

import main
from unittest import TestCase
from unittest.mock import Mock
from requests.exceptions import Timeout

main.requests = Mock()

lat = -14.235004
lng = -51.92528


class TestAPI(TestCase):
    """Test api get temperature."""

    def log_request(self, url):
        """Log a fake request for test output purposes."""
        response_mock = Mock()
        response_mock.json.return_value = {'currently':
                                           {'temperature': 62}}
        return response_mock

    def test_get_temperature_by_lat_lng(self):
        """Test temperature convertion."""
        main.requests.get.side_effect = self.log_request
        assert main.get_temperature(lat, lng) == 16

    def test_get_temperature_timeout(self):
        """Test connection timeout."""
        main.requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            main.get_temperature(lat, lng)
