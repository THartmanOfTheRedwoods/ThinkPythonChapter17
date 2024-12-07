#!/usr/bin/env python3

from deck import Deck

class Trick(Deck):
    """Represents a trick in contract bridge."""
    def __init__(self, cards):
        super().__init__(cards)

    def find_trick(self):
        """Loops through the cards in the Trick and returns the index of the card that wins."""
        winner = 0
        led_suit = self.cards[0].suit
        for i in range(1, len(self.cards)):
            if self.cards[i].suit == led_suit and self.cards[i].rank > self.cards[winner].rank:
                winner = i
        return winner

def main():
    cards = [Card( 1, 3 ),
             Card( 1, 10 ),
             Card( 1, 12 ),
             Card( 2, 13 )]
    trick = Trick( cards )
    print( trick )
    print(trick.find_trick())

if __name__ == '__main__':
    from card import Card
    main()