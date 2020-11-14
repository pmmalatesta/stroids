import pygame,utilities
import sys,ship
from pygame.locals import *

WIDTH=1200
HEIGHT=800

screen: pygame.Surface = pygame.display.set_mode((WIDTH,HEIGHT))

def main():
    pygame.init()
    screen.fill(utilities.BLACK)
    serenity = ship.Ship((WIDTH/2,HEIGHT/2))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.update()
                pygame.time.wait(1000)
                pygame.quit()
                sys.exit()
