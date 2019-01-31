import sys

import pygame

from constants import *
from deck import Deck
from hand import hand_create
from loading import load_deck, load_next_quest,load_hero
from button import Button
from scene import *
QUIT=pygame.USEREVENT
FPS = 60
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
deck = Deck(load_deck('deck1.json'))
print((screen.get_width(), screen.get_height()))
q1=create_scene((screen.get_width(), screen.get_height()),load_next_quest())
screen.fill(WHITE)
q1.blit_me(screen)

pygame.display.update()
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

    screen.fill(WHITE)
    q1.blit_me(screen)
    pygame.display.update()
