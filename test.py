import sys

import pygame
from button import Button
from label import Label
from constants import WHITE,CYAN

FPS = 60
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
but=Button(('Выход',' '),(190,74))
l1=Label(('Выход','вникуда'),(160,48),(15,13))
screen.fill(WHITE)
but.blit_me(screen)
l1.blit_me(screen)
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
