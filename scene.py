import os
from abc import ABCMeta, abstractmethod

import pygame


class Scene(metaclass=ABCMeta):
    def __init__(self, image, screen_size):
        width = screen_size[0]
        self._image = pygame.image.load(image).convert_alpha()
        height = int(self._image.get_height() * width / self._image.get_width())
        self._image = pygame.transform.scale(self._image, (width, height))
        self._rect = self._image.get_rect()
        self._rect.move_ip(0, screen_size[1] - height)

    @property
    def rect(self):
        return self._rect

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def blit_me(self, surface):
        surface.blit(self._image, self._rect)

    @abstractmethod
    def handle_event(self, event):
        pass

    @property
    @abstractmethod
    def is_over(self):
        pass


class Battle(Scene):
    def __init__(self, screen_size, scene_config):
        self._image_path = os.path.join('BG', scene_config['image'])
        Scene.__init__(self, self._image_path, screen_size)

    def update(self):
        pass

    def blit_me(self, surface):
        Scene.blit_me(self, surface)

    def handle_event(self, event):
        pass

    @property
    def is_over(self):
        pass


class Quest(Scene):
    def __init__(self, screen_size, scene_config):
        self._image_path = os.path.join('pictures', 'blueframe2.png')
        Scene.__init__(self, self._image_path, screen_size)

    def update(self):
        pass

    def blit_me(self, surface):
        for button in self._buttons:
            button.blit_me(surface)
        Scene.blit_me(self, surface)

    def handle_event(self, event):
        pass

    @property
    def is_over(self):
        pass


def create_scene(screen_size, scene_config):
    if scene_config['type'] == 'quest':
        pass
    elif scene_config['type'] == 'battle':
        pass
    else:
        raise ValueError('Scene has unknown type.')
