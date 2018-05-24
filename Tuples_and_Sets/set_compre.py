seta = {x**2 for x in range(10)}
print(seta)

print("dictionary comprehension")
setb = {x:x**2 for x in range(10)}
print(setb)

#set example for duplicated char in a string
setc = {char.upper() for char in 'hello'}
print(setc)


