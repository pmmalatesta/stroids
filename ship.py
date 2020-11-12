import utilities
class Ship:
    def __init__(self,pos):
        self.pos = pos
        self.vel = [0,0]
        self.angle = (3.14/4.0)
        self.thrust = False

    def getPos(self):
        return self.pos

    def updatePos(self):
