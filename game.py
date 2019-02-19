import sys

import pygame

from const.event import QUIT, START_BATTLE, TAKE_DAMAGE, ENEMY_DAMAGE, BATTLE_END, REGEN
from loading import load_hero, load_next_quest, load_battle
from panel import Panel
from scene import create_scene


class Game:
    FPS = 60

    def __init__(self, player_file):
        pygame.init()
        self._screen = pygame.display.set_mode((0, 0), (pygame.FULLSCREEN | pygame.DOUBLEBUF))
        self._panel = Panel(self._screen.get_width())
        self._hero = load_hero(player_file)
        self._quest = load_next_quest()
        self._scene = create_scene(self._screen.get_size(), self._quest)

    def start(self):
        clock = pygame.time.Clock()
        pygame.display.update()
        while True:
            clock.tick(self.FPS)
            self.handle_events()
            self.update()
            self.screen_blit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT or event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and event.mod == pygame.KMOD_LALT:
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos == BATTLE_END:
                    print("jjj")
                elif event.pos == REGEN:
                    self._hero = self._scene.hero_info
                    self._panel.update(self._hero)
                self._scene.handle_event(event)  # TODO ??
                self._panel.handle_event(event)

            elif event.type == ENEMY_DAMAGE:
                self._hero = self._scene.hero_info
                self._panel.update(self._hero)

            elif event.type == START_BATTLE:
                self._scene = create_scene(self._screen.get_size(), load_battle(self._quest['battle']), self._hero)
                self._panel.handle_event(event)

            elif event.type == TAKE_DAMAGE:
                self._hero = self._scene.hero_info
                self._panel.update(self._hero)

            else:
                self._scene.handle_event(event)
                self._panel.handle_event(event)

    def update(self):
        self._scene.update()

    def screen_blit(self):
        self._scene.blit_me(self._screen)
        self._panel.blit_me(self._screen)
        pygame.display.update()
