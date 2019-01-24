import pygame

from animation import Animation
from constants import *
from unit import Unit


class Enemy(Unit):
    """Base class for all enemies.
    TODO implement base class methods"""

    def __init__(self, power, max_hp, level):
        """
        :param level: int
        :param power: int
        :param max_hp: int
        :return: Enemy object
        """
        Unit.__init__(self, max_hp, level)
        self.power = power
        self.bar = pygame.image.load('pictures/manabar.png').convert_alpha()
        # self.actions = actions

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
        pass


class Golem(Enemy):
    def __init__(self, level, power, max_hp):
        """
        :param level: int
        :param power: int
        :param max_hp: int
        """
        Enemy.__init__(self, level, power, max_hp)
        self.animations = []
        self.animations.append(Animation('pictures/Archive (1)/idle-walk/idle', 6))
        self.animations.append(Animation('pictures/Archive (1)/attack/hit', 6))
        self.animations.append(Animation('pictures/Archive (1)/appear/appear', 15))
        self.animations.append(Animation('pictures/Archive (1)/die/die', 7))
        self.state = APPEAR
        self.image = self.animations[APPEAR].frame
        self.rect = self.image.get_rect()
        self.bar_rect = self.bar.get_rect(center=self.rect.center)

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
        pygame.draw.rect(surface, (255, 0, 0), (
            self.bar_rect.x + X_BAR, self.bar_rect.y + Y_BAR, int(MAX_HP_BAR * (float(self.hp / self.max_hp))), H_BAR))
        surface.blit(self.bar, self.bar_rect)


"""
pygame.init()
srf = pygame.display.set_mode((1000, 500))
gol = Golem(1, 1000, 1000)
gol.rect.y = 100
gol.blit_me(srf)
pygame.display.update()
clock = pygame.time.Clock()
param = True
while param:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            param = False
    gol.animated()
    srf.fill((0, 0, 0))
    gol.blit_me(srf)
    pygame.display.update()
    clock.tick(20)
"""
