"""
Module provides all card types:
    Attack cards:
        Magic
        Physical
    TODO
"""
from abc import ABCMeta, abstractmethod

import pygame


class Card(pygame.sprite.Sprite, metaclass=ABCMeta):
    """Abstract base card class for all cards."""

    def __init__(self, image: str):
        """

        Img_path is absolute or relative path to unit`s sprite picture.
        TODO
        """
        self.image = pygame.image.load(image).convert_alpha()
        self.back = pygame.image.load('Cards_Image/background.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.hover = False

    def blit(self, surf: pygame.Surface):
        """Method for displaying card on screen."""
        if self.hover:
            surf.blit(self.back, self.rect)
        surf.blit(self.image, self.rect)


class Attack_card(Card, metaclass=ABCMeta):
    """Abstract base class for all attack cards."""

    def __init__(self, image, damage):
        self.damage = damage
        Card.__init__(self, image)

    @abstractmethod
    def Attack(self, player, enemy):
        pass


class Magic_Attack(Attack_card):
    def __init__(self, image, damage, mana):
        self.mana = mana
        Attack_card.__init__(self, image, damage)

    def Attack(self, player, enemy):
        pass


class Physical_Attak(Attack_card):
    def __init__(self, image, damage, energy):
        self.energy = energy
        Attack_card.__init__(self, image, damage)

    def Attack(self, player, enemy):
        pass


"""
pygame.init()
srf=pygame.display.set_mode((1000,500))
c=Physical_Attak('Cards_Image/attack_card1.png',1000,100)
c.rect.x=50
c.blit(srf)
pygame.display.update()
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if c.rect.collidepoint(pygame.mouse.get_pos()):
        c.hover=True
    else:
        c.hover=False
    srf.fill((0,0,0))
    c.blit(srf)
    pygame.display.update()
    clock.tick(60)
    """
