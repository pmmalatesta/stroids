import pygame
from pygame.locals import *

TURNRATE = 1
F_ACCEL = 15
R_ACCEL = -5

def keydown(event,ship):
    angAc=1;
    bullVel = 25
    if event.key == K_a:
        ship.rotSpeed(angAc)
    if event.key == K_d:
        ship.rotSpeed(-angAc)
    if event.key == K_w:
        ship.set_thrust(True)
    if event.key == K_SPACE:
        ship.shoot(ship.getPos(),ship.angle,bullVel)
        #ship.lives -=1
def keyup(event,ship):
    if event.key in (K_a,K_d):
        ship.rotSpeed(0)
    if event.key == K_w:
        ship.set_thrust(False)