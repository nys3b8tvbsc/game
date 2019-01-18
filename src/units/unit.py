from abc import ABCMeta, abstractmethod

import pygame


class Unit(pygame.sprite.Sprite, metaclass=ABCMeta):
    def __init__(self, level: int, img_path: str):
        self.level = level
        self.image = pygame.image.load(img_path).convert()

    # ?? @abstractmethod
    def blit(self, screen):
        pass

    @abstractmethod
    def take_damage(self, damage: int):
        pass

    @abstractmethod
    def attack_animation(self):
        pass

# TODO ?? HP
