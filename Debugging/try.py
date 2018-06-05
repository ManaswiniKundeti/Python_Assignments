#basic syntax
# try:
# except :

# try:
# 	foobar
# except:
# 	print("PROBLEM!!")
# print("After the try block!!")


def get(d,key):
	try:
		return d[key]
	except KeyError : 
		return None

d = {"name" : "Manaswini"}

print(get(d,"name"))
print(get(d,"city"))