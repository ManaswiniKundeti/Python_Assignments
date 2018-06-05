def add_and_multiply_numbers(a,b,c,**kwargs):
	print(a + b * c)
	print("other stuf...")
	print(kwargs)

data = dict(a=1,b=2,c=3,d=45,name="Tony",age=4.5)

add_and_multiply_numbers(**data , cat = "blue", eyes="black")   
		# 7
		# other stuf...
		# {'d': 45, 'name': 'Tony', 'age': 4.5,'cat': 'blue', 'eyes': 'black'}