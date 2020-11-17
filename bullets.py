import utilities
import pygame
class Bullet:
    def __init__(self,heading,vel,pos):
        self.velocity = vel*utilities.angle_to_vector(heading)
        self.lifetime=0
        self.pos = pos
        self.image = pygame.surface([5, 5])
        pygame.draw.circle(self.image,utilities.WHITE,[3, 3], 2
                           )
    def update(self):
        self.lifetime+=1
        self.pos[0]+=self.velocity[0]
        self.pos[1]+=self.velocity[1]

