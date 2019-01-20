"""
Module provides Animation class for units animations.
"""
import pygame


class Animation:
    """
    TODO
    """

    def __init__(self, frames, n):
        """
        :param frames: str
        :param n: int
        :return: Animation object
        """
        self.frames = []
        for i in range(1, n + 1):
            path = frames + '_{}.png'.format(i)
            frame = pygame.image.load(path).convert_alpha()
            self.frames.append(frame)
        self.n = n
        self.number = 0
        self.frame = self.frames[0]

    def update(self):
        """
        Get next frame.

        :return: False if animation starts from the beginning, else True.
        """
        self.number += 1
        if self.number == self.n:
            self.number = 0
            self.frame = self.frames[0]
            return False
        self.frame = self.frames[self.number]
        return True


"""
pygame.init()
srf = pygame.display.set_mode((1000, 500))
animation = Animation('pictures/Archive (1)/idle-walk/idle', 6)
srf.blit(animation.frame, (0, 0))
pygame.display.update()
clock = pygame.time.Clock()
param = True
while param:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            param = False
    srf.fill((0, 0, 0))
    srf.blit(animation.frame, (0, 0))
    animation.update()
    pygame.display.update()
    clock.tick(15)
"""
