#Lineweight_130513 Pythones@Manuel
#proyectar sobre plano identificando espesores

import rhinoscriptsyntax as rs
import math as mt

#User comunication module 
def imput(): 

    #Creamos un plano sobre el que proyectar
    PlProy = rs.WorldYZPlane()
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
            
            
            
    #Comprobamos a que hemos llegado
    for i in range(len(distMin)):
        rs.AddTextDot("PtMin",distMin[i])
    
    print (len(distMin))
    
input()