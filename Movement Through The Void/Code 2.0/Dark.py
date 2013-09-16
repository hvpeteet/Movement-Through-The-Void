from math import*
from visual.graph import*
from bodies import*
from random import*
from Movement import*
from Birth import*

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



DivisorMass = SolarMass*10000000

def single_orbit_mass_refresh(System,StarNum):
    System.sort()
    lower_mass = 0
    for i in range (StarNum):
        lower_mass += System[i].body.mass
    System[StarNum].OrbitMass.mass = lower_mass
def create_DM_in_area(Min,Max,Mass,SingleMass):
    DM_List = []
##    print "creating", int(Mass/SingleMass), "stars"
##    print " ....................."
    for i in range(int(Mass/SingleMass)):
        RandTheta = float(randint(0,2*31415))/10000
        RandDist = float(randint(Min * 1000,Max * 1000))/1000
        Location = vector(RandDist*cos(RandTheta),RandDist*sin(RandTheta),0)
        NewBod = Body(mass = SingleMass, position = Location)
        NewVisual = sphere (pos = Location + vector(0,0,0), radius = MilkyDiameter/750, color = (.2,0,1))
        DM = FullBody(NewBod, NewVisual, Body(position = vector(0,0,0), mass = 0), Type = "DM")
        DM_List.append(DM)
    return DM_List
    
def DarkCompensate(F_B_System):
    F_B_System.sort()
    max_vel = 0
    max_vel_star = 0
    addendum = 0
    for star in range(len(F_B_System)):
        if mag(F_B_System[star].body.velocity)> max_vel:
            max_vel = mag(F_B_System[star].body.velocity)
            max_vel_star = star
    print max_vel, max_vel_star
    addendum = max_vel_star
    compensate_num = len(F_B_System)-max_vel_star
    for i in range(compensate_num-1):
        
        star = addendum + i + 1
        single_orbit_mass_refresh(F_B_System, star)
        single_orbit_mass_refresh(F_B_System, star - 1)
##        print "at star number: ", star
        CM1 = F_B_System[star-1].OrbitMass.mass
        CM2 = F_B_System[star].OrbitMass.mass
        r1  = mag(F_B_System[star - 1].body.position)
        r2  = mag(F_B_System[star].body.position)
##        print CM1<CM2,r1<r2
        needed_mass = (CM1 * r2 / r1) - CM2
        if needed_mass < 0:
            needed_mass = 0
##        print "needed: " , needed_mass


        
        ## create needed mass
        F_B_System += create_DM_in_area(r1,r2,needed_mass,DivisorMass)
        F_B_System.sort()
        addendum += int(needed_mass/DivisorMass)
        
        
    
