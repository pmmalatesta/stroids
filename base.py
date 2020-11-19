import pygame,utilities, getComs
import sys,ship, bigrock
from pygame.locals import *

WIDTH=1600
HEIGHT=900
clock = pygame.time.Clock()

def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(utilities.BLACK)
    serenity = ship.Ship([WIDTH/2,HEIGHT/2])
    rockOn = bigrock.iceRocks(WIDTH,HEIGHT)
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
        j=[]
        for shooty in serenity.bullList:
            screen.blit(shooty.bull, shooty.position)
            shooty.fly()
            if shooty.lifetime< shooty.maxl:
                j.append(shooty)
        serenity.bullList=j
        for brock in rockOn.largeRocks:
            screen.blit(brock.image, brock.pos)
        rockOn.updaterocks()
        pygame.display.update()

main()