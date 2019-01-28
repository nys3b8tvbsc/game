"""
Module provides all card types:
    Attack cards:
        Magic
        Physical
    TODO
"""

import os
from abc import ABCMeta

import pygame

from constants import NAME_LABEL, TEXT_LABEL, LEFT_LABEL, RIGHT_LABEL, WHITE
from label import Label


class Card(metaclass=ABCMeta):
    def __init__(self, pos, height, config):
        self._config = config
        image = os.path.join('card_images', config['image'])
        self._image = pygame.image.load(image).convert_alpha()
        self._scaling = height / self._image.get_height()
        width = int(round(self._image.get_width() * self._scaling))
        self._image = pygame.transform.scale(self._image, (width, height))
        self._rect = self._image.get_rect()
        self._rect.move_ip(pos)

        self._name_label = Label(text=config['name'],
                                 size=(NAME_LABEL[2] * self._scaling, NAME_LABEL[3] * self._scaling),
                                 pos=(NAME_LABEL[0] * self._scaling, NAME_LABEL[1] * self._scaling),font_name='fonts/font.ttf',color=WHITE)

        self._text_label = Label(text=config['text'],
                                 size=(TEXT_LABEL[2] * self._scaling, TEXT_LABEL[3] * self._scaling),
                                 pos=(TEXT_LABEL[0] * self._scaling, TEXT_LABEL[1] * self._scaling),font_name='fonts/DECOR6DI.TTF')

        back_path = os.path.join('card_images', 'background.png')
        self._back = pygame.image.load(back_path).convert_alpha()

        self._right_label = Label()
        self._left_label = Label()

        self._hover = False  # TODO method

    def blit_me(self, surface):
        self._name_label.blit_me(self._image)
        self._text_label.blit_me(self._image)
        self._left_label.blit_me(self._image)
        self._right_label.blit_me(self._image)
        if self._hover:
            surface.blit(self._back, self._rect)
        surface.blit(self._image, self._rect)


class AttackCard(Card, metaclass=ABCMeta):
    def __init__(self, pos, height, config):
        Card.__init__(self, pos, height, config)
        self._damage = config['value']
        self._left_label = Label(text=config['value'],
                                 size=(LEFT_LABEL[2] * self._scaling, LEFT_LABEL[3] * self._scaling),
                                 pos=(LEFT_LABEL[0] * self._scaling, LEFT_LABEL[1] * self._scaling))

    def attack(self, enemy):
        pass


class MagicAttack(AttackCard):
    def __init__(self, pos, height, config):
        AttackCard.__init__(self, pos, height, config)
        self._magic_type = config['magic_type']
        self._mana_cost = config['cost']
        self._right_label = Label(text=config['cost'],
                                  size=(RIGHT_LABEL[2] * self._scaling, RIGHT_LABEL[3] * self._scaling),
                                  pos=(RIGHT_LABEL[0] * self._scaling, RIGHT_LABEL[1] * self._scaling))

    def attack(self, enemy):
        AttackCard.attack(self, enemy)


class PhysicalAttack(AttackCard):
    def __init__(self, pos, height, config):
        AttackCard.__init__(self, pos, height, config)
        self._energy = config['cost']
        self._right_label = Label(text=config['cost'],
                                  size=(RIGHT_LABEL[2] * self._scaling, RIGHT_LABEL[3] * self._scaling),
                                  pos=(RIGHT_LABEL[0] * self._scaling, RIGHT_LABEL[1] * self._scaling))

    def attack(self, enemy):
        AttackCard.attack(self, enemy)


def create_card(pos, height, config):
    if config['card_type'] == 'attack':
        if config['subtype'] == 'magic':
            return MagicAttack(pos, height, config)
        elif config['subtype'] == 'physical':
            return PhysicalAttack(pos, height, config)
        else:
            raise ValueError('Wrong subtype')
    else:
        raise ValueError('Wrong type')