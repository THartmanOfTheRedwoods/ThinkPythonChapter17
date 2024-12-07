#!/usr/bin/env python3

from deck import Deck

class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label='', cards=None):
        super().__init__([] if cards is None else cards)
        self.label = label