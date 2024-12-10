#!/usr/bin/env python3
from collections import defaultdict

from card import Card
from hand import Hand
from copy import copy

class PokerHand( Hand ):

    def __init__(self, player_name=None, cards=None):
        super().__init__(f"{player_name}'s poker hand", cards=cards)

    def get_suit_counts(self):
        counter = {}
        for card in self.cards:
            key = card.suit
            counter[key] = counter.get( key, 0 ) + 1
        return counter

    def get_rank_counts(self):
        counter = {}
        for card in self.cards:
            key = card.rank
            counter[key] = counter.get( key, 0 ) + 1
        return counter

    def has_flush(self):
        return any(count >= 5 for count in self.get_suit_counts().values())

    def has_straight(self, n=5):
        """Checks whether this hand has a straight."""
        counter = self.get_rank_counts()
        aces = counter.get(1, 0) + counter.get(14, 0)
        counter[1] = aces
        counter[14] = aces

        in_a_row = 0
        for i in range(1, 15):
            if counter.get(i, 0):
                in_a_row += 1
                if in_a_row == n:
                    return True
            else:
                in_a_row = 0
        return False

    def partition(self):
        """Make a list of four hands, each containing only one suit."""
        hands = []
        for i in range( 4 ):
            hands.append( PokerHand(self.label) )

        for card in self.cards:
            hands[card.suit].put_card( card )

        return hands

    def partition(self):
        """Make 4 hands, 1 for each suit. Loop over cards and put them in suit hands.
           If any suit hand has a straight after partitioning, it will be a straight flush"""
        hands = defaultdict(PokerHand)

        for card in self.cards:
            hands[card.suit].put_card( card )

        return hands

    def has_straight_flush(self):
        """Check whether a hand has a straight flush, by checking suit partitioned hands for a straight."""
        return any(hand.has_straight() for suit, hand in self.partition().items())

    def check_sets(self, *need_list):
        counts = self.get_rank_counts()
        set_list = sorted( counts.values(), reverse=True )

        for need, have in zip( need_list, set_list ):
            if need > have:
                return False
        return True

    def has_pair(self):
        return self.check_sets( 2 )

    def has_full_house(self):
        return self.check_sets( 3, 2 )


def main():
    print("-"*80)
    cards = [Card( 1, 3 ),
             Card( 2, 10 ),
             Card( 1, 10 ),
             Card( 1, 12 ),
             Card( 1, 13 ),
             Card( 1, 9)]
    my_hand = PokerHand('Trevor', cards)
    print(my_hand)
    print(f'Has flush? {my_hand.has_flush()}')

    print("-"*80)
    cards = [Card( 1, 1 ),
             Card( 2, 10 ),
             Card( 3, 11 ),
             Card( 3, 12 ),
             Card( 1, 13)]
    my_hand = PokerHand('Trevor', cards)
    print(my_hand)
    print(f'Has straight? {my_hand.has_straight()}')

    print("-"*80)
    cards = [Card( 1, 14 ),
             Card( 2, 2 ),
             Card( 3, 3 ),
             Card( 3, 4 ),
             Card( 1, 5)]
    my_hand = PokerHand('Trevor', cards)
    print(my_hand)
    print(f'Has straight? {my_hand.has_straight()}')

    print("-"*80)
    cards = [Card( 1, 2 ),
             Card( 3, 3 ),
             Card( 1, 3 ),
             Card( 1, 4 ),
             Card( 2, 4 ),
             Card( 1, 5 ),
             Card( 1, 14)]
    my_hand = PokerHand('Trevor', cards)
    print(my_hand)
    print(f'Has flush? {my_hand.has_flush()}')
    print(f'Has straight? {my_hand.has_straight()}')
    print(f'Has straight-flush? {my_hand.has_straight_flush()}')

    print("-"*80)
    cards = [Card( 1, 1 ),
             Card( 2, 3 ),
             Card( 2, 2 ),
             Card( 1, 5 ),
             Card( 3, 14)]
    my_hand = PokerHand('Trevor', cards)
    print(my_hand)
    print(f'Has pair? {my_hand.has_pair()}')

    print("-"*80)
    cards = [Card( 1, 1 ),
             Card( 2, 10 ),
             Card( 3, 1 ),
             Card( 0, 1 ),
             Card( 3, 10)]
    my_hand = PokerHand('Trevor', cards)
    print(my_hand)
    print(f'Has full house? {my_hand.has_full_house()}')


if __name__ == '__main__':
    from card import Card
    main()