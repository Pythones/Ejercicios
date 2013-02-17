#Testing new algorithms based on screensaver logic.

import rhinoscriptsyntax as rs
import math as m
import random as r
i = 0

def main():
    #asking for data.
    dblLength = rs.GetReal("Initial growing length",1,0.01,10)
    dblAngle = m.radians(rs.GetReal("Random angle limit",25,0,90))
    strPt = rs.GetPoint("Growing point")
    intLimit = rs.GetInteger("Iterations limit",7,1,1000)
    tree(strPt,dblLength, dblAngle, intLimit, i)

def tree(Pto,dblStep,dblAngle,intLimit,x):
    if x>intLimit: return
    dblRand = r.uniform(-dblAngle,dblAngle)
    v3dRand = (m.cos(dblRand+(m.pi/2)),m.sin(dblRand+(m.pi/2)),0)
    PtM = rs.PointAdd(Pto,v3dRand)
    rs.AddLine(Pto,PtM)
    intBranch = r.randint(1,5)
    if x>intLimit-0.5: 
        rs.AddCircle(PtM,0.01*x)
    x+=1
    for x in range(1,intBranch):
        tree(PtM,dblStep*0.8,dblAngle*1.1,intLimit*0.9,x+1)

main()