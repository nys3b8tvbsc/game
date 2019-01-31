import sys

import pygame

from constants import WHITE
from deck import Deck
from hand import hand_create
from loading import load_deck
from button import Button
QUIT=pygame.USEREVENT
FPS = 60
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
deck = Deck(load_deck('deck1.json'))
print(len(deck))
but1=Button(size=(100,100),text='Выход', on_press=QUIT)
h1 = hand_create(deck, (screen.get_width(), screen.get_height()), 450)
screen.fill(WHITE)
h1.blit_me(screen)
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
            h1.click(pygame.mouse.get_pos())
            but1.click(pygame.mouse.get_pos())
    h1.hover(pygame.mouse.get_pos())
    screen.fill(WHITE)
    h1.blit_me(screen)
    but1.blit_me(screen)
    pygame.display.update()
