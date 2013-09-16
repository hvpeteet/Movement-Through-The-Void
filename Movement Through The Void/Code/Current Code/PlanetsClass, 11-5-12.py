from math import*
from visual import*

class Body(object):
    Bodies={}
    def __init__(self,mass=0,position=vector(0,0,0),velocity=vector(0,0,0),identity=0):
        assert type(identity)==string and identity!=0 and identity not in Bodies
        self.mass=mass
        self.position=position
        self.velocity=velocity
        self.accel=0
    
