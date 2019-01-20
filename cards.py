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

        'TODO'
        BLACK = (0, 0, 0)
        rect1 = pygame.Rect((140, 288, 0, 0))
        f1 = pygame.font.Font('fonts/DECOR6DI.TTF', 26)  # Грамотное отображение текста
        while len(text) > 25:
            n = text[0:25].rfind(' ')
            txt = f1.render(text[0:n], 1, BLACK)
            self.image.blit_me(txt, rect1)
            rect1.y += 17
            text = text[n:]
        txt = f1.render(text[0:n], 1, BLACK)  # TODO n might be referenced before assignment
        self.image.blit_me(txt, rect1)

        f1 = pygame.font.Font('fonts/font.ttf', 30)
        txt = f1.render(self.name, 1, BLACK)
        rect1 = txt.get_rect(center=(230, 275))
        self.image.blit_me(txt, rect1)

    def blit_me(self, surface):
        """
        Method for displaying card on screen.

        :param surface: pygame.Surface. Surface on which this card is drawn.
        """
        if self.hover:
            surface.blit_me(self.back, self.rect)
        surface.blit_me(self.image, self.rect)

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
    def attack(self, hero, enemy):
        """
        :param hero: Hero
        :param enemy: Enemy
        """
        pass


class MagicAttack(AttackCard):
    def __init__(self, image, name, text, damage, mana_cost, type_magic):
        """

        :param image: path. Absolute or relative path to unit`s sprite picture.
        :param name: str
        :param text: str
        :param damage: int
        :param mana_cost: int
        :param type_magic: TODO ??
        """
        AttackCard.__init__(self, image, name, text, damage)
        self.mana_cost = mana_cost
        self.type = type_magic

    def attack(self, hero, enemy):
        """
        :param hero: Hero
        :param enemy: Enemy
        """
        pass

    def get_info(self):
        return {'type': 'Magic attack', 'image': self.image_path, 'name': self.name, 'text': self.text,
                'damage': self.damage, 'mana_cost': self.mana_cost, 'type_magic': self.type}


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

    def attack(self, hero, enemy):
        """
        :param hero: Hero
        :param enemy: Enemy
        """
        pass

    def get_info(self):
        return {'type': 'Physical attack', 'image': self.image_path, 'name': self.name, 'text': self.text,
                'damage': self.damage, 'energy': self.energy}


def create_card(type, image, name, text, damage, mana_or_energy, type_magic='Fire'):
    """
    TODO config param
    :param type: str
    :param image: path
    :param name: str
    :param text: str
    :param damage: int
    :param mana_or_energy: int
    :param type_magic: str
    :return: Card object
    """
    type = type.split()
    if type[1] == 'attack':
        if type[0] == 'Magic':
            return MagicAttack(image, name, text, damage, mana_or_energy, type_magic)
        elif type[0] == 'Physical':
            return PhysicalAttack(image, name, text, damage, mana_or_energy)


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
