def square_of_7():
	print("I am before return")
	return 7**2
	print("I am after return") # wont print as the return stmt exits the function 

result = square_of_7()
print(result)