def add(a,b):
	return a+b

def subtract(a,b):
	return a-b

def math(a,b, fn = add):
	return fn(a,b)

print(math(3,2,subtract))