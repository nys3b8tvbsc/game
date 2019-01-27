"""
Module provides top panel.
"""
import pygame

from constants import BLACK


class Panel:
    def __init__(self, screen_width):
        """
        :param int screen_width:
        :rtype: Panel
        """
        width = screen_width
        pos = 0, 0
        self.main_surface = pygame.image.load('pictures/panel.png').convert_alpha()
        height = int(self.main_surface.get_height() * width / self.main_surface.get_width())
        self.main_surface = pygame.transform.scale(self.main_surface, (width, height))
        self.rect = self.main_surface.get_rect()
        self.font = pygame.font.Font(None, 20)
        self.text_color = BLACK

    def blit_me(self, surface, hero):
        hp = '{}/{}'.format(hero['hp'], hero['max_hp'])
        mana = '{}/{}'.format(hero['mana'], hero['max_mana'])  # TODO refactor energy
        t_hp = self.font.render('HP', 0, self.text_color)
        i_hp = self.font.render(hp, 0, self.text_color)
        t_mana = self.font.render('Mana', 0, self.text_color)
        i_mana = self.font.render(mana, 0, self.text_color)
        self.main_surface.blit(t_hp, (10, 10))
        self.main_surface.blit(t_mana, (10, 30))
        self.main_surface.blit(i_hp, (70, 10))
        self.main_surface.blit(i_mana, (70, 30))
        surface.blit(self.main_surface, self.rect)

    """
    def update(self, hero):
        self.hp = '{}/{}'.format(hero['hp'], hero['max_hp'])
        self.mana = '{}/{}'.format(hero['mana'], hero['max_mana'])
    """

    def handle_event(self, event):
        pass
