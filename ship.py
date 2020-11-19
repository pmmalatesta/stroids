import utilities, pygame, bang
import math,sys,os,random
class Ship(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.vel = [0,0]
        self.angle = 90
        self.angVel = 0
        self.thrust = False
        self.front = utilities.angle_to_vector(self.angle)
        self.lives = 3
        self.image = pygame.Surface([51, 51])
        self.detAng = 0;
        self.pic = pygame.image.load('shipp.png')
        self.pic.set_colorkey(utilities.WHITE)
        self.pic.convert_alpha()
        #self.image.fill(utilities.WHITE)----------------------------
        self.image.blit(self.pic, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.angac=0
        self.clean = self.image.copy()
        self.bullList = []
        self.pythag = math.sqrt(pos[0]*pos[0]+pos[1]*pos[1])
        pygame.mixer.pre_init()
        self.shootsound = pygame.mixer.Sound('shot.wav')
        self.shootsound.set_volume(1)



    def getPos(self):
        oset = 30;
        cx = self.rect.centerx
        cy = self.rect.centery
        return [cx+oset*math.cos(math.radians(self.angle)), cy+oset*math.sin(math.radians(-self.angle ))]


    def set_thrust(self,thruster):
        self.thrust = thruster

    def updatePos(self,wid,hei):
        self.pos[0] = self.pos[0] + self.vel[0]
        self.pos[1] = self.pos[1] + self.vel[1]
        if self.pos[0] > wid+10:
            self.pos[0]=0
        if self.pos[0]<-10:
            self.pos[0]=wid
        if self.pos[1]> hei+10:
            self.pos[1] = 0
        if self.pos[1]< -10:
            self.pos[1] = hei

        self.angle += self.angVel
        self.angle = self.angle % 360
        self.detAng += self.angVel
        self.detAng = self.detAng%360
        self.image = utilities.rot(self.clean,self.detAng)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
    def updateVels(self):
        accel = .5
        self.front = utilities.angle_to_vector(self.angle)
        friction = accel/18
        angfric = .1
        if self.thrust:
            self.vel[0] += self.front[0]*accel
            self.vel[1] += self.front[1] * accel;
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('thrustsound.mp3'))
        else:
            j=2
            #self.thrustsound.stop()
        self.vel[0] -= self.vel[0]*friction
        self.vel[1] -= self.vel[1] * friction
        self.angVel+= self.angac
        if self.angVel>0:
            self.angVel -= self.angVel*angfric
        if self.angVel<0:
            self.angVel -= self.angVel*angfric

    def rotSpeed(self,ang):
        self.angac = ang

    def shoot(self, loc, direct, quick):
        self.bullList.append(bang.Bang(loc,direct,quick,self.pythag))
        self.shootsound.play()
