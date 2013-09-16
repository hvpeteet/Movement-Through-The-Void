from math import*
from visual import*
print pi
class planet(object):
    def __init__(self,mass=0.0,position=vector(0,0,0),velocity=vector(0,0,0),volume=0.0):
        """Takes a mass as a float, a position as a vector, a velocity as a vector,and volume as a float.
            This class allows for analysis of solar systems and galaxies"""
##        assert type(mass)==float,type(position)==vector,type(velocity)==vector,type(volume)=float
        self.mass=mass
        self.position=position
        self.velocity=velocity
        self.volume=volume
        self.density=mass/volume
        
##       Get Functions
    def get_mass(self):
        return self.mass
    def get_position(self):
        return self.position
    def get_velocity(self):
        return self.velocity
    def get_volume(self):
        return self.volume
    def get_density(self):
        return self.density
    
##      Set Functions
    def set_mass(self,mass):
        """Sets a float as the mass of the celestial body"""
        self.mass=mass
        self.density=self.mass/self.volume
    def set_position(self,position):
        """Sets a vector as the postion vector of a celestial body"""
        self.position=position
    def set_velocity(self,velocity):
        """Sets a vector as the velocity vector for a celestial body"""
        self.velocity=velocity
    def set_volume(self,volume):
        """Sets a float as the volume of celestial body"""
        self.volume=volume
        self.density=self.mass/self.volume

        
def Gravity(Planet1,Planet2,G=1):
    """Takes two celestial bodies and identifies the gravitational force from the two, outputting two acceleration vectors"""
    dist=mag(Planet1.position-Planet2.position)
    print dist
    force=G*((Planet1.mass*Planet2.mass)/(dist**2))
    print force
    force_vector=force*(Planet2.position-Planet1.position)/mag(Planet2.position-Planet1.position)
    accel_vector_1=force_vector/Planet1.mass
    accel_vector_2=(-force_vector)/Planet2.mass
    return accel_vector_1,accel_vector_2

def Simulate_Movement(system,t):
    """simulates movement of a system of bodies for time t, the smaller the time the more precise the measurement"""
    assert type(system)==list
    for i in range(len(system)):
        for k in range(len(system)-i):
            k=len(system)-k-1
            if i!=k:
##                print "change made"

## inputs
                Planet1=system[i]
                Planet2=system[k]

## Gravity acceleration and velocity
                new_vel_1,new_vel_2=Gravity(Planet1,Planet2)
                new_vel_1,new_vel_2=new_vel_1*t,new_vel_2*t
##                print Planet1.velocity,Planet2.velocity
##                print new_vel_1,new_vel_2
                Planet1.velocity=Planet1.velocity+new_vel_1
                Planet2.velocity=Planet2.velocity+new_vel_2
##                print new_vel_1==-new_vel_1

## Gravity causing Postion change
    for Star in system:
        Star.position=Star.position+Star.velocity*t


        
x=planet(5,vector(10.0,0.0,0.0),vector(0.0,0.0,0.0),5)
y=planet(5,vector(0.0,0.0,0.0),vector(0.0,0.0,0.0),5)
z=planet(5,vector(-10.0,0.0,0.0),vector(0.0,0.0,0.0),5)
sys=[x,y,z]



Simulate_Movement(sys,1)
print x.position,x.velocity
print y.position,y.velocity
print z.position,z.velocity

## System to calculate for time t with interval i

##Begin Visual Element


