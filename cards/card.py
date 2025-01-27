"""
Module provides all cards types:
    Attack cards:
        Magic
        Physical
    TODO
"""

import os
from abc import ABCMeta, abstractmethod

import pygame

from const.card import NAME_LABEL, TEXT_LABEL, LEFT_LABEL, RIGHT_LABEL
from const.color import WHITE, BLACK, GREEN
from engine.label import Label


class Card(metaclass=ABCMeta):
    def __init__(self, height, config):
        self._config = config

        image = os.path.join('pictures', 'card_images', config['image'])
        self._image = pygame.image.load(image).convert_alpha()
        self._scaling = height / self._image.get_height()
        width = int(self._image.get_width() * self._scaling)
        self._def_im = pygame.transform.scale(self._image, (width, height))
        self._image = pygame.transform.scale(self._image, (width, height))
        self._rect = self._image.get_rect()

        self._name_label = Label(text=config['name'],
                                 pos=(NAME_LABEL[0] * self._scaling, NAME_LABEL[1] * self._scaling),
                                 size=(NAME_LABEL[2] * self._scaling, NAME_LABEL[3] * self._scaling),
                                 font_name='fonts/CharlemagneC.ttf', color=WHITE)

        self._text_label = Label(text=config['text'],
                                 pos=(TEXT_LABEL[0] * self._scaling, TEXT_LABEL[1] * self._scaling),
                                 size=(TEXT_LABEL[2] * self._scaling, TEXT_LABEL[3] * self._scaling),
                                 font_name='fonts/PhillippScript.ttf')

        back_path = os.path.join('pictures', 'card_images', 'background.png')
        self._back = pygame.image.load(back_path).convert_alpha()
        self._back = pygame.transform.scale(self._back, (width, height))

        back_path1 = os.path.join('pictures', 'card_images', 'background1.png')
        self._back1 = pygame.image.load(back_path1).convert_alpha()
        self._back1 = pygame.transform.scale(self._back1, (width, height))

        self._right_label = Label()
        self._left_label = Label()

        self._focus = False
        self._select = False

        self._name_label.blit_me(self._image)
        self._text_label.blit_me(self._image)

    def blit_me(self, surface):
        if self.selected:
            surface.blit(self._back1, self._rect)
        elif self.focused:
            surface.blit(self._back, self._rect)
        surface.blit(self._image, self._rect)

    def click(self):
        self._select = not self._select

    def deselect(self):
        self._select = False

    @property
    def selected(self):
        return self._select

    @property
    def conf_name(self):
        return self._config["conf_name"]

    def focus(self):
        self._focus = True

    def defocus(self):
        self._focus = False

    @property
    def focused(self):
        return self._focus

    @property
    def rect(self):
        return self._rect

    @property
    @abstractmethod
    def cost(self):
        pass

    def move_to(self, x, y):
        self._rect.x = x
        self._rect.y = y

    @staticmethod
    def card_height(screen_height):
        return int((400 / 1080) * screen_height)

    @property
    def type(self):
        return self._type


class AttackCard(Card, metaclass=ABCMeta):
    def __init__(self, height, config):
        Card.__init__(self, height, config)
        self._damage = config['value']
        self._left_label = Label(text=config['value'],
                                 pos=(LEFT_LABEL[0] * self._scaling, LEFT_LABEL[1] * self._scaling),
                                 size=(LEFT_LABEL[2] * self._scaling, LEFT_LABEL[3] * self._scaling))

        self._left_label.blit_me(self._image)

    @property
    @abstractmethod
    def subtype(self):
        pass

    @property
    def damage(self):
        return self._damage

    @abstractmethod
    def update_image(self):
        color = BLACK
        if self._damage > self._config['value']:
            color = GREEN
        self._left_label = Label(text=self._damage,
                                 pos=(LEFT_LABEL[0] * self._scaling, LEFT_LABEL[1] * self._scaling),
                                 size=(LEFT_LABEL[2] * self._scaling, LEFT_LABEL[3] * self._scaling), color=color)
        image = os.path.join('pictures', 'card_images', self._config['image'])
        self._image = pygame.image.load(image).convert_alpha()
        height = int(self._image.get_height() * self._scaling)
        width = int(self._image.get_width() * self._scaling)
        self._image = pygame.transform.scale(self._image, (width, height))
        self._name_label.blit_me(self._image)
        self._text_label.blit_me(self._image)
        self._left_label.blit_me(self._image)
        self._right_label.blit_me(self._image)


