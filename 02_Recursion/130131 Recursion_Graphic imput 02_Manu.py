#Recursion para todos_130131 Pythones@Manuel

import rhinoscriptsyntax as rs
import random as rd
import math as mt
    
    
def imput():
    pt1 = rs.GetPoint("Start point")
    pt2 = rs.GetPoint("Next point")
    pt3 = rs.GetPoint("End point")
    
    l1 = rs.AddLine(pt1,pt2)
    l2 = rs.AddLine(pt2,pt3)
    l3 = rs.MirrorObject(l2,pt1,pt2,True)    
    
    recursion (l1,l2,l3)
        
        
def recursion (l1,l2,l3):   
    for i in range(5):
        #Principios y finales de curvas L1 y L2
        ptStart = rs.CurveStartPoint(l1)
        ptEnd = rs.CurveEndPoint(l2)
        #Creamos vector desplazamiento del grupo de tres lineas
        v1 = rs.VectorCreate(ptEnd,ptStart)
        #Creamos nuevas lineas
        l1 = rs.CopyObject(l1,v1)
        l2 = rs.CopyObject(l2,v1)
        l3 = rs.CopyObject(l3,v1)
        
        
imput()