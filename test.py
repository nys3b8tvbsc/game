import sys
import os
import pygame
from button import Button
from label import Label
from constants import WHITE,CYAN

FPS = 60
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 1000))
but=Button(('Выход',),(190,74))
screen.fill(WHITE)
but.blit_me(screen)
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
