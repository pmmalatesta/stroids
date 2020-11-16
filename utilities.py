import pygame, math
BLACK = [0,0,0]
WHITE = [255,255,255]

def angle_to_vector(ang):
    return[math.cos(math.radians(ang)), math.sin(math.radians(-ang))]

def rot(im,ang):
    rotIm = pygame.transform.rotate(im,ang)
    return rotIm