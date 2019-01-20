from abc import ABCMeta, abstractmethod
from Animation import *
from constans import *
import pygame


class Unit(pygame.sprite.Sprite, metaclass=ABCMeta):
    """Abstract base class for all other units.
    Provides methods for display on screen.
    And methods for interaction between characters.
    """

    def __init__(self, level: int): #""" image: str"""
        """
        Unit`s level should be 1 or more.
        Img_path is absolute or relative path to unit`s sprite picture."""
        assert level >= 1
        self.level = level
        #self.image = pygame.image.load(image).convert_alpha()

    @abstractmethod
    def blit(self, screen):
        """Method for displaying character on screen"""
        pass

    @abstractmethod
    def take_damage(self, damage: int):
        pass

    #@abstractmethod
    #def attack_animation(self):
        #pass


# TODO ?? HP

class Player(Unit):
    def __init__(self): #cards
        self.animations=[]
        self.animations.append(Animation('pictures/Knight/Stand/',9))
        self.animations.append(Animation('pictures/Knight/Attack1H/', 9))
        self.animations.append(Animation('pictures/Knight/Die/', 9))
        self.state =DEFAULT
        self.image = self.animations[self.state].cadr
        self.rect = self.image.get_rect()
        Unit.__init__(self, level=1)
        #self.cards = cards

    def take_damage(self, damage: int):
        pass

    def blit(self,screen):
        screen.blit(self.image,self.rect)


    def animated(self):
        if not self.animations[self.state].update():
            self.state = DEFAULT
        self.image = self.animations[self.state].cadr


"""
pygame.init()
srf = pygame.display.set_mode((1000, 500))
p1=Player()
p1.blit(srf)
pygame.display.update()
clock = pygame.time.Clock()
param = True
while param:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            param = False
    p1.animated()
    srf.fill((0, 0, 0))
    p1.blit(srf)
    pygame.display.update()
    clock.tick(20)
"""