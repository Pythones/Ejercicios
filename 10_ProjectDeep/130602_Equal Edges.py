#Equal Edges_130602 Pythones@Manuel
#equal edges detection (complement script for lineweight projection)
#deletes our projection lines if they are hidden after make2d

import rhinoscriptsyntax as rs

#User comunication module 
def imput(): 

    #Units
    rs.UnitAngleTolerance(2.0)
    rs.UnitAbsoluteTolerance(0.1)

    #lists for our projected lines and the ones projected by the make2d
    Projection = []
    Hiddenornot = []
    
    #Feeding Lists
    #filter necessary to avoid brake down
    Projection = rs.ObjectsByLayer("Projection",rs.filter.curve)
    Hiddenornot = rs.ObjectsByLayer("Hidden",rs.filter.curve)
    Hiddenornot.append(rs.ObjectsByLayer("Visible",rs.filter.curve))
    
    #List for projection and hiddenornot end and starts points
    Projection1,Projection2 = [],[]
    Hiddenornot1,Hiddenornot2 = [],[]
    ProjectionAngle, HiddenornotAngle = [],[]
    Coincido = []
    
    #Feeding Lists
    for i in range (len(Projection)):
        Projection1.append(rs.CurveStartPoint(Projection[i]))
        Projection2.append(rs.CurveEndPoint(Projection[i]))
        ProjectionAngle.append(rs.Angle(Projection1[i],Projection2[i]))
        
    for i in range (len(Hiddenornot)):
        Hiddenornot1.append(rs.CurveStartPoint(Hiddenornot[i]))
        Hiddenornot2.append(rs.CurveEndPoint(Hiddenornot[i]))
        HiddenornotAngle.append(rs.Angle(Hiddenornot1[i],Hiddenornot2[i]))
        
    #to avoid working with long tuples we create list from them
    #as we feed the list we change the angle sign
    #listB is just for testing scrip
    angleListProjb = []
    for i in range (len(Projection)):
        angleListProjb.append(ProjectionAngle[i][0])
        
    angleListProj = []
    for i in range (len(Projection)):
        if -90<=ProjectionAngle[i][0]<0:
            angleListProj.append(ProjectionAngle[i][0]*(-1))
        elif -180<=ProjectionAngle[i][0]<-90:
            angleListProj.append((-180-ProjectionAngle[i][0])*(-1))
        elif ProjectionAngle[i][0]>90:
            angleListProj.append(180-ProjectionAngle[i][0])
        else:
            angleListProj.append(ProjectionAngle[i][0])
        
    #Now the turn for HiddenornotAngle
    #listB is just for testing scrip
    angleListHiddenb = []
    for i in range (len(Hiddenornot)):
        angleListHiddenb.append(HiddenornotAngle[i][0])

    angleListHidden = []
    for i in range (len(Hiddenornot)):
        if -90<=HiddenornotAngle[i][0]<0:
            angleListHidden.append(HiddenornotAngle[i][0]*(-1))
        elif -180<=HiddenornotAngle[i][0]<-90:
            angleListHidden.append((-180-HiddenornotAngle[i][0])*(-1))
        elif HiddenornotAngle[i][0]>90:
            angleListHidden.append(180-HiddenornotAngle[i][0])
        else:
            angleListHidden.append(HiddenornotAngle[i][0])
        
    #Looking for duplicates
    #First we look for extrem points, then we make sure with angle
    for i in range (len(Projection)):
        for j in range (len(Hiddenornot)):
            if (rs.PointCompare(Projection1[i],Hiddenornot1[j])) is True:
                if (cmp(angleListProj[i],angleListHidden[j]) == 0) is True:
                    Coincido.append(Projection[i])
                    
    for i in range (len(Projection)):
        for j in range (len(Hiddenornot)):
            if (rs.PointCompare(Projection1[i],Hiddenornot2[j])) is True:
                if (cmp(angleListProj[i],angleListHidden[j]) == 0) is True:
                    Coincido.append(Projection[i])
        
    for i in range (len(Projection)):
        for j in range (len(Hiddenornot)):
            if (rs.PointCompare(Projection2[i],Hiddenornot1[j])) is True:
                if (cmp(angleListProj[i],angleListHidden[j]) == 0) is True:
                    Coincido.append(Projection[i])
                    
    for i in range (len(Projection)):
        for j in range (len(Hiddenornot)):
            if (rs.PointCompare(Projection2[i],Hiddenornot2[j])) is True:
                if (cmp(angleListProj[i],angleListHidden[j]) == 0) is True:
                    Coincido.append(Projection[i])
                    
    #Cambiar de capa los elementos duplicados
    if not rs.IsLayer("Delete"): rs.AddLayer("Delete")
    for i in range (len(Coincido)):
        rs.ObjectLayer(Coincido[i],"Delete")
    rs.LayerVisible("Delete",False)
    rs.LayerVisible("Hidden",False)
    
    #CurveDirectionsMatch - Compares the direction of two curve objects
    
    #Testing Script
    print (len(angleListProjb),len(angleListProj))
    print angleListProjb
    print angleListProj
    
    print (len(angleListHiddenb),len(angleListHidden))
    print angleListHiddenb
    print angleListHidden

    print len(Coincido)
    
imput()