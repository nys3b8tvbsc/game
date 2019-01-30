# TODO min size ? / line wrap
import pygame

from constants import BLACK

"""
def print_txt(surface, rect, text, font, font_size, color):  # version 1.0 :)
    f = pygame.font.Font(font, font_size)
    n = rect.width // f.get_linesize()
    while len(text) > n:
        num = text[:n].rfind(' ') + 1
        if num <= 0:
            num = n
        txt = f.render(text[:num], 1, color)
        surface.blit(txt, rect)
        text = text[num:]
        rect.y += f.get_height() + 2
    txt = f.render(text, 1, color)
    surface.blit(txt, rect)
"""


class Label:
    def __init__(self, text='', size=(0, 0), pos=(0, 0), font_name=None, color=BLACK):
        self._raw_text = text
        if isinstance(text, str):
            strings = (text,)
        elif isinstance(text, int) or isinstance(text, float):
            strings = (str(text),)
        else:
            strings = tuple(text)

        self.__size = size
        self.__font_name = font_name

        self.__font_size = self.calc_size(strings)

        self.__font = pygame.font.Font(font_name, self.__font_size)
        self.__spacing = self.__font.get_linesize()
        self.__positions = self.calc_pos(strings, pos)
        self.__strings = tuple(self.__font.render(string, 1, color) for string in strings)

    def calc_size(self, strings):
        width, height = self.__size
        for font_size in range(6, 10 ** 5):
            font = pygame.font.Font(self.__font_name, font_size)
            sizes = [font.size(string) for string in strings]
            for size in sizes:
                if size[0] > width:
                    return font_size - 1
            if (2 * len(strings) - 1) * font.get_linesize() > height:
                return font_size - 1

    def calc_pos(self, strings, pos):
        width, height = self.__size
        positions = []
        for i, string in enumerate(strings):
            x = pos[0] + (width - self.__font.size(string)[0]) / 2
            y = pos[1] + i * self.__font.get_linesize()
            positions.append((x, y))
        return tuple(positions)

    def blit_me(self, surface):
        for string, pos in zip(self.__strings, self.__positions):
            surface.blit(string, pos)

    def get_info(self):
        return self._raw_text
