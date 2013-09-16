
class weight(object):
    def __init__(self, mass, units = 'kg'):
        """
            if units = 'kg' takes mass in kilograms
            if units = 'lb' takes mass in lbs
        """
        mass = float(mass)
        if units == 'kg':
            self.kg = mass
            self.g = mass*1000
            self.solar = mass/(1.9891 * (10 ** 30))
            self.mton = mass/1000
            self.lb = 2.20462*mass
            self.ston = self.lb/2000
        if units == 'lb':
            self.kg = mass/2.20462
            self.g = self.kg*1000
            self.solar = self.kg/(1.9891 * (10 ** 30))
            self.mton = self.kg/1000
            self.lb = mass
            self.ston = mass/2000

I = weight(190,'lb')
print I.kg
print I.g
print I.solar
print I.mton
print I.lb
print I.ston
