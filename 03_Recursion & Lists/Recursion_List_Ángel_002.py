# Recurssion tree over multiple curves. 
# AKA.: Loops and arrays madness :D
#@Angel || Pythones 2013

import rhinoscriptsyntax as rs
import math as m
import random as r

def main():
    strCurves = [] #declarando listas.
    p3dPto = []
    dblParam = []
    v3dTangents = []
    v3dNormals = []
    
    strCurves = rs.GetObjects("Select support curves", 4, False, True)
    if strCurves is None: return #Error checking
    intDiv = rs.GetInteger("Population per curve. Be careful with values grater than 5",5,1,50)
    dblStep = rs.GetReal("Initial path length",1,0.1,25)
    dblAngle = m.radians(rs.GetReal("Initial growing angle",60,5,90))
    
    
    #Loop used to create division point list.
    for i in range(len(strCurves)):
        #Creating parameters and divission points arrays
        dblParam.append(rs.DivideCurve(strCurves[i],intDiv,False,False))
        p3dPto.append(rs.DivideCurve(strCurves[i],intDiv))
    
    #Nested loops used to create normal vectors.
    for j in range(len(strCurves)):
        v3dTangents.append([])
        v3dNormals.append([])
        for k in range(intDiv+1): #Dado que ptos. de div. = segmentos + 1
            v3dTangents[j].append(rs.CurveTangent(strCurves[j],dblParam[j][k]))
            #Cross product with Z to calculate normal vectors to curves.
            v3dNormals[j].append(rs.VectorCrossProduct(v3dTangents[j][k],(0,0,1)))
    #trees(p3dPto, v3dNormals, dblAngle, intDiv)
    
#def trees(Pts, Normals, Angle, Div):
#    p3dPm = []
#    # Loops para el acceso de los datos y la creacion de p3dPm.
#    for i in range (len(Pts)):
#        for j in range(0,Div,1):
#            p3dPm[i][j] = rs.PointAdd(Pts[i][j],Normals[i][j])
    
    
main()    