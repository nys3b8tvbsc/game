import json
import random

import pygame

import card
from animation import Animation
from constants import *
from unit import Unit, Create_Hero


class Enemy(Unit):
    """Base class for all enemies.
    TODO implement base class methods"""

    def __init__(self, level, power, max_hp, animations):
        """
        :param level: int
        :param power: int
        :param max_hp: int
        :return: Enemy object
        """
        Unit.__init__(self, max_hp, level)
        self.power = power
        self.bar = pygame.image.load('pictures/manabar.png').convert_alpha()
        self.animations=animations
        self.state = APPEAR
        self.image = self.animations[APPEAR].frame
        self.rect = self.image.get_rect()
        self.bar_rect = self.bar.get_rect(center=self.rect.center)
        # self.actions = actions

    def animated(self):
        if not self.animations[self.state].update():
            self.state = DEFAULT
        self.image = self.animations[self.state].frame


    def blit_me(self, surface):
        """
        :param surface: pygame.Surface
        """
        surface.blit(self.image, self.rect)
        self.bar_rect.y = self.rect.y - 25
        pygame.draw.rect(surface, RED, (
            self.bar_rect.x + X_BAR, self.bar_rect.y + Y_BAR, int(MAX_HP_BAR * (float(self.hp / self.max_hp))), H_BAR))
        surface.blit(self.bar, self.bar_rect)

    def make_action(self, hero):
        """
        :param hero: Hero
        """
        # action = random.choice(self.actions)
        # action(self, hero)
        pass

    def take_damage(self, damage):
        """
        :param damage: int
        """
        self.hp-=damage
        if self.hp<=0:
            self.state=DEAD
    def attack(self,hero):
        hero.take_damage(random.randint(int(0.7*self.power),self.power))


class Golem(Enemy):
    def __init__(self, level, power, max_hp):
        """
        :param level: int
        :param power: int
        :param max_hp: int
        """
        self.animations = []
        self.animations.append(Animation('pictures/Archive (1)/idle-walk/idle', 6))
        self.animations.append(Animation('pictures/Archive (1)/attack/hit', 6))
        self.animations.append(Animation('pictures/Archive (1)/appear/appear', 15))
        self.animations.append(Animation('pictures/Archive (1)/die/die', 7))
        Enemy.__init__(self, level, power, max_hp, self.animations)

class Vampire(Enemy):
    def __init__(self,level,power, max_hp):
        self.animations = []
        self.animations.append(Animation('pictures/Archive/walk-idle/go', 8))
        self.animations.append(Animation('pictures/Archive/attack/hit', 13))
        self.animations.append(Animation('pictures/Archive/appear/appear', 12))
        self.animations.append(Animation('pictures/Archive/die/appear', 12))
        Enemy.__init__(self, level, power, max_hp, self.animations)

def Create_Enemy(enemy_config):
    if enemy_config["type"]=='golem':
        return Golem(enemy_config["level"],enemy_config["power"],enemy_config["max_hp"])
    elif enemy_config["type"]=='vampire':
        return Vampire(enemy_config["level"],enemy_config["power"],enemy_config["max_hp"])

pygame.init()
srf = pygame.display.set_mode((1000, 500))
with open('config/cards/card1.json', 'r', encoding='utf-8') as fh:
    card = card.create_card(json.load(fh))
with open('config/enemy/enemy1.json', 'r', encoding='utf-8') as fh:
    enemy_config=json.load(fh)
gol=Create_Enemy(enemy_config)
with open('config/hero/hero1.json', 'r', encoding='utf-8') as fh:
    player_config=json.load(fh)
p1=Create_Hero(player_config)
print(gol.hp)
p1.attack(gol,card)
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
        elif event.type==pygame.KEYDOWN:
            p1.attack(gol, card)
    gol.animated()
    srf.fill((0, 0, 0))
    gol.blit_me(srf)
    pygame.display.update()
    clock.tick(20)

