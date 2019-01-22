import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, size, text, on_click, color):
        """

        :param pos: Tuple(x, y)
        :param size: Tuple(width, height)
        :param text: str
        :param on_click: Callable
        :param color: Tuple(R, G, B)
        """
        pygame.sprite.Sprite().__init__(self)
        self.rect = pygame.Rect(pos, size)
        self.rect.fill(color)

    def blit_me(self):
        pass
