"""
Module provides top panel.
"""
import pygame


class Panel:
    """
    TODO
    """

    def __init__(self, screen_width):

        """
        :param screen: pygame.Surface
        :param players_config: Dict
        :return: Panel object
        """
        self.width = screen_width
        self.pos = 0, 0
        self.main_surface = pygame.image.load('pictures/panel.png').convert_alpha()
        self.height=int(self.main_surface.get_height()*self.width/self.main_surface.get_width())
        self.main_surface=pygame.transform.scale(self.main_surface,(self.width,self.height))
        self.rect=self.main_surface.get_rect()
        self.font = pygame.font.Font(None, 20)
        self.text_color = (0, 0, 0)

    def blit_me(self,surface,hero):
        """
        TODO
        """
        self.hp = '{}/{}'.format(hero['hp'], hero['max_hp'])
        self.mana = '{}/{}'.format(hero['mana'], hero['max_mana'])
        self.text11 = self.font.render('HP', 0, self.text_color)
        self.text12 = self.font.render(self.hp, 0, self.text_color)
        self.text21 = self.font.render('Mana', 0, self.text_color)
        self.text22 = self.font.render(self.mana, 0, self.text_color)
        self.main_surface.blit(self.text11, (10, 10))
        self.main_surface.blit(self.text21, (10, 30))
        self.main_surface.blit(self.text12, (70, 10))
        self.main_surface.blit(self.text22, (70, 30))
        surface.blit(self.main_surface, self.pos)

"""
    def update(self, hero):
        self.hp = '{}/{}'.format(hero['hp'], hero['max_hp'])
        self.mana = '{}/{}'.format(hero['mana'], hero['max_mana'])
"""

pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
i = Panel(screen.get_width())
i.blit_me(screen,{'hp':50,'max_hp':100,'mana':25,'max_mana':100})
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

