"""
Module provides top panel.
"""

import os

import pygame

from constants import BLACK


class Panel:
    def __init__(self, screen_width):
        """
        :param int screen_width:
        :rtype: Panel
        """
        width = screen_width
        path = os.path.join('pictures', 'panel.png')
        self._image = pygame.image.load(path).convert_alpha()
        height = int(self._image.get_height() * width / self._image.get_width())
        self._image = pygame.transform.scale(self._image, (width, height))
        self._rect = self._image.get_rect()
        self._font = pygame.font.Font(None, 20)
        self._text_color = BLACK

    @property
    def rect(self):
        return self._rect

    def blit_me(self, surface, hero):
        hp = '{}/{}'.format(hero['hp'], hero['max_hp'])
        mana = '{}/{}'.format(hero['mana'], hero['max_mana'])  # TODO refactor energy
        t_hp = self._font.render('HP', 0, self._text_color)
        i_hp = self._font.render(hp, 0, self._text_color)
        t_mana = self._font.render('Mana', 0, self._text_color)
        i_mana = self._font.render(mana, 0, self._text_color)
        self._image.blit(t_hp, (10, 10))
        self._image.blit(t_mana, (10, 30))
        self._image.blit(i_hp, (70, 10))
        self._image.blit(i_mana, (70, 30))
        surface.blit(self._image, self._rect)

    """
    def update(self, hero):
        self.hp = '{}/{}'.format(hero['hp'], hero['max_hp'])
        self.mana = '{}/{}'.format(hero['mana'], hero['max_mana'])
    """

    def handle_event(self, event):
        pass
