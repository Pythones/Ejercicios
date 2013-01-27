#Turtle para todos
#130124 Pythones@Manuel

import rhinoscriptsyntax as rs
import random as rd

        
def movingToLeft():
    
    Pt1 = rs.GetPoint("Select a point to run throw your window")
    intIterations = 0
    while (intIterations < 500):
        intIterations = (intIterations+1)
        intrandom = rd.randint(1,4)
        print intrandom
        if (intrandom == 1):
            Pt2 = rs.PointAdd(Pt1,(1,0,0))
        elif (intrandom == 2):
            Pt2 = rs.PointAdd(Pt1,(0,1,0))
        elif (intrandom == 3):
            Pt2 = rs.PointAdd(Pt1,(-1,0,0))
        else:
            Pt2 = rs.PointAdd(Pt1,(0,-1,0))
            
        rs.AddLine(Pt1,Pt2)
        Pt1 = Pt2
    
movingToLeft()