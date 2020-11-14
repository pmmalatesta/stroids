import pygame
from pygame.locals import *

TURNRATE = 15*3.14/180.0
F_ACCEL = 15
R_ACCEL = -5
def keydown(event,ship):
    ang_vel = 4.5
    if event.key == K_a:
        ship.rotSpeed(-ang_vel)
    if event.key == K_d:
        ship.rotSpeed(ang_vel)
    if event.key == K_w:
        ship.set_thrust(True)
    if event.key == K_SPACE:
        #ship.shoot()
        ship.lives -= 1

def keyup(event,ship):
    if event.key in (K_a,K_d):
        ship.rotSpeed(0)
    if event.key == K_w:
        ship.set_thrust(False)