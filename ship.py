import utilities
import math,sys,os,random
class Ship:
    def __init__(self,pos):
        self.pos = pos
        self.vel = [0,0]
        self.angle = (3.14/2.0)
        self.angVel = 0
        self.thrust = False
        self.front = utilities.angle_to_vector(self.angle)
        self.lives = 3

    def getPos(self):
        return self.pos[0], self.pos[1]


    def set_thrust(self,thruster):
        self.thrust = thruster


    def updatePos(self,wid,hei):
        self.pos[0] = self.pos[0] + self.vel[0]
        self.pos[1] = self.pos[1] + self.vel[1]
        self.angle += self.angVel


    def updateVels(self):
        accel = 1
        self.front = utilities.angle_to_vector(self.angle)
        friction = accel/20
        if self.thrust:
            self.vel[0] += self.front[0]*accel
            self.vel[1] += self.front[1] * accel;
        self.vel[0] -= self.vel[0]*friction
        self.vel[1] -= self.vel[1] * friction

    def rotSpeed(self,ang):
        self.angVel+= ang

    