"""name gender code test."""

import sys
sys.path.append("..")
from gender.gender import GenderDetector


def test_is_female_name():
    """Test Famele name."""
    detector = GenderDetector()
    expected_gender = detector.run('Ana')
    assert expected_gender == 'female'


def test_is_male_name():
    """Test Male name."""
    detector = GenderDetector()
    expected_gender = detector.run('Pedro')
    assert expected_gender == 'male'
