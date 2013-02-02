#Recursion para todos_130131 Pythones@Manuel

import rhinoscriptsyntax as rs
import random as rd
import math as mt
    
    
def imput():
    #Pedimos dos puntos para linea base y un angulo de rotacion recursiva
    pt1 = rs.GetPoint("Start point")
    pt2 = rs.GetPoint("End point")
    pt3 = rs.GetPoint("specify an angle_imput a revisar (tuple)")
    #Lanzamos la linea base
    l1 = rs.AddLine(pt1,pt2)
    #Calculamos el angulo
    #angle = rs.Angle2((pt1,pt2),(pt1,pt3)) COMO SACAR VALOR DEL TUPLE?
    angle = rs.GetReal("angle of rotation", 10, 1, 90)
    
    recursion (l1,angle)
        
        
def recursion (l1,angle):   
    for i in range(5):
        #Principio y final de curva L1
        ptStart = rs.CurveStartPoint(l1)
        ptEnd = rs.CurveEndPoint(l1)
        #Creamos vector desplazamiento
        v0 = rs.VectorCreate(ptEnd,ptStart)
        v1 = rs.VectorRotate(v0,angle,[0,0,1])
        v2 = rs.VectorRotate(v0,-angle,[0,0,1])
        #Movemos puntos finales
        PtEnda = rs.PointAdd(ptEnd,v1)
        PtEndb = rs.PointAdd(ptEnd,v2)
        #Creamos nuevas lineas
        l1 = rs.AddLine(ptEnd,PtEnda)
        l2 = rs.AddLine(ptEnd,PtEndb) 
        
        
imput()