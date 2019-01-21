"""
TODO
"""
from abc import ABCMeta, abstractmethod

import pygame


class Scene(metaclass=ABCMeta):
    def __init__(self, back, screen):
        self.back = pygame.image.load(back).convert_alpha()
        self.back = pygame.transform.scale(self.back, (screen.get_width(), screen.get_height() - 100))
        self.back_rect = self.back.get_rect()
        self.screen = screen
        self.pos = (0, 100)

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def blit_me(self):
        self.screen.blit(self.back, self.pos)

    @abstractmethod
    def handle_events(self):
        pass


class Battle(Scene):
    def __init__(self, back, screen):
        Scene.__init__(self, back, screen)

    def update(self):
        pass

    def blit_me(self):
        Scene.blit_me(self)

    def handle_events(self):
        pass


class Quest(Scene):
    def __init__(self, back, screen):
        Scene.__init__(self, back, screen)

    def update(self):
        pass

    def blit_me(self):
        Scene.blit_me(self)

    def handle_events(self):
        pass


def create_scene(scene_info: dict):
    pass


"""
pygame.init()
screen = pygame.display.set_mode()
q = Quest('pictures/BG/battleback1.png', screen)
q.blit_me()
pygame.display.update()
clock = pygame.time.Clock()
param = True
while param:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            param = False
    clock.tick(60)
"""
