"""Print all integers from 1 to 100. However, for multiples of three,
print 'Fizz' instead of the number, for multiples of five, print
'Buzz', and for numbers which are multiples of both three and five,
print 'FizzBuzz'.
"""
def is_appropriate(number):
    """Assert whether or not a given number is an integer between 0 and
    101. Is so, return the boolean True.
    """
    assert isinstance(number, int)
    assert 0 < number <= 100
    return True

def determine_element(element):
    """Determine whether the element should be named, 'Fizz', 'Buzz',
    'FizzBuzz', or itself, make the change to the element(if
    applicable), and return it.
    """
    if is_appropriate(element):
        if element % 15 == 0:
            return 'FizzBuzz'
        elif element % 3 == 0:
            return 'Fizz'
        elif element % 5 == 0:
            return 'Buzz'
        return element

def format_element(number, element):
    """Structure the number according to the amount of digits it
    contains and print it out with its corresponding element.
    """
    if is_appropriate(number):
        if number < 10:
            return "  " + str(number) + "  :  "+str(element)
        if 10 <= number < 100:
            return " " + str(number) + "  :  "+str(element)
        if number == 100:
            return str(number) + "  :  "+str(element)

for integer in range(1, 101):
    ELEMENT = determine_element(integer)
    print format_element(integer, ELEMENT)
