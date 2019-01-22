"""
Module provides top panel.
"""
import pygame

from constans import BLACK


class Panel:
    """
    TODO
    """

    def __init__(self, screen_width):
        """
        :param screen_width: int
        :return: Panel object
        """
        width = screen_width
        self.pos = 0, 0
        self.main_surface = pygame.image.load('pictures/panel.png').convert_alpha()
        height = int(self.main_surface.get_height() * width / self.main_surface.get_width())
        self.main_surface = pygame.transform.scale(self.main_surface, (width, height))
        self.rect = self.main_surface.get_rect()
        self.font = pygame.font.Font(None, 20)
        self.text_color = BLACK

    def get_rect(self):
        """
        :return: pygame.Rect object
        """
        return self.rect

    def blit_me(self, surface, hero):
        """
        TODO
        """
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
        surface.blit(self.main_surface, self.pos)

    """
    def update(self, hero):
        self.hp = '{}/{}'.format(hero['hp'], hero['max_hp'])
        self.mana = '{}/{}'.format(hero['mana'], hero['max_mana'])
    """

    def handle_event(self, event):
        pass


pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
i = Panel(screen.get_width())
i.blit_me(screen, {'hp': 50, 'max_hp': 100, 'mana': 25, 'max_mana': 100})
pygame.display.update()
clock = pygame.time.Clock()
param = True
while param:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            param = False
        elif event.type==pygame.KEYDOWN:
            param = False
    pygame.display.update()
    clock.tick(60)
