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
    """(Body, Body) -> vector, vector

    Returns the acceleration due to gravity between two bodies

    """
    G = 6.673 * (10**-11)
    dist = (Body2.position-Body1.position)
    force = (G*Body1.mass*Body2.mass) / (mag(dist)**2)
    accel1 = dist*(force/Body1.mass)
    accel2 = -dist*(force/Body2.mass)
    return accel1,accel2

def SystemGravity(system, time):
    """changes the position of the bodies in system in time 'time' as one step, the smaller the step the better the outcome"""
    for Body1 in range(len(system)):
        for Body2 in range(len(system) - (Body1+1)):
            Body2 = len(system) - (Body2+1)
            ac1,ac2 = GravityToAccel(system[Body1],system[Body2])
            system[Body1].velocity += ac1*time
            system[Body2].velocity += ac2*time
            system[Body1].position += system[Body1].velocity*time
            system[Body2].position += system[Body2].velocity*time
##            print system[Body1], system[Body1].position,system[Body2],system[Body2].position
        
    
def SystemRun(system, timestep, time):
    VisualSystem = []
    for body in range ( len (system) ):
        print system[body]
        Visual = sphere(pos = system[body].position, radius = 10**12)
        Visual.trail = curve(color = color.blue)
        VisualSystem.append (Visual)
        print len(VisualSystem)
    frame = 0
    final_frame = time/timestep
    while frame < final_frame:
        rate(1)
        SystemGravity(system, timestep)
        for body in range ( len(system)):
            VisualSystem[body].pos = system[body].position
            VisualSystem[body].trail.append(pos = VisualSystem[body].pos)            
        frame += 1
    print "done"
    

##Test Harness 

x = Body(velocity = vector(0,0,0), mass = 1.9891*(10**30), position = vector(0, 0, 0),identity = "sun")
y = Body(velocity = vector(0,107300000,0), mass = 5.97219*(10**24), position = vector(150*(10**6),0,0), identity = "earth")
z = Body(velocity = vector(0,-11245,1), mass = 6.41693*(10**23), position = vector(-206669*(10**6),0,0), identity = "mars")
##print GetSystem()
##print GravityToAccel(x,y)
sys1 = [1,2,3,4,5,6,7,8,9,10]
sys2 = [x,y,z]
##SystemGravity(sys1,5)

SystemRun(sys2,1,100)

##SystemGravity(sys2,0)
##SystemGravity(sys2,1)
##SystemGravity(sys2,0)
##SystemGravity(sys2,1)


##x = sphere(pos = x.position, radius = .25, color = color.blue)
##y = sphere(pos = y.position, radius = .125, color = color.white)
##t = 0
##r = vector(0, 0, 0)
##y.trail = curve(color = color.blue)
##while t < 100:
##    rate(7)
##    r = (sin(t), cos(t), sin(t))
##    y.pos = r
##    y.trail.append(pos = y.pos)
##    t = t + .1
##while t < 100:
##    rate(7)
##    r = (sin(t), cos(t), sin(t))
##    y.pos = r
##    y.trail.append(pos = y.pos)
##    t = t + .1  
