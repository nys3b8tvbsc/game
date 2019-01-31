import random

import pygame

from animation import Animation
from constants import DEFAULT, APPEAR, DEAD
from constants import MAX_HP_BAR, X_BAR, Y_BAR, H_BAR
from constants import RED
from unit import Unit


class Enemy(Unit):
    """Base class for all enemies.
    TODO implement base class methods"""

    def __init__(self, config, animations):
        """
        :rtype: Enemy
        """
        Unit.__init__(self, config)
        self._power = config['power']
        self._animations = animations
        self._state = APPEAR
        self._image = self._animations[self._state].frame
        self._rect = self._image.get_rect()
        self._bar = pygame.image.load('pictures/manabar.png').convert_alpha()
        self._bar_rect = self._bar.get_rect(center=self._rect.center)
        # self.actions = actions

    def animated(self):
        self._animations[self._state].update()
        if self._animations[self._state].is_finished:
            self._state = DEFAULT
        self._image = self._animations[self._state].frame

    def blit_me(self, surface):
        surface.blit(self._image, self._rect)
        self._bar_rect.y = self._rect.y - 25
        pygame.draw.rect(surface, RED,
                         (self._bar_rect.x + X_BAR, self._bar_rect.y + Y_BAR,
                          int(MAX_HP_BAR * (float(self._hp / self._max_hp))),
                          H_BAR))
        surface.blit(self._bar, self._bar_rect)

    def make_action(self, hero):
        # action = random.choice(self.actions)
        # action(self, hero)
        pass

    @property
    def is_dead(self):
        return self._hp == 0

    def take_damage(self, damage):
        """
        :param damage: int
        """
        Unit.take_damage(self, damage)
        if self.is_dead:
            self._state = DEAD

    def attack(self, hero):
        hero.take_damage(random.randint(int(0.7 * self._power), self._power))


class Golem(Enemy):
    def __init__(self, config):
        """
        :rtype: Golem
        """
        animations = list()
        animations.append(Animation('pictures/Archive (1)/idle-walk/idle', 6))
        animations.append(Animation('pictures/Archive (1)/attack/hit', 6))
        animations.append(Animation('pictures/Archive (1)/appear/appear', 15))
        animations.append(Animation('pictures/Archive (1)/die/die', 7))
        Enemy.__init__(self, config, animations)


class Vampire(Enemy):
    def __init__(self, config):
        animations = list()
        animations.append(Animation('pictures/Archive/walk-idle/go', 8))
        animations.append(Animation('pictures/Archive/attack/hit', 13))
        animations.append(Animation('pictures/Archive/appear/appear', 12))
        animations.append(Animation('pictures/Archive/die/appear', 12))
        Enemy.__init__(self, config, animations)


def create_enemy(enemy_config):
    if enemy_config["type"] == 'golem':
        return Golem(enemy_config)
    elif enemy_config["type"] == 'vampire':
        return Vampire(enemy_config)
    else:
        raise ValueError('Wrong enemy type.')


"""
pygame.init()
srf = pygame.display.set_mode((1000, 500))
with open('config/cards/fire_card1.json', 'r', encoding='utf-8') as fh:
    card = card.create_card(json.load(fh))
with open('config/enemy/enemy1.json', 'r', encoding='utf-8') as fh:
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
