from abc import ABCMeta, abstractmethod

import pygame

from animation import Animation
from constans import *


class Unit(pygame.sprite.Sprite, metaclass=ABCMeta):
    """Abstract base class for all other units.
    Provides methods for display on screen.
    And methods for interaction between characters.
    """

    def __init__(self, max_hp, level):
        """
        Img_path is absolute or relative path to unit`s sprite picture.

        :param level: int. Unit`s level should be 1 or more
        :param max_hp: int
        :return: Unit object
        """
        assert level >= 1
        self.level = level
        self.max_hp = max_hp
        self.hp = self.max_hp
        # self.image = pygame.image.load(image).convert_alpha()

    @abstractmethod
    def blit_me(self, screen):
        """Method for displaying character on screen.

        :param screen: pygame.sprite.Sprite
        """
        pass

    @abstractmethod
    def take_damage(self, damage):
        """
        :param damage: int
        """
        pass

    # @abstractmethod
    # def attack_animation(self):
    # pass


class Hero(Unit):
    def __init__(self, max_hp, animations, level=1):  # cards
        Unit.__init__(self, max_hp, level)
        self.animations = animations
        self.state = DEFAULT
        self.image = self.animations[self.state].frame
        self.rect = self.image.get_rect()
        # self.cards = cards

    def take_damage(self, damage):
        pass

    def blit_me(self, screen):
        screen.blit(self.image, self.rect)

    def animated(self):
        if not self.animations[self.state].update():
            self.state = DEFAULT
        self.image = self.animations[self.state].frame


class Knight(Hero):
    def __init__(self, max_hp, level=1):
        animations = list()
        animations.append(Animation('pictures/Knight/Stand/', 9))
        animations.append(Animation('pictures/Knight/Attack1H/', 9))
        animations.append(Animation('pictures/Knight/Die/', 9))
        Hero.__init__(self, max_hp, animations,level)


class Mage(Hero):
    def __init__(self, max_hp, level=1):
        animations = list()
        animations.append(Animation('pictures/IceWizard/Stand/', 9))
        animations.append(Animation('pictures/IceWizard/Cast1H/', 10))
        animations.append(Animation('pictures/IceWizard/Die/', 9))
        Hero.__init__(self, max_hp, animations,level)
        'TODO'

"""
pygame.init()
srf = pygame.display.set_mode((1000, 500))
p1=Mage(10000,1)
p1.blit_me(srf)
pygame.display.update()
clock = pygame.time.Clock()
param = True
while param:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            param = False
    p1.animated()
    srf.fill((0, 0, 0))
    p1.blit_me(srf)
    pygame.display.update()
    clock.tick(20)
"""
