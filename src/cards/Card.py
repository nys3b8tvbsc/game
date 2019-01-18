import pygame

class Card(pygame.sprite.Sprite):
    def __init__(self,damage,mana,image,rect):
        self.mana=mana
        self.damage=damage
        self.image=pygame.image.load(image).convert_alpha()
        self.rect=rect
    def blit(self,surf:pygame.Surface):
        surf.blit(self.image,self.rect)

