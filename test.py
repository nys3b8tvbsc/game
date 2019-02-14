import sys

import pygame

from const.color import WHITE
from deck import Deck
from loading import load_deck, load_battle
from scene import Battle

QUIT = pygame.USEREVENT
ADD_EXP = pygame.USEREVENT + 1

FPS = 60
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
deck = Deck(load_deck('deck1.json'))
print((screen.get_width(), screen.get_height()))
b1 = Battle((screen.get_width(), screen.get_height()), load_battle("battle1.json"))
b1.blit_me(screen)
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
    screen.fill(WHITE)
    b1.update()
    b1.blit_me(screen)
    pygame.display.update()
