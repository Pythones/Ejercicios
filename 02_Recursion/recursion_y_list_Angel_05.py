import rhinoscriptsyntax as rs
import math as m
import random as r



def RAMAS(punto,dist,angle):
    strPtM= rs.PointAdd(punto,(0,dist,0))
    #ang1=r.uniform(A,B)
    #ang2=r.uniform(A,B)
    strPt1= rs.PointAdd(strPtM,(dist*m.cos(angle),dist*m.sin(angle),0))
    strPt2= rs.PointAdd(strPtM,(-dist*m.cos(angle),dist*m.sin(angle),0))
    rs.AddLine(punto,strPtM)
    rs.AddLine(strPtM,strPt1)
    rs.AddLine(strPtM,strPt2)
    if dist>dblDist/100: 
        RAMAS(strPt1,dist/1.2,angle+(m.pi/12))
        RAMAS(strPt2,dist/2,angle+(m.pi/12))
    else: return

def main():
    strPt0 = []
    strPt0= rs.GetPointCoordinates("Introduzca puntos de origen")
    dblDist= rs.GetReal("Distancia de la rama")
    dblAngle = m.radians(rs.GetReal("Angulo de dibujo en grados"))
    
    rs.EnableRedraw(False)
    
    for i in range(len(strPt0)):
        RAMAS(strPt0[i],dblDist,dblAngle)
    
    rs.EnableRedraw(True)
    
main()