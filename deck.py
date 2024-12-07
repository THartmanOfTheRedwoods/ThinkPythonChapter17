#!/usr/bin/env python3

import random
from card import Card

class Deck:

    def __init__(self, cards):
        self.cards = cards

    @staticmethod
    def make_cards():
        cards = []
        for suit in range( 4 ):
            for rank in range( 2, 15 ):
                card = Card( suit, rank )
                cards.append( card )
        return cards

    def move_cards(self, other, num):
        for i in range( num ):
            card = self.take_card()
            other.put_card( card )

    def take_card(self):
        return self.cards.pop()

    def put_card(self, card):
        self.cards.append( card )

    def shuffle(self):
        random.shuffle( self.cards )

    def sort(self):
        self.cards.sort()

    def __str__(self):
        res = []
        for card in self.cards:
            res.append( str( card ) )
        return '\n'.join( res )
