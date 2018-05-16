print("...Rock...")
print("...Paper...")
print("...Scissors...")

player1 = input("Player1, make your move : ")
print("**** NO CHEATING***\n" * 30)
player2 = input("Player2, make your move : ")

if player1 == player2:
	print("its a tie")
elif player1 == "rock":
	if player2 == "scissors":
		print("player1 wins!!")
	elif player2 == "paper":
		print("player2 wins!")
elif player1 == "paper":
	if player2 == "scissors":
		print("player2 wins!!")
	elif player2 == "rock":
		print("player1 wins!")
elif player1 == "scissors":
	if player2 == "rock":
		print("player2 wins!!")
	elif player2 == "paper":
		print("player1 wins!")
else:
	print("Something went wrong :( ")






# if player1 == "rock" and player2 == "scissors":
# 	print("player1 wins!!")
# elif player1 == "rock" and player2 == "paper":
# 	print("player2 wins!!")
# elif player1 == "paper" and player2 == "rock":
# 	print("player1 wins!!")
# elif player1 == "paper" and player2 == "scissors":
# 	print("player2 wins!!")
# elif player1 == "scissors" and player2 == "rock":
# 	print("player2 wins!")
# elif player1 == "scissors" and player2 == "paper":
# 	print("player1 wins!!")
# elif player1 == player2:
# 	print("Its a tie")
# else:
# 	print("Something went wrong :( ")