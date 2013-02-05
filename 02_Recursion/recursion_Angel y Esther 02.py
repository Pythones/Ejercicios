import rhinoscriptsyntax as rs
import math as m
import random as r

strPt0= rs.GetPoint("Introduzca el punto de origen")
dblDist= rs.GetReal("Distancia de la rama")
dblTheta=r.uniform(-m.pi/6,m.pi*7/6)
dblAlpha=r.uniform(-m.pi/6,m.pi*7/6)

def RAMAS(punto,dist,ang1,ang2):
    strPtM= rs.PointAdd(punto,(0,dist,0))
    strPt1= rs.PointAdd(strPtM,(dist*m.cos(ang1),dist*m.sin(ang1),0))
    strPt2= rs.PointAdd(strPtM,(-dist*m.cos(ang2),dist*m.sin(ang2),0))
    rs.AddLine(punto,strPtM)
    rs.AddLine(strPtM,strPt1)
    rs.AddLine(strPtM,strPt2)
    if dist>dblDist/100: 
        RAMAS(strPt1,dist/2,ang1/2,ang2/2)
        RAMAS(strPt2,dist/2,ang1/2,ang2/2)
    else: return

RAMAS(strPt0,dblDist,dblTheta,dblAlpha)
    