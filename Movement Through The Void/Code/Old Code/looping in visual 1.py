from visual import*
from math import*
##n=1
##while n<=10:
##    print n
##    n=n+1
##print "end of program"

PPlanet=sphere(pos=vector(0,0,0),radius=.25,color=color.blue)
PMoon=sphere(pos=vector(1,1,1),radius=.125,color=color.white)
t=0
r=vector(0,0,0)
Dist=arrow(pos=PPlanet.pos,axis=vector(0,0,0))

PMoon.trail=curve(color=color.blue)
while t<100:
    rate(7)
    r=(sin(t),cos(t),sin(t))
    PMoon.pos=r
    PMoon.trail.append(pos=PMoon.pos)
##    Dist.axis=PMoon.pos-PPlanet.pos
    t=t+.1
