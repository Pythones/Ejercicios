#Lineweight elimina_130519 Pythones@Manuel
#borrar lineas coincidentes

import rhinoscriptsyntax as rs
import math as mt

#modulo a anadir al tema anterior
def elimina():
    #Establecemos listas con grupos de estudio
    Trampeo = []
    Hidden = []
    Trampeo = rs.ObjectsByColor((100,0,0))
    Hidden = rs.ObjectsByLayer("Hidden")
    
    #Creamos listas de para comparar lineas por sus puntos extremos
    Trampeo1 = []
    Trampeo2 = []
    Hidden1 = []
    Hidden2 = []
    Coincido = []
    
    for i in range(len(Trampeo)):
        Trampeo1.append(rs.CurveStartPoint(Trampeo[i]))
        Trampeo2.append(rs.CurveEndPoint(Trampeo[i]))
    for i in range(len(Hidden)):
        Hidden1.append(rs.CurveStartPoint(Hidden[i]))
        Hidden2.append(rs.CurveEndPoint(Hidden[i]))
    
    #Comparamos
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
        
            
    print len(Coincido)



elimina()