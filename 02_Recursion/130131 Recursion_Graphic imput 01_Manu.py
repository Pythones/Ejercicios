#Recursion para todos_130131 Pythones@Manuel

import rhinoscriptsyntax as rs
import random as rd
import math as m

#def main():
    #Pt1 = rs.GetPoint("Choose a point")
    #dblLength = rs.GetReal("dame un largor",1,0.1,15)
    #dblalpha1 = m.radians(rs.GetReal("alpha1 (degrees)",45,30,150)
    #dblalpha2 = m.radians(180 - dblalpha1)
    #dblbeta1 = m.radians(rs.GetReal("alpha1 (degrees)",45,30,150)
    #rd.uniform()
    
def imput():
    pt1 = rs.GetPoint("Start point")
    pt2 = rs.GetPoint("Next point")
    rs.AddLine(pt1,pt2)
    pt3 = rs.GetPoint("End point")
    rs.AddLine(pt2,pt3)
    dblLine2 = rs.AddLine(pt2,pt3)
    rs.MirrorObject(dblLine2,pt1,pt2)

#def recursion():    

imput()