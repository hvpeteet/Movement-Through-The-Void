from math import*
from visual import*

##Classes
##A single body
class Body(object):
    def __init__(self, velocity = vector(0,0,0), mass = 0, position = vector(0,0,0), identity = "unknown", radius = 0):
        self.velocity = velocity
        self.mass = mass
        self.position = position
        self.identity = identity
        self.radius = radius
        self.volume = (4/3)*pi*self.radius**3
        self.density = self.mass/self.volume
        SystemOfBodies.append(self)
    def __str__(self):
        return self.identity

## A set of bodies
class System(object):
    def __init__(self, ListOfBodies, position, sidelength):
        self.bodies = ListOfBodies
        self.position = position
        self.sidelength = sidelength
        self.mass = 0
        for i in self.bodies:
            self.mass += self.bodies[i].mass
        self.min = vector(0,0,0)
        self.max = vector(0,0,0)
        for body in ListOfBodies
            

    def applyaccel(self, accel, timestep):
        for i in self.bodies:
            self.bodies[i].velocity += accel * timestep
            
    def inarea(position, minvector,maxvector):
        if maxvector.x > position.x > minvector.x:
            if maxvector.y > position.y > minvector.y:
                if maxvector.z > position.z > minvector.z:
                    return True
                else: return False
            else: return False
        else: return False

    def octasect(self):
        Newset = []
        for 
            
        
