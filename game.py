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
        self.screen = pygame.display.set_mode()
        self.__hero = load_player(player_file)  # Type Dict
        self.__quest = load_next_quest()
        self.__scene = create_scene(self.__quest)
        self.__panel = Panel(self.screen, self.__hero)

    def start(self):
        """Main game loop."""
        clock = pygame.time.Clock()
        pygame.display.update()
        while True:
            clock.tick(self.FPS)
            self.handle_events()
            self.game_logic()
            self.screen_update()

    def handle_events(self):
        """Handles events:
            game quit
            TODO
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def game_logic(self):
        pass
        # TODO ??

    def screen_update(self):
        self.__scene.update()