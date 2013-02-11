#Recursion para todos_130131 Pythones@Manuel
#Recursive tree from three lines and a final length

import rhinoscriptsyntax as rs
import random as rd
import math as mt
    
    #User comunication module 
def imput(): 
    #Pedimos dos puntos para linea base y un angulo de rotacion recursiva
    pt1 = rs.GetPoint("Start point")
    pt2 = rs.GetPoint("Next point")
    l1 = rs.AddLine(pt1,pt2)
    pt3 = rs.GetPoint("End point")
    l2 = rs.AddLine(pt2,pt3)
    #Calculamos el angulo de giro recursivo
    dblAngle = rs.Angle2(l1,l2)
    #Calculamos la longitud inicial dada por el usuario
    initialLength = rs.CurveLength(l1)
    #Definimos una reduccion por salto
    ScaleFactor = rs.GetReal("Jump factor scale",.8)
    #Establecemos un punto de rotura
    deadLength = rs.GetReal("Set tree dead length",3)
    
    recursion (pt1,dblAngle,ScaleFactor,initialLength,deadLength)
        
def recursion (point,angle,scale,dista,distb):
    #Principio y final de Line
    ptStart = rs.CurveStartPoint(line)
    ptEnd = rs.CurveEndPoint(line)
    #Creamos vector desplazamiento
    v = rs.VectorCreate(ptEnd,ptStart)
    v0 = rs.VectorScale(v,scale)
    v1 = rs.VectorRotate(v0,angle,[0,0,1])
    v2 = rs.VectorRotate(v0,-angle,[0,0,1])
    
    
    #Movemos puntos finales
    PtEnda = rs.PointAdd(ptEnd,v1)
    PtEndb = rs.PointAdd(ptEnd,v2)
    #Creamos nuevas lineas
    line1 = rs.AddLine(ptEnd,PtEnda)
    line2 = rs.AddLine(ptEnd,PtEndb)
    dista = rs.CurveLength(line1)
    #Establecemos un punto de rotura
    if dista>distb:
        recursion (line1,angle,scale,distb)
        recursion (line2,angle,scale,distb)
        
        
imput()