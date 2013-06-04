

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

class Raindrop:
    'Implementa una gota de agua sobre una superficie'
    dblLenCheck = 0
    
    def __init__(self,p3dLocation):
        self.p3dLocation = p3dLocation
    
    def falls(self,strSrf):
        p3dProjectedPt = rs.ProjectPointToSurface(self.p3dLocation,strSrf,(0,0,-1))
        #print p3dProjectedPt
        #if p3dProjectedPt != None:
        self.p3dLocation = rs.coerce3dpoint(p3dProjectedPt[0])
        #print self.p3dLocation
        rs.AddPoint(self.p3dLocation)
        
    def flow(self,strSrf):
        #print self.p3dLocation[0]
        global dblLenCheck
        p3dDummy0 = self.p3dLocation
        puvClosest0 = rs.SurfaceClosestPoint(strSrf,self.p3dLocation)
        v3dNormal = rs.SurfaceNormal(strSrf,puvClosest0)
        self.p3dLocation = rs.PointAdd(self.p3dLocation,(v3dNormal[0],v3dNormal[1],0))
        puvClosest1 = rs.SurfaceClosestPoint(strSrf,self.p3dLocation)
        p3dDummy1 = rs.EvaluateSurface(strSrf,puvClosest1[0],puvClosest1[1])
        self.p3dLocation = p3dDummy1
        dblLenCheck = rs.Distance(p3dDummy0,p3dDummy1)
        if dblLenCheck < 0.01: 
            return None
        else:
            return rs.AddLine(p3dDummy0,p3dDummy1)
        
            
#        rs.AddPoint(self.p3dLocation)