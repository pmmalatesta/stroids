import pygame,utilities, getComs
import sys,ship, time
from pygame.locals import *

WIDTH=1600
HEIGHT=900
clock = pygame.time.Clock()

def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(utilities.BLACK)
    serenity = ship.Ship([WIDTH/2,HEIGHT/2])

    while serenity.lives>0:

        clock.tick(30)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                getComs.keydown(event, serenity)
            if event.type == KEYUP:
                getComs.keyup(event,serenity)
            if event.type == QUIT:
                if event.type == QUIT:
                    pygame.display.update()
                    pygame.time.wait(1000)
                    pygame.quit()
                    sys.exit()
        serenity.updateVels()
        serenity.updatePos(WIDTH,HEIGHT)
        screen.fill(utilities.BLACK)
        screen.blit(utilities.rot(serenity.image,serenity.angVel),serenity.rect)
        pygame.display.update()

main()