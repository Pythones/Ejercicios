#Turtle para todos_130124 Pythones@Manuel

import rhinoscriptsyntax as rs
import random as rd

def choosingmodule (intMovement,intDistance):
        
    #Dos caminos a elegir
    strMovement = rs.GetString("movement type","gridding",("gridding","triangulate"))
    if strMovement == "gridding": intMovement = 4
    else: intMovement = 8
        
    #scalefactor altera al vector desplazamiento (1,0,0) pasa a (strScale,0,0)
    #intScale = rs.GetInteger("Factor Scale",1,0.1,10)
        
    #este integer es el que alimenta al loop
    intDistance = rs.GetInteger("How long do you want to go?",1000,150,2500)
    
    return (intDistance,intMovement)
    
    
def runningengine():
    
    Pt1 = rs.GetPoint("Select a point to run throw your window")
    intIterations = 0
    intDistance = choosingmodule (intMovement,intDistance)
    intMovement = choosingmodule (intMovement,intDistance)    
    while (intIterations < intDistance):
        
        intScale = rd.uniform(1.0,5.0)
        intIterations = (intIterations+1)
        intrandom = rd.randint(1,intMovement)
        print intrandom
        
        if (intrandom == 1): Pt2 = rs.PointAdd(Pt1,(intScale,0,0))
        elif (intrandom == 2): Pt2 = rs.PointAdd(Pt1,(0,intScale,0))
        elif (intrandom == 3): Pt2 = rs.PointAdd(Pt1,(-intScale,0,0))
        elif (intrandom == 4): Pt2 = rs.PointAdd(Pt1,(0,-intScale,0))
        elif (intrandom == 5): Pt2 = rs.PointAdd(Pt1,(-intScale,-intScale,0))
        elif (intrandom == 6): Pt2 = rs.PointAdd(Pt1,(intScale,-intScale,0))
        elif (intrandom == 7): Pt2 = rs.PointAdd(Pt1,(-intScale,intScale,0))
        elif (intrandom == 8): Pt2 = rs.PointAdd(Pt1,(intScale,intScale,0))
        else: print "la hemos liado"
        
        rs.AddLine(Pt1,Pt2)
        Pt1 = Pt2
    
    
runningengine ()