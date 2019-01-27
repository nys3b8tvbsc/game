"""
Module provides main game class.
"""
import sys

import pygame

from loading import load_hero, load_next_quest
from panel import Panel
from scene import create_scene


class Game:
    """
    Main game class.
    Provides initialization of all game objects,
    main game loop,
    events handling,
    all game logic,
    display updating.
    """
    FPS = 60

    def __init__(self, player_file):
        """
        Initialization of pygame and game objects.

        :param str player_file: path
        :rtype: Game
        """
        pygame.init()
        self._screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self._panel = Panel(self.__screen.get_width())
        self._hero = load_hero(player_file)  # Type dict
        self._quest = load_next_quest()  # Type dict
        self._scene = create_scene(self._screen.get_size(), self._quest)

    def start(self):
        """Main game loop."""
        clock = pygame.time.Clock()
        pygame.display.update()
        while True:
            clock.tick(self.FPS)
            self.handle_events()
            self.game_logic()
            self.screen_blit()

    def handle_events(self):
        """Handles events:
            game quit
            alt + f4
            mouse left click
            TODO
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and event.mod == pygame.KMOD_LALT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if self._scene.rect.collidepoint(event.pos):
                        self._scene.handle_event(event)
                    elif self._panel.rect.collidepoint(event.pos):
                        self._panel.handle_event(event)

    def game_logic(self):
        self._scene.update(self._hero)
        self._panel.update(self._hero)
        # TODO ??

    def screen_blit(self):
        self._scene.blit_me(self._screen)
        self._panel.blit_me(self._screen)
        if self._scene.is_over:
            self._scene.get_data()  # TODO refactor ??
            # TODO if data ...
