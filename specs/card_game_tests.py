import unittest

from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card = Card("Ace", 1)
        self.card1 = Card("Spades", 2)
        self.card2 = Card("Spades", 3)
        self.game = CardGame()
        self.cards = [1,2,3,4]

    def test_check_for_ace(self):
        self.assertEqual(False, self.game.check_for_ace(self.card1))

    def test_highest_card(self):
        self.assertEqual(self.card2, self.game.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 10", self.game.cards_total(self.cards))