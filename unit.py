import pygame
from abc import ABCMeta, abstractmethod

from animation import Animation
from const.animation import DEFAULT, DEAD
from const.event import GAME_OVER
from deck import Deck


class Unit(metaclass=ABCMeta):
    """Abstract base class for all other units.
    Provides methods for display on screen.
    And methods for interaction between characters.
    """

    def __init__(self, config, animations, state):
        self._config = config
        self._level = config['level']
        self._max_hp = config['max_hp']
        self._hp = config['hp']
        self._animations = animations
        self._state = state
        self._image = self._animations[self._state].frame
        self._rect = self._image.get_rect()

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


class Hero(Unit):
    def __init__(self, config, animations):
        Unit.__init__(self, config, animations, state=DEFAULT)
        self.exp = config['exp']
        self._max_mana = config['max_mana']
        self._mana = config['mana']
        self._max_power = config['max_power']
        self._power = config['power']
        self._points = config['points']
        self._specifications = dict()
        self._specifications['fire'] = config['fire']
        self._specifications['water'] = config['water']
        self._specifications['terra'] = config['terra']
        self._specifications['air'] = config['air']
        self._specifications['sword'] = config['sword']
        self._specifications['archery'] = config['archery']
        self._specifications['fists'] = config['fists']
        self._deck = config["deck"]
        self._stack = Deck()

    def blit_me(self, surface):
        Unit.blit_me(self, surface)

    def take_damage(self, damage):
        Unit.take_damage(self, damage)
        if self.is_dead:
            self._state = DEAD
            pygame.event.post(pygame.event.Event(GAME_OVER,{}))

    def attack(self, enemy, card):
        if card.subtype == 'magic' and self._mana-card._mana_cost>=0:
            self._mana -= card._mana_cost
            enemy.take_damage(int(self._specifications[card._type] / 100 * card._damage))
            return True
        elif card.subtype == 'physical' and self._power-card._energy>=0:
            self._power -= card._energy
            enemy.take_damage(int(self._specifications[card._type] / 100 * card._damage))
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
        if self.exp >= exp:
            return True
        else:
            return False


class Knight(Hero):
    def __init__(self, config):
        animations = list()
        animations.append(Animation('pictures/Knight/Stand/'))
        animations.append(Animation('pictures/Knight/Attack1H/'))
        animations.append(Animation('pictures/Knight/Die/'))
        Hero.__init__(self, config, animations)


class Mage(Hero):
    def __init__(self, config):
        animations = list()
        animations.append(Animation('pictures/IceWizard/Stand/'))
        animations.append(Animation('pictures/IceWizard/Cast1H/'))
        animations.append(Animation('pictures/IceWizard/Die/'))
        Hero.__init__(self, config, animations)


def create_hero(player_config):
    if player_config['type'] == 'warrior':
        return Knight(player_config)
    elif player_config['type'] == 'mage':
        return Mage(player_config)
    else:
        raise ValueError('Wrong hero type.')
