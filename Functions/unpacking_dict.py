def display_names(first,second):
	print(f"{first} says hello to {second}")

names = {"first" : "Manaswini" , "second" : "Kundeti"}

display_names(first = "Sai" , second = "Emani")
#display_names(names)  # nope..error


# ** unpack the dictionary 'names' to separate keyword arguments
display_names(**names) 