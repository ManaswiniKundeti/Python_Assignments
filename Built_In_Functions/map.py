names = [
	{ 'first' : 'Rusty' , 'last' : 'Emani' },
	{ 'first' : 'Colt' , 'last' : 'Emani' },
	{ 'first' : 'Blue' , 'last' : 'Emani' }
]

first_names = list(map(lambda x : x['first'] , names))

print(first_names)