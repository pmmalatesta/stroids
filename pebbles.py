import pygame, math, random, utilities

class Pebbles(pygame.sprite.Sprite):
    def __init__(self,pos,lifespan,spood,ang):
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
        if random.randint(0,1) > 0:
            self.pic = pygame.image.load('lstroid1.png')
        else:
            self.pic = pygame.image.load('lstroid2.png')

        self.pic.set_colorkey(utilities.WHITE)
        self.pic.convert_alpha()
        self.image = pygame.Surface([45,45])
        self.image.blit(self.pic, (0, 0))
        self.clean = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.angSpeed = random.randint(-15, 15)