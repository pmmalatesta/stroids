import pygame, math, random, utilities

class Pebbles(pygame.sprite.Sprite):
    def __init__(self,pos,lifespan,spood,ang,col):
        pygame.sprite.Sprite.__init__(self)
        self.age = 0
        self.pos = pos
        self.ang = random.randint(0,360)
        self.vel = [0,0]
        self.angle = 0
        self.vel[0] = spood*math.cos(math.radians(ang))
        self.vel[1] = spood * math.sin(math.radians(ang))
        self.expiration = lifespan
        self.big = False
        a= random.randint(0,1)
        if a == 0 & col == 0:
            self.pic = pygame.image.load('lstroid1.png')
        elif a == 1 & col == 0:
            self.pic = pygame.image.load('lstroid2.png')
        elif a == 0:
            self.pic = pygame.image.load('lstroid3.png')
        else:
            self.pic = pygame.image.load('lstroid4.png')
        self.pic.set_colorkey(utilities.WHITE)
        self.pic.convert_alpha()
        self.image = pygame.Surface([45,45],pygame.SRCALPHA)
        self.image.blit(self.pic, (0, 0))
        self.clean = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.angSpeed = random.randint(-15, 15)