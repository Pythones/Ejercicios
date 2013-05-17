#Lineweight_130513 Pythones@Manuel
#proyectar sobre plano identificando espesores

import rhinoscriptsyntax as rs
import math as mt


PlBase = rs.WorldXYPlane()

edge = []
paraproyectar = rs.GetObject("Dame algo que proyectar")
edge = rs.DuplicateEdgeCurves(paraproyectar)

pointStart = []
pointEnd = []
pointCut = []

for i in range(len(edge)):
    pointStart.append(rs.CurveStartPoint(edge[i]))
    pointEnd.append(rs.CurveEndPoint(edge[i]))
    pointCut.append(rs.LinePlaneIntersection((pointStart[i],pointEnd[i]),PlBase))
    #pointCut.append(rs.PlaneClosestPoint(PlBase,pointStart[i]))
    
for i in range(len(pointCut)):
    rs.AddTextDot("Punto",pointCut[i])
    
print (pointCut)