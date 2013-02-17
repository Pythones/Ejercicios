#Testing new algorithms based on screensaver logic.

import rhinoscriptsyntax as rs
import math as m
import random as r

i = 0

def main():
    #asking for data.
    strPt = rs.GetPoint("Growing point")
    dblLength = rs.GetReal("Initial growing length",1,0.01,10)
    dblAngle = (rs.GetReal("Random angle limit",25,0,90))
    intLimit = rs.GetInteger("Iterations limit",7,1,1000)
    v3dIni = (0,dblLength,0)
    tree(strPt,dblLength, dblAngle, intLimit, i, v3dIni)

def tree(Pto,dblStep,dblAngle,intLimit,x, v3d):
    if x>intLimit: return
    #Never go back
    if dblAngle>90: dblAngle = 90
    PtM = rs.PointAdd(Pto,randomv(v3d,dblAngle,dblStep))
    rs.AddLine(Pto,PtM)
    v3d = rs.VectorCreate(PtM,Pto)
    intBranch = r.randint(1,5)
    #if x>intLimit-0.5: 
        #rs.AddCircle(PtM,0.01*x)
    x+=1
    for x in range(1,intBranch):
        tree(PtM, dblStep*0.9, dblAngle*1.1, intLimit*0.9, x+1, v3d)

#There is a problem with VectorScale and the general algorithm scale.
# Values of 2 in the input generates great results. The smaller the value, the worst the result.

def randomv (vec, maxAngle, maxLength):
    vec = rs.VectorScale(vec,r.uniform(0.5*maxLength,maxLength))
    vec = rs.VectorRotate(vec,randsign()*r.uniform(0.5*maxAngle,maxAngle),(0,0,1))
    return vec

def randsign():
    a = r.randrange(0,2,1)*2-1
    return a
    
main()