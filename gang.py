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
        if self.__len__()>0:
            for i in range(len(self.enemies)):
                self.enemies[i].blit_me(screen)

    def animated(self):
        if self.__len__()>0:
            for i in range(len(self.enemies)):
                self.enemies[i].animated()

    def dead(self):
        for i in range(self.__len__()):
            if self.enemies[i].is_dead:
                del self.enemies[i]
                return 0


    def __len__(self):
        return len(self.enemies)
