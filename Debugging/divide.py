def divide(a,b):
	try:
		result = a/b
	except ZeroDivisionError:
		print("Dont divide by zero please")
	except TypeError as e:
		print("a and b must be int or float")
		print(e)
	else:
		print(f"{a} divided by {b} gives {result}")

print(divide(1,2))
print(divide(1,0))
print(divide(1,'a'))


##CATCHING BOTH ERROR"S AT A TIME
# def divide(a,b):
# 	try:
# 		result = a/b
# 	except (ZeroDivisionError,TypeError) as e:
# 		print("Something went wrong!!")
# 		print(e)
# 	else:
# 		print(f"{a} divided by {b} gives {result}")

# print(divide(1,2))
# print(divide(1,0))
# print(divide(1,'a'))