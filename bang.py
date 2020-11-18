import utilities, pygame,math

class Bang(pygame.sprite.Sprite):
    def __init__(self,posit, hed, spd,lengthy):
        self.position = posit
        self.velo= [spd*math.cos(math.radians(hed)), spd*math.sin(math.radians(-hed))]
        self.bull = pygame.Surface([5, 5])
        pygame.draw.circle(self.bull,utilities.CYAN,[3,3],2)
        self.lifetime = 0
        self.maxl = lengthy/spd

    def fly(self):
        self.position[0] += self.velo[0]
        self.position[1] += self.velo[1]
        self.lifetime +=1