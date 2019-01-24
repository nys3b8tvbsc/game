import pygame

from constants import BLACK, WHITE


class Label:
    def __init__(self, size, text, font, font_size, color=WHITE, text_color=BLACK):
        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect()
        self.font = pygame.font.Font(font, font_size)
        self.text = self.font.render(text, 0, text_color)

    def set_rect(self, center):
        self.rect = self.surface.get_rect(center)
