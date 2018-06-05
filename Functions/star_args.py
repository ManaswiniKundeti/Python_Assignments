# the code below is limited to adding only 4 numbers.
#for each extra number we need, we have to pass another variable in the parameter

# def sum_all_nums(num1,num2,num3=0,num4=0):
# 	return num1+num2+num3+num4

# print(sum_all_nums(2,4,3,5))
# print(sum_all_nums(3,4))



# we can use *args to do this. 
# '*args' stores all the input arguments passed to a function in a tuple
# in the code below, we can pass any number of inputs


def sum_all_nums(*args):
	print(args)
	total = 0
	for num in args:
		total += num
	return total


print(sum_all_nums(2,4,3,5))
print(sum_all_nums(3,4))