#Lineweight_130513 Pythones@Manuel
#proyectar sobre plano identificando espesores

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
        
    #Creamos listas con las distancias de estas lineas (a traves de sus ptos extremos
    distPt1 = []
    distPt2 = []
    distMin = []
    #alimentamos estas listas
    for i in range(len(edge)):
        distPt1.append(rs.DistanceToPlane(PlProy,Pt1[i]))
        distPt2.append(rs.DistanceToPlane(PlProy,Pt2[i]))
        
    #Creamos una nueva lista con las distancias minimas
    for i in range(len(edge)):
        if (distPt1[i]<distPt2[i]):
            distMin.append(distPt1[i])
        else:
            distMin.append(distPt2[i])
            
    #Interpretamos si es cerca o lejos
    lineMod = rs.GetObject("Dame linea de referencia")
    refMod = rs.CurveLength(lineMod)
    
    #Comparamos las distancias
    farclose = []
    for i in range(len(edge)):
        if distMin[i]<refMod:
            farclose.append(True)
        else:
            farclose.append(False)
            
            
            
    #Comprobamos a que hemos llegado
    #for i in range(len(distMin)):
        #rs.AddTextDot("PtMin",distMin[i])
    
    print (farclose)
    #deeper(PlProy,edge,farclose)
    
    #User comunication module 
    #def deeper(plane,lines,dist):
    
    #Proyectamos las lineas
    Proj = []
    Proj = rs.ProjectCurveToSurface(edge,PlFinal,(1,0,0))
    
    #Damos espesor a la proyeccion
    for i in range(len(Proj)):
        if farclose[i] is True:
            #rs.AddLayer("Deep_Cerca",Red)
            rs.ObjectColor(Proj[i],(100,0,0))
            

#Eliminamos las lineas ocultas de nuestra proyeccion            
def hiddenlines():
    
    #hacemos make2d
    
    
    
imput()