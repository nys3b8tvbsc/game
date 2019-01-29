import pygame
import random
from loading import load_card
from card import create_card
import json

class Deck:
    def __init__(self,deck_config=[]):
        self.cards=[]
        for i in deck_config:
            self.cards.append(load_card(i))
    @property
    def get_size(self):
        return len(self.cards)
    def return_cards(self,n,heigt):
        cards=[]
        if n<self.get_size:
            N=n
        else:
            N=self.get_size
        for i in range(N):
            k=random.randint(0,self.get_size-1)
            cards.append(create_card(pos=(0,0),height=heigt,config=self.cards[k]))
            del self.cards[k]
        return cards
    def appcard(self,config):
        self.cards.append(config)

"""
pygame.init()
pygame.display.set_mode((100,100))
with open('config/deck/deck1.json', 'r', encoding='utf-8') as fh:
    d1=json.load(fh)
dec=Deck(d1)
print(dec.get_size)
dec.return_cards(6,100)
print(dec.get_size)
"""