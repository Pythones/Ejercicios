#Small ramdom walk agent.
#@Angel - Pythones 2013.

#Importing modules.
import rhinoscriptsyntax as rs
import math as m
import random as r

def walker (strLocation, dblStepSize, intChoice, strMode):
    #Selecting direction
    if (intChoice < 1):
        vectWalk = (-1,1,0)
    elif (intChoice < 2):
        vectWalk = (0,1,0)
    elif (intChoice < 3):
        vectWalk = (1,1,0)
    elif (intChoice < 4):
        vectWalk = (-1,0,0)
    elif (intChoice < 5):
        vectWalk = (1,0,0)
    elif (intChoice < 6):
        vectWalk = (-1,-1,0)
    elif (intChoice < 7):
        vectWalk = (0,-1,0)
    else:
        vectWalk = (1,-1,0)
    
    #Adding scaled vectorWalk by StepSize to initial location.
    strPt = rs.PointAdd(strLocation,rs.PointScale(vectWalk,dblStepSize))
    return strPt

def main():
    strPt1 = rs.GetPoint("Select a point for walker initial position")
    dblStep = rs.GetReal("Set step size", 1, 0.01, 100)
    strMode = rs.GetString("Set walker mode","Mixed",("Mixed","Ortho","Diagonal")
    intIterations = rs.GetInteger("Set iterations number", 50, 1, 10000)
    srtWalkerLayer = rs.AddLayer("Walker_Path")

    for i in range(0, intIterations, 1): # main loop
        intDirection = r.randint(0,7) #random number for direction choice.
        strPt2 = walker (strPt1, dblStep, intDirection) #Call to walker function
        strLine = rs.AddLine(strPt1,strPt2) #Adding a line using Pt1 & Pt2
        rs.ObjectLayer(strLine,srtWalkerLayer)
        strPt1 = strPt2 #moving pt2 to pt1 variable.
        print "Iteration: "+`i` #print iteration state

main()
