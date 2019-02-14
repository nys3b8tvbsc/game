import pygame

from const.animation import DEFAULT
from const.event import ENEMY_TOUCH


class Gang:
    def __init__(self, enemies):
        self._enemies = list(enemies)
        self._active = None

    def click(self, xy):
        for enemy in self._enemies:
            if enemy.click(xy):
                self._active = enemy
                pygame.event.post(pygame.event.Event(ENEMY_TOUCH, {}))

    def positioning(self):
        pass

    def blit_me(self, surface):
        for enemy in self._enemies:
            enemy.blit_me(surface)

    def animated(self):
        for enemy in self._enemies:
            enemy.animated()

    def dead(self):
        for enemy in self._enemies.copy():
            if enemy.is_dead and enemy.state == DEFAULT:
                self._enemies.remove(enemy)

    def __len__(self):
        return len(self._enemies)
