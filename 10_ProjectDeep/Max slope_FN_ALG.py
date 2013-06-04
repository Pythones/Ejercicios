# Same script that Max slope but "functions style"
# 130604 Pythones@Angel

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
    Flows(strBaseSrf,dblStep,intIterations)
    rs.EnableRedraw(True)
    
    time1 = t.time()
    print 'running time: ' + str(time1-time0) + 'sec.'
    
    
def Falls(strSrf):
    
    global p3dDropsPos
    global p3dDropProj
    
    for i in range(len(p3dDropsPos)):
        p3dProjectedPt = rs.ProjectPointToSurface(p3dDropsPos[i],strSrf,(0,0,-1))
        #print p3dProjectedPt
        if len(p3dProjectedPt)>0:
            p3dDropProj.append(rs.AddPoint(rs.coerce3dpoint(p3dProjectedPt[0])))
    if not rs.IsLayer("Drops"):
        rs.AddLayer("Drops",(30,30,255))
    rs.ObjectLayer(p3dDropProj,"Drops")
            
            
def Flows(strSrf,step,iterations):
    
    global p3dDropsPos
    global p3dDropProj
    print "Longitud de la matriz de puntos proyectados: " + str(len(p3dDropProj))
    lines = []
    
    for i in range(0,len(p3dDropProj)):
        for j in range(iterations):
            p3dDummy0 = rs.coerce3dpoint(p3dDropProj[i])
            puvClosest0 = rs.SurfaceClosestPoint(strSrf,p3dDropProj[i])
            v3dNormal = rs.SurfaceNormal(strSrf,puvClosest0)
            v3dMovement = rs.VectorScale(rs.VectorUnitize((v3dNormal[0],v3dNormal[1],0)),step)
            p3dDropProj[i] = rs.PointAdd(p3dDummy0,v3dMovement)
            
            puvClosest1 = rs.SurfaceClosestPoint(strSrf,p3dDropProj[i])
            #print puvClosest1
            p3dDummy1 = rs.EvaluateSurface(strSrf,puvClosest1[0],puvClosest1[1])
            p3dDropProj[i] = p3dDummy1
            #print str(rs.coerce3dpoint(p3dDummy0)) + '|| ' + str(rs.coerce3dpoint(p3dDummy1))
            
            dblLenCheck = rs.Distance(p3dDummy0,p3dDummy1)
            strTrail = rs.AddLine(p3dDummy0,p3dDummy1)
            if dblLenCheck>0.01 and rs.IsCurve(strTrail):
                lines.append(strTrail)
            else:
                break
                
        #rs.JoinCurves(lines,True)
        
main()