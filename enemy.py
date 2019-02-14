import os
import random

import pygame

from animation import Animation
from const.animation import APPEAR
from const.color import RED
from const.enemy import MAX_HP_BAR, X_BAR, Y_BAR, H_BAR
from const.unit_size import GOLEM, VAMPIRE
from unit import Unit


class Enemy(Unit):
    def __init__(self, config, animations):
        Unit.__init__(self, config, animations, state=APPEAR)
        self._power = config['power']
        bar_path = os.path.join('pictures', 'manabar.png')
        self._bar = pygame.image.load(bar_path).convert_alpha()
        self._bar_rect = self._bar.get_rect(center=self._rect.center)

    def blit_me(self, surface):
        Unit.blit_me(self, surface)
        self._bar_rect.y = self._rect.y - 25
        pygame.draw.rect(surface, RED,
                         (self._bar_rect.x + X_BAR, self._bar_rect.y + Y_BAR,
                          int(MAX_HP_BAR * (self._hp / self._max_hp)),
                          H_BAR))
        surface.blit(self._bar, self._bar_rect)

    def take_damage(self, damage):
        Unit.take_damage(self, damage)

    def attack(self, hero):
        hero.take_damage(random.randint(int(0.7 * self._power), self._power))

    def make_action(self, hero):
        pass

    def click(self, xy):
        if self._rect.collidepoint(xy):
            return True
        else:
            return False


class Golem(Enemy):
    def __init__(self, config, screen_height):
        animations = list()
        animations.append(Animation('pictures/Archive (1)/idle-walk/', GOLEM, screen_height, 4))
        animations.append(Animation('pictures/Archive (1)/attack/', GOLEM, screen_height))
        animations.append(Animation('pictures/Archive (1)/appear/', GOLEM, screen_height, 2))
        animations.append(Animation('pictures/Archive (1)/die/', GOLEM, screen_height, 2))
        Enemy.__init__(self, config, animations)


class Vampire(Enemy):
    def __init__(self, config, screen_height):
        animations = list()
        animations.append(Animation('pictures/Archive/walk-idle/', VAMPIRE, screen_height, 5))
        animations.append(Animation('pictures/Archive/attack/', VAMPIRE, screen_height))
        animations.append(Animation('pictures/Archive/appear/', VAMPIRE, screen_height, 3))
        animations.append(Animation('pictures/Archive/die/', VAMPIRE, screen_height))
        Enemy.__init__(self, config, animations)


def create_enemy(enemy_config, screen_height):
    if enemy_config["type"] == 'golem':
        return Golem(enemy_config, screen_height)
    elif enemy_config["type"] == 'vampire':
        return Vampire(enemy_config, screen_height)
    else:
        raise ValueError('Wrong enemies type.')
