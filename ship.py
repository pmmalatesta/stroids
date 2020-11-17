import utilities, pygame
import math,sys,os,random
class Ship:
    def __init__(self,pos):
        self.pos = pos
        self.vel = [0,0]
        self.angle = 90
        self.angVel = 0
        self.thrust = False
        self.front = utilities.angle_to_vector(self.angle)
        self.lives = 3
        self.image = pygame.Surface([30, 30])
        self.detAng = 0;
        #self.image.fill(utilities.WHITE)
        pygame.draw.polygon(self.image, utilities.WHITE, [(15, 0), (5, 25), (25, 25)])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.angac=0
        self.clean = self.image.copy()

    def getPos(self):
        return self.pos[0], self.pos[1]

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
        self.vel[0] -= self.vel[0]*friction
        self.vel[1] -= self.vel[1] * friction
        self.angVel+= self.angac
        if self.angVel>0:
            self.angVel -= self.angVel*angfric
        if self.angVel<0:
            self.angVel -= self.angVel*angfric

    def rotSpeed(self,ang):
        self.angac = ang

    def shoot(self):
        print('babababababa')

    