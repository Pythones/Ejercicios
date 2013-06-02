#Lineweight_130519 Pythones@Manuel
#proyectar sobre un plano identificando espesores

import rhinoscriptsyntax as rs
import math as mt

#User comunication module 
def imput(): 

    #Creamos un plano sobre el que proyectar
    PlProy = rs.WorldYZPlane()
    PlFinal = rs.GetObject("Dame algo sobre lo que proyectar")
    #Pedimos la volumetria y obtenemos sus lineas
    edge = []
    paraproyectar = rs.GetObject("Dame algo que proyectar")
    edge = rs.DuplicateEdgeCurves(paraproyectar)
    
    #Vamos a comprobar como cerca o lejos estan estas lineas de PlProy
    #Creamos listas con puntos extremos de cada linea
    Pt1 = []
    Pt2 = []
    PtClosest = []
    #alimentamos estas listas
    for i in range(len(edge)):
        Pt1.append(rs.CurveStartPoint(edge[i]))
        Pt2.append(rs.CurveEndPoint(edge[i]))
        
    #Creamos listas con las distancias de estas lineas a traves de sus ptos extremos
    distPt1 = []
    distPt2 = []
    distMin = []
    #alimentamos estas listas
    for i in range(len(edge)):
        distPt1.append(rs.DistanceToPlane(PlProy,Pt1[i]))
        distPt2.append(rs.DistanceToPlane(PlProy,Pt2[i]))
        
    #Creamos una nueva lista con las distancias minimas de las anteriores listas
    for i in range(len(edge)):
        if (distPt1[i]<distPt2[i]):
            distMin.append(distPt1[i])
        else:
            distMin.append(distPt2[i])
            
    #Interpretamos si es cerca o lejos
    lineMod = rs.GetObject("Dame una linea, usaremos su longitud de referencia")
    refMod = rs.CurveLength(lineMod)
    
    #Comparamos las distancias y creamos una lista con que esta lejos y que cerca
    farclose = []
    for i in range(len(edge)):
        if distMin[i]<refMod:
            farclose.append(True)
        else:
            farclose.append(False)
    
    print (farclose)
    deeper(PlFinal,edge,farclose)


#Vamos a vincular lejos y cerca en las lineas proyectadas
def deeper(plane,lines,dist):

    #Proyectamos las lineas
    Proj = []
    Proj = rs.ProjectCurveToSurface(lines,plane,(1,0,0))
    #Borramos las aristas duplicadas
    for i in range(len(lines)):
        rs.DeleteObject(lines[i])
    
    #Creamos una capa si fuera necesario
    if rs.IsLayer("Projection"):
        strProj = "Projection"
    else:
        strProj = rs.AddLayer("Projection")
    
    #Damos espesor a la proyeccion y cambiamos de capa
    for i in range(len(Proj)):
        rs.ObjectLayer(Proj[i],"Projection")
        if dist[i] is True:
            rs.ObjectColor(Proj[i],(255,0,0))
            
    EliminaDuplicados()
            
#Apoyandonos en un make2d, veremos que lineas de nuestra proyeccion deberian ser ocultas. Las borraremos
def EliminaDuplicados():
    #Copy and paste from 130602_Equal Edges.py
    #lists for our projected lines and the ones projected by the make2d
    Projection = []
    Hiddenornot = []
    
    #Feeding Lists
    #filter necessary to avoid brake down
    Projection = rs.ObjectsByLayer("Projection",rs.filter.curve)
    Hiddenornot = rs.ObjectsByLayer("Hidden",rs.filter.curve)
    #Hiddenornot.append(rs.ObjectsByLayer("Visible",rs.filter.curve))
    #Make sense including Visible?
    #Anyway append visible is a group into Hiddenornot
    
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
            angleListProj.append(round((ProjectionAngle[i][0]*(-1)),2))
        elif -180<=ProjectionAngle[i][0]<-90:
            angleListProj.append(round(((-180-ProjectionAngle[i][0])*(-1)),2))
        elif ProjectionAngle[i][0]>90:
            angleListProj.append(round((180-ProjectionAngle[i][0]),2))
        else:
            angleListProj.append(round((ProjectionAngle[i][0]),2))
        
    #Now the turn for HiddenornotAngle
    #listB is just for testing scrip
    angleListHiddenb = []
    for i in range (len(Hiddenornot)):
        angleListHiddenb.append(HiddenornotAngle[i][0])

    angleListHidden = []
    for i in range (len(Hiddenornot)):
        if -90<=HiddenornotAngle[i][0]<0:
            angleListHidden.append(round((HiddenornotAngle[i][0]*(-1)),2))
        elif -180<=HiddenornotAngle[i][0]<-90:
            angleListHidden.append(round(((-180-HiddenornotAngle[i][0])*(-1)),2))
        elif HiddenornotAngle[i][0]>90:
            angleListHidden.append(round((180-HiddenornotAngle[i][0]),2))
        else:
            angleListHidden.append(round((HiddenornotAngle[i][0]),2))
        
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
    
    #xtra test
    #for i in range(len(Coincido)):
        #rs.AddText("COINCIDO1",rs.CurveEndPoint(Coincido[i]))
        #rs.AddText("COINCIDO2",rs.CurveStartPoint(Coincido[i]))

imput()