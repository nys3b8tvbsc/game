import pygame

from const.animation import DEFAULT
from const.event import ENEMY_TOUCH


class Gang:
    def __init__(self, enemies, screen_size):
        self._enemies = list(enemies)
        self._active = None
        self.positioning(screen_size)

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

    def positioning(self, screen_size):
        pos = int(0.25 * screen_size[0])
        y = int(0.6 * screen_size[1])
        for enemy in self._enemies:
            enemy.move_to(pos, y - enemy._rect.height)
            pos += enemy._rect.width + int(0.03 * screen_size[0])

    def dead(self):
        for enemy in self._enemies.copy():
            if enemy.is_dead and enemy.state == DEFAULT:
                self._enemies.remove(enemy)

    def __len__(self):
        return len(self._enemies)
