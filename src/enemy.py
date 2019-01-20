import random
from Animation import *
from constans import *
from typing import List, Callable
from unit import Unit, Player
import pygame


class Enemy(Unit):
    def __init__(self, level: int , power: int, hp: int): #"""actions: List[Callable],image: str"""
        self.power=power
        self.max_hp=hp
        self.hp=self.max_hp
        self.bar = pygame.image.load('pictures/manabar.png').convert_alpha()
        Unit.__init__(self, level)
        #self.actions = actions

    def make_action(self, player: Player):
        action = random.choice(self.actions)
        action(self, player)

    def take_damage(self, damage: int):
        pass

class Golem(Enemy):
    def __init__(self,level,power,hp):
        self.animations=[]
        self.animations.append(Animation('pictures/Archive (1)/idle-walk/idle',6))
        self.animations.append(Animation('pictures/Archive (1)/attack/hit', 6))
        self.animations.append(Animation('pictures/Archive (1)/appear/appear', 15))
        self.animations.append(Animation('pictures/Archive (1)/die/die', 7))
        self.state=APPEAR
        self.image=self.animations[APPEAR].cadr
        self.rect=self.image.get_rect()
        Enemy.__init__(self,level,power,hp)
        self.bar_rect = self.bar.get_rect(center=self.rect.center)
    def animated(self):
        if not self.animations[self.state].update():
            self.state=DEFAULT
        self.image=self.animations[self.state].cadr
    def blit(self,srf):
        srf.blit(self.image,self.rect)
        self.bar_rect.y = self.rect.y-25
        pygame.draw.rect(srf, (255, 0, 0), (self.bar_rect.x+X_BAR,self.bar_rect.y+Y_BAR,int(MAX_HP_BAR*(float(self.hp/self.max_hp))),H_BAR))
        srf.blit(self.bar,self.bar_rect)

"""
pygame.init()
srf = pygame.display.set_mode((1000, 500))
gol=Golem(1,1000,1000)
gol.rect.y=100
gol.blit(srf)
pygame.display.update()
clock = pygame.time.Clock()
param = True
while param:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            param = False
    gol.animated()
    srf.fill((0, 0, 0))
    gol.blit(srf)
    pygame.display.update()
    clock.tick(20)
"""


