#Turtle para todos_130124 Pythones@Manuel

import rhinoscriptsyntax as rs
import random as rd

def choosingmodule ():
        
    #Dos caminos a elegir: triangulas, cuadriculas o mezclas
    strMovement = rs.GetString("movement type","gridding",("gridding","triangulate","mixed"))
    if strMovement == "gridding":
        intMovement1 = 1
        intMovement2 = 4
    elif strMovement == "triangulate":
        intMovement1 = 5
        intMovement2 = 8 
    else: 
        intMovement1 = 1
        intMovement1 = 8
        
    #En este script la escala del salto no se elije, es un random (line 27)
        
    #este integer es el que alimenta al loop
    intDistance = rs.GetInteger("How long do you want to go?",1000,150,2500)
    
    runningengine(intMovement1,intMovement2,intDistance)
    
    
def runningengine(intMovement1,intMovement2,intDistance):
    
    Pt1 = rs.GetPoint("Select a point to run throw your window")
    intIterations = 0
    while (intIterations < intDistance):
        
        intScale = rd.uniform(0.5,5.0)
        intIterations = (intIterations+1)
        intrandom = rd.randint(intMovement1,intMovement2)
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
    
    
choosingmodule ()