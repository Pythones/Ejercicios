#Equal Edges_130529 Pythones@Manuel
#equal edges detection

import rhinoscriptsyntax as rs
import math as mt

#User comunication module 
def imput(): 

    #Base List Creation
    Projection = []
    Hiddenornot = []
    
    #Feeding Base List
    Projection = rs.ObjectsByLayer("Projection")
    Hiddenornot = rs.ObjectsByLayer("Hidden")
    Hiddenornot.append(rs.ObjectsByLayer("Visible"))
    
    #Second List Creation
    Projection1 = []
    Projection2 = []
    Hiddenornot1 = []
    Hiddenornot2 = []
    ProjectionAngle = []
    HiddenornotAngle = []
    Coincido = []
    
    #Feeding Second Lists
    for i in range (len(Projection)):
        Projection1.append(rs.CurveStartPoint(Projection[i]))
        Projection2.append(rs.CurveEndPoint(Projection[i]))
        ProjectionAngle.append(rs.Angle(Projection1[i],Projection2[i]))
        
    for i in range (len(Hiddenornot)):
        Hiddenornot1.append(rs.CurveStartPoint(Hiddenornot[i]))
        Hiddenornot2.append(rs.CurveEndPoint(Hiddenornot[i]))
        HiddenornotAngle.append(rs.Angle(Hiddenornot1[i],Hiddenornot2[i]))
        
    #Looking for duplicates
    for i in range (len(Projection)):
        for j in range (len(Hiddenornot)):
            if (rs.PointCompare(Projection1[i],Hiddenornot1[j])) is True:
                if (cmp(ProjectionAngle[i][0],HiddenornotAngle[j][0]) == 0) is True:
                    Coincido.append(Projection[i])
    
    for i in range (len(Projection)):
        for j in range (len(Hiddenornot)):
            if (rs.PointCompare(Projection2[i],Hiddenornot1[j])) is True:
                if (cmp(ProjectionAngle[i][0],HiddenornotAngle[j][0]) == 0) is True:
                    Coincido.append(Projection[i])
                    
    #Cambiar de capa los elementos duplicados
    if not rs.IsLayer("Delete"): rs.AddLayer("Delete")
    for i in range (len(Coincido)):
        rs.ObjectLayer(Coincido[i],"Delete")
    rs.LayerVisible("Delete",False)
    
    #Testing Script
    #print len(Hiddenornot)
    #print len(Hiddenornot1)
    #print len(HiddenornotAngle)
    print (HiddenornotAngle)
    print (ProjectionAngle)
    print (cmp(ProjectionAngle[0][0],HiddenornotAngle[0][0]))
    print (cmp(ProjectionAngle[0],HiddenornotAngle[1]))
    print len(Coincido)

    
imput()
    

    