# Raindrop_Manu developement Classes
# 130622 Pythones@Manu

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

class Raindrop_Manu:
    
    def __init__(self,p3dLocation):
        self.p3dLocation = p3dLocation
        
    def flow(self,strSrf):
        
        p3dDummy1 = self.p3dLocation
        #obtenemos pto en srf #obtenemos su uv
        p3dUV = rs.SurfaceClosestPoint(strSrf,p3dDummy1)
        
        #sacamos la normal en ese pto a la srf #hacemos unitario el vector #desplazamos el pto
        v3dNormal = rs.SurfaceNormal(strSrf,p3dUV)
        v3dUni = rs.VectorUnitize(v3dNormal)
        p3dDummy2 = rs.PointAdd(p3dDummy1,v3dUni)
        
        #anadimos linea #Proyectamos la linea sobre la superficie #borramos los pelos
        lineDummy = rs.AddLine(p3dDummy1,p3dDummy2)
        lineProyTest = rs.ProjectCurveToSurface(lineDummy,strSrf,(0,0,-1))
        rs.DeleteObjects(lineDummy)#para acelerar meter en lista y borrar al final
        
        self.p3dLocation = rs.CurveEndPoint(lineProyTest)
        
        #permitir escalar la linea pelo
        #break poin para cuando no hay superficie
        #break point con linea pequena (no avanza)
        #metodo brotar punto (poblando)

