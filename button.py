import pygame


class Button:
    def __init__(self, pos, size, label, on_click, color):
        """
        :param pos: Tuple(x, y)
        :param size: Tuple(width, height)
        :param label: Label object
        :param on_click: Callable
        :param color: Tuple(R, G, B)
        """
        pygame.sprite.Sprite().__init__(self)
        self.surface = pygame.Surface(size)
        self.surface.fill(color)
        self.rect = (pos, size)
        self.label = label
        self.label.set_rect(center=(size[0] / 2, size[1] / 2))

        self.on_click = on_click

    def blit_me(self, screen):
        self.label.blit_me(self.surface)
        screen.blit(self.surface, self.rect)


def create_button(config):
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
