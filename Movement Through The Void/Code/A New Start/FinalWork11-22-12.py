from visual import*
from math import*
from random import*
from BodiesClass import*

## MKS Units

##Constants

SolarMass = 1.9891  * (10 ** 30)
G         = 6.673   * (10 ** -11)
SpeedOfLight = 299792458
LightYear = 9.4605284 * (10**15)
parsec = 3.08567758 * (10**16)
kpc = 1000*parsec

## Variables for Galaxy
MilkyBodies = []
MilkySMBH = Body(mass = 4.1*(10**6)*SolarMass, radius = (2*G*(4.1*(10**6)))/(SpeedOfLight**2))


## Gravity Functions
def Gravity (Body1,Body2):
    """(Body,Body)->Force
        returns the gravitational force between Body1 and Body2"""
    m1,m2 = Body1.mass, Body2.mass
    dist = Body2.position-Body1.position
    UnitForceVector = dist/mag(dist)
    force = (G*m1*m2)/(mag(dist)**2)*UnitForceVector
    return force

def VelocityChangeFromGravity(Body1,Body2,timestep):
    return (Gravtiy(Body1,Body2)/Body1.mass)*timestep

## Create Galaxy Functions
def RandLocation(center, maxdist):
    dispcenters = sphere(pos = center,radius = 1, color = color.red)
    Location = center
    RandDist = 0.0
    RandTheta = 0.0
    RandDist = float(randint(0,10000*maxdist))/10000
    RandTheta = float(randint(0,2*31415))/10000
    Location = Location + vector(RandDist*cos(RandTheta),RandDist*sin(RandTheta),0)
    return Location

def RandBody(SMBH,maxdist,bodymass):
    NewBody = Body(position = RandLocation(SMBH.position, maxdist),mass = bodymass, radius = bodymass/10**12)
    return NewBody

def NewGalaxy(SMBH, numstars, maxdist):
    """outputs a system of FullBodies with the first element as the SMBH with a None tytpe orbit mass for catching"""
    OutputList = []
## Create Bodies List
    BodiesList = [SMBH]
    for i in range(numstars):
        Star = RandBody(SMBH, maxdist, SolarMass)
        BodiesList.append(Star)
        
## Create the visual List
    VisualList = [sphere(position = SMBH.position, radius = SMBH.radius, color = color.red)]
    for i in range(numstars):
        if i != 0:
            Visual = sphere(pos = BodiesList[i].position, radius = BodiesList[i].radius)
            VisualList.append(Visual)
## Create the orbit mass velocities
    OrbitMassList = [None]
    for body in range(numstars):
        OrbitMass = SMBH.mass
        for other in range (numstars):
            if mag(BodiesList[other].position) < mag(BodiesList[body].position):
                OrbitMass += BodiesList[other].mass
        OrbitMassList.append(OrbitMass)

## Compile Lists
    for i in range(numstars):
        x = FullBody(Body = BodiesList[i], Visual = VisualList[i], OrbitMass = OrbitMassList[i])
        OutputList.append(x)
    print "compiled"
    return OutputList

def OrbitVelocity(FullBodyOrbiter,FullBodyCenter):
    """Sets the velocity of Body 1 to orbit velocity with regard to Body 2"""
    dist = FullBodyCenter.body.position-FullBodyOrbiter.body.position
    UnitTangentVector = vector(dist.y, -dist.x, 0)/mag(dist)
    FullBodyOrbiter.body.velocity = UnitTangentVector*sqrt((Body2.mass*G)/mag(FullBodyOrbiter.body.position-FullBodyCenter.body.position))
    
def SetupRandomGalaxy(SMBH, numstars,maxdist):
    Gal = NewGalaxy(SMBH, numstars, maxdist)
    for Orbiter in Gal:
        if Orbiter.body != SMBH:
            OrbitVelocity(Orbiter, Gal[0])
          
    
## Simulate Movemend and Displays
            
def ApplyOneWayGravity(Orbiter,Center):
    m1,m2 = Orbiter.body.mass, Center.body.mass
    dist = Center.body.position-Orbiter.body.position
    UnitForceVector = dist/mag(dist)
    force = (G*m1*m2)/(mag(dist)**2)*UnitForceVector
    accel = force/Orbiter.body.mass
    Orbiter.body.velocity += accel*timestep

def SingleFrameMovement(Galaxy,timestep):
    for Bod in Galaxy:
        if Bod != Galaxy[0]:
            ApplyOneWayGravity(Bod,Galaxy[0])
            Bod.body.position += Bod.body.velocity*timestep
            Bod.visual.pos = Bod.body.position
            
def RunGalaxy(Galaxy,time,timestep):
    rate(10)
    for frame in range(int(time/timestep)):
        SingleFrameMovement(Galaxy,timestep)
        


            


##Test Harness
##points = int(raw_input("Number of points to be created"))
##for i in range(points):
##    x = sphere (pos = RandLocation(vector(0,0,0),10), radius = .125)
##    print i
MilkyBodies = NewGalaxy(MilkySMBH, 1000, 34*kpc)

##for i in range(100):
##    print MilkyBodies[i].body.position, MilkyBodies[i].body.radius, MilkyBodies[i].visual.pos
##
##for i in range(100):
##    print mag(MilkyBodies[i].body.position),MilkyBodies[i].OrbitMass
##


