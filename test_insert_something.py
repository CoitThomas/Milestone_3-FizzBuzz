from FizzBuzz import insert_something

def test_insert_something():
	assert insert_something([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],'pow',2) == [0,1,'pow',3,'pow',5,'pow',7,'pow',9,'pow',11,'pow',13,'pow',15,'pow']
	assert insert_something([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],'whack',4) == [0,1,2,3,'whack',5,6,7,'whack',9,10,11,'whack',13,14,15,'whack']
	assert insert_something([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],5,3) == [0,1,2,5,4,5,5,7,8,5,10,11,5,13,14,5,16]
	assert insert_something([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],chr(97),5) == [0,1,2,3,4,'a',6,7,8,9,'a',11,12,13,14,'a',16]
	