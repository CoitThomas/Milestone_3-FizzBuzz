def create_list(size):
	# takes one positive int 'size' and returns a list of all integers 0 to 'size'  
	list = []
	for i in range(0,size+1):
		list.append(i)
	return list
	
def insert_something(someList,someThing,divisor):
	# takes a list 'someList', a desired variable to be inserted into the list 'someThing', and an int 'divisor'
	# 'someThing' gets inserted into 'someList' at every element where the element's index is divisible by 'divisor'
	for n,i in enumerate(someList):
		if n%divisor == 0 and n!=0:
			someList[n]=someThing
	return someList
				
new_list = create_list(100)
print insert_something(new_list, 'fizz', 3)
print insert_something(new_list, 'buzz', 5)
print insert_something(new_list, 'fizzbuzz', 15)
			
