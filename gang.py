import pygame

from const.animation import DEFAULT
from const.event import ENEMY_TOUCH, TURN_END


class Gang:
    def __init__(self, enemies, screen_size):
        self._enemies = list(enemies)
        self._active = None
        self.positioning(screen_size)
        self.attack_init()

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
            enemy.move_to(pos, y - enemy.rect.height)
            pos += enemy.rect.width + int(0.03 * screen_size[0])

    def dead(self):
        for enemy in self._enemies.copy():
            if enemy.is_dead and enemy.state == DEFAULT:
                self._enemies.remove(enemy)

    def is_dead(self):
        return all((enemy.is_dead for enemy in self._enemies))

    def attack(self, hero):
        self._enemies[self.attacking].walking(self.v)
        if self._enemies[self.attacking].rect.x == self.start_pos:
            self.v = -self.v
            self.attacking += 1
            if self.attacking == len(self):
                pygame.event.post(pygame.event.Event(TURN_END, {}))
                return
            self.start_pos = self._enemies[self.attacking].rect.x
        elif self._enemies[self.attacking].rect.x == hero.rect.x + int(
                self._enemies[self.attacking]._at_pos * hero.rect.width):
            self.v = -self.v
            self._enemies[self.attacking].walking(self.v)
            self._enemies[self.attacking].attack(hero)

    def attack_init(self):
        self.attacking = 0
        self.start_pos = self._enemies[0].rect.x
        self.v = -1

    def __len__(self):
        return len(self._enemies)
