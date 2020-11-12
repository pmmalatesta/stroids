import pygame
from pygame.locals import *

TURNRATE = 15
F_ACCEL = 15
R_ACCEL = -5
events = pygame.event.get()
def keydown(event,ship):
    ang_vel = 4.5

    if event.key == K_LEFT:
        ship.set_angle_vel(ang_vel)
    if event.key == K_RIGHT:
        ship.set_angle_vel(-ang_vel)
    if event.key == K_UP:
        ship.set_thrust(True)
    if event.key == K_SPACE:
       ship.shoot()