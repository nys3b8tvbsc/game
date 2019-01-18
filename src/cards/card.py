from abc import ABCMeta
from typing import Dict

import pygame


class Card(pygame.sprite.Sprite, metaclass=ABCMeta):
    def __init__(self, img_path: str, params: Dict):
        self.image = pygame.image.load(img_path).convert()
        self.params = params

    def blit(self, screen):
        pass
