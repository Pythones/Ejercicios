#Small ramdom walk agent v4.0
#Added limit cheking for long runtime session.
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

def checkLimit(dblLimitX, dblLimitY, strPt, originPt):
    
    if (strPt[0] > (originPt [0] + dblLimitX)) : strPt[0] = originPt[0] - dblLimitX
    elif (strPt[0] < (originPt [0] - dblLimitX)) : strPt[0] = originPt[0] + dblLimitX

    if (strPt[1] > originPt[1]+dblLimitY) : strPt[1] = originPt[1] - dblLimitX
    elif (strPt[1] < originPt[1]-dblLimitY) : strPt[1] = originPt[1] + dblLimitX
    
    return strPt

def main():
    
    ###################
    #User communication
    ###################
    strOrigin = rs.GetPoint("Select a strPt for walker initial position")
    if strOrigin is None: #Error cheking
        print "You need to give me a start strPt!"
        return 
    strPt1 = strOrigin
    
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

    #Setting canvas limits
    dblLimitX = rs.GetReal("Set canvas X limit value", 100,10,10000)
    dblLimitY = rs.GetReal("Set canvas Y limit value", 100,10,10000)
    
    intIterations = rs.GetInteger("Set iterations number", 50, 1, 1000000)
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
        strPt2 = checkLimit(dblLimitX,dblLimitY,strPt2,strOrigin) #Cheking if strPt2 is outside the canvas.
        strLine = rs.AddLine(strPt1,strPt2) #Adding a line using Pt1 & Pt2
        rs.ObjectLayer(strLine,strWalkerLayer)
        strPt1 = strPt2 #moving pt2 to pt1 variable.
        
    if (strProcess == "No"): rs.EnableRedraw(True) #Turning redraw on

main()