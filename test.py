import sys

import pygame

from constants import WHITE

FPS = 60
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill(WHITE)
pygame.display.update()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4 and event.mod == pygame.KMOD_LALT:
                pygame.quit()
                sys.exit()
    pygame.display.update()
