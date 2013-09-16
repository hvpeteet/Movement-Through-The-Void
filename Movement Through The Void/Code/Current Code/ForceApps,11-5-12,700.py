from math import*
from visual import*
from PlanetsClass import*

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
    new_vel=velocity+.5*(accel*timestep)
    return new_vel

def update_pos(Position,Velocity,Timestep):
    pos=Position+Velocity*Timestep
    return pos

def simulate_one_step(L_Of_Bodies,t):
    for body1 in range(len(L_Of_Bodies)):
        accel=0
        for body2 in range(body1+1,len(L_Of_Bodies)):
            L_Of_Bodies[body1].accel,L_Of_Bodies[body2].accel=accel_gravity(L_Of_Bodies[body1].position,L_Of_Bodies[body2].position,L_Of_Bodies[body1].mass,L_Of_Bodies[body2].mass)
        update_pos(L_Of_Bodies[body1].position,L_Of_Bodies[body1].velocity,t)


##Test Harness
L1=vector(0,0,0)
L2=vector(1,0,0)
m1=2
m2=.5
print gravity(L1,L2,m1,m2)
print accel_gravity(L1,L2,m1,m2)

x=planet(
test=[x,y,z]
simulate_one_step(test,1)

