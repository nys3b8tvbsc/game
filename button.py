import os

import pygame

from constants import WHITE
from label import Label


class Button:
    def __init__(self, size=(0, 0), pos=(0, 0), text='',on_press=0):
        """
        :param size: Tuple(width, height)
        :param pos: Tuple(x, y)
        :param on_press: Callable
        :param str text: label text
        :rtype: Button
        """

        self.__image_path = os.path.join('pictures', 'button1.png')
        self.__image = pygame.image.load(self.__image_path).convert_alpha()
        self.__image = pygame.transform.scale(self.__image, size)

        self.__rect = self.__image.get_rect()
        self.__rect.move_ip(pos)

        self.__label = Label(text, size, font_name='fonts/DECOR6DI.TTF', color=WHITE)

        self.on_press = on_press

    def blit_me(self, surface):
        self.__label.blit_me(self.__image)
        surface.blit(self.__image, self.__rect)

    def click(self,xy):
        if self.__rect.collidepoint(xy):
            pygame.event.post(pygame.event.Event(self.on_press,{}))

    @property
    def rect(self):
        return self.__rect


def create_button(config, creator, size=(0, 0), pos=(0, 0)):
    pass
