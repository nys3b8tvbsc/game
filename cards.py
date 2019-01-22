"""
Module provides all card types:
    Attack cards:
        Magic
        Physical
    TODO
"""
from abc import ABCMeta, abstractmethod

import pygame

from constans import BLACK


# TODO move ??
def blit_long_text(surface, text):
    rect = pygame.Rect((140, 288, 0, 0))
    f1 = pygame.font.Font('fonts/DECOR6DI.TTF', 26)
    while len(text) > 25:
        string_end = text[:25].rfind(' ')
        string = f1.render(text[:string_end], 1, BLACK)
        surface.blit(string, rect)
        rect.y += 17
        text = text[string_end:]
    text = f1.render(text, 1, BLACK)
    surface.blit(text, rect)


def blit_text(surface, text):
    font = pygame.font.Font('fonts/font.ttf', 30)
    txt = font.render(text, 1, BLACK)
    rect = txt.get_rect(center=(230, 275))
    surface.blit(txt, rect)


class Card(pygame.sprite.Sprite, metaclass=ABCMeta):
    """Abstract base card class for all cards."""

    def __init__(self, image, name, text):
        """
        :param image: path. Absolute or relative path to unit`s sprite picture.
        :param name: str
        :param text: str
        :return: Card object
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.image_path = image
        self.back = pygame.image.load('card_images/background.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.hover = False
        self.name = name
        self.text = text

        blit_long_text(self.image, text)

        blit_text(self.image, name)

    def blit_me(self, surface):
        """
        Method for displaying card on screen.

        :param surface: pygame.Surface. Surface on which this card is drawn.
        """
        if self.hover:
            surface.blit(self.back, self.rect)
        surface.blit(self.image, self.rect)

    @abstractmethod
    def get_info(self):
        """Get config of this card.

        :return: Dict.
        """
        pass


class AttackCard(Card, metaclass=ABCMeta):
    """Abstract base class for all attack cards."""

    def __init__(self, image, name, text, damage):
        """
        :param image: path. Absolute or relative path to unit`s sprite picture.
        :param name: str
        :param text: str
        :param damage: int
        :return: AttackCard object
        """
        Card.__init__(self, image, name, text)
        self.damage = damage

    @abstractmethod
    def attack(self, enemy):
        """
        :param enemy: Enemy
        """
        pass


class MagicAttack(AttackCard):
    def __init__(self, image, name, text, damage, mana_cost, magic_type):
        """

        :param image: path. Absolute or relative path to unit`s sprite picture.
        :param name: str
        :param text: str
        :param damage: int
        :param mana_cost: int
        :param magic_type: TODO ??
        """
        AttackCard.__init__(self, image, name, text, damage)
        self.mana_cost = mana_cost
        self.type = magic_type

    def attack(self, enemy):
        """
        :param enemy: Enemy
        """
        pass

    def get_info(self):
        return {'type': 'attack', 'subtype': 'magic',
                'image': self.image_path, 'name': self.name, 'text': self.text,
                'damage': self.damage, 'cost': self.mana_cost, 'magic_type': self.type}


class PhysicalAttack(AttackCard):
    def __init__(self, image, name, text, damage, energy):
        """
        :param image: path. Absolute or relative path to unit`s sprite picture.
        :param name: str
        :param text: str
        :param damage: int
        :param energy: int
        """
        AttackCard.__init__(self, image, name, text, damage)
        self.energy = energy

    def attack(self, enemy):
        """
        :param enemy: Enemy
        """
        pass

    def get_info(self):
        return {'type': 'attack', 'subtype': 'physical',
                'image': self.image_path, 'name': self.name, 'text': self.text,
                'damage': self.damage, 'cost': self.energy}


def create_card(config):
    """
    :param config: Dict
    :return: Card object
    """
    if config['card_type'] == 'attack':
        if config['subtype'] == 'magic':
            return MagicAttack(config['image'],
                               config['name'],
                               config['text'],
                               config['damage'],
                               config['cost'],
                               config['magic_type'])

        elif config['subtype'] == 'physical':
            return PhysicalAttack(config['image'],
                                  config['name'],
                                  config['text'],
                                  config['damage'],
                                  config['cost'])


"""
pygame.init()
srf = pygame.display.set_mode((1000, 500))
c = create_card('Physical attack', 'card_images/attack_card1.png', 'Буря мечей',
                'Наносит урон в 1000 единиц всем юнитам на поле', 1000, 100)
print(c.get_info())
c.rect.x = 50
c.blit_me(srf)
pygame.display.update()
clock = pygame.time.Clock()
param = True
while param:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            param = False
    if c.rect.collidepoint(pygame.mouse.get_pos()):
        c.hover = True
    else:
        c.hover = False
    srf.fill((0, 0, 0))
    c.blit_me(srf)
    pygame.display.update()
    clock.tick(60)
"""
