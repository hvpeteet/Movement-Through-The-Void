from visual import*
from math import*


class system(object):
    def __init__(self):
        self.all_sub_systems=[]
    def __str__(self):
        out=""
        for planet in self.all_sub_systems:
            out+= (str(planet)+",")
        return out
    def __add__(self,other):
        return self.combine(other)
    def combine(self,other):
        return set(self.all_sub_systems+other.all_sub_systems)
    
    def Gravity_In_Sys(self):
        print "hello"
class planet(object):
    def __init__(self,Parent_System,alias="unknown"):
        self.alias=alias
        self.radius=.5
        self.location=vector(0,0,0)
        self.velocity=vector(0,0,0)
        self.mass=0
        self.color="white"
        self.volume=(4/3)*pi*(self.radius**3)
        Parent_System.all_sub_systems.append(self)
    def __str__(self):
        return "Planet"+":"+self.alias+" "+str(self.location)




    

#Test Harness

    
a=system()
b=system()
x=planet(a,"earth")
y=planet(a)
z=planet(b,"mars")
print a
print b
print x
a.combine(b)
print a
a+b

##def Interpret_Planet_Input(text):
##    dividers=[]
##    stop=False
##    place_in_text=0
##    while stop==False:
##        try:
##            dividers.append(text.index(",",place_in_text))
##            place_in_text=dividers[-1]+1
##        except ValueError:
##            stop=True
##    location=text[dividers[
##    return dividers
##
##print Interpret_Planet_Input("<0,0,1,,>")
