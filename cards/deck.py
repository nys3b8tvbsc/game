import random

from cards.card import create_card
from loading import load_card


class Deck:
    def __init__(self, deck_config=()):
        self._cards = [load_card(card) for card in deck_config]

    def __len__(self):
        return len(self._cards)

    def return_cards(self, number, card_height, hero, effects):
        number = min(number, len(self))
        random.shuffle(self._cards)
        cards = []
        for i in range(number):
            card_config = self._cards.pop()
            cards.append(create_card(card_height, card_config, hero, effects))
        return cards

    def append(self, config):
        self._cards.append(load_card(config))
