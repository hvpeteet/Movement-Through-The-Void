from __future__ import division
from visual import*
from math import*
from visual.graph import *

##Solar Mass in Kilograms
SolarMass = 1.9891*(10**30)

##List of all bodies entered, automatically appended
SystemOfBodies = []
class System(object):
    def __init__(self, ListOfBodies, SideLength):
        self.bodies = ListOfBodies
        self.position = position
        self.sidelen = SideLength
        self.mass = 0
        for i in self.bodies:
            self.mass += self.bodies[i].mass
    def DistributeForce(force, timestep):
        for i in self.bodies:
            self.velocity = force/self.bodies[i].mass*tiemstep

            
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

def GetSystem():
    """returns a list of all bodies created in the system"""
    return SystemOfBodies


def GravityToAccel(Body1,Body2):
    """(Body, Body) -> vector, vector

    Returns the acceleration due to gravity between two bodies

    """
##    G = 6.673 * (10**-11)
    G = 1
    dist = (Body2.position-Body1.position)
## remove padding if collision sim is added
    force = (G*Body1.mass*Body2.mass) / ((mag(dist)**2)+1)
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
        
def SortSystem(system):
    """(list)->(list of lists)"""
    

    
def SystemRun(system, timestep, time):

    VisualSystem = []
    for body in range ( len (system) ):
        print system[body]
        Visual = sphere(pos = system[body].position, radius = system[body].radius)
        Visual.trail = curve(color = color.blue)
        VisualSystem.append (Visual)
        print len(VisualSystem)
    frame = 0
    final_frame = time/timestep
    while frame < final_frame:
        rate(7)
        TempSystem = SortSystem(system)
        SystemGravity(TempSystem, timestep)
        for body in range ( len(system)):
            VisualSystem[body].pos = system[body].position
            VisualSystem[body].trail.append(pos = VisualSystem[body].pos)
            ##Need to change when mases are made realistic format - 1st num = 0 so we are in the red spectrum
            ## second and third in between 0 and 1
            ## second, the closer to 0, the brighter
            ## third the closer to 0 the closer to black
            VisualSystem[body].color = color.hsv_to_rgb((0,system[body].mass/(3*SolarMass),system[body].density/10))

            ##Collision
## add collisions in if we can afford it, this will decrese efficiecy
        frame += 1
    print "done"

##Test Harness 

x = Body(velocity = vector(0,0,0), mass = 100, position = vector(0, 0, 0),identity = "sun", radius = 1.5)
y = Body(velocity = vector(1,2,.5), mass = 1, position = vector(-5,0,0), identity = "earth", radius = 1)
z = Body(velocity = vector(0,-2,-10), mass = 1, position = vector(5,0,0), identity = "mars", radius = .5)

sys2 = [x,y,z]
SystemRun(sys2,.1,10)

print x.density,y.density,z.density



