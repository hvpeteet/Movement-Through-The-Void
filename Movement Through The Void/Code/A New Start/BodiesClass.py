from math import*
from visual import*

SystemOfBodies = []
class Body(object):
    def __init__(self, velocity = vector(0, 0, 0), mass = 0, position = vector(0, 0, 0), identity = "unknown", radius = 0):
        self.velocity = velocity
        self.mass = mass
        self.position = position
        self.identity = identity
        self.radius = radius
        self.volume = (4/3) * pi * self.radius ** 3
        self.density = self.mass / self.volume
        SystemOfBodies.append(self)
    def __str__(self):
        return self.identity
def ReturnSystem():
    return SystemOfBodies

class FullBody(object):
    def __init__(self,Body,Visual,OrbitMass):
        self.visual = Visual
        self.OrbitMass = OrbitMass
        self.body = Body

##x = Body(mass = 5, radius = 1)
##y = sphere(pos=vector(10,10,10),radius = .25)
##z = 56
##a  = FullBody(x,y,z)
##rate(10)
##for i in range(100):
##    a.visual.pos = a.visual.pos + vector(1,0,0)
##
