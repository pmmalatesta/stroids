import pygame, rock, math, utilities, pebbles, random
class Rocklist(pygame.sprite.Group):
    def __init__(self,wid,hei):
        pygame.sprite.Group.__init__(self)
        self.wid = wid
        self.hei = hei
        self.spawndelay = 60
        self.largeRocks = []
        self.smallRocks = []
        self.bspeed = 15
        self.life = math.sqrt(wid*wid+hei*hei)/self.bspeed
        self.ticker = 0



    def createbigRock(self):
        self.add(rock.Rock(self.wid,self.hei, self.bspeed, self.life))

    def updaterocks(self):
        for boulder in self:
            boulder.pos[0] += boulder.vel[0]
            boulder.pos[1] += boulder.vel[1]
            boulder.rect.center = boulder.pos
            boulder.angle += boulder.angSpeed
            boulder.image = utilities.rot(boulder.clean, boulder.angle)
            boulder.age +=1
            if boulder.age > boulder.expiration:
                boulder.kill()
        self.ticker +=1
        if self.ticker > self.spawndelay:
            self.ticker=0
            self.createbigRock()

    def createsmallrocks(self, bigboy):
        angle = random.randint(0,180)
        angle2 = angle + random.randint(150,210)
        self.add(pebbles.Pebbles(bigboy.getpos(), bigboy.expiration*1.5,self.bspeed/1.5,angle,bigboy.col))
        self.add(pebbles.Pebbles(bigboy.getpos(), bigboy.expiration*1.5,self.bspeed/1.5,angle2,bigboy.col))