"""Gender Detector API."""

import requests
import json


class GenderDetector(object):
    """Run Gender Detector API."""

    def run(self, name):
        """Run Gender Detector API."""
        result = requests.get('https://api.genderize.io/?name={}'.format(name))
        result = json.loads(result.text)
        print(result)
        return result['gender']
