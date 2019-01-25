import os

import pygame

from label import Label


class Button:
    def __init__(self, size=(0, 0), pos=(0, 0), on_press=lambda: None, label=None):
        """
        :param size: Tuple(width, height)
        :param pos: Tuple(x, y)
        :param on_press: Callable
        :param label: Label object
        :return: Button object
        """

        self.__image_path = os.path.join('pictures', 'button1.png')
        self.__image = pygame.image.load(self.__image_path).convert_alpha()
        self.__image = pygame.transform.scale(self.__image, size)

        self.__rect = self.__image.get_rect()
        self.__rect.move_ip(pos)

        self.__label = label if label is not None else Label()

        self.on_press = on_press

    def blit_me(self, surface):
        self.__label.blit_me(self.__image)
        surface.blit(self.__image, self.__rect)

    @property
    def rect(self):
        return self.__rect


def create_button(config, creator, size=(0, 0), pos=(0, 0)):
    pass
