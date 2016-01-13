"""Print all integers from 1 to 100. However, for multiples of three,
print 'Fizz' instead of the number, for multiples of five, print
'Buzz', and for numbers which are multiples of both three and five,
print 'FizzBuzz'.
"""
def is_appropriate(number):
    """Return True if the given number is an integer between 0 and
    101. Otherwise, return False.
    """
    return isinstance(number, int) and 0 < number <= 100

def determine_element(element):
    """Determine whether the element should be named, 'Fizz', 'Buzz',
    'FizzBuzz', or itself, make the change to the element(if
    applicable), and return it.
    """
    assert is_appropriate(element)
    if element % 15 == 0:
        return 'FizzBuzz'
    elif element % 3 == 0:
        return 'Fizz'
    elif element % 5 == 0:
        return 'Buzz'
    return element

def format_element(element):
    """Right justify the given element."""
    return "{0:>8s}".format(str(element))

for integer in range(1, 101):
    ELEMENT = determine_element(integer)
    print format_element(ELEMENT)
