import rhinoscriptsyntax as rs

class Raindrop:
    'Implements a raindrop over a surface'
    strSrf = 'Not defined'
    def __init__(self,p3dLocation):
        self.p3dLocation = p3dLocation
    
    def falls():
        p3dProjectedPt = rs.ProjectPointToSurface(self.p3dLocation,strSrf,(0,0,-1))
        self.p3dLocation = p3dProjectedPt