class MagicAttack(AttackCard):
    def __init__(self, height, config, hero, effects):
        self._type = config['type']
        config['value'] = max(int(config['value'] * hero[self._type] / 100), 1)
        AttackCard.__init__(self, height, config)
        self._mana_cost = config['cost']
        self._right_label = Label(text=config['cost'],
                                  pos=(RIGHT_LABEL[0] * self._scaling, RIGHT_LABEL[1] * self._scaling),
                                  size=(RIGHT_LABEL[2] * self._scaling, RIGHT_LABEL[3] * self._scaling))

        self._right_label.blit_me(self._image)
        for effect in effects:
            effect.on(self)

    @property
    def subtype(self):
        return "magic"

    @property
    def cost(self):
        return self._mana_cost

    def update_image(self):
        color = BLACK
        if self._mana_cost < self._config['cost']:
            color = GREEN
        self._right_label = Label(text=self._mana_cost,
                                  pos=(RIGHT_LABEL[0] * self._scaling, RIGHT_LABEL[1] * self._scaling),
                                  size=(RIGHT_LABEL[2] * self._scaling, RIGHT_LABEL[3] * self._scaling), color=color)
        AttackCard.update_image(self)


class PhysicalAttack(AttackCard):
    def __init__(self, height, config, hero, effects):
        self._type = config['type']
        config['value'] = max(int(config['value'] * hero[self._type] / 100), 1)
        AttackCard.__init__(self, height, config)
        self._energy_cost = config['cost']
        self._right_label = Label(text=config['cost'],
                                  pos=(RIGHT_LABEL[0] * self._scaling, RIGHT_LABEL[1] * self._scaling),
                                  size=(RIGHT_LABEL[2] * self._scaling, RIGHT_LABEL[3] * self._scaling))

        self._right_label.blit_me(self._image)
        for effect in effects:
            effect.on(self)

    @property
    def subtype(self):
        return "physical"

    @property
    def cost(self):
        return self._energy_cost

    def update_image(self):
        color = BLACK
        if self._energy_cost < self._config['cost']:
            color = GREEN
        self._right_label = Label(text=self._energy_cost,
                                  pos=(RIGHT_LABEL[0] * self._scaling, RIGHT_LABEL[1] * self._scaling),
                                  size=(RIGHT_LABEL[2] * self._scaling, RIGHT_LABEL[3] * self._scaling), color=color)
        AttackCard.update_image(self)


class RegenCard(Card):
    def __init__(self, height, config):
        Card.__init__(self, height, config)
        self._value = config['value']
        self._type = config['type']

    @property
    def cost(self):
        return 0

    @property
    def subtype(self):
        return "regen"

    def action(self, hero):
        if self._type == 'hp':
            hero._hp = min(hero._max_hp, hero._hp + self._value)
            hero._config['hp'] = hero._hp
        elif self._type == 'mana':
            hero._mana = min(hero._max_mana, hero._mana + self._value)
            hero._config['mana'] = hero._mana
        elif self._type == 'energy':
            hero._power = min(hero._max_power, hero._power + self._value)
            hero._config['hp'] = hero._energy


class EffectCard(Card):
    def __init__(self, height, config):
        Card.__init__(self, height, config)
        self._value = config['value']
        self._round = config['round']
        self._type = config['type']
        self._type2 = config['type2']

    @property
    def cost(self):
        pass

    @property
    def subtype(self):
        return "effect"

    def on(self, card):
        if card.type == self._type and card.subtype != 'effect':
            if self._type2 == 'damage':
                card._damage += max(int(self._value * card._config['value']), 1)
                card.update_image()
            elif self._type2 == 'cost':
                if card.subtype == 'magic':
                    card._mana_cost -= int(self._value * card._config['cost'])
                else:
                    card._energy_cost -= int(self._value * card._config['cost'])
                card.update_image()

    def off(self, card):
        if card.type == self._type and card.subtype != 'effect':
            if self._type2 == 'damage':
                card._damage -= max(int(self._value * card._config['value']), 1)
                card.update_image()
            elif self._type2 == 'cost':
                if card.subtype == 'magic':
                    card._mana_cost += int(self._value * card._config['cost'])
                elif card.subtype == 'physical':
                    card._energy_cost += int(self._value * card._config['cost'])
                card.update_image()

    def action(self, hero):
        hero._effects.append(self)
        hero._hand.on_effect(self)

    def update(self):
        self._round -= 1


def create_card(height, config, hero, effects):
    if config['card_type'] == 'attack':
        if config['subtype'] == 'magic':
            return MagicAttack(height, config, hero, effects)
        elif config['subtype'] == 'physical':
            return PhysicalAttack(height, config, hero, effects)
        else:
            raise ValueError('Wrong cards subtype.')
    elif config['card_type'] == 'regen':
        return RegenCard(height, config)
    elif config['card_type'] == 'effect':
        return EffectCard(height, config)
    else:
        raise ValueError('Wrong cards type.')
