import rhinoscriptsyntax as rs
import math as m
import Rhino.Geometry as rg
pts = []

def tree(point,length,a1,a2,iterations):
    PtM = rs.PointAdd(point,(length*m.cos(m.radians(a1)),length*m.sin(m.radians(a1)),0))
    Pt1 = rs.PointAdd(PtM,(length*m.cos(m.radians(a1+a2)),length*m.sin(m.radians(a1+a2)),0))
    Pt2 = rs.PointAdd(PtM,(length*m.cos(m.radians(a1-a2)),length*m.sin(m.radians(a1-a2)),0))
    l0 = rg.Line(point,PtM)
    #Problema con rg.Line al procesar "point" dice que es un GUI.
    l1 = rg.Line(PtM,Pt1)
    l2 = rg.Line(PtM,Pt2)
    if iterations>0:
        iterations -= 1
        tree(Pt1,length/1.4,a1/1.1,a2,iterations)
        tree(Pt2,length/1.4,a1/1.1,a2,iterations)
    pts.extend([l0,l1,l2])

tree(Pto,L,Ang1,Ang2,It)
Pt = pts
