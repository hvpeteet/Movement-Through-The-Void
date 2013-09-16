from math import*
from visual.graph import*
from bodies import*
from random import*

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

def Accel(Orbiter,Center):
    """(body,body) -> vector
    creates a acceleration vector from the orbiter to the center mass based on gravity"""
    diff = Orbiter.position - Center.position
    accel = (G*Center.mass) / (mag(diff)**2)
    ACfinal = accel * -diff/mag(diff)
    return ACfinal

def MAccel (System, Timestep):
    """(List of full bodies) ->  void
    applies the acceleration due to gravity to a system of full bodies"""
    for i in range(len(System)):
        if i != 0:
            System[i].body.velocity += Accel(System[i].body, System[i].OrbitMass) * Timestep

def OneFrameMove(System, Timestep):
    """(List of Full Bodies, int) -> void
    moves each body in the system according to velocity and gravity"""
    MAccel (System, Timestep)
    for i in range(len(System)):
        if i != 0 and System[i].type != "DM":
            System[i].body.position += System[i].body.velocity * Timestep
            System[i].visual.pos = System[i].body.position
            System[i].visual.trail.append(pos = System[i].body.position)

def MultiFrameMove(System, Time, Timestep):
    """(List of Full Bodies, int, int) -> Void
    moves all bodies in a system according to velocity and gravity"""
    print int(Time/Timestep),"Frames"
    for i in range(int(Time/Timestep)):
        rate(10)
        OneFrameMove(System, Timestep)
##        im = ImageGrab.grab((0,0,900,900))
##        filename = "1000Starframe" + str(i) + ".jpg"
##        im.save(filename)
##        print System[1].body.position,System[1].visual.pos

