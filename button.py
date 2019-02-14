import os

import pygame

from const.button import DEFAULT_H, DEFAULT_W, LABEL_XY, LABEL_SIZE
from const.color import WHITE
from label import Label


class Button:
    def __init__(self, size=(0, 0), pos=(0, 0), text='', event=0):
        self.__image_path = os.path.join('pictures', 'button1.png')
        self.__image = pygame.image.load(self.__image_path).convert_alpha()
        self.__image = pygame.transform.scale(self.__image, size)

        self.__rect = self.__image.get_rect()
        self.__rect.move_ip(pos)

        trans_x = size[0] / DEFAULT_W
        trans_y = size[1] / DEFAULT_H
        lab_size = (int(trans_x * LABEL_SIZE[0]), int(trans_y * LABEL_SIZE[1]))
        lab_pos = (int(trans_x * LABEL_XY[0]), int(trans_y * LABEL_XY[1]))

        self.__label = Label(text, size=lab_size, pos=lab_pos, font_name='fonts/DECOR6DI.TTF', color=WHITE)

        self._event = event

    def blit_me(self, surface):
        self.__label.blit_me(self.__image)  # TODO ??
        surface.blit(self.__image, self.__rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                pygame.event.post(pygame.event.Event(self._event, {}))

    @property
    def rect(self):
        return self.__rect
