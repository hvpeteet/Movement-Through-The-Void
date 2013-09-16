from math import*
from visual import*

def gravity(Location_Vector_1,Location_Vector_2,mass_1,mass_2):
    G=1
    Difference_Vector=Location_Vector_2-Location_Vector_1
    ## Sets Force vector equal to newtonian gravitation for G
    Force_Vector=Difference_Vector*G*(mass_1*mass_2)/(mag(Difference_Vector)**2)
    return Force_Vector,-Force_Vector

def accel_gravity(Location_Vector_1,Location_Vector_2,mass_1,mass_2):
    F1,F2=gravity(Location_Vector_1,Location_Vector_2,mass_1,mass_2)
    Accel_1,Accel_2=F1/mass_1,F2/mass_2
    return Accel_1,Accel_2

def update_vel(accel,velocity,timestep):
    new_vel=velocity+(accel*timestep)
    return new_vel

##Test Harness
L1=vector(0,0,0)
L2=vector(1,0,0)
m1=2
m2=.5
print gravity(L1,L2,m1,m2)
print accel_gravity(L1,L2,m1,m2)
