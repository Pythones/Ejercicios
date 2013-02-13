import rhinoscriptsyntax as rs
import math as m
import Rhino.Geometry as rg
import random as rd
pts = []

def tree(point,length,a1,a2,iterations):
    PtM = rs.PointAdd(point,(length*m.cos(m.radians(a1)),length*m.sin(m.radians(a1)),0))
    Pt1 = rs.PointAdd(PtM,(length*m.cos(m.radians(a1+a2)),length*m.sin(m.radians(a1+a2)),0))
    Pt2 = rs.PointAdd(PtM,(length*m.cos(m.radians(a1-a2)),length*m.sin(m.radians(a1-a2)),0))
    l0 = rg.Line(point,PtM)
    #Problema con rg.Line al procesar "point" dice que es un GUI.
    l1 = rg.Line(PtM,Pt1)
    l2 = rg.Line(PtM,Pt2)
    choiceA = rd.randint(0,100)
    if iterations>0 and choiceA>=10:
        iterations -= 1
        choiceB1 = rd.randint(0,100)
        choiceB2 = rd.randint(0,100)
        if choiceB1 > ((iterations/It)*100)-70:
            tree(Pt1,length/ScaleRat,a1+AngRat1,a2+AngRat2,iterations)
        if choiceB2 > ((iterations/It)*100)-70:
            tree(Pt2,length/ScaleRat,a1+AngRat1,a2+AngRat2,iterations)
    pts.extend([l0,l1,l2])

tree(Pto,L,Ang1,Ang2,It)
Pt = pts
