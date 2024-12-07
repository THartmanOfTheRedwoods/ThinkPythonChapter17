#!/usr/bin/env python3

from hand import Hand

class PokerHand( Hand ):
    """Represents a poker hand."""
    WINDOW_SZ = 5

    def __init__(self, player_name, cards):
        super().__init__(f"{player_name}'s poker hand", cards=cards)
        self.rank_window = []

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

    # Exercise 03
    def has_flush(self):
        return any(x >= 5 for x in self.get_suit_counts().values())

    def process_rank(self, rank):
        self.rank_window.append(rank)
        check = False
        if len(self.rank_window) == PokerHand.WINDOW_SZ:
            check = PokerHand.is_straight(self.rank_window)
            self.rank_window.pop( 0 )
        return check

    @staticmethod
    def is_straight(ranks):
        if len(ranks) < PokerHand.WINDOW_SZ:  # Guard method to speed up processing a bit.
            return False

        prev_rank = ranks[0]
        for i in range(1, len(ranks)):
            if ranks[i] != prev_rank + 1:
                return False
            prev_rank = ranks[i]  # Update the previous rank for each iteration
        return True

    @staticmethod
    def count_aces(counter, for_straight=False):
        # Let's handle the dual ranked Ace
        one_type_aces = counter.get(1, 0)
        aces = one_type_aces + counter.get(14, 0)
        if aces > 0:
            if one_type_aces > 0:
                del counter[1]  # Deleting one type aces so we don't double count
            counter[14] = aces  # No need to return because we modify the object.
            if for_straight:  # For straigts, double counting doesn't matter, and helps for straights including aces.
                counter[1] = aces

    # Exercise 04
    def has_straight(self):
        # First get our rank counts
        counter = self.get_rank_counts()
        PokerHand.count_aces(counter, True)
        ranks = sorted(counter.keys())
        return any(self.process_rank(rank) for rank in ranks)

    # Exercise 05
    # TODO: Make sure this method handles when flush cards are different than straight cards but both still exist.
    def has_straight_flush(self):
        return self.has_flush() and self.has_straight()

    # Exercise 06
    def has_n(self, counter, need):
        PokerHand.count_aces(counter)
        return any(count >= need for count in counter.values() )

    # Exercise 06
    def has_pair(self):
        counter = self.get_rank_counts()
        return self.has_n(counter, 2)

    # Exercise 07
    def has_full_house(self):
        counter = self.get_rank_counts()
        PokerHand.count_aces(counter)
        print(counter)
        triplet = 0
        pair = 0
        for k, v in counter.items():
            if v >= 3:
                triplet += 1
            elif v >= 2:
                pair += 1

        return triplet >= 2 or (triplet >= 1 and pair >= 1)


def main():
    cards = [Card( 1, 3 ),
             Card( 1, 10 ),
             Card( 1, 12 ),
             Card( 2, 13 ),
             Card( 1, 9)]
    my_hand = PokerHand('Trevor', cards)
    print(my_hand)
    print(f'Has flush? {my_hand.has_flush()}')

    cards = [Card( 1, 1 ),
             Card( 2, 10 ),
             Card( 3, 11 ),
             Card( 3, 12 ),
             Card( 1, 13)]
    my_hand = PokerHand('Trevor', cards)
    print(my_hand)
    print(f'Has straight? {my_hand.has_straight()}')

    cards = [Card( 1, 14 ),
             Card( 2, 2 ),
             Card( 3, 3 ),
             Card( 3, 4 ),
             Card( 1, 13)]
    my_hand = PokerHand('Trevor', cards)
    print(my_hand)
    print(f'Has straight? {my_hand.has_straight()}')

    cards = [Card( 1, 2 ),
             Card( 1, 3 ),
             Card( 1, 4 ),
             Card( 1, 5 ),
             Card( 1, 6)]
    my_hand = PokerHand('Trevor', cards)
    print(my_hand)
    print(f'Has flush? {my_hand.has_flush()}')
    print(f'Has straight? {my_hand.has_straight()}')
    print(f'Has straight-flush? {my_hand.has_straight_flush()}')

    cards = [Card( 1, 1 ),
             Card( 2, 3 ),
             Card( 2, 2 ),
             Card( 1, 5 ),
             Card( 3, 14)]
    my_hand = PokerHand('Trevor', cards)
    print(my_hand)
    print(f'Has pair? {my_hand.has_pair()}')

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