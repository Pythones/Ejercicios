#Small ramdom walk agent.
#Added mode selection.
#@Angel - Pythones 2013.

#Importing modules.
import rhinoscriptsyntax as rs
import math as m
import random as r

def walker (strLocation, dblStepSize, strMode):
    #Selecting mode
    if (strMode == "Mixed"):
        intChoice = r.randint(0,7) #random number for direction choice.
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
            
    if (strMode == "Ortho"):
        intChoice = r.randint(0,3) #random number for direction choice.
        #Selecting direction
        if (intChoice < 1):
            vectWalk = (0,1,0)
        elif (intChoice < 2):
            vectWalk = (-1,0,0)
        elif (intChoice < 3):   
            vectWalk = (1,0,0)
        else:
            vectWalk = (0,-1,0)
    
    if (strMode == "Diagonal"):
        intChoice = r.randint(0,3) #random number for direction choice.
        #Selecting direction
        if (intChoice < 1):
            vectWalk = (-1,1,0)
        elif (intChoice < 2):
            vectWalk = (1,1,0)
        elif (intChoice < 3):   
            vectWalk = (-1,-1,0)
        else:
            vectWalk = (1,-1,0)
            
    #Adding scaled vectorWalk by StepSize to initial location.
    strPt = rs.PointAdd(strLocation,rs.PointScale(vectWalk,dblStepSize))
    return strPt

def main():
    strPt1 = rs.GetPoint("Select a point for walker initial position")
    if strPt1 is None: #Error cheking
        print "You need to give me a start point!"
        return 
    dblStep = rs.GetReal("Set step size", 1, 0.01, 100)
    strMode = rs.GetString("Set walker mode","Mixed",("Mixed","Ortho","Diagonal"))
    intIterations = rs.GetInteger("Set iterations number", 50, 1, 10000)
    strProcess = rs.GetString("Show drawing process?","No",("Yes","No"))
    if rs.IsLayer("Walker_Path"): #Creating layer for the path if is needed
        strWalkerLayer = "Walker_Path"
    else:
        strWalkerLayer = rs.AddLayer("Walker_Path")

    if (strProcess == "No"): rs.EnableRedraw(False)

    for i in range(0, intIterations, 1): # main loop
        strPt2 = walker (strPt1, dblStep, strMode) #Call to walker function
        strLine = rs.AddLine(strPt1,strPt2) #Adding a line using Pt1 & Pt2
        rs.ObjectLayer(strLine,strWalkerLayer)
        strPt1 = strPt2 #moving pt2 to pt1 variable.
        #Mejor implementar timer 
        #http://stackoverflow.com/questions/4720073/python-time-a-while-loop-has-been-running
        #print "Iteration: "+`i` #print iteration state

    if (strProcess == "No"): rs.EnableRedraw(True)

main()