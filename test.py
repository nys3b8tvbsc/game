import sys

import pygame
from card import *
from hand import *
from deck import *
from  loading import load_card
import json
from constants import WHITE

FPS = 60
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
with open('config/deck/deck1.json', 'r', encoding='utf-8') as fh:
    d1=json.load(fh)
dec=Deck(d1)
h1=hand_create(dec,(screen.get_width(),screen.get_height()),450)
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
