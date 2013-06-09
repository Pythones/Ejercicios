# Review_Same script that Max slope but "functions style"
# 130609 Pythones@Manu

import rhinoscriptsyntax as rs
import time as t

p3dDropsPos = []
p3dDropProj = []

def main():
    
    global p3dDropsPos
    
    #Pidiendo datos al usuario y anulandolo si alguno falta.
    strCurves = []
    strBaseSrf = rs.GetObject("Select the surface to calculate drop",rs.filter.surface)
    if not strBaseSrf:
        print 'At least one surface is needed to run the script'
        return
    p3dDropsPos = rs.GetObjects("Select the drop point",rs.filter.point)
    if not p3dDropsPos:
        print 'At least one point is needed to run the script'
        return
    intIterations = rs.GetInteger("Iterations",1000)
    dblStep = rs.GetReal("Step size", 0.1,0.01,100)
    strGradient = rs.GetString("Represent flowlines length?","Yes",('Yes','No'))
    
    time0 = t.time()
    
    rs.EnableRedraw(False)
    Falls(strBaseSrf)
    #Flows(strBaseSrf,dblStep,intIterations)
    rs.EnableRedraw(True)
    
    time1 = t.time()
    print 'running time: ' + str(time1-time0) + 'sec.'
    
    
def Falls1(strSrf):
            
    global p3dDropsPos
    global p3dDropProj
    
    for i in range (len(p3dDropsPos)):
        p3dDropProj.append(rs.ProjectPointToSurface(p3dDropsPos[i],strSrf,(0,0,-1)))
        
    print p3dDropProj[3]
    print (rs.PointCoordinates(p3dDropProj[3]))
    print len(p3dDropProj)
    
def Falls(strSfr):
   
    global p3dDropsPos
    global p3dDropProj
    
    # Get the number of rows
    rows = rs.GetInteger("Number of rows", 2, 2)
    if not rows: return
 
    # Get the number of columns
    cols = rs.GetInteger("Number of columns", 2, 2)
    if not cols: return
 
    # Get the domain of the surface
    u, v = rs.SurfaceDomain(strSfr, 0), rs.SurfaceDomain(strSfr, 1)
    if not u or not v: return
 
    # Turn off redrawing (faster)
    rs.EnableRedraw(False)
 
    # Add the points
    for i in range(rows):
        s = u[0] + ((u[1]-u[0])/(rows-1))*i
        for j in range(cols):
            t = v[0] + ((v[1]-v[0])/(cols-1))*j
            pt = rs.EvaluateSurface(strSfr, s, t)
            p3dDropProj.append(rs.AddPoint(pt)) # add the point
    
    # Turn on redrawing
    rs.EnableRedraw(True)
    
    
#def Flows(strSrf,step,iterations):
    

main()
