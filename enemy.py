import os
import random

import pygame

from animation import Animation
from const.animation import APPEAR
from const.color import RED
from const.enemy import MAX_HP_BAR, X_BAR, Y_BAR, H_BAR
from unit import Unit


class Enemy(Unit):
    """Base class for all enemies."""

    def __init__(self, config, animations):
        """
        :param dict config:
        :param list animations:
        :rtype: Enemy
        """
        Unit.__init__(self, config, animations, state=APPEAR)
        self._power = config['power']
        bar_path = os.path.join('pictures', 'manabar.png')
        self._bar = pygame.image.load(bar_path).convert_alpha()
        self._bar_rect = self._bar.get_rect(center=self._rect.center)
        # self.actions = actions

    def blit_me(self, surface):
        Unit.blit_me(self, surface)
        self._bar_rect.y = self._rect.y - 25
        pygame.draw.rect(surface, RED,
                         (self._bar_rect.x + X_BAR, self._bar_rect.y + Y_BAR,
                          int(MAX_HP_BAR * (float(self._hp / self._max_hp))),
                          H_BAR))
        surface.blit(self._bar, self._bar_rect)

    def take_damage(self, damage):
        Unit.take_damage(self, damage)

    def attack(self, hero):
        hero.take_damage(random.randint(int(0.7 * self._power), self._power))

    def make_action(self, hero):
        # action = random.choice(self.actions)
        # action(self, hero)
        pass

    def click(self, xy):
        if self._rect.collidepoint(xy):
            return True
        else:
            return False

    # Может стоит сделать click через поле вроде is_clicked ?


class Golem(Enemy):
    def __init__(self, config):
        """
        :rtype: Golem
        """
        animations = list()
        animations.append(Animation('pictures/Archive (1)/idle-walk/'))
        animations.append(Animation('pictures/Archive (1)/attack/'))
        animations.append(Animation('pictures/Archive (1)/appear/'))
        animations.append(Animation('pictures/Archive (1)/die/'))
        Enemy.__init__(self, config, animations)


class Vampire(Enemy):
    def __init__(self, config):
        animations = list()
        animations.append(Animation('pictures/Archive/walk-idle/'))
        animations.append(Animation('pictures/Archive/attack/'))
        animations.append(Animation('pictures/Archive/appear/'))
        animations.append(Animation('pictures/Archive/die/'))
        Enemy.__init__(self, config, animations)


def create_enemy(enemy_config):
    if enemy_config["type"] == 'golem':
        return Golem(enemy_config)
    elif enemy_config["type"] == 'vampire':
        return Vampire(enemy_config)
    else:
        raise ValueError('Wrong enemies type.')


"""
pygame.init()
srf = pygame.display.set_mode((1000, 500))
with open('config/cards/fire_card1.json', 'r', encoding='utf-8') as fh:
    card = card.create_card(json.load(fh))
with open('config/enemies/enemy1.json', 'r', encoding='utf-8') as fh:
    enemy_config = json.load(fh)
gol = create_enemy(enemy_config)
with open('config/hero/hero1.json', 'r', encoding='utf-8') as fh:
    player_config = json.load(fh)
p1 = create_hero(player_config)
print(gol.hp)
p1.attack(gol, card)
print(gol.hp)
gol.rect.y = 100
gol.blit_me(srf)
pygame.display.update()
clock = pygame.time.Clock()
param = True
while param:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            param = False
        elif event.type == pygame.KEYDOWN:
            p1.attack(gol, card)
    gol.animated()
    srf.fill((0, 0, 0))
    gol.blit_me(srf)
    pygame.display.update()
    clock.tick(20)
"""
