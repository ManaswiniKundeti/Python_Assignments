import random

random_number = random.randint(1,10)   # numbers 1 - 10
print(random_number)

guess = None

while True:    # while guess != random_number lets user play only 1 game. "while True: " allows the user to play infinite games till he breaks it
	guess = int(input("Pick a number from 1 to 10 : "))
	if guess < random_number:
		print("Too LOW!")
	elif guess > random_number:
		print("Too HIGH!!")
	else:
		print("YOU WON!!!")
		play_again = input("Do you want to play again?? (y/n) ")
		if play_again == "y":
			random_number = random.randint(1,10)
			guess = None
		else:
			print("Thank you for playing!!")
			break



#handle guesses of the user
#	if correct => tell they won
#		else => tell if they are too high or too low

# BONUS - Let user play again (y/n)