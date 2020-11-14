import pygame, math
BLACK = [0,0,0]
WHITE = [255,255,255]

def angle_to_vector(ang):
    return[math.cos(ang), math.sin(-ang)]