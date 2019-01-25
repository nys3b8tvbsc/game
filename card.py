"""
Module provides all card types:
    Attack cards:
        Magic
        Physical
    TODO
"""

import os
from abc import ABCMeta, abstractmethod

import pygame

from label import Label

"""
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
"""


class Card(metaclass=ABCMeta):
    """Abstract base card class for all cards."""

    def __init__(self, pos, height, image, name_label, text_label):
        """
        :param pos: Tuple(x, y)
        :param height: int
        :param image: path. Absolute or relative path to unit`s sprite picture.
        :param name_label: Label
        :param name_label: Label
        :return: Card object
        """
        self._image_path = image
        self._image = pygame.image.load(image).convert_alpha()
        width = int(round((self._image.get_width() * height / self._image.get_height())))
        self._image = pygame.transform.scale(self._image, (width, height))
        self._rect = self._image.get_rect()
        self._rect.move_ip(pos)
        self._name_label = name_label
        self._text_label = text_label
        self._hover = False  # TODO method
        back_path = os.path.join('card_images', 'background.png')
        self._back = pygame.image.load(back_path).convert_alpha()

    def blit_me(self, surface):
        """
        Method for displaying card on screen.

        :param surface: pygame.Surface. Surface on which this card is drawn.
        """
        self._name_label.blit_me(self._image)
        self._text_label.blit_me(self._image)
        if self._hover:
            surface.blit(self._back, self._rect)
        surface.blit(self._image, self._rect)

    @abstractmethod
    def get_info(self):
        """Get config of this card.

        :return: Dict.
        """
        pass


class AttackCard(Card, metaclass=ABCMeta):
    """Abstract base class for all attack cards."""

    def __init__(self, pos, height, image, name_label, text_label, damage):
        """
        :param pos: Tuple(x, y)
        :param height: int
        :param image: path. Absolute or relative path to unit`s sprite picture.
        :param name_label: Label
        :param text_label: Label
        :param damage: int
        :return: AttackCard object
        """
        Card.__init__(self, pos, height, image, name_label, text_label)
        self._damage = damage

    @abstractmethod
    def attack(self, enemy):
        """
        :param enemy: Enemy
        """
        pass


class MagicAttack(AttackCard):
    def __init__(self, pos, height, image, name_label, text_label, damage, mana_cost, magic_type):
        """
        :param pos: Tuple(x, y)
        :param height: int
        :param image: path. Absolute or relative path to unit`s sprite picture.
        :param name_label: Label
        :param text_label: Label
        :param damage: int
        :param mana_cost: int
        :param magic_type: str
        """
        AttackCard.__init__(self, pos, height, image, name_label, text_label, damage)
        self._mana_cost = mana_cost
        self._magic_type = magic_type

    def attack(self, enemy):
        """
        :param enemy: Enemy
        """
        pass

    def get_info(self):
        # TODO label get_info
        """
        return {'type': 'attack', 'subtype': 'magic',
                'image': self.image_path, 'name': self.name, 'text': self.text,
                'damage': self.damage, 'cost': self.mana_cost, 'magic_type': self.type}
        """
        pass


class PhysicalAttack(AttackCard):
    def __init__(self, pos, height, image, name_label, text_label, damage, energy):
        """
        :param pos: Tuple(x, y)
        :param height: int
        :param image: path. Absolute or relative path to unit`s sprite picture.
        :param name_label: Label
        :param text_label: Label
        :param damage: int
        :param energy: int
        """
        AttackCard.__init__(self, pos, height, image, name_label, text_label, damage)
        self._energy = energy

    def attack(self, enemy):
        """
        :param enemy: Enemy
        """
        pass

    def get_info(self):
        # TODO label get_info
        """
        return {'type': 'attack', 'subtype': 'physical',
                'image': self.image_path, 'name': self.name, 'text': self.text,
                'damage': self.damage, 'cost': self.energy}
        """
        pass


def create_card(pos, height, config):
    """
    :param pos: Tuple(x, y)
    :param height: int
    :param config: Dict
    :return: Card object
    """

    name_size = (300, 100)  # TODO
    name_pos = (0, 0)
    name_font = os.path.join('fonts', 'DECOR6DI.TTF')

    name_label = Label(strings=(config['name'],),
                       size=name_size,
                       pos=name_pos,
                       font_name=name_font)

    text_size = (300, 100)  # TODO
    text_pos = (500, 500)
    text_font = os.path.join('fonts', 'font.ttf')

    text_label = Label(strings=(config['text'],),
                       size=text_size,
                       pos=text_pos,
                       font_name=text_font)

    if config['card_type'] == 'attack':
        if config['subtype'] == 'magic':
            return MagicAttack(pos,
                               height,
                               config['image'],
                               name_label,
                               text_label,
                               config['damage'],
                               config['cost'],
                               config['magic_type'])

        elif config['subtype'] == 'physical':
            return PhysicalAttack(pos,
                                  height,
                                  config['image'],
                                  name_label,
                                  text_label,
                                  config['damage'],
                                  config['cost'])
