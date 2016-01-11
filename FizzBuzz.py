"""This module creates a list of 100 enumerated integers and inserts
'Fizz' into the list at every point divisible by 3, 'Buzz' into the
list at every point divisible by 5, and 'FizzBuzz' at every point
divisible by both 3 and 5. The list is then printed out.
"""
from types import ListType, IntType

def create_list(size):
    """Create an enumerated integer list of length, 'size'."""
    assert isinstance(size, IntType)
    some_list = []
    for i in range(0, size+1):
        some_list.append(i)
    return some_list

def insert_something(some_list, anything, divisor):
    """Insert an unknown variable into a list.

    Insert a variable at every point in a list where the index of the
    variable is divisible by an int variable, 'divisor'.
    """
    assert isinstance(some_list, ListType)
    assert isinstance(divisor, IntType)
    for index, content in enumerate(some_list):
        if index%divisor == 0 and index != 0:
            some_list[index] = some_thing
    return some_list

new_list = create_list(100)
insert_something(new_list, 'Fizz', 3)
insert_something(new_list, 'Buzz', 5)
insert_something(new_list, 'FizzBuzz', 15)

print new_list
