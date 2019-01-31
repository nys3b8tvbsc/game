import sys

import pygame

from constants import *
from deck import Deck
from hand import hand_create
from loading import load_deck, load_next_quest,load_hero
from button import Button
from scene import *
from unit import *

QUIT=pygame.USEREVENT
ADD_EXP=pygame.USEREVENT+1

FPS = 60
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
deck = Deck(load_deck('deck1.json'))
print((screen.get_width(), screen.get_height()))
q1=create_scene((screen.get_width(), screen.get_height()),load_next_quest())
screen.fill(WHITE)
q1.blit_me(screen)
p1=create_hero(load_hero('hero1.json'))
print(p1.new_level)
pygame.display.update()
print(p1.exp)
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            q1.click(pygame.mouse.get_pos())
        elif event.type==ADD_EXP:
            add_exp(p1,q1)
            print(p1._level)

    screen.fill(WHITE)
    q1.blit_me(screen)
    pygame.display.update()

