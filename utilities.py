# https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame for rot
import pygame, math, random
BLACK = [0,0,0]
FONT_PATH = 'assets/FutilePro.ttf'
WHITE = [255,255,255]
RED = [255,0 ,0]
CYAN = [0,255,255]
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

def AHHHH():
    return [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

def create_text(text, size, color):
    font = pygame.font.Font(FONT_PATH, size)
    image = font.render(text, True, color)
    return image