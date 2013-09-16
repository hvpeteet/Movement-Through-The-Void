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

SunEarthDist =   149597870700
## Variables for Galaxy
MilkyBodies = []
MilkySMBH = Body(mass = 4.1*(10**6)*SolarMass, radius = (2*G*(4.1*(10**6)))/(SpeedOfLight**2)*10**39)
TheSunBody = Body(mass = SolarMass, radius = 1000)
TheSunVisual = sphere (pos = vector(0,0,0),radius = 10**10)
TheSunVisual.trail = curve(color = color.blue)
TheSun = FullBody(TheSunBody,TheSunVisual,0)
SolarBodies = []
StarMass = 10**10*SolarMass
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
    RandDist = float(randint(0,10000*maxdist))/10000 + 10*41
    RandTheta = float(randint(0,2*31415))/10000
    Location = Location + vector(RandDist*cos(RandTheta),RandDist*sin(RandTheta),0)
    return Location

def RandBody(SMBH,maxdist,bodymass):
    NewBody = Body(position = RandLocation(SMBH.position, maxdist),mass = bodymass, radius = SMBH.radius)
    return NewBody

def NewGalaxy(SMBH, numstars, maxdist):
    """outputs a system of FullBodies with the first element as the SMBH with a None tytpe orbit mass for catching"""
    OutputList = []
## Create Bodies List
    BodiesList = [SMBH]
    for i in range(numstars):
        Star = RandBody(SMBH, maxdist, StarMass)
        BodiesList.append(Star)
        
## Create the visual List
    VisualList = [sphere(position = SMBH.position, radius = SMBH.radius, color = color.red)]
    for i in range(numstars):
        if i != 0:
            Visual = sphere(pos = BodiesList[i].position, radius = BodiesList[i].radius)
            Visual.trail = curve(color = color.blue)
            VisualList.append(Visual)
## Create the orbit mass velocities
    OrbitMassList = [None]
    for body in range(numstars):
        if body != 0:
            OrbitMass = SMBH.mass
            for other in range (numstars):
                if other != 0:
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
    FullBodyOrbiter.body.velocity = UnitTangentVector*sqrt((FullBodyCenter.body.mass*G)/mag(dist))
##    print UnitTangentVector, dist, FullBodyOrbiter.body.position, FullBodyOrbiter.body.velocity
    
def SetupRandomGalaxy(SMBH, numstars,maxdist):
    """(Body, int, int) -> Galaxy AKA [FullBody, FullBody,...FullBody]"""
    Gal = NewGalaxy(SMBH, numstars, maxdist)
    for Orbiter in Gal:
        if Orbiter.body != SMBH and Orbiter != Gal[0]:
##            print Orbiter.OrbitMass-SolarMass
            OrbitVelocity(Orbiter, FullBody(Body = Body(mass = Orbiter.OrbitMass, radius = 1) , Visual = None, OrbitMass = None ))
    return Gal
          
    
## Simulate Movemend and Displays
            
def ApplyOneWayGravity(Orbiter,Center,timestep):
    m1,m2 = Orbiter.body.mass, Center.body.mass
    dist = Center.body.position-Orbiter.body.position
    UnitForceVector = dist/mag(dist)
    force = (G*m1*m2)/(mag(dist)**2)*UnitForceVector
    accel = force/Orbiter.body.mass
    Orbiter.body.velocity += accel*timestep

def SingleFrameMovement(Galaxy,timestep):
    for Bod in Galaxy:
        if Bod != Galaxy[0]:
            print Bod.body.velocity
            ApplyOneWayGravity(Bod,Galaxy[0],timestep)
            
            Bod.body.position += Bod.body.velocity*timestep
##            print Bod.body.velocity,Bod.body.position
            Bod.visual.pos = Bod.body.position
            Bod.visual.trail.append(pos = Bod.visual.pos)
##    print Galaxy[1].body.position
            
def RunGalaxy(Galaxy,time,timestep):
    for frame in range(int(time/timestep)):
        rate(10)
        SingleFrameMovement(Galaxy,timestep)
        


            


##Test Harness

##MilkyBodies = NewGalaxy(MilkySMBH, 1000, 34*kpc)
##MilkyWay = SetupRandomGalaxy(MilkySMBH, 100, 34*kpc)
##RunGalaxy(MilkyWay, 60*60*24*365*250*10**6,60*60*24*365*10**5)

##SolarBodies = NewGalaxy(TheSun, 10, 4.4*10*12 )
SolarSystem = SetupRandomGalaxy(TheSunBody, 2,4.4*10*12)
##for i in range(100):
##    rate(1)

##x = Body(position = vector(SunEarthDist,0,0), mass = 5.97219 * (10 ** 24), radius = 100)
##y = sphere(pos = x.position, radius = 10**9)
##y.trail = curve(color = color.blue)
##TheEarth = FullBody(x,y,SolarMass)
##SolarSystem = [TheSun,TheEarth]
##OrbitVelocity(TheEarth,TheSun)
RunGalaxy(SolarSystem, 60*60*24*365,60*60*24)
print "done"
