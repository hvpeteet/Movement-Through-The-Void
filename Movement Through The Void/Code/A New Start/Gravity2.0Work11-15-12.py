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

def OrbitVelocity(Body1,Body2):
    Body1.velocity = 
##    Body1.velocity.y = 100000*sqrt((Body2.mass*G)/mag(Body1.position-Body2.position))
    print Body1.velocity
##Test Harness 

x = Body(velocity = vector(0,0,0), mass = SolarMass, position = vector(0, 0, 0),identity = "sun", radius = SunEarthDist/2-1000000000)
y = Body(velocity = vector(0,0,0), mass = EarthMass, position = vector(SunEarthDist,0,0), identity = "earth", radius = 6378.1)
##z = Body(velocity = vector(0,-2,-10), mass = 1, position = vector(5,0,0), identity = "mars", radius = .5)
OrbitVelocity(y,x)
sys2 = [x,y]

SystemRun(sys2,.1,1000000000000)

print x.density,y.density



