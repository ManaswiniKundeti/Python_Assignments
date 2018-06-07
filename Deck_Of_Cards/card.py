class Card:
	valid_suits = ["Hearts", "Diamonds", "Clubs","Spades"]
	valid_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
	def __init__(self,value,suit):
		if suit not in Card.valid_suits:
			raise ValueError(f"{suit} is not a valid Suit")
		elif value not in Card.valid_values:
			raise ValueError(f"{value} is not a valid Value")
		self.value = value
		self.suit = suit

	def __repr__(self):
		return f"{self.value} of {self.suit}"

# card1 = Card("Clubs","A")
# print(card1)