import pygame,utilities, getComs,random, time
import sys,ship, rocklist
from pygame.locals import *

WIDTH=1600
HEIGHT=900
clock = pygame.time.Clock()
def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    score = 0
    bkground = pygame.image.load('background.jpg')
    screen.fill(utilities.BLACK)
    screen.blit(bkground, (0, 0))
    serenity = ship.Ship([WIDTH/2,HEIGHT/2])
    listofRocks = rocklist.Rocklist(WIDTH,HEIGHT)
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
    shootmessage = utilities.create_text("Space to Fire", 24, utilities.WHITE)
    r3 = shootmessage.get_rect()
    r3.centerx = WIDTH / 2
    r3.centery = HEIGHT * .5
    screen.blit(shootmessage, r3)
    pygame.display.update()
    time.sleep(1.25)
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
        screen.blit(bkground, (0,0))
        #if score > 15:
            #screen.fill(utilities.AHHHH())
        screen.blit(utilities.rot(serenity.image,serenity.angVel),serenity.rect)
        for projectile in serenity.bullList:
            screen.blit(projectile.bull, projectile.position)
            projectile.fly()
            if projectile.lifetime > projectile.maxl:
                projectile.kill()

        # update all the asteroids
        listofRocks.update()

        # find asteroids hit by bullets
        collisions = pygame.sprite.groupcollide(listofRocks, serenity.bullList, True, True)
        # collisions is a dictionary of rock => bullet pairs
        # we don't care about the bullets, just go through the rocks which are the keys in the dict
        # the kill parameters to this function are both True so we don't have to worry
        # about removing the rock or bullet
        for rock in collisions.keys():
            score += 1
            serenity.blowup()
            if rock.big:
                listofRocks.createsmallrocks(rock)

        # find asteroids that hit our ship (this handles multiple simultaneous collisions)
        collisions = pygame.sprite.spritecollide(serenity, listofRocks, True)
        for _ in collisions:
            serenity.loselife()
            print("Ouch!")

        listofRocks.updaterocks()

        # draw the asteroids, don't use blit, just let the group draw itself
        listofRocks.draw(screen)

        pygame.display.update()

        listofRocks.spawndelay = 55- score
    death = utilities.create_text("You Lose",100,utilities.RED)
    scorestring = ("You blew up %d rocks!" % score)
    scoremess = utilities.create_text(scorestring, 75, utilities.RED)
    r = death.get_rect()
    r.centerx = WIDTH / 2
    r.centery = HEIGHT * .25
    r2 = scoremess.get_rect()
    r2.centerx = WIDTH / 2
    r2.centery = HEIGHT * .5
    screen.blit(death, r)
    screen.blit(scoremess,r2)
    pygame.display.update()
    time.sleep(1.5)


main()