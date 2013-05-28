# 130527 Pythones@Angel
# Automatic polysurface shading.

#import Rhino.Display as rd
import rhinoscriptsyntax as rs

# Gets the data from user and puts in global variables.
def ui():
    
    global strBrep 
    global strSrf
    global intGrad 
    global strDirect
    global ptoLine
    
    strBrep = rs.GetObject("Select a polysurface",rs.filter.polysurface)
    intGrad = rs.GetInteger("Gradient density",3,1,15)
    strDirect = rs.GetString("Shading direction","Current_View",["Current_View","Line"])
    if strDirect == "Line":
        ptoLine = rs.GetLine(0,None,"Pick the first point on the line","Pick the second point")
    elif strDirect == "Current_View":
        ptoLine = rs.ViewCameraTarget()
    strSrf = rs.ExplodePolysurfaces(strBrep)

def main():
    #Call user interface
    ui()
    
    #Initializing lists.
    global strCrv
    strCrv = []
    v3dNormals = []
    dblAngle = []
    
    # Cheking surfaces.
    
    for srf in strSrf:
        if rs.IsSurfaceClosed(srf,0) or rs.IsSurfaceClosed(srf,(1)):
            print "This script doesn't support trimmed or closed surfaces"
            return
        strCrv.append(rs.DuplicateSurfaceBorder(srf))
        v3dNormals.append(rs.SurfaceNormal(srf,[0,0]))
    
    print str(ptoLine[0])+", "+str(ptoLine[1])
    
    v3dLine = rs.VectorCreate(ptoLine[0],ptoLine[1])
        
    for vect in v3dNormals:
        dblAngle.append(rs.VectorAngle(vect,v3dLine))
    strHaches = []
    for i in range(0,len(dblAngle)):
        dblAngle[i] = int((dblAngle[i]/max(dblAngle))*intGrad)
        strHatches.append(rs.AddHatch(strCrv[i],None,dblAngle[i],0))
        
    
    
main()
    
    
    



