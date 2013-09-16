from math import*
import numpy as np
import pylab as pl
f=open('test1.txt','w')
i=1
c=0
z_list=[1,]
c_list=[0,]
while c<10:
    c=c+1
    while i<10:
        z=z_list[i-1]
        z_list.append((z**2)+c)
        c_list.append(c)
        i=i+1

for h in z_list:
    print h
pl.plot(c_list,z_list)
pl.show()
