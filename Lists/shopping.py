# to do : shopping cart using lists
# add items from command line
# display list of all items at the end

cart = []
print("WELCOME TO YOUR SHOPPING CART")
item = input("Add something to the cart? Press q to quit : ")
while True:
	if item == "q" :
		break
	else:
		cart.append(item)
		item = input("Add something to the cart? Press q to quit : ")
if len(cart) != 0:
	print("YOUR FINAL GROCERY LIST :")
	[print("- "+val) for val in cart]
