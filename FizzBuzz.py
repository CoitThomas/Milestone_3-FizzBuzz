"""Print all integers from 1 to 100. However, for multiples of three,
print 'Fizz' instead of the number, for multiples of five, print
'Buzz', and for numbers which are multiples of both three and five,
print 'FizzBuzz'.
"""
def is_appropriate(number):
    """Return True if the given number is an integer between 0 and
    101. Otherwise, return False.
    """
    if isinstance(number, int) and 0 < number <= 100:
        return True
    return False

def determine_element(element):
    """Determine whether the element should be named, 'Fizz', 'Buzz',
    'FizzBuzz', or itself, make the change to the element(if
    applicable), and return it.
    """
    assert is_appropriate(element) is True
    if element % 15 == 0:
        return 'FizzBuzz'
    elif element % 3 == 0:
        return 'Fizz'
    elif element % 5 == 0:
        return 'Buzz'
    return element

def format_element(number, element):
    """Arrange the given number and element to fit the following
    format: {ddd  :  element} where the number 'ddd' is given a
    right-side alignment.
    """
    assert is_appropriate(number) is True
    return "{0:3d}  :  ".format(number) + str(element)

for integer in range(1, 101):
    ELEMENT = determine_element(integer)
    print format_element(integer, ELEMENT)
