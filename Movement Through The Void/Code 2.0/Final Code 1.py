## Imports

from math import*
from visual import*
from visual.graph import*
from bodies import*
from random import*
from Movement import*
from Birth import*
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


## Test Harness

display(x = 0, y = 0, width =700, height = 700)

MilkyWay = CreateGal(MilkySMBHmass, MilkyRadialScalelength, 100, MilkyVisibleMass, MilkyBufferDist, MilkyDiameter)
MilkyCopy = []
for Full in MilkyWay:
    if Full.type == 'Visible':
        MilkyCopy.append(Full.copy())
displacement = 2*(10**21)
for Full in MilkyCopy:
    Full.visual.pos+=vector(displacement,0,0)
    Full.body.position+=vector(displacement,0,0)
    Full.OrbitMass.position+=vector(displacement,0,0)
MilkyCopy.sort()
MilkyCopyBodies = []
for full in MilkyCopy:
    MilkyCopyBodies.append(full.body)
MilkyCopyOrbit = OrbitMassPopulate(MilkyCopyBodies)
for i in range(len(MilkyCopy)):
    MilkyCopy[i].OrbitMass = MilkyCopyOrbit[i]
    MilkyCopy[i].OrbitMass.position += vector(displacement,0,0)
SysVelInit(MilkyCopy)
print len(MilkyCopy)
##for i in range(len(MilkyWay)):
##    print MilkyWay[i].body.position - MilkyCopy[i].body.position
## run add dak matter function
##DarkCompensate(MilkyWay)
totMass = 0
normMass= 0
print "Phase 1 Complete"
print len(MilkyWay),MilkyWay[2].visual.pos, MilkyWay[1].body.position
points = []
for Full in MilkyWay:
    if Full.type != "DM":
        totMass += 1
        points.append((mag(Full.body.position),mag(Full.body.velocity)))
    else:
        normMass += 1
DM_Dist_List = []
Visible_Dist_List = []
for Matter in MilkyWay:
    if (Matter.type == "DM"):
        DM_Dist_List.append(mag(Matter.body.position))
    else:
        Visible_Dist_List.append(mag(Matter.body.position))
graph = ghistogram(bins = arange(0, max(DM_Dist_List), max(DM_Dist_List)/100), color = (.2,0,1))
graph.plot(data = DM_Dist_List)
DM_Mass = totMass * SolarMass*100000000
normMass = normMass * MilkyVisibleMass / 10000
totMass = DM_Mass + normMass
print DM_Mass / totMass

##DM_Density_Bins = []
##maxdlist = max(DM_Dist_List)
##mindlist = min(DM_Dist_List)
##for i  in range(100):
##    DM_Density_Bins.append(0)
##for DM in DM_Dist_List:
##    DM_Density_Bins[int(DM/(maxdlist - mindlist))] += 1
##Graph = gdisplay(x = 1200, y = 0, width = 1200, height = 400)
##Density_Graph = gdots(x = 0, y = 900, pos = DM_Density_Bins, color = color.red)
##Density_Graph.plot(data = DM_Dist_List)
##VelocityCurve = gdots(x = 0,y = 900, pos = points, color = color.blue)
print "Phase 2 Complete"
##MultiFrameMove(MilkyWay, (60*60*24*366)*1.02*(10**9),(60*60*24*366)*34.1*(10**3) )
RunFrames = (60*60*24*366)*1.02*(10**6)
i = 0
while i < int(RunFrames):
    OneFrameMove(MilkyWay, (60*60*24*366)*34.1*(10**3))
    OneFrameMove(MilkyCopy, (60*60*24*366)*34.1*(10**3))
    i += 1
print "Phase 3 Complete"
