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
    def copy(self):
        copy = Body(vector(self.velocity.x,self.velocity.y,self.velocity.z),self.mass,vector(self.position.x,self.position.y,self.position.z))
        return copy

class FullBody(object):
    def __init__(self,Body,Visual,OrbitMass,Type = "Visible"):
        self.type = Type
        self.visual = Visual
        self.OrbitMass = OrbitMass
        self.body = Body
        SystemOfFullBodies.append(self)

    def __lt__(self,OtherFull):
        return mag(self.body.position) < mag(OtherFull.body.position)

    def copy(self):
        s = sphere(radius = self.visual.radius,pos = vector(self.visual.pos.x,self.visual.pos.y,self.visual.pos.z))
        s.trail = curve(color = color.red)
        copy = FullBody(self.body.copy(),s,self.OrbitMass.copy())
        return copy


def ReturnSystem():
    return SystemOfBodies

def ReturnFullSystem():
    return SystemOfFullBodies

##x = Body(vector(1,1,1),1,vector(1,1,1))
##
##y = x.copy()
##y.position += vector(1,0,0)
##z = Body(vector(0,0,0),10,vector(0,0,0))
##print x.position-y.position
##t = sphere()##1,vector(0,0,0))
##t.pos = vector(1,1,1)
##t.radius = 2
##t.color = color.red
##a = FullBody(x,t,z)
##b = a.copy()
##b.visual.pos += vector(1,0,0)
##
##
