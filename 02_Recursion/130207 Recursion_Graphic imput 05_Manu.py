#Recursion para todos_130131 Pythones@Manuel
#Recursive tree from point, angle, initial length and final length

import rhinoscriptsyntax as rs
import random as rd
import math as mt
    
#User comunication module 
def imput(): 
    #Pedimos un punto inicial y un angulo de rotacion
    objPoint = rs.GetPoint("Start point")
    dblAngle = rs.GetReal("angle of rotation", 10, 1, 90)
    #Establecemos un punto de rotura
    initialLength = rs.GetReal("Set initial length",8)
    deadLength = rs.GetReal("Set tree dead length",3)
    #Definimos una reduccion por salto
    ScaleFactor = rs.GetReal("Jump factor scale",0.8)
    #Llamando al motor recursivo
    recursion (objPoint,dblAngle,ScaleFactor,initialLength,deadLength)

#Basic recursive engine
def recursion (ptStart,angle,scale,dista,distb):
    #PtEnds... Intentar hallar el punto de una manera alternativa
    ptEnd1 = rs.PointAdd(ptStart,(dista*mt.cos(angle),dista*mt.sin(angle),0))
    ptEnd2 = rs.PointAdd(ptStart,(-dista*mt.cos(angle),dista*mt.sin(angle),0))
    #Trazamos las lineas
    line1 = rs.AddLine(ptStart,ptEnd1)
    line2 = rs.AddLine(ptStart,ptEnd2)
    #Establecemos un punto de rotura
    if dista>distb:
        recursion (ptEnd1,angle,scale,dista*scale,distb)
        recursion (ptEnd2,angle,scale,dista*scale,distb)
        
imput()