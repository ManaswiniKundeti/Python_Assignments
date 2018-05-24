from random import random #random is a module that comes with python

# def flip_coin():
# 	#generate random number between 0-1
# 	r = random()
# 	if r > 0.5:
# 		return "Heads"
# 	else:
# 		return "Tails"
# print(flip_coin())

#shortened version of abv prog

def flip_coin():
	if random() > 0.5:
		return "HEADS"
	else:
		return "TAILS"
print(flip_coin())