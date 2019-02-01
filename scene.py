import os
from abc import ABCMeta, abstractmethod
from button import *
import pygame
from constants import *
from label import Label
from unit import Hero


class Scene(metaclass=ABCMeta):
    def __init__(self, image, screen_size, scene_config):
        self._config = scene_config

        width = screen_size[0]
        self._image = pygame.image.load(image).convert_alpha()
        height = int(self._image.get_height() * width / self._image.get_width())
        self._image = pygame.transform.scale(self._image, screen_size)
        self._rect = self._image.get_rect()
        self._rect.move_ip(0, 0)

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
        self.exp = scene_config["exp"]
        self.name = scene_config["name"]
        self._buttons = []
        trans_x = screen_size[0] / DEFAULT_SIZE[0]
        trans_y = screen_size[1] / DEFAULT_SIZE[1]
        but1_pos = (int(BUT1_POS[0] * trans_x), int(BUT1_POS[1] * trans_y))
        but2_pos = (int(BUT2_POS[0] * trans_x), int(BUT2_POS[1] * trans_y))
        but_size = (int(DEFAULT_W * trans_x), int(DEFAULT_H * trans_y))
        self._buttons.append(
            Button(but_size, but1_pos, scene_config["buttons"][0]["text"], scene_config["buttons"][0]["on_click"]))
        self._buttons.append(
            Button(but_size, but2_pos, scene_config["buttons"][1]["text"], scene_config["buttons"][1]["on_click"]))
        lab_pos = (int(DEFAULT_LABEL[0] * trans_x), int(DEFAULT_LABEL[1] * trans_y))
        lab_size = (int(DEFAULT_LABEL[2] * trans_x), int(DEFAULT_LABEL[3] * trans_y))
        self._label = Label(scene_config["text"], pos=lab_pos, size=lab_size, font_name='fonts/PhillippScript.ttf',
                            color=WHITE)
        self._lab_name = Label(text=self.name, pos=(DEFAULT_NAME[0], DEFAULT_NAME[1]),
                               size=(DEFAULT_NAME[2], DEFAULT_NAME[3]), color=WHITE,
                               font_name='fonts/PhillippScript.ttf')
        self._lab_exp = Label(text='Опыт за квест: {}'.format(self.exp), pos=(DEFAULT_EXP[0], DEFAULT_EXP[1]),
                              size=(DEFAULT_EXP[2], DEFAULT_EXP[3]), color=WHITE, font_name='fonts/PhillippScript.ttf')

    def update(self):
        pass

    def blit_me(self, surface):
        self._lab_name.blit_me(self._image)
        self._label.blit_me(self._image)
        self._lab_exp.blit_me(self._image)
        for button in self._buttons:
            button.blit_me(self._image)
        Scene.blit_me(self, surface)

    def click(self, xy):
        for button in self._buttons:
            button.click(xy)

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


def add_exp(hero, quest):
    hero.exp += quest.exp
    if hero.new_level:
        hero.level_up()
