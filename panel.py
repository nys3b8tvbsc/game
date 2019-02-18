import os

import pygame

from button import Button
from const.button import DEFAULT_W, DEFAULT_H
from const.event import TAKE_DAMAGE, START_BATTLE, ENEMY_DAMAGE, QUIT, REGEN
from const.screen import DEFAULT_SIZE
from label import Label


class Panel:
    def __init__(self, screen_width):
        width = screen_width
        path = os.path.join('pictures', 'panel.png')
        self._image = pygame.image.load(path).convert_alpha()
        self._scaling = width / self._image.get_width()
        height = int(self._image.get_height() * self._scaling)
        self._image = pygame.transform.scale(self._image, (width, height))
        self._rect = self._image.get_rect()
        self._selected = False
        self._labels = [Label() for _ in range(6)]
        self._label_size = (50 * self._scaling, 10 * self._scaling)
        self._label_pos = [(0 * self._scaling, 15 * self._scaling),
                           (50 * self._scaling, 15 * self._scaling),
                           (100 * self._scaling, 15 * self._scaling),
                           (150 * self._scaling, 15 * self._scaling),
                           (200 * self._scaling, 15 * self._scaling),
                           (250 * self._scaling, 15 * self._scaling)]
        W = int(0.7 * DEFAULT_W * screen_width / DEFAULT_SIZE[0])
        H = int(DEFAULT_H * W / DEFAULT_W)
        self._buttons = [Button((W, H), (screen_width - W, 0), "Выход", QUIT)
                         ]  # TODO
        self._updated = False

    @property
    def rect(self):
        return self._rect

    def blit_me(self, surface):
        if not self._selected:
            return

        surface.blit(self._image, self._rect)
        for label in self._labels:
            label.blit_me(surface)
        for button in self._buttons:
            button.blit_me(surface)

    def update(self, hero_config):
        if not self._updated:
            return

        size = self._label_size
        pos = self._label_pos
        self._labels[0] = Label('Жизнь', size, pos[0])

        current = hero_config['hp']
        maximum = hero_config['max_hp']
        self._labels[1] = Label('{}/{}'.format(current, maximum), size, pos[1])

        current = hero_config['mana']
        maximum = hero_config['max_mana']

        self._labels[2] = Label('Мана', size, pos[2])
        self._labels[3] = Label('{}/{}'.format(current, maximum), size, pos[3])

        current = hero_config['energy']
        maximum = hero_config['max_energy']

        self._labels[4] = Label('Энергия', size, pos[4])
        self._labels[5] = Label('{}/{}'.format(current, maximum), size, pos[5])

    def handle_event(self, event):
        self._updated = False

        if event.type == pygame.MOUSEMOTION:
            self._selected = self.rect.collidepoint(event.pos)
        elif self._selected and event.type == pygame.MOUSEBUTTONDOWN:
            for button in self._buttons:
                button.handle_event(event)
        elif event.type in (TAKE_DAMAGE, START_BATTLE, ENEMY_DAMAGE, REGEN):  # TODO
            self._updated = True
