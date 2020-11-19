import pygame, math, random, utilities

class Rock(pygame.sprite.Sprite):
    def __init__(self,wid,hei,BASEV, lifespan):
        pygame.sprite.Sprite.__init__(self)
        quad= random.randint(1,4)
        self.speed = BASEV
        self.pos = self.assignPos(quad,wid,hei)
        self.vel = self.assignVels(quad,wid,hei)
        self.pic = pygame.image.load('bstroid.png')
        self.pic.set_colorkey(utilities.WHITE)
        self.pic.convert_alpha()
        self.image = pygame.Surface([81, 81])
        self.image.blit(self.pic, (0,0))
        self.age = 0
        self.expiration = lifespan
        self.angSpeed = random.randint(-15,15)
        self.angle = 0
        self.clean = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos


    def assignPos(self,quad,wid,hei):
        if quad == 1:
            return [-50, random.randint(0,hei)]
        if quad == 2:
            return [random.randint(0,wid), hei + 50]
        if quad == 3:
            return [wid + 50, random.randint(0, hei)]
        if quad == 4:
            return [random.randint(0, wid), -50]


    def assignVels(self,quad, wid, hei):
        if quad == 1:
            if self.pos[1] > hei/2:
                ang = math.radians(random.randint(0,45))
            else:
                ang = -math.radians(random.randint(0, 45))
        if quad ==3:
            if self.pos[1] > hei / 2:
                ang = math.radians(random.randint(135, 180))
            else:
                ang = -math.radians(random.randint(135, 180))
        if quad == 2:
            if self.pos[0] > wid/2:
                ang = math.radians((random.randint(90,135)))
            else:
                ang = math.radians((random.randint(45, 90)))
        if quad == 4:
            if self.pos[0] < wid/2:
                ang = -math.radians((random.randint(90,135)))
            else:
                ang = -math.radians((random.randint(45, 90)))
        return [self.speed*math.cos(ang), self.speed*math.sin(-ang)]