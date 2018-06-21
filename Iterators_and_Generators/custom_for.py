 #Custom for loop

 # for num in [1,2,3]
 # for char in "hi there"

def my_for(iterable,func):
 	iterator = iter(iterable)
 	while True:
 		try:
 			thing = next(iterator)
 		except StopIteration:
 			print("END OF ITERATOR")
 			break
 		else:
 			func(thing)

def square(x):
	print(x*x)

my_for("hello",print)  #print each char separately
my_for([1,2,3],square)