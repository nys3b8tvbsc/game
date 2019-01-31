from abc import ABCMeta, abstractmethod

from animation import Animation
from constants import DEFAULT, DEAD
from deck import Deck


class Unit(metaclass=ABCMeta):
    """Abstract base class for all other units.
    Provides methods for display on screen.
    And methods for interaction between characters.
    """

    def __init__(self, config, animations):
        self._config = config
        self._level = config['level']
        self._max_hp = config['max_hp']
        self._hp = config['hp']
        self._animations = animations
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

    @abstractmethod
    def attack(self):
        pass

    @property
    def is_dead(self):
        return self._hp == 0


class Hero(Unit):
    def __init__(self, config, animations):
        self._state = DEFAULT
        Unit.__init__(self, config, animations)
        self.exp = config['exp']
        self._max_mana = config['max_mana']
        self._mana = config['mana']
        self._max_power = config['max_power']
        self._power = config['power']
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

    def attack(self, enemy, card):
        enemy.take_damage(int(self._specifications[card._type] / 100 * card._damage))
        if card.subtype == 'magic':
            self._mana -= card.mana_cost
        elif card.subtype == 'physical':
            self._power -= card.energy


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
