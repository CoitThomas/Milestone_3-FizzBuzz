"""Verify if the function format_element(number, element) correctly
returns a number and its corresponding element in the desired format.
"""
from FizzBuzz import format_element

def test_format_element():
    """Assert that numbers between 0 and 10, 9 and 100, and 100, return
    in their desired respective formats.
    """
    assert format_element(7, 'foo') == '  7  :  foo'
    assert format_element(11, 'man') == ' 11  :  man'
    assert format_element(100, 'chu') == '100  :  chu'
