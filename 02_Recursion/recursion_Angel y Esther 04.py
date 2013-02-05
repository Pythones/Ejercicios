import rhinoscriptsyntax as rs
import math as m
import random as r

strPt0= rs.GetPoint("Introduzca el punto de origen")
dblDist= rs.GetReal("Distancia de la rama")
dblA=2*m.pi/6
dblB=4*m.pi/6


def RAMAS(punto,dist,A,B):
    strPtM= rs.PointAdd(punto,(0,dist,0))
    ang1=r.uniform(A,B)
    ang2=r.uniform(A,B)
    strPt1= rs.PointAdd(strPtM,(dist*m.cos(ang1),dist*m.sin(ang1),0))
    strPt2= rs.PointAdd(strPtM,(-dist*m.cos(ang2),dist*m.sin(ang2),0))
    rs.AddLine(punto,strPtM)
    rs.AddLine(strPtM,strPt1)
    rs.AddLine(strPtM,strPt2)
    if dist>dblDist/100: 
        RAMAS(strPt1,dist/1.2,A-(m.pi/12),B+(m.pi/12))
        RAMAS(strPt2,dist/2,A-(m.pi/12),B+(m.pi/12))
    else: return

RAMAS(strPt0,dblDist,dblA,dblB)
    