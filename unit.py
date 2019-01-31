from abc import ABCMeta, abstractmethod

from animation import Animation
from constants import DEFAULT
from deck import Deck


class Unit(metaclass=ABCMeta):
    """Abstract base class for all other units.
    Provides methods for display on screen.
    And methods for interaction between characters.
    """

    def __init__(self, config):
        self._config = config
        self._level = config['level']
        self._max_hp = config['max_hp']
        self._hp = config['hp']
        # self._image = pygame.image.load(config['image']).convert_alpha()
        self._image = None  # TODO
        self._rect = None

    @abstractmethod
    def blit_me(self, surface):
        surface.blit(self._image, self._rect)

    @abstractmethod
    def take_damage(self, damage):
        self._hp = max(0, self._hp - damage)


class Hero(Unit):
    def __init__(self, config, animations):
        Unit.__init__(self, config)
        self._animations = animations
        self._state = DEFAULT
        self._image = self._animations[self._state].frame
        self._rect = self._image.get_rect()
        self._specifications = {}
        self._max_mana = config['max_mana']
        self._mana = config['mana']
        self._max_power = config['max_power']
        self._power = config['power']
        self._specifications['fire'] = config['fire']
        self._specifications['water'] = config['water']
        self._specifications['terra'] = config['terra']
        self._specifications['air'] = config['air']
        self._specifications['sword'] = config['sword']
        self._specifications['archery'] = config['archery']
        self._specifications['fists'] = config['fists']
        self._deck = config["deck"]
        self._stack = Deck()

    def take_damage(self, damage):
        Unit.take_damage(self, damage)

    def blit_me(self, surface):
        Unit.blit_me(self, surface)

    def animated(self):
        self._animations[self._state].update()
        if self._animations[self._stack].is_finished:
            self._state = DEFAULT
        self._image = self._animations[self._state].frame

    def attack(self, enemy, card):
        enemy.take_damage(int(self._specifications[card._type] / 100 * card._damage))
        if card.get_type == 'magic':
            self._mana -= card.mana_cost
        elif card.get_type == 'physical':
            self._power -= card.energy


class Knight(Hero):
    def __init__(self, config):
        animations = list()
        animations.append(Animation('pictures/Knight/Stand/', 9))
        animations.append(Animation('pictures/Knight/Attack1H/', 9))
        animations.append(Animation('pictures/Knight/Die/', 9))
        Hero.__init__(self, config, animations)


class Mage(Hero):
    def __init__(self, config):
        animations = list()
        animations.append(Animation('pictures/IceWizard/Stand/', 9))
        animations.append(Animation('pictures/IceWizard/Cast1H/', 10))
        animations.append(Animation('pictures/IceWizard/Die/', 9))
        Hero.__init__(self, config, animations)


def create_hero(player_config):
    if player_config['type'] == 'warrior':
        return Knight(player_config)
    elif player_config['type'] == 'mage':
        return Mage(player_config)
    else:
        raise ValueError('Wrong hero type.')
