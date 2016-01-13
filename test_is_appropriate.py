"""Verify if the function is_appropriate(number) returns True when an
appropriate number is given and False when it is not."""
from FizzBuzz import is_appropriate

def test_is_appropriate():
    """Assert that integers between 0 and 101 return True and that all
    other inputs return False.
    """
    assert is_appropriate(1)
    assert is_appropriate(100)
    assert is_appropriate(53)
    assert not is_appropriate(0)
    assert not is_appropriate(101)
    assert not is_appropriate(50.5)
    assert not is_appropriate('a')
    assert not is_appropriate('hello')
    assert not is_appropriate(['hello', 'world'])
