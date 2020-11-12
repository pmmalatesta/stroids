import utilities
class Ship:
    def __init__(self,pos,vel,angle,image,thrustim):
        self.pos = pos;
        self.vel = vel;
        self.angle = angle;
        self.image = image;
        self.thrustim = thrustim;

    def draw(self, canvas):

        if self.thrust:
            canvas.blit(utilities.rot_center(self.thrust_image, self.angle), self.pos)
        else:
            canvas.blit(utilities.rot_center(self.image, self.angle), self.pos)