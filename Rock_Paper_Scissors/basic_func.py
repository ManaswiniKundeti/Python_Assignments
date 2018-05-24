from random import randint

player_wins = 0
computer_wins = 0 

def display_header():
	print(f" Player Score : {player_wins} Computer Score : {computer_wins} ")
	print("...Rock...")
	print("...Paper...")
	print("...Scissors...")

def pick_computer_move():
	rand_num = randint(0,2)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"	
	print(f"The Computer plays : {computer}" )
	return computer

def calculate_winner(player,computer):
	global player_wins
	global computer_wins
	if player == computer:
		print("its a tie")
	elif player == "rock":
		if computer == "scissors":
			print("player wins!!")
			player_wins += 1
		else:
			print("computer wins!")
			computer_wins += 1
	elif player == "paper":
		if computer == "scissors":
			print("computer wins!!")
			computer_wins += 1
		else:
			print("player wins!")
			player_wins += 1
	elif player == "scissors":
		if computer == "rock":
			print("computer wins!!")
			computer_wins += 1
		else:
			print("player wins!")
			player_wins += 1
	else:
		print("Please enter a valid move")

def start_game(winning_score):
	while player_wins < winning_score and computer_wins < winning_score :
		display_header()

		player = input("(Enter your choice) : ").lower()
		if player == "quit" or player == "q" :
			break
		computer = pick_computer_move()
		calculate_winner(player,computer)

def display_winner():
	if player_wins > computer_wins:
		print("CONGRATS!!! YOU WON!")
	elif player_wins == computer_wins:
		print("IT'S A TIE")
	else:
		print("OH NO!! :( THE COMPUTER WON ")

start_game(3)
display_winner()