import rhinoscriptsyntax as rs
import math as m
import random as r

strPt0= rs.GetPoint("Introduzca el punto de origen")
dblDist= rs.GetReal("Distancia de la rama")
dblA=m.pi/3



def RAMAS(punto,dist,A):
    #Calculamos el punto M
    strPtM= rs.PointAdd(punto,(0,dist,0))
    #Calculamos los angulos aleatorios entre los extremos que hemos fijado
    #Calculamos los puntos extremos
    strPt1= rs.PointAdd(strPtM,(dist*m.cos(A),dist*m.sin(A),0))
    strPt2= rs.PointAdd(strPtM,(-dist*m.cos(A),dist*m.sin(A),0))
    rs.AddLine(punto,strPtM)
    rs.AddLine(strPtM,strPt1)
    rs.AddLine(strPtM,strPt2)
    if (dist>dblDist/5 and r.randint(0,10)>2): 
        if r.randint(0,20)>1:
            RAMAS(strPt1,dist-(dist/5),A*1.1)
        if r.randint(0,20)>1:           
            RAMAS(strPt2,dist-(dist/5),A*1.1)
    else: return

#rs.EnableRedraw(False)
RAMAS(strPt0,dblDist,dblA)
#rs.EnableRedraw(True) 