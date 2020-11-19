import pygame, rock, math
spawnDelay = 30
class iceRocks(pygame.sprite.Sprite):
    def __init__(self,wid,hei):
        self.wid = wid
        self.hei = hei
        self.largeRocks = []
        self.smallRocks = []
        self.bspeed = 25
        self.life = math.sqrt(wid*wid+hei*hei)/self.bspeed
        self.ticker = 0


    def createbigRock(self):
        self.largeRocks.append(rock.Rock(self.wid,self.hei, self.bspeed, self.life))

    def updaterocks(self):
        j=[]
        for boulder in self.largeRocks:
            boulder.pos[0] += boulder.vel[0]
            boulder.pos[1] += boulder.vel[1]
            boulder.age +=1
            if boulder.age < boulder.expiration:
                j.append(boulder)
        self.largeRocks = j
        self.ticker +=1
        if self.ticker > spawnDelay:
            self.ticker=0
            self.createbigRock()
