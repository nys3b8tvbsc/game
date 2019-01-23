import pygame
from constans import BLACK, WHITE

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, size, text, on_click, color):
        """

        :param pos: Tuple(x, y)
        :param size: Tuple(width, height)
        :param text: str
        :param on_click: Callable
        :param color: Tuple(R, G, B)
        """
        pygame.sprite.Sprite().__init__(self)
        self.rect = pygame.Rect(pos, size)
        self.rect.fill(color)

    def blit_me(self):
        pass


def print_txt(surface,rect,text, font, font_size,color): #version 1.0 :)
    f=pygame.font.Font(font,font_size)
    n=rect.width//f.get_linesize()
    while len(text)>n:
        num=text[:n].rfind(' ')+1
        if num<=0:
            num=n
        txt=f.render(text[:num],1,color)
        surface.blit(txt,rect)
        text=text[num:]
        rect.y+=f.get_height()+2
    txt = f.render(text, 1, color)
    surface.blit(txt, rect)

"""
pygame.init()
srf=pygame.display.set_mode()
srf.fill(WHITE)
rect=pygame.Rect((0,0,500,100))
print_txt(srf,rect,'Какой-то непонятный текст, который нужно отобразить в ректе','fonts/DECOR6DI.TTF',30,BLACK)
pygame.display.update()
param=True
while param:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            param = False
"""