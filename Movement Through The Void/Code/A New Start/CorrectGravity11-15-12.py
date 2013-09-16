from __future__ import division
from visual import*
from math import*
from visual.graph import *
## MKS units


##Solar Mass in Kilograms
SolarMass = 1.9891 * (10 ** 30)
EarthMass = 5.97219 * (10 ** 24)

SunEarthDist = 149597870700

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

def Gravity (Body1,Body2):
    m1,m2 = Body1.mass, Body2.mass
    dist = Body2.position-Body1.position
    UnitForceVector = dist/mag(dist)
    force = (G*m1*m2)/(mag(dist)**2)*UnitForceVector
##    print force
    return force

def SystemGravity(system, timestep):
    """changes the position of the bodies in system in time 'time' as one step, the smaller the step the better the outcome"""
    for body1 in system:
        for body2 in system:
            if body1 != body2:
##                print body1.velocity
                ac = (Gravity(body1,body2)/body1.mass)
##                print ac
                body1.velocity = body1.velocity + ac*timestep
##                print ac,ac*timestep
                a = body1.position
                body1.position = body1.position + body1.velocity*timestep
##                print body1.velocity*timestep,
##                print a-body1.position
##                print body1,body1.position
                

def OrbitVelocity(Body1,Body2):
    dist = Body2.position-Body1.position
    UnitTangentVector = vector(dist.y, -dist.x, 0)/mag(dist)
    print mag(UnitTangentVector)
    Body1.velocity = UnitTangentVector*sqrt((Body2.mass*G)/mag(Body1.position-Body2.position))
    print Body1.velocity
##Test Harness



x = Body(velocity = vector(0,0,0), mass = SolarMass, position = vector(0, 0, 0),identity = "sun", radius = SunEarthDist/2)
y = Body(velocity = vector(0,0,0), mass = EarthMass, position = vector(SunEarthDist,0,0), identity = "earth", radius = SunEarthDist/8)
##z = Body(velocity = vector(0,-2,-10), mass = 1, position = vector(5,0,0), identity = "mars", radius = .5)
OrbitVelocity(y,x)
##Gravity(x,y)
sys2 = [x,y]
##SystemGravity(sys2,.1)
##
##SystemRun(sys2,1,1000000000000)
##def RunSystem(system, timestep, time):
##    VisualSystem = []
##    for body in range (len(system)):
##        visual = sphere(pos = system[body].position, radius = system[body].radius)
##        visual.trail = curve(color = color.blue)
##        VisualSystem.append(visual)
##        
##    for frame in range(int(time/timestep)):
##        rate (10)
##        system[1].position = frame*10**20
####        SystemGravity(system, timestep)

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
        rate(15)
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


SystemRun(sys2, 60*60*24, 60*60*24*365)

