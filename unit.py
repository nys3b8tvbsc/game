from abc import ABCMeta, abstractmethod

import pygame

from animation import Animation
from constants import *
from loading import load_deck
from deck import *

class Unit(pygame.sprite.Sprite, metaclass=ABCMeta):
    """Abstract base class for all other units.
    Provides methods for display on screen.
    And methods for interaction between characters.
    """

    def __init__(self, max_hp, level):
        """
        :param int max_hp:
        :param int level: Unit`s level should be 1 or more
        :rtype: Unit
        """
        assert level >= 1
        self.level = level
        self.max_hp = max_hp
        self.hp = self.max_hp
        # self.image = pygame.image.load(image).convert_alpha()

    @abstractmethod
    def blit_me(self, screen):
        pass

    @abstractmethod
    def take_damage(self, damage):
        """
        :param int damage:
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
        self.deck=load_deck(player_config["deck"])
        self.stack=Deck()
        # self.cards = cards

    def take_damage(self, damage):
        self.hp-=damage

    def blit_me(self, screen):
        screen.blit(self.image, self.rect)

    def animated(self):
        if not self.animations[self.state].update():
            self.state = DEFAULT
        self.image = self.animations[self.state].frame
    def attack(self,enemy,card):
        enemy.take_damage(int(self.specifications[card.type]/100*card.damage))
        info=card.get_info()
        if info["subtype"]=='magic':
            self.mana=-card.mana_cost
        elif info["subtype"]=='physycal':
            self.power-=card.energy


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
