"""
TODO
"""
from abc import ABCMeta, abstractmethod

import pygame


class Scene(metaclass=ABCMeta):
    def __init__(self, image, screen_size):
        width = screen_size[0]
        self.image = pygame.image.load(image).convert_alpha()
        height = int(self.image.get_height() * width / self.image.get_width())
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect[0] = 0, screen_size[1] - height

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def blit_me(self, screen):
        screen.blit(self.image, self.rect)

    @abstractmethod
    def handle_event(self, event):
        pass

    @property
    @abstractmethod
    def is_over(self):
        pass

    @abstractmethod
    def get_data(self):
        """
        :return: Dict
        """
        pass


class Battle(Scene):
    def __init__(self, screen_size, scene_config):
        Scene.__init__(self, scene_config['image'], screen_size)

    def update(self):
        pass

    def blit_me(self, screen):
        Scene.blit_me(self, screen)

    def handle_event(self, event):
        pass

    @property
    def is_over(self):
        pass

    def get_data(self):
        pass


class Quest(Scene):
    def __init__(self, screen_size, scene_config):
        Scene.__init__(self, scene_config['image'], screen_size)

    def update(self):
        pass

    def blit_me(self, screen):
        Scene.blit_me(self, screen)

    def handle_event(self, event):
        pass

    @property
    def is_over(self):
        pass

    def get_data(self):
        pass


def create_scene(screen_size, scene_config):
    """
    :param screen_size: Tuple(width, height)
    :param scene_config: Dict
    :return: Union[Battle, Quest] object
    """
    pass
