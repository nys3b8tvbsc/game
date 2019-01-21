"""
Module provides main game class.
TODO ohhhh...
"""
import sys

import pygame

from loading import load_player, load_next_quest
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
        :param player_file: path
        """
        pygame.init()
        self.__screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Type pygame.Surface
        self.__panel = Panel(self.__screen)
        self.__panel_rect = self.__panel.get_rect()
        self.__hero = load_player(player_file)  # Type Dict
        self.__quest = load_next_quest()  # Type Dict
        self.__scene = create_scene(self.get_scene_size(), self.__quest)
        self.__scene_rect = self.__scene.get_rect()

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
                if event.button == 1:
                    if self.__scene_rect.collidepoint(event.pos):
                        self.__scene.handle_events()
                    elif self.__panel_rect.collidepoint(event.pos):
                        self.__panel.handle_events()

    def game_logic(self):
        self.__scene.update(self.__hero)
        self.__panel.update(self.__hero)
        # TODO ??

    def screen_blit(self):
        self.__scene.blit_me(self.__screen)
        self.__panel.blit_me(self.__screen)
        if self.__scene.is_over():
            self.__scene.get_data()  # TODO refactor ??
            # TODO if data ...

    def get_scene_rect(self):  # tuple tuple pos, tuple rect
        pass  # self.__panel_rect / self.screen
