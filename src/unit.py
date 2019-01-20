from abc import ABCMeta, abstractmethod

import pygame


class Unit(pygame.sprite.Sprite, metaclass=ABCMeta):
    """Abstract base class for all other units.
    Provides methods for display on screen.
    And methods for interaction between characters.
    """

    def __init__(self, level: int): #""" image: str"""
        """
        Unit`s level should be 1 or more.
        Img_path is absolute or relative path to unit`s sprite picture."""
        assert level >= 1
        self.level = level
        #self.image = pygame.image.load(image).convert_alpha()

    @abstractmethod
    def blit(self, screen):
        """Method for displaying character on screen"""
        pass

    @abstractmethod
    def take_damage(self, damage: int):
        pass

    #@abstractmethod
    #def attack_animation(self):
        #pass


# TODO ?? HP

class Player(Unit):
    def __init__(self, cards):
        Unit.__init__(self, level=1)
        self.cards = cards

    def take_damage(self, damage: int):
        pass
