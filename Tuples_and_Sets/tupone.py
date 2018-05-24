#creating tuple using tuple function
asd = tuple(1,2,3)
print(asd)

#tuples commonly used for unchanging data
months = ('Jan','Feb','March','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
print(months[1])

#o.p: Feb


#using "for" lopp for iteration : months in order
print("using FOR loop for iteration : months in order")
for mo in months:
	print(f"month is {mo}")


#using "while" loop for iteration : print in rev order
print("using WHILE loop for iteration : print in rev order")
iter = len(months) - 1
while iter >= 0:
	print(months[iter])
	iter -= 1


#tuples can be used as keys in dictionaries
locations = {
	(35.6895,39.4567) : "Tokyo Office",
	(75.2345,78.4534) : "New York Office",
	(37.2234,122.5674) : "San Francisco Office"
}
print(locations[(75.2345,78.4534)])

#o.p : New York Office



#some dictionary methods like .items() return tuples
cat = {"name":"ammi","age":3.7,"favourite_toy":"chapstick"}
print(cat.items())

# o.p: dict_items([('name', 'ammi'), ('age', 3.7), ('favourite_toy', 'chapstick')])
                        #tuple            #tuple               #tuple