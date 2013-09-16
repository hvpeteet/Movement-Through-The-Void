## Imports

from math import*
from visual.graph import*
from bodies import*
from random import*
##import Image
##import ImageGrab 

## MKS Units

##Constants

SolarMass = 1.9891  * (10 ** 30)
G         = 6.673   * (10 ** -11)
SpeedOfLight = 299792458
LightYear = 9.4605284 * (10**15)
parsec = 3.08567758 * (10**16)
kpc = 1000*parsec

SunEarthDist =   149597870700



MilkySMBHmass = 4.3 * 10**6 * SolarMass
MilkyRadialScalelength = 2.7 * kpc
MilkyVisibleMass = 400 * 10 ** 9 * SolarMass
MilkyBufferDist = .1 * kpc
MilkyDiameter = 37 * kpc


## Solar System
Sun = Body(mass = SolarMass, position = vector(0,0,0), radius = 1, identity = "Sun")
Earth = Body(mass = 5.97219 * (10 ** 24), position = vector(0,149597870700,0), radius = 1,identity = "earth")
SBody = [Sun, Earth]


## Movement

def Accel(Orbiter,Center):
    """(body,body) -> vector"""
    diff = Orbiter.position - Center.position
    accel = (G*Center.mass) / (mag(diff)**2)
    ACfinal = accel * -diff/mag(diff)
    return ACfinal

def MAccel (System, Timestep):
    """(List of full bodies) -> AutoChangeVelocity / None"""
    for i in range(len(System)):
        if i != 0:
##            Placeholder = Body(position = vector (0,0,0), mass = System[i].OrbitMass, radius = 1)
            System[i].body.velocity += Accel(System[i].body, System[i].OrbitMass) * Timestep

def OneFrameMove(System, Timestep):
    MAccel (System, Timestep)
    for i in range(len(System)):
        if i != 0:
            System[i].body.position += System[i].body.velocity * Timestep
            System[i].visual.pos = System[i].body.position
##            System[i].visual.trail.append(pos = System[i].body.position)

def MultiFrameMove(System, Time, Timestep):
    print int(Time/Timestep),"Frames"
    for i in range(int(Time/Timestep)):
##        print "frame"
        rate(10)
        OneFrameMove(System, Timestep)
##        im = ImageGrab.grab((0,0,900,900))
##        filename = "1000Starframe" + str(i) + ".jpg"
##        im.save(filename)
##        print System[1].body.position,System[1].visual.pos

## Initial Conditions

##Velocities
            
def VelInit(Orbiter,Center):
    """(body,body) -> auto"""
    dist = Center.position-Orbiter.position
    UnitTangentVector = vector(dist.y, -dist.x, 0)/mag(dist)
##    print UnitTangentVector
##    print Center.mass
    Orbiter.velocity = UnitTangentVector * sqrt((Center.mass*G)/mag(dist))
##    print Orbiter.velocity

def SysVelInit(System):
    for i in range(len(System)):
        if i != 0:
##            Placeholder = Body(position = vector (0,0,0), mass = System[i].OrbitMass, radius = 1)
##            print System[i].OrbitMass
            VelInit(System[i].body,System[i].OrbitMass)
            print System[i].body.position


## Physical Galaxy

def PhysicalPopulate(CenterMass, RadialScaleLength, Numstars, VisibleMassNonSMBH, MinDist, Diameter):
    TotMass = CenterMass + VisibleMassNonSMBH
    MeanMass = VisibleMassNonSMBH / Numstars
    SMBHbod = Body(position = vector(0,0,0), mass = CenterMass, radius = 1)
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
    Out = []
    for i in range(Number):
        RandTheta = float(randint(0,2*31415))/10000
        RandDist = float(randint(Min * 1000,Max * 1000))/1000
        Location = vector(RandDist*cos(RandTheta),RandDist*sin(RandTheta),0)
        NewBod = Body(mass = Mass, position = Location, radius = 1)
        Out.append(NewBod)
    return Out
        
## Stats on Galaxy


## Visual Galaxy
def VisualPopulate(ListOfBodies, Diameter):
    Visual = []
    for i in range(len(ListOfBodies)):
        if i != 0:
            single = sphere (pos = ListOfBodies[i].position, radius = Diameter/750 )
##            single.trail = curve(color = color.blue)
        if i == 0:
            single = sphere (pos = ListOfBodies[i].position, radius = Diameter/200 )
            single.color = color.red
        Visual.append(single)
    return Visual

## Orbit Masses
def OrbitMassPopulate(ListOfBodies):
    OrbitMasses = []
    for i in range(len(ListOfBodies)):
        single = 0
        if i != 0:
            for j in range(len(ListOfBodies)):
                if mag(ListOfBodies[j].position) < mag(ListOfBodies[i].position):
##                    print ListOfBodies[j],"<",ListOfBodies[i]
                    single += ListOfBodies[j].mass
##                    print single,SolarMass
        OrbitMasses.append(Body(position = vector(0,0,0), mass = single, radius = 1))
##    print OrbitMasses
    return OrbitMasses

## Create New Galaxy

def CreateGal(CenterMass, RadialScaleLength, Numstars, VisibleMassNonSMBH, MinDist, Diameter):
    ListOfBodies = PhysicalPopulate(CenterMass, RadialScaleLength, Numstars, VisibleMassNonSMBH, MinDist, Diameter)
    ListOfVisuals = VisualPopulate(ListOfBodies, Diameter)
    ListOfOrbitMasses = OrbitMassPopulate(ListOfBodies)
    FullList = []
    for i in range(len(ListOfBodies)):
        Full = FullBody(ListOfBodies[i],ListOfVisuals[i],ListOfOrbitMasses[i])
        FullList.append(Full)
    SysVelInit(FullList)
    return FullList


## Test Harness

##SVisual = VisualPopulate(SBody,9.09*10**12)
####print len(SVisual), SVisual[1].pos
##SOM = OrbitMassPopulate(SBody)
##FullList = []
##for i in range(len(SBody)):
##    Full = FullBody(SBody[i],SVisual[i],SOM[i])
##    FullList.append(Full)
##SysVelInit(FullList)
##MultiFrameMove(FullList, 60*60*366*200, 60*60*24)
##print FullList[1].body.velocity,FullList[1].body.position

display(x = 0, y = 0, width =900, height = 900)

MilkyWay = CreateGal(MilkySMBHmass, MilkyRadialScalelength, 1000,MilkyVisibleMass, MilkyBufferDist, MilkyDiameter)
print "Phase 1 Complete"
print len(MilkyWay),MilkyWay[2].visual.pos, MilkyWay[1].body.position
points = []
for Full in MilkyWay:
    points.append((mag(Full.body.position),mag(Full.body.velocity)))
    
Graph = gdisplay(x = 1000, y = 200, width = 800, height = 400)

VelocityCurve = gdots(x = 0,y = 900, pos = points, color = color.blue)
print "Phase 2 Oomplete"
##im = ImageGrab.grab((1000,200,800,400))
##filename = "VelocityGraph" + ".jpg"
##im.save(filename)

MultiFrameMove(MilkyWay, (60*60*24*366)*1.02*(10**9),(60*60*24*366)*34.1*(10**3) )
print "Phase 3 Complete"
