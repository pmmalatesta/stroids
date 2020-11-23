import pygame,utilities, getComs,random, time
import sys,ship, bigrock
from pygame.locals import *

WIDTH=1600
HEIGHT=900
clock = pygame.time.Clock()
def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    score = 0
    screen.fill(utilities.BLACK)
    serenity = ship.Ship([WIDTH/2,HEIGHT/2])
    rockOn = bigrock.iceRocks(WIDTH,HEIGHT)
    welcome = utilities.create_text("Welcome to Asteroids",48,utilities.WHITE)
    r = welcome.get_rect()
    r.centerx = WIDTH/2
    r.centery = HEIGHT*.25
    screen.blit(welcome, r)
    instrs = utilities.create_text("W A D to Move and Turn", 24, utilities.WHITE)
    r2 = instrs.get_rect()
    r2.centerx = WIDTH / 2
    r2.centery = HEIGHT * .375
    screen.blit(instrs, r2)
    nancysinatra = utilities.create_text("Space to Fire", 24, utilities.WHITE)
    r3 = nancysinatra.get_rect()
    r3.centerx = WIDTH / 2
    r3.centery = HEIGHT * .5
    screen.blit(nancysinatra, r3)
    pygame.display.update()
    time.sleep(1)
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
        #if score > 15:
            #screen.fill(utilities.AHHHH())
        screen.blit(utilities.rot(serenity.image,serenity.angVel),serenity.rect)
        for shooty in serenity.bullList:
            screen.blit(shooty.bull, shooty.position)
            shooty.fly()
            if shooty.lifetime> shooty.maxl:
                shooty.kill()

        for brock in rockOn.sprlist:
            screen.blit(brock.image, brock.pos)
            snipped = pygame.sprite.spritecollide(brock, serenity.bullList, True)
            if snipped:
                score+=1
                if brock.big:
                    rockOn.babyboys(brock)
                brock.kill()
                serenity.blowup()
        rockOn.updaterocks()
        pygame.display.update()
        ouch = pygame.sprite.spritecollide(serenity, rockOn.sprlist, True)
        if ouch:
            serenity.loselife()
        rockOn.spawndelay = 60 - score
    death = utilities.create_text("You Lose",100,utilities.RED)
    scorestring = ("You blew up %d rocks!" % score)
    scoremess = utilities.create_text(scorestring, 75, utilities.RED)
    r = death.get_rect()
    r.centerx = WIDTH / 2
    r.centery = HEIGHT * .25
    r2 = scoremess.get_rect()
    r2.centerx = WIDTH / 2
    r2.centery = HEIGHT * .5
    screen.fill(utilities.BLACK)
    screen.blit(death, r)
    screen.blit(scoremess,r2)
    pygame.display.update()
    time.sleep(1.5)


main()