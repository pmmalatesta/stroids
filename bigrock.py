import pygame, rock, math, utilities
spawnDelay = 25
class iceRocks(pygame.sprite.Sprite):
    def __init__(self,wid,hei):
        pygame.sprite.Sprite.__init__(self)
        self.wid = wid
        self.hei = hei
        self.largeRocks = []
        self.smallRocks = []
        self.bspeed = 15
        self.life = math.sqrt(wid*wid+hei*hei)/self.bspeed
        self.ticker = 0
        self.sprlist = pygame.sprite.Group()


    def createbigRock(self):
        self.sprlist.add(rock.Rock(self.wid,self.hei, self.bspeed, self.life))

    def updaterocks(self):
        for boulder in self.sprlist:
            boulder.pos[0] += boulder.vel[0]
            boulder.pos[1] += boulder.vel[1]
            boulder.angle += boulder.angSpeed
            boulder.image = utilities.rot(boulder.clean, boulder.angle)
            boulder.age +=1
            if boulder.age > boulder.expiration:
                boulder.kill()
        self.ticker +=1
        if self.ticker > spawnDelay:
            self.ticker=0
            self.createbigRock()
