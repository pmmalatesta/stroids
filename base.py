import pygame,utilities, getComs
import sys,ship, time
from pygame.locals import *

WIDTH=1200
HEIGHT=800
clock = pygame.time.Clock()

def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(utilities.BLACK)
    serenity = ship.Ship([WIDTH/2,HEIGHT/2])
    print(serenity.lives)
    while serenity.lives>0:
        clock.tick(60)
        screen.blit(serenity.image,serenity.pos)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                getComs.keydown(event, serenity)
            if event.type == QUIT:
                if event.type == QUIT:
                    pygame.display.update()
                    pygame.time.wait(1000)
                    pygame.quit()
                    sys.exit()
        serenity.updateVels()
        serenity.updatePos(0,0)
        pygame.display.flip()

main()