"""Print all numbers from 1 to 100. However, for multiples of three,
print 'Fizz' instead of the number, for multiples of five, print
'Buzz', and for numbers which are multiples of both three and five,
print 'FizzBuzz'.
"""

def determine_element(element):
    """Determine whether the element should be named, 'Fizz', 'Buzz',
    'FizzBuzz', or itself, make the change to the element(if
    applicable), and return it.
    """
    if element % 15 == 0:
        return 'FizzBuzz'
    elif element % 3 == 0:
        return 'Fizz'
    elif element % 5 == 0:
        return 'Buzz'
    return element

def print_element(number, element):
    """Structure the number according to the amount of digits it
	contains and print it out with its corresponding element.
	"""
    if number < 10:
        print "  " + str(number) + "  :  "+str(element)
    if 10 <= number < 100:
        print " " + str(number) + "  :  "+str(element)
    if number >= 100:
        print str(number) + "  :  "+str(element)

for integer in range(1, 101):
    ELEMENT = determine_element(integer)
    print_element(integer, ELEMENT)
