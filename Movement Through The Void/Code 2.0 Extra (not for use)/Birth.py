## Imports

from math import*
from visual.graph import*
from bodies import*
from random import*
from Movement import*
from Dark import*
##import Image
##import ImageGrab 

## MKS Units

##Constants

SolarMass = 1.9891  * (10 ** 30)
G         = 6.673   * (10 ** -11)
SpeedOfLight = 299792458
LightYear = 9.4605284 * (10**15)
parsec = 3.08567758 * (10**16)
kpc = 1000 * parsec

SunEarthDist =   149597870700



MilkySMBHmass = 4.3 * 10 ** 6 * SolarMass
MilkyRadialScalelength = 2.7 * kpc
MilkyVisibleMass = 400 * 10 ** 9 * SolarMass
MilkyBufferDist = .1 * kpc
MilkyDiameter = 37 * kpc


## Solar System
Sun = Body(mass = SolarMass, position = vector(0,0,0))
Earth = Body(mass = 5.97219 * (10 ** 24), position = vector(0,149597870700,0))
SBody = [Sun, Earth]

def VelInit(Orbiter,Center):
    """(body,body) -> Void
    sets the initial velocity of an orbiter to the orbit velocity"""
    dist = Center.position - Orbiter.position
    UnitTangentVector = vector(dist.y, -dist.x, 0)/mag(dist)
    Orbiter.velocity = UnitTangentVector * sqrt((Center.mass*G)/mag(dist))

def SysVelInit(System):
    """(List of Full bodies) -> Void
    sets initial velocities of all bodies in a system to orbit velocities"""
    for i in range(len(System)):
        if i != 0 and System[i].type != "DM":
            VelInit(System[i].body,System[i].OrbitMass)


## Physical Galaxy

def PhysicalPopulate(CenterMass, RadialScaleLength, Numstars, VisibleMassNonSMBH, MinDist, Diameter):
    """(int, int, int, int, int, int) -> Void
    creates a system of full bodies from:
    1. Center Mass (Supermassive Black Hole)
    2. Radial Scale length (varries from galaxy to galaxy
    3. Number of stars (determines number of stars it divides the mass into
    4. Visible mass (not including Supermassive black hole
    5. Minimum distance (no stars inside this range
    6. Diameter of the galaxy"""
    TotMass = CenterMass + VisibleMassNonSMBH
    MeanMass = VisibleMassNonSMBH / Numstars
    SMBHbod = Body(position = vector(0,0,0), mass = CenterMass)
    Gal = [SMBHbod]
    NumDivisions = 100
    DivisionLen = Diameter / (2 * NumDivisions)
    DivisionMass = []
    totmass = 0.0
    DivisionProbability = []
    for i in range(NumDivisions):
        Min = MinDist + DivisionLen * i
        Max = MinDist + DivisionLen * (i+1)
        Area = 2 * pi * Max**2 - 2 * pi * Min**2
        MinDensity = (RadialScaleLength * TotMass) / ((2 * pi *(Min**2 + RadialScaleLength**2)**(3/2)))
        MaxDensity =(RadialScaleLength * TotMass) / ((2 * pi *(Max**2 + RadialScaleLength**2)**(3/2)))
        AvgDensity = (MinDensity + MaxDensity) / 2
        AreaMass = Area * AvgDensity
        DivisionMass.append(AreaMass)
    for i in range(NumDivisions):
        totmass += DivisionMass[i]
    for i in range(NumDivisions):
        Prob = DivisionMass[i]/totmass
        DivisionProbability.append(Prob)
    for i in range(NumDivisions):
        Min = MinDist + DivisionLen * i
        Max = MinDist + DivisionLen * (i+1)
        Area = 2 * pi * Max**2 - 2 * pi * Min**2
        Number = int(round (Numstars * DivisionProbability[i]))      
        Gal += CreateInRange(Number, Min, Max, MeanMass)
    return Gal

def CreateInRange(Number, Min, Max, Mass):
    """(int, int, int, int) -> List of Bodies
    creates a number of bodies in a ring with max and min radial distance with a set total mass"""
    Out = []
    for i in range(Number):
        RandTheta = float(randint(0,2*31415))/10000
        RandDist = float(randint(Min * 1000,Max * 1000))/1000
        Location = vector(RandDist*cos(RandTheta),RandDist*sin(RandTheta),0)
        NewBod = Body(mass = Mass, position = Location)
        Out.append(NewBod)
    return Out
        
## Stats on Galaxy


## Visual Galaxy
def VisualPopulate(ListOfBodies, Diameter):
    """(List of Bodies, int) -> List of Visual Spheres
    creates a visual list of spheres from a list of bodies and sets their visual diameter to the input diameter"""
    Visual = []
    for i in range(len(ListOfBodies)):
        if i != 0:
            single = sphere (pos = ListOfBodies[i].position, radius = Diameter/750 )
            single.trail = curve(color = color.blue)
        if i == 0:
            single = sphere (pos = ListOfBodies[i].position, radius = Diameter/200 )
            single.color = color.red
        Visual.append(single)
    return Visual

## Orbit Masses
def OrbitMassPopulate(ListOfBodies):
    """(List of Bodies) -> List of Bodies
    Creates a list of central masses that the full bodies will orbit around"""
    OrbitMasses = []
    ListOfBodies.sort()
    previous_sum = 0
    for i in range(len(ListOfBodies)):
        previous_sum += ListOfBodies[i-1].mass
        OrbitMasses.append(Body(vector(0,0,0), previous_sum, vector(0,0,0)))
    return OrbitMasses

## Create New Galaxy

def CreateGal(CenterMass, RadialScaleLength, Numstars, VisibleMassNonSMBH, MinDist, Diameter):
    """(float, float, int, float, float, float) -> List of Full Bodies
    Creates a galaxy from the given input"""
    ListOfBodies = PhysicalPopulate(CenterMass, RadialScaleLength, Numstars, VisibleMassNonSMBH, MinDist, Diameter)
    ListOfVisuals = VisualPopulate(ListOfBodies, Diameter)
    ListOfOrbitMasses = OrbitMassPopulate(ListOfBodies)
    FullList = []
    for i in range(len(ListOfBodies)):
        Full = FullBody(ListOfBodies[i],ListOfVisuals[i],ListOfOrbitMasses[i])
        FullList.append(Full)
    print "Begin First Compile"
    SysVelInit(FullList)
    print "First Compile Done"
    DarkCompensate(FullList)
    print "Second Compile Done"
    SysVelInit(FullList)
    print "Third Compile Done"
    return FullList
