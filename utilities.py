import pygame, math
BLACK = [0,0,0]
WHITE = [255,255,255]

def angle_to_vector(ang):
    return[math.cos(math.radians(ang)), math.sin(math.radians(-ang))]

def rot(im,ang):
    clean = im.copy()
    orig_rect = clean.get_rect()
    rot_image = pygame.transform.rotate(clean, ang)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image