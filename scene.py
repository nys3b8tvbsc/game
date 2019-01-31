import os
from abc import ABCMeta, abstractmethod
from button import *
import pygame
from  constants import *
from label import Label


class Scene(metaclass=ABCMeta):
    def __init__(self, image, screen_size, scene_config):
        self._config = scene_config

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

    def create_button_fun(self):
        pass


class Battle(Scene):
    def __init__(self, screen_size, scene_config):
        self._image_path = os.path.join('BG', scene_config['image'])
        Scene.__init__(self, self._image_path, screen_size, scene_config)

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
        Scene.__init__(self, self._image_path, screen_size, scene_config)
        self._buttons=[]
        self._buttons.append(Button((DEFAULT_W,DEFAULT_H),BUT1_POS,scene_config["buttons"][0]["text"],scene_config["buttons"][0]["on_click"]))
        self._buttons.append(Button((DEFAULT_W, DEFAULT_H), BUT2_POS, scene_config["buttons"][1]["text"],scene_config["buttons"][1]["on_click"]))
        self._label=Label(scene_config["text"],pos=(DEFAULT_LABEL[0],DEFAULT_LABEL[1]),size=(DEFAULT_LABEL[2],DEFAULT_LABEL[3]),font_name='fonts/PhillippScript.ttf',color=WHITE)
    def update(self):
        pass

    def blit_me(self, surface):
        self._label.blit_me(self._image)
        for button in self._buttons:
            button.blit_me(self._image)
        Scene.blit_me(self, surface)

    def handle_event(self, event):
        pass

    @property
    def is_over(self):
        pass


def create_scene(screen_size, scene_config):
    if scene_config['type'] == 'quest':
        return Quest(screen_size, scene_config)
    elif scene_config['type'] == 'battle':
        return Battle(screen_size, scene_config)
    else:
        raise ValueError('Scene has unknown type.')
