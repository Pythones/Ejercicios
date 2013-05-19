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
    #Establecemos listas con los grupos de estudio
    Trampeo = []
    Hidden = []
    Trampeo = rs.ObjectsByLayer("Projection")
    Hidden = rs.ObjectsByLayer("Hidden")
    
    #Creamos listas de para comparar lineas por sus puntos extremos
    Trampeo1 = []
    Trampeo2 = []
    Hidden1 = []
    Hidden2 = []
    Coincido = []
    
    #Este codigo es para ver donde estamos. Realmente no hace falta
    for i in range(len(Trampeo)):
        Trampeo1.append(rs.CurveStartPoint(Trampeo[i]))
        Trampeo2.append(rs.CurveEndPoint(Trampeo[i]))
        rs.AddText("T1",Trampeo1[i])
        rs.AddText("T2",Trampeo2[i])
    for i in range(len(Hidden)):
        Hidden1.append(rs.CurveStartPoint(Hidden[i]))
        Hidden2.append(rs.CurveEndPoint(Hidden[i]))
        rs.AddText("H1",Hidden1[i])
        rs.AddText("H2",Hidden2[i])
    
    #Volvemos a la parte util de comparacion
    for i in range(len(Hidden)):
        for j in range(len(Trampeo)):
            if rs.PointCompare(Hidden1[i],Trampeo1[j]) is True:
                if rs.PointCompare(Hidden2[i],Trampeo2[j]) is True:
                    Coincido.append(Trampeo[j])
            
    for i in range(len(Hidden)):
        for j in range(len(Trampeo)):
            if rs.PointCompare(Hidden2[i],Trampeo1[j]) is True:
                if rs.PointCompare(Hidden1[i],Trampeo2[j]) is True:
                    Coincido.append(Trampeo[j])
                    
    #Creamos una capa si fuera necesario
    if rs.IsLayer("Delete"):
        strDelete = "Delete"
    else:
        strDelete = rs.AddLayer("Delete")
    
    #Vemos donde estamos y movemos a una capa la no necesario de nuestra proyeccion
    print len(Coincido)
    for i in range(len(Coincido)):
        rs.AddText("COINCIDO1",rs.CurveEndPoint(Coincido[i]))
        rs.AddText("COINCIDO2",rs.CurveStartPoint(Coincido[i]))
        rs.ObjectLayer((Coincido[i]),"Delete")
    #Apagamos la capa delete
    rs.LayerVisible("Delete",False)

imput()