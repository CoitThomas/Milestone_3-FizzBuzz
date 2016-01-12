"""Verify if the function is_appropriate(number) returns True when an
appropriate number is given and False when it is not."""
from FizzBuzz import is_appropriate

def test_is_appropriate():
    """Assert that integers between 0 and 101 return True and that all
    other inputs return False.
    """
    assert is_appropriate(1) is True
    assert is_appropriate(100) is True
    assert is_appropriate(53) is True
    assert is_appropriate(0) is False
    assert is_appropriate(101) is False
    assert is_appropriate(50.5) is False
    assert is_appropriate('a') is False
    assert is_appropriate('hello') is False
    assert is_appropriate(['hello', 'world']) is False
