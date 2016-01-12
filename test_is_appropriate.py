"""Verify if the function is_appropriate(number) returns True when an
appropriate number is given."""
from FizzBuzz import is_appropriate

def test_is_appropriate():
    """Assert that integers between 0 and 101 return True."""
    assert is_appropriate(1) is True
    assert is_appropriate(100) is True
    assert is_appropriate(53) is True
