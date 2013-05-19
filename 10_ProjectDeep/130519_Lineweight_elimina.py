#Lineweight elimina_130519 Pythones@Manuel
#borrar lineas coincidentes

import rhinoscriptsyntax as rs
import math as mt

#modulo a anadir al tema anterior
def elimina():
    #Establecemos listas con grupos de estudio
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
    for i in range(len(Coincido)):
        rs.AddText("COINCIDO1",rs.CurveEndPoint(Coincido[i]))
        rs.AddText("COINCIDO2",rs.CurveStartPoint(Coincido[i]))
        rs.ObjectLayer((Coincido[i]),"Delete")

elimina()