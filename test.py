import sys

import pygame
from card import *
from hand import *
from  loading import load_card
import json
from constants import WHITE

FPS = 60
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
c1=create_card((0,0),450,load_card('card1.json'))
c2=create_card((0,0),450,load_card('card2.json'))
c3=create_card((0,0),450,load_card('card1.json'))
cards=[]
cards.append(c1)
cards.append(c2)
cards.append(c3)
c1=create_card((0,0),450,load_card('card1.json'))
c2=create_card((0,0),450,load_card('card2.json'))
c3=create_card((0,0),450,load_card('card1.json'))
cards.append(c1)
cards.append(c2)
cards.append(c3)
h1=Hand((screen.get_width(),screen.get_height()),cards)
screen.fill(WHITE)
print(h1.get_size)
h1.blit_me(screen)
pygame.display.update()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            h1.click(pygame.mouse.get_pos())
    h1.hover(pygame.mouse.get_pos())
    screen.fill(WHITE)
    h1.blit_me(screen)
    pygame.display.update()
