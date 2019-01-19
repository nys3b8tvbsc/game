"""
Module provides main game class.
"""
import sys

import pygame


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

    def __init__(self, player, enemies, cards):
        """Initialization of pygame and game objects."""
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.player = player
        self.enemies = enemies
        self.cards = cards

    def start(self):
        """Main game loop."""
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            self.game_logic()
            self.screen_update()
            pygame.display.update()
            clock.tick(self.FPS)

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

    def screen_update(self):
        pass

    def quest(self):
        pass
