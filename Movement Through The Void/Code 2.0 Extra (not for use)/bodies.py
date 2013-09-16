from math import*
from visual import*

SystemOfBodies = []
SystemOfFullBodies  = []
class Body(object):
    def __init__(self, velocity = vector(0, 0, 0), mass = 0, position = vector(0, 0, 0)):
        self.velocity = velocity
        self.mass = mass
        self.position = position
        SystemOfBodies.append(self)
    def __str__(self):
        return self.identity
    def __lt__(self,other):
        return mag(self.position)<mag(other.position)

class FullBody(object):
    def __init__(self,Body,Visual,OrbitMass,Type = "Visible"):
        self.type = Type
        self.visual = Visual
        self.OrbitMass = OrbitMass
        self.body = Body
        SystemOfFullBodies.append(self)

    def __lt__(self,OtherFull):
        return mag(self.body.position) < mag(OtherFull.body.position)


def ReturnSystem():
    return SystemOfBodies

def ReturnFullSystem():
    return SystemOfFullBodies
        
