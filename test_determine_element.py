"""Verify if the function determine_element(element) correctly
determines what should be printed out.
"""
from FizzBuzz import determine_element

def test_determine_element():
    """Assert that numbers divisible by 3 return 'Fizz', numbers
    divisible by 5 return 'Buzz', and numbers divisible by both 3 and
    5, return 'FizzBuzz'. Otherwise, assert that a number given which
    is not divisible by 3 or 5 or both, returns itself.
    """
    assert determine_element(9) == 'Fizz'
    assert determine_element(20) == 'Buzz'
    assert determine_element(60) == 'FizzBuzz'
    assert determine_element(98) == 98
