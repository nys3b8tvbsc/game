import pygame

from label import Label


class Button:
    def __init__(self, size=(0, 0), pos=(0, 0), on_press=lambda: None, label=Label()):
        """
        :param size: Tuple(width, height)
        :param pos: Tuple(x, y)
        :param on_press: Callable
        :param label: Label object
        :return: Button object
        """

        self.__image = pygame.image.load('Рома доделай и подгони по размеру').convert_alpha()  # TODO

        self.__rect = self.__image.get_rect()
        self.__rect.move_ip(pos)

        self.__label = label

        self.on_press = on_press

    def blit_me(self, surface):
        self.__label.blit_me(self.__image)
        surface.blit(self.__image, self.__rect)

    @property
    def rect(self):
        return self.__rect


def create_button(config, creator, size=(0, 0), pos=(0, 0)):
    pass
