from card import card
from deck import deck
import unittest

class CardTests(unittest.TestCase):
	def setUp(self):
		self.card = Card("Hearts","A")

	def test_init(self):
		"""cards should have a suit and a value"""
		self.assertEqual(self.card.suit,"Hearts")
		self.assertEqual(self.card.value,"A")

	def test_repr(self):
	"""repr should return a string of the form 'VALUE' of suit"""
	self.assertEqual(repr(self.card),"A of Hearts")


class DeckTests(unittest.TestCase):
	def setUp(self):
		self.deck = Deck()

	def test_init(self):
		"""decks should have a cards attribute, which is a list """
		self.assertTrue(isinstance(self.deck.cards,list))
		self.assertEqual(len(self.deck.cards),52)

	def test_repr(self):
		""" repr should return a string of the form 'Deck of COUNT' """
		self.assertEqual(repr(self.deck), "Deck of 52 cards.")

	def test_count(self):
		"""count should return a count of the number of cards in  """
		self.assertEqual(self.deck.count(), 52)
		self.deck.cards.pop()
		self.assertEqual(self.deck.count(), 51)

	def test_deal_sufficient_cards(self):
		"""deal should deal the number of cards specified, if  """
		cards =  self.deck._deal(10)
		self.assertEqual(len(cards),10)
		self.assertEqual(self.deck.count(),42)

	def test_deal_insufficient_cards(self):
		"""deal should deal the number of cards left in  """
		cards =  self.deck._deal(100)
		self.assertEqual(len(cards),52)
		self.assertEqual(self.deck.count(), 0)

	def test_deal_no_cards(self):
		"""deal should throw a ValueError if the deck is """
		self.deck._deal(self.deck.count())
		with self.assertRaise(ValueError):
			self.deck._deal(1)

	def test_deal_card(self):
		"""deal should deal a single card from the deck """
		card = self.deck.cards[-1]
		dealt_card = self.deck.deal_card()
		self.assertEqual(card._dealt.card)0


		
