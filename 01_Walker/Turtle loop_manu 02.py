#Turtle para todos
#130124 Pythones@Manuel

import rhinoscriptsyntax as rs
import random as rd

#def choosingmodule ():
 
#Dos caminos a elegir
strMovement = rs.GetString("movement type","gridding",("gridding","triangulate"))
if strMovement == "gridding": intMovement = 3
else: intMovement = 7
    
#scalefactor altera al vector desplazamiento (1,0,0) pasa a (strFactorScale,0,0)
strScale = rs.GetString("about scale?","equal",("equal","equal+scale","nonequal","nonequal+scale"))
if strScale == "equal": intScale = 1
else: intScale = 1
    
#este integer es el que alimenta al loop
intDistance = rs.GetInteger("How long do you want to go?",1000,150,2500)

        
def runningengine():
    
    Pt1 = rs.GetPoint("Select a point to run throw your window")
    intIterations = 0
    while (intIterations < intDistance):
        intIterations = (intIterations+1)
        intrandom = rd.randint(0,intMovement)
        print intrandom
        if (intrandom == 1):
            Pt2 = rs.PointAdd(Pt1,(intScale,0,0))
        elif (intrandom == 2):
            Pt2 = rs.PointAdd(Pt1,(0,intScale,0))
        elif (intrandom == 3):
            Pt2 = rs.PointAdd(Pt1,(-intScale,0,0))
        else:
            Pt2 = rs.PointAdd(Pt1,(0,-intScale,0))
            
        rs.AddLine(Pt1,Pt2)
        Pt1 = Pt2
        

runningengine ()