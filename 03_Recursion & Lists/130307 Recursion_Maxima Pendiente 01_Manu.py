#Maxima pendiente_130307 Pythones@Manuel
#Calculo de linea de maima pendiente en un plano unico

import rhinoscriptsyntax as rs
import random as rd
import math as mt
    
    
#User comunication module 
def main():
    #Pedimos un punto y pedimos un plano de referencia
    pl1 = rs.GetObject("Select a surface to analized",rs.filter.surface)
    if pl1:
        pt1 = rs.GetPoint("Select a point to start with")
        pt2 = rs.SurfaceClosestPoint(pl1,pt1)
    
    normalDraw(pt1,pt2,pl1)
    
    
def normalDraw (pointa,pointb,plane):
    #accedemos a la normal
    normal = rs.SurfaceNormal(plane,pointb)
    p1 = rs.EvaluateSurface(plane,pointb[0],pointb[1])
    pointc = rs.AddPoint(pointa+normal)
    rs.AddPoint(p1)
    
    #Getting limits
    limits = []
    limits.append(plane)
    
    #Adding line on the plane
    results = rs.ProjectPointToSurface(pointc,plane,(0,0,-1))
    line = rs.AddLine(p1,results[0])
    lineXtend = rs.ExtendCurve(line,2,0,limits)
    p2 = rs.CurveEndPoint(lineXtend)
    rs.AddLine(p1,p2)
    
    
main()