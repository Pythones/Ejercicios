import rhinoscriptsyntax as rs
import math as m
import random as r


def Main():
    #strPt0= rs.GetPoint("Introduzca el punto de origen")
    ptsList = []
    ptsList = rs.GetPointCoordinates("Introduzca varios puntos")
    dblDist = rs.GetReal("Distancia de la rama",4)
    dblAngle = m.radians(rs.GetReal("Dame Angulo",10))
    
    for i in range (len(ptsList)):
        Ramas(ptsList[i],dblDist,dblDistNo,dblAngle)
    
    
def Ramas(punto,dist,dist2,angle):
    
    strPtM= rs.PointAdd(punto,(0,dist,0))
    strPt1= rs.PointAdd(strPtM,(dist*m.cos(angle),dist*m.sin(angle),0))
    strPt2= rs.PointAdd(strPtM,(-dist*m.cos(angle),dist*m.sin(angle),0))
    rs.AddLine(punto,strPtM)
    rs.AddLine(strPtM,strPt1)
    rs.AddLine(strPtM,strPt2)
    if dist>dist2/100: 
        Ramas(strPt1,dist/1.2,2,angle-(m.pi/12))
        Ramas(strPt2,dist/2,2,angle-(m.pi/12))
    else: return
    
    
Main()