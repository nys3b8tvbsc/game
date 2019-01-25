from abc import ABCMeta, abstractmethod

import pygame
import json

from animation import Animation
from constants import *


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
    def __init__(self, player_config, animations):  # cards
        Unit.__init__(self, player_config['max_hp'], player_config['level'])
        self.animations = animations
        self.state = DEFAULT
        self.image = self.animations[self.state].frame
        self.rect = self.image.get_rect()
        self.specifications={}
        self.max_mana=player_config['max_mana']
        self.mana=self.max_mana
        self.max_power=player_config['max_power']
        self.power=self.max_power
        self.specifications['fire']=player_config['fire']
        self.specifications['water'] = player_config['water']
        self.specifications['terra'] = player_config['terra']
        self.specifications['air'] = player_config['air']
        self.specifications['sword']=player_config['sword']
        self.specifications['archery']=player_config['archery']
        self.specifications['fists']=player_config['fists']
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
    def __init__(self, player_config):
        animations = list()
        animations.append(Animation('pictures/Knight/Stand/', 9))
        animations.append(Animation('pictures/Knight/Attack1H/', 9))
        animations.append(Animation('pictures/Knight/Die/', 9))
        Hero.__init__(self, player_config, animations)


class Mage(Hero):
    def __init__(self, player_config):
        animations = list()
        animations.append(Animation('pictures/IceWizard/Stand/', 9))
        animations.append(Animation('pictures/IceWizard/Cast1H/', 10))
        animations.append(Animation('pictures/IceWizard/Die/', 9))
        Hero.__init__(self, player_config, animations)
        'TODO'

def Create_Hero(player_config):
    if player_config['type']=='warrior':
        return Knight(player_config)
    elif player_config['type']=='mage':
        return Mage(player_config)


"""
pygame.init()
srf = pygame.display.set_mode((1000, 500))
with open('config/hero/hero1.json', 'r', encoding='utf-8') as fh:
    player_config=json.load(fh)
p1=Create_Hero(player_config)
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
