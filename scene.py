import os
from abc import ABCMeta, abstractmethod

import pygame

from button import Button
from const.button import DEFAULT_H, DEFAULT_W
from const.color import WHITE
from const.event import ENEMY_TOUCH, TURN_END, BATLE_END_POST, REGEN_POST
from const.panel import BUT1_POS, BUT2_POS, DEFAULT_NAME, DEFAULT_EXP, DEFAULT_LABEL
from const.screen import DEFAULT_SIZE
from enemy import create_enemy
from gang import Gang
from label import Label
from loading import load_enemy
from unit import create_hero


class Scene(metaclass=ABCMeta):
    def __init__(self, image, screen_size, scene_config):
        self._config = scene_config
        self._image = pygame.image.load(image).convert_alpha()
        self._image = pygame.transform.scale(self._image, screen_size)
        self._rect = self._image.get_rect()

    @property
    def rect(self):
        return self._rect

    @property
    @abstractmethod
    def is_over(self):
        pass


class Battle(Scene):
    def __init__(self, screen_size, scene_config, hero_config):
        image_path = os.path.join('pictures', 'BG', scene_config['image'])
        Scene.__init__(self, image_path, screen_size, scene_config)
        self._turn_hero = True
        self._enemies = [create_enemy(load_enemy(enemy), screen_size[0]) for enemy in scene_config['enemies']]
        self._enemies = Gang(self._enemies, screen_size)
        self._hero = create_hero(hero_config, screen_size)
        self._hero.move_to(int(screen_size[1] * 0.05), int(screen_size[1] * 0.35))
        H = int(DEFAULT_H * screen_size[1] / DEFAULT_SIZE[1])
        W = int(DEFAULT_W * screen_size[0] / DEFAULT_SIZE[0])
        self._button = Button((W, H), (int(0.05 * screen_size[0]), int(0.3 * screen_size[1])), "Конец хода", TURN_END)

    def update(self):
        self._enemies.animated()
        self._hero.animated()
        self._enemies.dead()
        if self._turn_hero:
            self._hero.hand.hover(pygame.mouse.get_pos())
        else:
            self._enemies.attack(self._hero)
        if len(self._enemies) == 0:
            pygame.event.post(BATLE_END_POST)

    def blit_me(self, surface):
        surface.blit(self._image, self._rect)
        self._hero.blit_me(surface)
        self._enemies.blit_me(surface)
        if self._turn_hero:
            self._button.blit_me(surface)

    def click(self, xy):
        self._enemies.click(xy)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self._turn_hero:
            self.click(event.pos)
            self._hero.hand.click(event.pos)
            self._button.handle_event(event)
        elif event.type == ENEMY_TOUCH:
            if self._hero.hand._selected_card != None:
                self._hero.attack(self._enemies._active, self._hero._hand._selected_card)
        elif event.type == TURN_END:
            self._turn_hero = not self._turn_hero
            if not self._turn_hero:
                self._enemies.attack_init()
            else:
                self._hero.regen()
                self._hero.update_hand()
                pygame.event.post(REGEN_POST)
        else:
            pass  # TODO

    @property
    def is_over(self):
        pass

    @property
    def hero_info(self):
        return self._hero.get_info()


class Quest(Scene):
    def __init__(self, screen_size, scene_config):
        image_path = os.path.join('pictures', 'blueframe2.png')
        Scene.__init__(self, image_path, screen_size, scene_config)
        self._exp = scene_config["exp"]
        self._name = scene_config["name"]
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
        self._lab_name = Label(text=self._name, pos=(DEFAULT_NAME[0], DEFAULT_NAME[1]),
                               size=(DEFAULT_NAME[2], DEFAULT_NAME[3]), color=WHITE,
                               font_name='fonts/PhillippScript.ttf')
        self._lab_exp = Label(text='Опыт за квест: {}'.format(self._exp), pos=(DEFAULT_EXP[0], DEFAULT_EXP[1]),
                              size=(DEFAULT_EXP[2], DEFAULT_EXP[3]), color=WHITE, font_name='fonts/PhillippScript.ttf')

    def update(self):
        pass

    def blit_me(self, surface):
        self._lab_name.blit_me(self._image)
        self._label.blit_me(self._image)
        self._lab_exp.blit_me(self._image)
        for button in self._buttons:
            button.blit_me(self._image)
        surface.blit(self._image, self._rect)

    def click(self, xy):
        for button in self._buttons:
            button.click(xy)

    def handle_event(self, event):
        for button in self._buttons:
            button.handle_event(event)
        # TODO

    @property
    def is_over(self):
        pass


def create_scene(screen_size, scene_config, hero_config=None):
    if scene_config['type'] == 'quest':
        return Quest(screen_size, scene_config)
    elif scene_config['type'] == 'battle':
        return Battle(screen_size, scene_config, hero_config)
    else:
        raise ValueError('Scene has unknown type.')


def add_exp(hero, quest_config):
    hero.exp += quest_config["_exp"]
    if hero.new_level:
        hero.level_up()
