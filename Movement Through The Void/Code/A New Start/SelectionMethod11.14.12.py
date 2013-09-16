from math import*
from visual import*

##Classes
##A single body

SystemOfBodies = []
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
            self.mass += i.mass
        self.min = vector(self.position.x-self.sidelength/2, self.position.y-self.sidelength/2, self.position.z-self.sidelength/2)
        self.max = vector(self.position.x+self.sidelength/2, self.position.y+self.sidelength/2, self.position.z+self.sidelength/2)      
       
            
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
        for body in self.bodies:

            ### Determine which side of origin is on
            OctantIdentity = [None,None,None]
            if body.position.x < self.position.x:
                OctantIdentity[0] = False
            if body.position.x > self.position.x:
                OctantIdentity[0] = True
            if body.position.y < self.position.y:
                OctantIdentity[1] = False
            if body.position.y > self.position.y:
                OctantIdentity[1] = True
            if body.position.z < self.position.z:
                OctantIdentity[2] = False
            if body.position.z > self.position.z:
                OctantIdentity[2] = True

            ### If is on one axis determine by velocity
            if type(OctantIdentity[0]) == 'None':
                if body.velocity.x < 0:
                    OctantIdentity[0] = False
                if body.velocity.x > 0:
                    OctantIdentity[0] = True
                if body.velocity.x == 0:
                    OctantIdentity[0] = True
            if type(OctantIdentity[1]) == 'None':
                if body.velocity.y < 0:
                    OctantIdentity[1] = False
                if body.velocity.y > 0:
                    OctantIdentity[1] = True
                if body.velocity.y == 0:
                    OctantIdentity[1] = True
            if type(OctantIdentity[2]) == 'None':
                if body.velocity.z < 0:
                    OctantIdentity[2] = False
                if body.velocity.z > 0:
                    OctantIdentity[2] = True
                if body.velocity.z == 0:
                    OctantIdentity[2] = True

            ### sort into 8 groups from identity
                
            print body,OctantIdentity
                

##Test Harness

x = Body(position = vector(1,1,1), mass = 1, identity = "Earth", radius = 2)
y = Body(position = vector(-1,-1,-1),mass = .5, identity = "Moon", radius = 1)
sys = System(SystemOfBodies, vector(0,0,0), 3)
sys.octasect()

##minvect = vector (-1,-1,-1)
##maxvect = vector(1,1,1)
##testvect1 = vector(0,0,0)
##testvect2 = vector(2,2,2)
##print inarea(testvect1, minvect, maxvect)
##print inarea(testvect2, minvect, maxvect)
            
        
