import sys

import pygame
from card import *
import json
from constants import WHITE

FPS = 60
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
with open('config/cards/card1.json', 'r', encoding='utf-8') as fh:
    c1=create_card((0,0),500,json.load(fh))
screen.fill(WHITE)
c1.blit_me(screen)
pygame.display.update()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pygame.quit()
            sys.exit()
    pygame.display.update()
