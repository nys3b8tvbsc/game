from abc import ABCMeta, abstractmethod

import pygame

from animation import Animation
from card import card_height
from const.animation import DEFAULT, DEAD
from const.event import GAME_OVER
from const.unit_size import HERO
from deck import Deck
from hand import hand_create



class Unit(metaclass=ABCMeta):
    def __init__(self, config, animations, state):
        self._config = config
        self._level = config['level']
        self._max_hp = config['max_hp']
        self._hp = config['hp']
        self._animations = animations
        self._state = state
        self._image = self._animations[self._state].frame
        self._rect = self._image.get_rect()

    @property
    def state(self):
        return self._state

    @abstractmethod
    def blit_me(self, surface):
        surface.blit(self._image, self._rect)

    def animated(self):
        self._animations[self._state].update()
        if self._animations[self._state].is_finished:
            self._state = DEFAULT
        self._image = self._animations[self._state].frame

    @abstractmethod
    def take_damage(self, damage):
        self._hp = max(0, self._hp - damage)
        if self.is_dead:
            self._state = DEAD

    @property
    def is_dead(self):
        return self._hp <= 0

    def move_to(self, x, y):
        self._rect.x = x
        self._rect.y = y


class Hero(Unit):
    def __init__(self, config, animations, screen_size):
        Unit.__init__(self, config, animations, state=DEFAULT)
        self._exp = config['_exp']
        self._max_mana = config['max_mana']
        self._mana = config['mana']
        self._max_power = config['max_energy']
        self._power = config['energy']
        self._points = config['points']
        self._specifications = config['specifications']
        self._deck = Deck(config["deck"])
        self._hand = hand_create(self._deck, screen_size, card_height(screen_size[1]))
        self._stack = Deck()

    def blit_me(self, surface):
        Unit.blit_me(self, surface)
        self._hand.blit_me(surface)

    def take_damage(self, damage):
        Unit.take_damage(self, damage)
        if self.is_dead:
            self._state = DEAD
            pygame.event.post(pygame.event.Event(GAME_OVER, {}))

    def attack(self, enemy, card):
        if card.subtype == 'magic' and self._mana - card.cost >= 0:
            self._mana -= card.cost
            enemy.take_damage(int(self._specifications[card.type] / 100 * card.damage))
            self._hand.delete_active()
            return True
        elif card.subtype == 'physical' and self._power - card.cost >= 0:
            self._power -= card.cost
            enemy.take_damage(int(self._specifications[card.type] / 100 * card.damage))
            self._hand.delete_active()
            return True
        return False

    def level_up(self):
        self._level += 1
        self._points += 5

    @property
    def new_level(self):
        exp = 0
        for i in range(1, self._level + 2):
            exp += 100 + (i - 1) * 50
        if self._exp >= exp:
            return True
        else:
            return False


class Knight(Hero):
    def __init__(self, config, screen_size):
        animations = list()
        animations.append(Animation('pictures/Knight/Stand/', HERO, screen_size[0], 4))
        animations.append(Animation('pictures/Knight/Attack1H/', HERO, screen_size[0], 4))
        animations.append(Animation('pictures/Knight/Die/', HERO, screen_size[0], 4))
        Hero.__init__(self, config, animations, screen_size)


class Mage(Hero):
    def __init__(self, config, screen_size):
        animations = list()
        animations.append(Animation('pictures/IceWizard/Stand/', HERO, screen_size[0], 4))
        animations.append(Animation('pictures/IceWizard/Cast1H/', HERO, screen_size[0], 4))
        animations.append(Animation('pictures/IceWizard/Die/', HERO, screen_size[0], 4))
        Hero.__init__(self, config, animations, screen_size)


def create_hero(player_config, screen_height):
    if player_config['type'] == 'warrior':
        return Knight(player_config, screen_height)
    elif player_config['type'] == 'mage':
        return Mage(player_config, screen_height)
    else:
        raise ValueError('Wrong hero type.')
