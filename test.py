import sys

import pygame

from constants import *
from deck import Deck
from hand import hand_create
from loading import load_deck, load_next_quest
from button import Button
from scene import *
QUIT=pygame.USEREVENT
FPS = 60
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1680, 1050))
deck = Deck(load_deck('deck1.json'))
print((screen.get_width(), screen.get_height()))
q1=create_scene((screen.get_width(), screen.get_height()),load_next_quest())
but1=Button(size=(DEFAULT_W,DEFAULT_H),text='Выход', on_press=QUIT)
#h1 = hand_create(deck, (screen.get_width(), screen.get_height()), 450)
screen.fill(WHITE)
q1.blit_me(screen)
#h1.blit_me(screen)
but1.blit_me(screen)
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
            #h1.click(pygame.mouse.get_pos())
            but1.click(pygame.mouse.get_pos())

    #h1.hover(pygame.mouse.get_pos())
    screen.fill(WHITE)
    q1.blit_me(screen)
    #h1.blit_me(screen)
    but1.blit_me(screen)
    pygame.display.update()
