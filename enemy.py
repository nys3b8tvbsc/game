import os
import random

import pygame

from animation import Animation
from const.animation import APPEAR, ATTACK, MOVE, DEFAULT
from const.color import RED
from const.enemy import MAX_HP_BAR, X_BAR, Y_BAR, H_BAR
from const.event import ENEMY_DAMAGE, TAKE_DAMAGE
from const.unit_size import GOLEM, VAMPIRE, SKELETON, HERO
from unit import Unit


class Enemy(Unit):
    def __init__(self, config, animations, state=APPEAR):
        Unit.__init__(self, config, animations, state)
        self._at_pos = config['at_pos']
        self._power = config['power']
        bar_path = os.path.join('pictures', 'manabar.png')
        self._bar = pygame.image.load(bar_path).convert_alpha()
        self._bar_rect = self._bar.get_rect(center=self._rect.center)
        self._v = config['v']

    def blit_me(self, surface):
        Unit.blit_me(self, surface)
        self._bar_rect.x = self._rect.x + int(0.5 * self._rect.width) - int(0.5 * self._bar_rect.width)
        self._bar_rect.y = self._rect.y - 25
        pygame.draw.rect(surface, RED,
                         (self._bar_rect.x + X_BAR, self._bar_rect.y + Y_BAR,
                          int(MAX_HP_BAR * (self._hp / self._max_hp)),
                          H_BAR))
        surface.blit(self._bar, self._bar_rect)

    def take_damage(self, damage):
        Unit.take_damage(self, damage)
        pygame.event.post(pygame.event.Event(ENEMY_DAMAGE, {}))

    def attack(self, hero):
        self._state = ATTACK
        hero.take_damage(random.randint(int(0.7 * self._power), self._power))
        pygame.event.post(pygame.event.Event(TAKE_DAMAGE, {}))

    def make_action(self, hero):
        pass

    def click(self, xy):
        if self._rect.collidepoint(xy):
            return True
        else:
            return False

    def walking(self, vector):
        if self._state != ATTACK:
            self._rect.x += vector * self._v
            self._state = MOVE


class Golem(Enemy):
    def __init__(self, config, screen_height):
        animations = list()
        animations.append(Animation('pictures/Archive (1)/idle-walk/', GOLEM, screen_height, 4))
        animations.append(Animation('pictures/Archive (1)/attack/', GOLEM, screen_height, 3))
        animations.append(Animation('pictures/Archive (1)/die/', GOLEM, screen_height, 2))
        animations.append(Animation('pictures/Archive (1)/idle-walk/', GOLEM, screen_height, 4))
        animations.append(Animation('pictures/Archive (1)/appear/', GOLEM, screen_height, 2))
        Enemy.__init__(self, config, animations)


class Vampire(Enemy):
    def __init__(self, config, screen_height):
        animations = list()
        animations.append(Animation('pictures/Archive/walk-idle/', VAMPIRE, screen_height, 5))
        animations.append(Animation('pictures/Archive/attack/', VAMPIRE, screen_height))
        animations.append(Animation('pictures/Archive/die/', VAMPIRE, screen_height))
        animations.append(Animation('pictures/Archive/walk-idle/', VAMPIRE, screen_height, 5))
        animations.append(Animation('pictures/Archive/appear/', VAMPIRE, screen_height, 3))
        Enemy.__init__(self, config, animations)


class Skeleton(Enemy):
    def __init__(self, config, screen_height):
        animations = list()
        animations.append(
            Animation('pictures/Knight Skeleton/Knight Skeleton/Idle/Separate sp', SKELETON, screen_height, 5))
        animations.append(
            Animation('pictures/Knight Skeleton/Knight Skeleton/Attack 1/Separated sp/', SKELETON, screen_height, 3))
        animations.append(
            Animation('pictures/Knight Skeleton/Knight Skeleton/Dead/Separate sp/', SKELETON, screen_height, 3))
        animations.append(
            Animation('pictures/Knight Skeleton/Knight Skeleton/Walk/Separate sp/', SKELETON, screen_height, 5))
        Enemy.__init__(self, config, animations, DEFAULT)


class Barbarian1(Enemy):
    def __init__(self, config, screen_height):
        animations = list()
        animations.append(Animation('pictures/Viking1/Stand1/', HERO, screen_height, 5))
        animations.append(Animation('pictures/Viking1/Attack', HERO, screen_height, 3))
        animations.append(Animation('pictures/Viking1/Dead', HERO, screen_height, 3))
        animations.append(Animation('pictures/Viking1/Walking1', HERO, screen_height, 5))
        Enemy.__init__(self, config, animations, DEFAULT)


def create_enemy(enemy_config, screen_height):
    if enemy_config["type"] == 'golem':
        return Golem(enemy_config, screen_height)
    elif enemy_config["type"] == 'vampire':
        return Vampire(enemy_config, screen_height)
    elif enemy_config["type"] == 'skeleton':
        return Skeleton(enemy_config, screen_height)
    elif enemy_config["type"] == 'barbarian1':
        return Barbarian1(enemy_config, screen_height)
    else:
        raise ValueError('Wrong enemies type.')
