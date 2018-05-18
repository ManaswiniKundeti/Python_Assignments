colors = ["purple","red","white","yellow"]

print(colors[0])
print(len(colors))
print(colors[-1])
print(colors)
print("white" in colors)

print(" Using For loop:")
for c in colors :
	print(c)

print(" Using While loop:")
i=0
while i<len(colors):
	print(colors[i])
	i+=1