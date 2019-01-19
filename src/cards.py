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

    def __init__(self, image: str, name: str, text: str):
        """

        Img_path is absolute or relative path to unit`s sprite picture.
        TODO
        """
        self.image = pygame.image.load(image).convert_alpha()
        self.back = pygame.image.load('Cards_Image/background.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.hover = False
        self.name = name
        self.text = text

        rect1=pygame.Rect((140,288,0,0))
        f1=pygame.font.Font('DECOR6DI.TTF', 26) #Грамотное отображение текста
        while len(text)>25:
            n=text[0:25].rfind(' ')
            txt=f1.render(text[0:n], 1, (0, 0, 0))
            self.image.blit(txt,rect1)
            rect1.y+=17
            text=text[n:]
        txt = f1.render(text[0:n], 1, (0, 0, 0))
        self.image.blit(txt, rect1)


        f1 = pygame.font.Font('font.ttf', 30)
        txt = f1.render(self.name, 1, (0, 0, 0))
        rect1 = txt.get_rect(center=(230, 275))
        self.image.blit(txt, rect1)



    def blit(self, surf: pygame.Surface):
        """Method for displaying card on screen."""
        if self.hover:
            surf.blit(self.back, self.rect)
        surf.blit(self.image, self.rect)



class Attack_card(Card, metaclass=ABCMeta):
    """Abstract base class for all attack cards."""

    def __init__(self, image, name, text, damage):
        self.damage = damage
        Card.__init__(self, image, name, text)

    @abstractmethod
    def Attack(self, player, enemy):
        pass


class Magic_Attack(Attack_card):
    def __init__(self, image, name, text, damage, mana_cost):
        self.mana_cost = mana_cost
        Attack_card.__init__(self, image, name, text, damage)

    def Attack(self, player, enemy):
        pass


class Physical_Attack(Attack_card):
    def __init__(self, image, name, text, damage, energy):
        self.energy = energy
        Attack_card.__init__(self, image, name, text, damage)

    def Attack(self, player, enemy):
        pass


"""
pygame.init()
srf=pygame.display.set_mode((1000,500))
c=Physical_Attack('Cards_Image/attack_card1.png','Буря мечей','Наносит урон в 1000 единиц всем юнитам на поле',1000,100)
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