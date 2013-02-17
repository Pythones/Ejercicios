#Testing new algorithms based on screensaver logic.

import rhinoscriptsyntax as rs
import math as m
import random as r
i = 0

def main():
    #asking for data.
    dblLength = rs.GetReal("Initial growing length",1,0.01,10)
    dblAngle = m.radians(rs.GetReal("Random angle limit",10,0,90))
    strPt = rs.GetPoint("Growing point")
    tree(strPt,dblLength, dblAngle)

def tree(Pto,dblStep,dblAngle):
    dblRand = r.uniform(-dblAngle,dblAngle)
    v3dRand = (m.cos(dblRand+(m.pi/2)),m.sin(dblRand+(m.pi/2)),0)
    PtM = rs.PointAdd(Pto,v3dRand)
    rs.AddLine(Pto,PtM)
    global i
    i += 1
    if i<200:
        tree(PtM,dblStep,dblAngle*1.1)

main()