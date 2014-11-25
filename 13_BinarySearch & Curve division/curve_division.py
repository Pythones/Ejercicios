#Iterative curve division

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import pydevd as pyd

pyd.settrace(port=5678,stdoutToServer=True, stderrToServer=True)

def divideCurve(crv,length):

    result = []
    points = []
    leftover = distEndPt(crv)
    counter = 0
    
    while leftover >= length:
        
        ##BUG: CurveArcLengthPoint doesn't work as spected, search for arternatives.
        newPt = rs.CurveArcLengthPoint(crv,length)
        newPar = rs.CurveClosestPoint(crv,newPt)
        points.append(newPt)
        newCurves = rs.SplitCurve(crv,newPar,False)
        
        c = longestCurve(newCurves)
        crv = c
        leftover = distEndPt(c)
        counter += 1
    
    ##BUG: Left over returns the length of the last element
    print leftover
    result = [counter,leftover,points]
    return result
    
def longestCurve(crvs):
    len = 0
    for c in crvs:
        newlen = rs.CurveLength(c)
        if newlen > len:
            len = newlen
            curveReturn = c
                
    return curveReturn              
    
def distEndPt(crv):
    pt0 = rs.CurveEndPoint(crv)
    pt1 = rs.CurveStartPoint(crv)
    return rs.Distance(pt0,pt1)

def flipCurves(crvs,origCrv,param):
    
    #m1 = rs.CurveMidPoint(origCrv)
    
    m1 = rs.EvaluateCurve(origCrv,param)
    newCrvs = []
    #Flipping curves to make them start at the midle point
    for crv in crvs:
        startPt = rs.CurveStartPoint(crv)
        compare = rs.PointCompare(m1,startPt)
        if not compare:
            rs.ReverseCurve(crv)
            newCrvs.append(crv)
        else:
            newCrvs.append(crv)
            
    return newCrvs           
    
def customSplitCrvs(crv,param):

    crvs = rs.SplitCurve(crv,param,False)
    print "t = " + str(param)
    #print "Curvas: " + str(crvs)
    newCrvs = flipCurves(crvs,crv,param)
    return newCrvs

#Taking initial curve domain to test
crvDom = rs.CurveDomain(curve)
print crvDom
dblMin = crvDom[0]
dblMax = crvDom[1]

dblCheck = dblMax
dblIncr = dblMax/2
dblCheck -= dblIncr

##########BISECTION SEARCH
guess = False
counter = 0
#curveCoer = rs.coercegeometry(curve)


while not guess:
    #Divide curves.
    ###NOT NECESSARY### closestM1 = rs.CurveClosestPoint(curve,m1)
    points = []
    newCrvs = customSplitCrvs(curve,dblCheck)

    #Dividing the curves and measuring the left over
    leftovers = []
    ##Analize how the curves are 
    for c in newCrvs:
        divResult = divideCurve(c,dist)
        leftovers.append(divResult[1])
        
        #print divResult
        
        for pt in divResult[2]:
            points.append(pt)
        
    dblError = abs(leftovers[0]-leftovers[1])
    
    print "Deviation: " + str(dblError)
    print "leftover0: " + str(leftovers[0])
    print "leftover1: " + str(leftovers[1])
    
    if leftovers[0]>leftovers[1] and dblError > tolerance:
        dblMax = dblCheck
        counter += 1
        #print dblMax
           
    elif leftovers[0]<leftovers[1] and dblError > tolerance:     
        dblMin = dblCheck
        counter += 1
        #print dblMax
        
    elif counter > maxSteps or dblError <= tolerance:
        t = dblCheck
        pts = rs.coerce3dpointlist(points)
        break
        
    dblCheck = (dblMax+dblMin)/2
    
#t = result
i = counter