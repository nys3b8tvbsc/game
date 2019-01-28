import sys

import pygame
from card import *
from hand import *
import json
from constants import WHITE

FPS = 60
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
with open('config/cards/card1.json', 'r', encoding='utf-8') as fh:
    c1=create_card((0,0),500,json.load(fh))
with open('config/cards/card2.json', 'r', encoding='utf-8') as fh:
    c2=create_card((0,0),500,json.load(fh))
with open('config/cards/card1.json', 'r', encoding='utf-8') as fh:
    c3=create_card((0,0),500,json.load(fh))
cards=[]
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
