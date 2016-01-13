"""Verify if the function format_element(number, element) correctly
returns a number and its corresponding element in the desired format.
"""
from FizzBuzz import format_element

def test_format_element():
    """Assert that numbers between 0 and 10, 9 and 100, and 100, return
    in their desired respective formats.
    """
    assert format_element('a') == '       a'
    assert format_element(11) == '      11'
    assert format_element('bbb') == '     bbb'
    assert format_element(2222) == '    2222'
    assert format_element('ccccc') == '   ccccc'
    assert format_element(333333) == '  333333'
    assert format_element('ddddddd') == ' ddddddd'
    assert format_element(44444444) == '44444444'
    assert format_element(0.0) == '     0.0'
