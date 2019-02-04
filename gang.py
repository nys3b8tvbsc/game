import pygame
from enemy import *
from const.event import ENEMY_TOUCH

class Gang:
    def __init__(self,enemies):
        self.enemies=[]
        for temp in enemies:
            self.enemies.append(temp)
        self.active=None

    def click(self,xy):
        for i in range(len(self.enemies)):
            if self.enemies[i].click(xy):
                self.active=i
                pygame.event.post(pygame.event.Event(ENEMY_TOUCH, {}))

    def blit_me(self,screen):
        for i in range(len(self.enemies)):
            self.enemies[i].blit_me(screen)

    def animated(self):
        for i in range(len(self.enemies)):
            self.enemies[i].animated()