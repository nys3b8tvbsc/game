from abc import ABCMeta, abstractmethod

import pygame

from animation import Animation
from card import Card
from const.animation import DEFAULT, DEAD, ATTACK
from const.event import GAME_OVER
from const.hand import MAX_HAND
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

    @property
    def rect(self):
        return self._rect


class Hero(Unit):
    def __init__(self, config, animations, screen_size):
        Unit.__init__(self, config, animations, state=DEFAULT)
        self._exp = config['_exp']
        self._max_mana = config['max_mana']
        self._max_hp = config['max_hp']
        self._mana = config['mana']
        self._max_power = config['max_energy']
        self._power = config['energy']
        self._points = config['points']
        self._specifications = config['specifications']
        self._regen = config["regen"]
        self._deck = Deck(config["deck"])
        self._card_height = Card.card_height(screen_size[1])
        self._hand = hand_create(self._deck, screen_size, self._card_height, self._specifications)
        self._stack = Deck()
        self._effects = list()

    def blit_me(self, surface):
        Unit.blit_me(self, surface)
        self._hand.blit_me(surface)

    def take_damage(self, damage):
        Unit.take_damage(self, damage)
        self._config['hp'] = self._hp
        if self.is_dead:
            self._state = DEAD
            pygame.event.post(pygame.event.Event(GAME_OVER, {}))

    def update_hand(self):
        self._hand.append(
            self._deck.return_cards(MAX_HAND - len(self._hand), self._card_height, self._specifications, self._effects))
        if len(self._deck) == 0:
            self._deck = self._stack
            self._stack = Deck()

    def update_effect(self):
        for effect in self._effects:
            effect.update()
            if effect._round == 0:
                self._hand.off_effect(effect)

        for effect in self._effects.copy():
            if effect._round == 0:
                self._effects.remove(effect)

    def regen(self):
        self._hp += self._regen['hp']
        if self._hp > self._max_hp:
            self._hp = self._max_hp
        self._mana += self._regen['mana']
        if self._mana > self._max_mana:
            self._mana = self._max_mana
        self._power += self._regen['energy']
        if self._power > self._max_power:
            self._power = self._max_power

        self._config['hp'] = self._hp
        self._config['mana'] = self._mana
        self._config['energy'] = self._power

    def attack(self, enemy, card):
        if card.subtype == 'magic' and self._mana - card.cost >= 0:
            self._mana -= card.cost
            self._config['mana'] = self._mana
            enemy.take_damage(card.damage)
            self._state = ATTACK
            self._stack.append(card.conf_name)
            self._hand.delete_active()
            return True
        elif card.subtype == 'physical' and self._power - card.cost >= 0:
            self._power -= card.cost
            self._config['energy'] = self._power
            enemy.take_damage(card.damage)
            self._state = ATTACK
            self._stack.append(card.conf_name)
            self._hand.delete_active()
            return True
        return False

    def action_card(self, card):
        card.action(self)
        self._stack.append(card.conf_name)
        self._hand.delete_active()

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

    def get_info(self):
        return self._config

    @property
    def hand(self):
        return self._hand


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
