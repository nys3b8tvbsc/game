"""
Module provides top panel.
"""
import os

import pygame

from button import Button
from label import Label


class Panel:
    def __init__(self, screen_width):
        """
        :param int screen_width:
        :rtype: Panel
        """
        width = screen_width
        path = os.path.join('pictures', 'panel.png')
        self._image = pygame.image.load(path).convert_alpha()
        self._scaling = width / self._image.get_width()
        height = int(self._image.get_height() * self._scaling)
        self._image = pygame.transform.scale(self._image, (width, height))
        self._rect = self._image.get_rect()
        self._selected = False
        self._labels = [Label() for _ in range(4)]
        self._label_size = (40 * self._scaling, 10 * self._scaling)
        self._label_pos = [(0 * self._scaling, 10 * self._scaling),
                           (35 * self._scaling, 10 * self._scaling),
                           (5 * self._scaling, 25 * self._scaling),
                           (35 * self._scaling, 25 * self._scaling)]
        self._buttons = [Button() for _ in range(2)]  # TODO

    @property
    def rect(self):
        return self._rect

    def blit_me(self, surface):
        if not self._selected:
            return

        for label in self._labels:
            label.blit_me(self._image)
        for button in self._buttons:
            button.blit_me(surface)
        surface.blit(self._image, self._rect)

    def update(self, hero_config):
        size = self._label_size
        pos = self._label_pos
        self._labels[0] = Label('Hp', size, pos[0])

        current = hero_config['hp']
        maximum = hero_config['max_hp']
        self._labels[1] = Label(f'{current}/{maximum}', size, pos[1])

        if hero_config['type'] == 'mage':
            resource = 'Mana'
            current = hero_config['mana']
            maximum = hero_config['max_mana']
        elif hero_config['type'] == 'warrior':
            resource = 'Energy'
            current = hero_config['energy']
            maximum = hero_config['max_energy']
        else:
            raise ValueError('Unknown hero type.')

        self._labels[2] = Label(resource, size, pos[2])
        self._labels[3] = Label(f'{current}/{maximum}', size, pos[3])

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self._selected = self.rect.collidepoint(event.pos)
        if self._selected and event.type == pygame.MOUSEBUTTONDOWN:
            for button in self._buttons:
                button.click(event.pos)
