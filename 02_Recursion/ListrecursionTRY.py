#Rewritten recursive action LISTS
#Imput: Point+Angle+scaleFactor+endLength

import rhinoscriptsyntax as rs
import math as mt


#User comunication
def Main():
    #List creation
    Pts1,Pts2 = []
    #Pts2 = []
    #Feeding first list
    Pts1 = rs.GetObjects("Set points",rs.filter.point)
    if Pts1 is None: return
    #Feeding second list
    for i in range(len(Pts1)):
        Pts2.append(rs.PointAdd(Pts1[i],(0,10,0)))
        rs.AddCircle(Pts2[i],10)
        rs.AddLine(Pts1[i],Pts2[i])
    #dblAngle = rs.GetReal("Choose an angle",10)
    #endLength = rs.GetReal("Dead length",5)
    #scaleFactor = rs.GetReal("Scale Factor",0.9)
    return
    
Main()