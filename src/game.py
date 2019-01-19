import sys

import pygame


class Game():
    FPS = 60

    def __init__(self, player, enemies, cards):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.player = player
        self.enemies = enemies
        self.cards = cards

    def start(self):
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            self.game_logic()
            self.screen_update()
            pygame.display.update()
            clock.tick(self.FPS)

    def handle_events(self):
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

