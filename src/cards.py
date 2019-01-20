"""
Module provides all card types:
    Attack cards:
        Magic
        Physical
    TODO
"""
from abc import ABCMeta, abstractmethod
from typing import Optional

import pygame


class Card(pygame.sprite.Sprite, metaclass=ABCMeta):
    """Abstract base card class for all cards."""

    def __init__(self, image: str, name: str, text: str):
        """

        Img_path is absolute or relative path to unit`s sprite picture.
        TODO
        """
        self.image = pygame.image.load(image).convert_alpha()
        self.image_path = image
        self.back = pygame.image.load('Cards_Image/background.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.hover = False
        self.name = name
        self.text = text

        rect1 = pygame.Rect((140, 288, 0, 0))
        f1 = pygame.font.Font('Fonts/DECOR6DI.TTF', 26)  # Грамотное отображение текста
        while len(text) > 25:
            n = text[0:25].rfind(' ')
            txt = f1.render(text[0:n], 1, (0, 0, 0))
            self.image.blit(txt, rect1)
            rect1.y += 17
            text = text[n:]
        txt = f1.render(text[0:n], 1, (0, 0, 0))
        self.image.blit(txt, rect1)

        f1 = pygame.font.Font('Fonts/font.ttf', 30)
        txt = f1.render(self.name, 1, (0, 0, 0))
        rect1 = txt.get_rect(center=(230, 275))
        self.image.blit(txt, rect1)

    def blit(self, surf: pygame.Surface):
        """Method for displaying card on screen."""
        if self.hover:
            surf.blit(self.back, self.rect)
        surf.blit(self.image, self.rect)

    @abstractmethod
    def getinf(self):
        pass


class Attack_card(Card, metaclass=ABCMeta):
    """Abstract base class for all attack cards."""

    def __init__(self, image, name, text, damage):
        self.damage = damage
        Card.__init__(self, image, name, text)

    @abstractmethod
    def Attack(self, player, enemy):
        pass


class Magic_Attack(Attack_card):
    def __init__(self, image, name, text, damage, mana_cost, type_magic):
        self.mana_cost = mana_cost
        self.type = type_magic
        Attack_card.__init__(self, image, name, text, damage)

    def Attack(self, player, enemy):
        pass

    def getinf(self):
        return {'type': 'Magic attack', 'image': self.image_path, 'name': self.name, 'text': self.text,
                'damage': self.damage, 'mana_cost': self.mana_cost, 'type_magic': self.type}


class Physical_Attack(Attack_card):
    def __init__(self, image, name, text, damage, energy):
        self.energy = energy
        Attack_card.__init__(self, image, name, text, damage)

    def Attack(self, player, enemy):
        pass

    def getinf(self):
        return {'type': 'Physical attack', 'image': self.image_path, 'name': self.name, 'text': self.text,
                'damage': self.damage, 'energy': self.energy}


def Card_Create(type, image, name, text, damage, mana_or_energy, type_magic='Fire') -> Optional[Card]:
    type = type.split()
    if type[1] == 'attack':
        if type[0] == 'Magic':
            return Magic_Attack(image, name, text, damage, mana_or_energy, type_magic)
        elif type[0] == 'Physical':
            return Physical_Attack(image, name, text, damage, mana_or_energy)


"""
pygame.init()
srf=pygame.display.set_mode((1000,500))
c=Card_Create('Physical attack','Cards_Image/attack_card1.png','Буря мечей','Наносит урон в 1000 единиц всем юнитам на поле',1000,100)
print (c.getinf())
c.rect.x=50
c.blit(srf)
pygame.display.update()
clock = pygame.time.Clock()
param=True
while param:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            param=False
    if c.rect.collidepoint(pygame.mouse.get_pos()):
        c.hover=True
    else:
        c.hover=False
    srf.fill((0,0,0))
    c.blit(srf)
    pygame.display.update()
    clock.tick(60)
"""
