import pygame

class Animation:
    def __init__(self,cadrs,n):
        self.cadrs=[]
        for i in range(n):
            path=cadrs+'_'+str(i+1)+'.png'
            temp=pygame.image.load(path).convert_alpha()
            self.cadrs.append(temp)
        self.n=n
        self.number=0
        self.cadr=self.cadrs[0]
    def update(self):
        self.number+=1
        if self.number==self.n:
            self.number=0
            self.cadr=self.cadrs[0]
            return False
        self.cadr = self.cadrs[self.number]
        return True

"""
pygame.init()
srf=pygame.display.set_mode((1000,500))
anim=Animation('pictures/Archive (1)/idle-walk/idle',6)
srf.blit(anim.cadr,(0,0))
pygame.display.update()
clock = pygame.time.Clock()
param=True
while param:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            param=False
    srf.fill((0,0,0))
    srf.blit(anim.cadr, (0, 0))
    anim.update()
    pygame.display.update()
    clock.tick(15)
"""