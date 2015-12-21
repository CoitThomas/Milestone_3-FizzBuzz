from types import ListType, IntType

def create_list(size):
    #takes one positive int 'size' and returns a list of all integers 0 to 'size'
    assert isinstance(size, IntType)
    some_list = []
    for i in range(0, size+1):
        some_list.append(i)
    return some_list

def insert_something(some_list, some_thing, divisor):
    #takes a list 'someList', a desired variable to be inserted into the list 'someThing', and an
    #int 'divisor'. 'someThing' gets inserted into 'someList' at every element where the element's
    #index is divisible by 'divisor'
    assert isinstance(some_list, ListType)
    assert isinstance(divisor, IntType)
    for index, content in enumerate(some_list):
        if index%divisor == 0 and index != 0:
            some_list[index] = some_thing
    return some_list

new_list = create_list(100)
insert_something(new_list, 'fizz', 3)
insert_something(new_list, 'buzz', 5)
insert_something(new_list, 'fizzbuzz', 15)

print new_list
