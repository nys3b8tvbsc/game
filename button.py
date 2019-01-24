import pygame


class Button:
    def __init__(self, pos, label, on_click):
        """
        :param pos: Tuple(x, y)
        :param label: Label object
        :param on_click: Callable
        """
        self.label = label
        self.label.rect[0] = pos
        self.rect = self.label.rect

        self.on_click = on_click

    def blit_me(self, screen):
        self.label.blit_me(self.screen)


def create_button(config):
    pass


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
