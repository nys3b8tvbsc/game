"""
Module provides top panel.
"""
import pygame


class Panel:
    """
    TODO
    """

    def __init__(self, screen, hero):
        """
        :param screen: pygame.Surface
        :param players_config: Dict
        :return: Panel object
        """
        self.screen = screen
        self.size = screen.get_width(), 50
        self.pos = 0, 0
        self.color = (128, 64, 64)
        self.main_surface = pygame.Surface(self.size)
        self.main_surface.fill(self.color)
        self.font = pygame.font.Font(None, 20)
        self.text_color = (0, 0, 0)
        self.hp = '{}/{}'.format(hero['hp'], hero['max_hp'])
        self.mana = '{}/{}'.format(hero['mana'], hero['max_mana'])
        self.text11 = self.font.render('HP', 0, self.text_color)
        self.text12 = self.font.render(self.hp, 0, self.text_color)
        self.text21 = self.font.render('Mana', 0, self.text_color)
        self.text22 = self.font.render(self.mana, 0, self.text_color)

    def blit_me(self):
        """
        TODO
        """
        self.main_surface.blit(self.text11, (10, 10))
        self.main_surface.blit(self.text21, (10, 30))
        self.main_surface.blit(self.text12, (70, 10))
        self.main_surface.blit(self.text22, (70, 30))
        self.screen.blit(self.main_surface, self.pos)

    def update(self, hero):
        self.hp = '{}/{}'.format(hero['hp'], hero['max_hp'])
        self.mana = '{}/{}'.format(hero['mana'], hero['max_mana'])


"""
pygame.init()
screen = pygame.display.set_mode()
i = Panel(screen, {})
i.blit_me()
pygame.display.update()
clock = pygame.time.Clock()
param = True
while param:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            param = False
    pygame.display.update()
    clock.tick(60)
"""
