#Recursion para todos_130131 Pythones@Manuel
#Recursive tree from three points and a final length

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
    ScaleFactor = rs.GetReal("Jump factor scale",0.9)
    #Establecemos un punto de rotura
    deadLength = rs.GetReal("Set tree dead length",0.5)
    #borramos l2
    rs.DeleteObject(l2)
    
    recursion (l1,dblAngle,ScaleFactor,initialLength,deadLength)
    
    
def recursion (line,angle,scale,dista,distb):
    #Analizo la linea
    pointStart = rs.CurveStartPoint(line)
    pointEnd = rs.CurveEndPoint(line)
    dist = rs.CurveLength(line)
    #obtengo su vector
    vector1 = rs.VectorCreate(pointEnd,pointStart)
    vector2 = rs.VectorScale(vector1,scale)
    v1 = rs.VectorRotate(vector2,angle[0],(0,0,1))
    v2 = rs.VectorRotate(vector2,-angle[0],(0,0,1))
    #Lanzo dos puntos
    pointv1 = rs.PointAdd(pointEnd,v1)
    pointv2 = rs.PointAdd(pointEnd,v2)
    #Incorporo nuevas lineas
    lv1 = rs.AddLine(pointEnd,pointv1)
    lv2 = rs.AddLine(pointEnd,pointv2)
    #Fabricamos un brake aleatorio
    brake = rd.randint(0,2)
    #Punto de rotura
    if dist*brake>distb:
        recursion(lv1,angle,scale,dist,distb)
        recursion(lv2,angle,scale,dist,distb)
    
    
imput()