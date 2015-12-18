from types import *

def create_list(size):
	# takes one positive int 'size' and returns a list of all integers 0 to 'size'  
	assert type(size) is IntType, "The 'size' of the list needs to be an integer."
	list = []
	for i in range(0,size+1):
		list.append(i)
	return list
	
def insert_something(someList,someThing,divisor):
	# takes a list 'someList', a desired variable to be inserted into the list 'someThing', and an int 'divisor'
	# 'someThing' gets inserted into 'someList' at every element where the element's index is divisible by 'divisor'
	assert type(someList) is ListType, "A list was not given."
	assert type(divisor) is IntType, "The positions of insertion need to be an integer."
	for n,i in enumerate(someList):
		if n%divisor == 0 and n!=0:
			someList[n]=someThing
	return someList
				
new_list = create_list(100)
insert_something(new_list, 'fizz', 3)
insert_something(new_list, 'buzz', 5)
insert_something(new_list, 'fizzbuzz', 15)

print new_list			
