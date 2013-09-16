from visual import*
from math import*
from BodiesClass import*
from MeasuresClass import*

## MKS units


##constants
SolarMass =    1.9891  * (10 ** 30)

G = 6.673 * (10 ** -11)

##Actual distribution follows:
def CreateSystem(CenterMass,Alpha,NumBodies):
    """outputs system from CenterMass such as a black hole, alpha for distributuon constant, and Number of Bodies to be created"""
    OutputSystem = []
    MaxDist = 10
    for i in range(NumBodies):
        distance = random(0,MaxDist)
##  distance will be evenly distributed unless otherwise discovered
##      
        
    return 
def Gravity (Body1,Body2):
    """(Body,Body)->Force
        returns the gravitational force between Body1 and Body2"""
    m1,m2 = Body1.mass, Body2.mass
    dist = Body2.position-Body1.position
    UnitForceVector = dist/mag(dist)
    force = (G*m1*m2)/(mag(dist)**2)*UnitForceVector
    return force

def SystemGravity(system, timestep):
    """changes the position of the bodies in system in time 'time' as one step, the smaller the step the better the outcome"""
    for body1 in system:
        for body2 in system:
            if body1 != body2:
                ac = (Gravity(body1,body2)/body1.mass)
##                print body1,body2,body1.position,ac,body2.position
                body1.velocity = body1.velocity + ac*timestep
                a = body1.position
    for body1 in system:
        body1.position = body1.position + body1.velocity*timestep

def SystemRun(system, timestep, time,center):
    """Runs a system under gravity in intervals of timestep in seconds for time in seconds"""
    MassOrbitVelocity(system,center)
    VisualSystem = []
    for body in range (len(system)):
        Visual = sphere(pos = system[body].position, radius = system[body].radius)
        Visual.trail = curve(color = color.blue)
        VisualSystem.append (Visual)
    frame = 0
    final_frame = time / timestep
    while frame < final_frame:
        rate(100)
        SystemGravity(system, timestep)
        for body in range(len(system)):
            VisualSystem[body].pos = system[body].position
            VisualSystem[body].trail.append(pos = VisualSystem[body].pos)
        frame += 1
    print "done"
    
def OrbitVelocity(Body1,Body2):
    """Sets the velocity of Body 1 to orbit velocity with regard to Body 2"""
    dist = Body2.position-Body1.position
    UnitTangentVector = vector(dist.y, -dist.x, 0)/mag(dist)
    Body1.velocity = UnitTangentVector*sqrt((Body2.mass*G)/mag(Body1.position-Body2.position))

def MassOrbitVelocity(system, center):
    for orbiter in range(len(system)):
        if orbiter != center:
            OrbitVelocity(system[orbiter],system[center])
##Test Harness


## Creates the initial bodies
x = Body(velocity = vector(0,0,0), mass = SolarMass, position = vector(0, 0, 0),identity = "sun", radius = SunEarthDist/2)
y = Body(velocity = vector(0,0,0), mass = EarthMass, position = vector(SunEarthDist,0,0), identity = "earth", radius = SunEarthDist/8)
z = Body(velocity = vector(0,0,0), mass = MartianMass, position = vector(-SunMarsDist,0,0), identity = "mars", radius = SunMarsDist/12)

## Combines x y and z as a system
sys2 = [x,y,z]

##  Runs the system for a set amount of time with a timestep
##SystemRun(sys2, 60*60*24, 60*60*24*700, 0)
SystemRun(SolarSystem, 60*60*24,60*60*24*365*166,0)

