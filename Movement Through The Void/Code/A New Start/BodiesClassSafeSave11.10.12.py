from visual import*
from math import*


SystemOfBodies = []

class Body(object):
    def __init__(self, velocity = vector(0,0,0), mass = 0, position = vector(0,0,0), identity = "unknown"):
        self.velocity = velocity
        self.mass = mass
        self.position = position
        self.identity = identity
        SystemOfBodies.append(self)
    def __str__(self):
        return self.identity
def GetSystem():
    """returns a list of all bodies created in the system"""
    return SystemOfBodies


def GravityToAccel(Body1,Body2):
    """returns the acceleration due to gravity between two bodies"""
    G = 1
    dist = (Body2.position-Body1.position)
    force = (G*Body1.mass*Body2.mass) / (mag(dist)**2)
    accel1 = dist*(force/Body1.mass)
    accel2 = dist*(force/Body2.mass)
    return accel1,accel2

def SystemGravity(system, time):
    """changes the position of the bodies in system in time 'time' as one step, the smaller the step the better the outcome"""
    NewSystem = system
    print "new"
    for Body1 in range(len(NewSystem)):
##        print Body1
        for Body2 in range(len(NewSystem) - (Body1+1)):
            Body2 = len(NewSystem) - (Body2+1)
##            print Body2
            print NewSystem[Body1],NewSystem[Body2]
            
        
    
        
    
    

##Test Harness 

x = Body(vector(1,1,1), mass = 12, position = vector(1,1,1),identity = "earth")
y = Body(vector(0,0,0), mass = 6, position = vector(-1,-1,-1), identity = "moon")
##print GetSystem()
print GravityToAccel(x,y)
sys1 = [1,2,3,4,5,6,7,8,9,10]
sys2 = [x,y]
SystemGravity(sys1,5)
SystemGravity(sys2,5)
