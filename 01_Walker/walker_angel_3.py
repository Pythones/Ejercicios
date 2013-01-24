#Small ramdom walk agent v3.0
#Added custom step scale per direction.
#@Angel - Pythones 2013.

#Importing modules.
import rhinoscriptsyntax as rs
import math as m
import random as r

def walker (strLocation, dblStepSizeX, dblStepSizeY, dblStepSizeD, strMode):
    #Selecting mode
    if (strMode == "Mixed"):
        intChoice = r.randint(0,7) #random number for direction choice.
        #Selecting direction
        if (intChoice < 1):
            vectWalk = (-dblStepSizeD,dblStepSizeD,0)
        elif (intChoice < 2):
            vectWalk = (0,dblStepSizeY,0)
        elif (intChoice < 3):
            vectWalk = (dblStepSizeD,dblStepSizeD,0)
        elif (intChoice < 4):
            vectWalk = (-dblStepSizeX,0,0)
        elif (intChoice < 5):
            vectWalk = (dblStepSizeX,0,0)
        elif (intChoice < 6):
            vectWalk = (-dblStepSizeD,-dblStepSizeD,0)
        elif (intChoice < 7):
            vectWalk = (0,-dblStepSizeY,0)
        else:
            vectWalk = (dblStepSizeD,-dblStepSizeD,0)
            
    if (strMode == "Ortho"):
        intChoice = r.randint(0,3) #random number for direction choice.
        #Selecting direction
        if (intChoice < 1):
            vectWalk = (0,dblStepSizeY,0)
        elif (intChoice < 2):
            vectWalk = (-dblStepSizeX,0,0)
        elif (intChoice < 3):   
            vectWalk = (dblStepSizeX,0,0)
        else:
            vectWalk = (0,-dblStepSizeY,0)
    
    if (strMode == "Diagonal"):
        intChoice = r.randint(0,3) #random number for direction choice.
        #Selecting direction
        if (intChoice < 1):
            vectWalk = (-dblStepSizeD,dblStepSizeD,0)
        elif (intChoice < 2):
            vectWalk = (dblStepSizeD,dblStepSizeD,0)
        elif (intChoice < 3):   
            vectWalk = (-dblStepSizeD,-dblStepSizeD,0)
        else:
            vectWalk = (dblStepSizeD,-dblStepSizeD,0)
            
    #Adding vectorWalk to initial location.
    strPt = rs.PointAdd(strLocation,vectWalk)
    return strPt

def main():
    
    ###################
    #User communication
    ###################
    strPt1 = rs.GetPoint("Select a point for walker initial position")
    if strPt1 is None: #Error cheking
        print "You need to give me a start point!"
        return 

    #Setting custom step scale.
    strMode = rs.GetString("Set walker mode","Mixed",("Mixed","Ortho","Diagonal"))
    dblStepX = dblStepY = dblStepD = 1
    if (strMode == "Mixed"):
        dblStepX = rs.GetReal("Set X step size", 1, 0.01, 100)
        dblStepY = rs.GetReal("Set Y step size", 1, 0.01, 100)
        dblStepD = rs.GetReal("Set diagonal step size", 1, 0.01, 100)
    elif (strMode == "Ortho"):
        dblStepX = rs.GetReal("Set X step size", 1, 0.01, 100)
        dblStepY = rs.GetReal("Set Y step size", 1, 0.01, 100)
    else:
        dblStepD = rs.GetReal("Set diagonal step size", 1, 0.01, 100)

    intIterations = rs.GetInteger("Set iterations number", 50, 1, 10000)
    strProcess = rs.GetString("Show drawing process?","No",("Yes","No"))
    
    if rs.IsLayer("Walker_Path"): #Creating layer for the path if is needed
        strWalkerLayer = "Walker_Path"
    else:
        strWalkerLayer = rs.AddLayer("Walker_Path")
        
    dblStepD = m.sqrt((dblStepD*dblStepD)/2) #Calculating vector component
 
    #################
    # Main loop
    #################
    if (strProcess == "No"): rs.EnableRedraw(False) #Turning redraw off

    for i in range(0, intIterations, 1): # main loop
        strPt2 = walker (strPt1, dblStepX, dblStepY, dblStepD, strMode) #Call to walker function
        strLine = rs.AddLine(strPt1,strPt2) #Adding a line using Pt1 & Pt2
        rs.ObjectLayer(strLine,strWalkerLayer)
        strPt1 = strPt2 #moving pt2 to pt1 variable.

    if (strProcess == "No"): rs.EnableRedraw(True) #Turning redraw on

main()