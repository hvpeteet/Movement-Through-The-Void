from __future__ import division
from visual import*
from math import*
from visual.graph import *
## MKS units


##Solar Mass in Kilograms
SolarMass = 1.9891 * (10 ** 30)
EarthMass = 5.97219 * (10 ** 24)

SunEarthDist = 149.60*10**9

G = 6.673 * (10 ** -11)

##List of all bodies entered, automatically appended
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

def GravityToAccel (Body1,Body2):
    m1,m2 = Body1.mass, Body2.mass
    dist = Body2.position-Body1.position
    force = (G*m1*m2)/(mag(dist)**2)
    accel = (force/m1)*dist
    return accel

def SystemGravity(system, timestep):
    """changes the position of the bodies in system in time 'time' as one step, the smaller the step the better the outcome"""
    for body1 in system:
        for body2 in system:
            if body1 != body2:
                ac = GravityToAccel(body1,body2)
                body1.velocity += ac*timestep
                body1.position += body1.velocity*timestep
                print body1,body1.velocity
            
    
def SystemRun(system, timestep, time):
    VisualSystem = []
    for body in range (len(system)):
        print system[body]
        Visual = sphere(pos = system[body].position, radius = system[body].radius)
        Visual.trail = curve(color = color.blue)
        VisualSystem.append (Visual)
        print len(VisualSystem)
    frame = 0
    final_frame = time / timestep
    while frame < final_frame:
        rate(7)
        SystemGravity(system, timestep)
        for body in range(len(system)):
            VisualSystem[body].pos = system[body].position
            VisualSystem[body].trail.append(pos = VisualSystem[body].pos)
            ##Need to change when mases are made realistic format - 1st num = 0 so we are in the red spectrum
            ## second and third in between 0 and 1
            ## second, the closer to 0, the brighter
            ## third the closer to 0 the closer to black
##            VisualSystem[body].color = color.hsv_to_rgb((0, system[body].mass / (3 * SolarMass), system[body].density / 10))
        frame += 1
    print "done"
    
def OrbitVelocity(Body1,Body2):
##    Body1.velocity = 
    Body1.velocity.y = 100000*sqrt((Body2.mass*G)/mag(Body1.position-Body2.position))
    print Body1.velocity
##Test Harness 

x = Body(velocity = vector(0,0,0), mass = SolarMass, position = vector(0, 0, 0),identity = "sun", radius = SunEarthDist/2)
y = Body(velocity = vector(0,0,0), mass = EarthMass, position = vector(SunEarthDist,0,0), identity = "earth", radius = 6378.1)
##z = Body(velocity = vector(0,-2,-10), mass = 1, position = vector(5,0,0), identity = "mars", radius = .5)
OrbitVelocity(y,x)
sys2 = [x,y]

SystemRun(sys2,1,1000000000000)

print x.density,y.density



