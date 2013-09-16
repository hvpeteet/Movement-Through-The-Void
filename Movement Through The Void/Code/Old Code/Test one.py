from visual import*
##xearth=0
##yearth=0
##zearth=0
##Earth = sphere(pos=vector(xearth,yearth,zearth), color=color.blue, radius=.5)
##TangentVect=arrow(pos=Earth.pos, axis=vector(1,1,1))
P1=sphere(pos=(0,0,0),radius=.5,color=color.blue)
P2=sphere(pos=(1,1,1),radius=.3,color=color.yellow)
P3=sphere(pos=(1,-1,-1),radius=.5,color=color.green)
P4=sphere(pos=(-2,-2,1),radius=.7,color=color.cyan)

PList=[P1,P2,P3,P4]
##print len(PList)
for Dist in range(len(PList)):
##    print "Hellow"
    if Dist==len(PList)-1:
        PFinal=PList[0]
    else:
        PFinal=PList[Dist+1]
    POrig=PList[Dist]
    arrow(pos=POrig.pos,axis=PFinal.pos-POrig.pos,color=color.yellow)
