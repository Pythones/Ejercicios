#probando bugs de turtle
#el problema esta en Pt1, pues Pt2 nace de su desplazamiento.
#parece que una vez desplazado no existe Pt1. Aparece Pt3 solo por rastrear el bug
#130126 Pythones@manu

import rhinoscriptsyntax as rs
import random as rd

Pt1 = rs.GetObject("pica sobre un punto")
Pt3 = rs.GetObject("pica sobre otro punto")

def prueba():
    rs.AddPoint(Pt1)
    intrandom = rd.randint(1,2)
    print intrandom
    
    if (intrandom == 1):
        Pt2 = rs.MoveObject(Pt1,(1,0,0))
    elif (intrandom == 2):
        Pt2 = rs.MoveObject(Pt1,(0,1,0))
    else:
        print "achuparla"
        
    rs.AddLine(Pt3,Pt2)
    
prueba()