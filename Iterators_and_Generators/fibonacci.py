def fib_list(max):
	nums = []
	a,b = 0,1
	while len(nums) < max:
		nums.append(b)
		a,b = b,a+b
	return nums




#using generators -  when dealing with large sequences,takes very less memory compared to a list(so is quick)

# def fib_gen(max):
# 	x = 0
# 	y = 1
# 	count = 0
# 	while count < max:
# 		x,y = y,x+y
# 		yield x
# 		count += 1



print(fib_list(10))  #comes in a list
#OR
for n in fib_list(10):  # each number comes in a new line
	print(n)