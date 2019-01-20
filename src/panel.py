import pygame


class Panel:
    def __init__(self, screen: pygame.Surface, players_config: dict):
        self.screen = screen
        self.size = screen.get_width(), 50
        self.pos = 0, 0
        self.color = (128, 64, 64)
        self.main_surface = pygame.Surface(self.size)
        self.main_surface.fill(self.color)
        self.font = pygame.font.Font(None, 20)
        self.text_color = (0, 0, 0)
        self.text11 = self.font.render('HP', 0, self.text_color)
        self.text12 = self.font.render('25/100', 0, self.text_color)
        self.text21 = self.font.render('Mana', 0, self.text_color)
        self.text22 = self.font.render('50/100', 0, self.text_color)

    def blit_me(self):
        self.main_surface.blit(self.text11, (10, 10))
        self.main_surface.blit(self.text21, (10, 30))
        self.main_surface.blit(self.text12, (70, 10))
        self.main_surface.blit(self.text22, (70, 30))
        self.screen.blit(self.main_surface, self.pos)


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
