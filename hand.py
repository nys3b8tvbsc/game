import pygame
import json
from card import *

class Hand:
    def __init__(self,screen_size,cards):
        self.cards=cards
        self._width=screen_size[0]
        self._y=screen_size[1]-cards[0]._rect.height
        self._card_width=cards[0]._rect.width
        self.positioning()
    def positioning(self):
        width=int(self._width/len(self.cards))
        start_position=int(width/2-self._card_width/2)
        if start_position<0:
            start_position=0
        for i in range(len(self.cards)):
            self.cards[i]._rect.x=start_position+i*width
            self.cards[i]._rect.y=self._y
    def blit_me(self,screen):
        for i in range(len(self.cards)):
            self.cards[i].blit_me(screen)
    def app_card(self,config):
        self.cards.append(create_card((0,0),self.cards[0]._rect.height,config))
        self.positioning()
    def hover(self,xy):
        for i in range(len(self.cards)):
            if self.cards[i]._rect.collidepoint(xy):
                self.cards[i]._hover=True
            else:
                self.cards[i]._hover=False



pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 1000))
cards=[]
with open('config/cards/card1.json', 'r', encoding='utf-8') as fh:
    c1=create_card((0,0),200,json.load(fh))
with open('config/cards/card2.json', 'r', encoding='utf-8') as fh:
    c2=create_card((0,0),200,json.load(fh))
with open('config/cards/card1.json', 'r', encoding='utf-8') as fh:
    c3=create_card((0,0),200,json.load(fh))
cards.append(c1)
cards.append(c2)
cards.append(c3)
h1=Hand((1000,1000),cards)
screen.fill(WHITE)
h1.blit_me(screen)
pygame.display.update()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            with open('config/cards/card1.json', 'r', encoding='utf-8') as fh:
                h1.app_card(json.load(fh))
    h1.hover(pygame.mouse.get_pos())
    screen.fill(WHITE)
    h1.blit_me(screen)
    pygame.display.update()
