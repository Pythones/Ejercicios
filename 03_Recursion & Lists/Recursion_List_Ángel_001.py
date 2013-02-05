# Recurssion tree over multiple curves. 
# AKA.: Loops and arrays madness :D
#@Angel || Pythones 2013

import rhinoscriptsyntax as rs
import math as m
import random as r

def main():
    strCurves = [] #declarando listas.
    dblParam = []
    p3dPto = []
    v3dTangents = []
    v3dTangentsGroups = []
    
    strCurves = rs.GetObjects("Select support curves", 4, False, True)
    if strCurves is None: return #Error checking
    intDiv = rs.GetInteger("Population per curve. Be careful with values grater than 5",5,1,50)
    dblAngle = m.radians(rs.GetReal("Initial growing angle",60,5,90))
    
    #Loop used to create division point list.
    for i in range(len(strCurves)):
        #Creating parameters and divission points arrays
        dblParam[i] = rs.DivideCurve(strCurves[i],intDiv,False,False)
        p3dPto[i] = rs.DivideCurve(strCurves[i],intDiv)
    
    #Nested loops used to create normal vectors.
    for j in range(len(strCurves)):
        for k in range(len(dblParam)):
            v3dTangents[j,k] = rs.CurveTangent(strCurves[j],dblParam[j,k])
            #Cross product with Z to calculate normal vectors to curves.
            v3dNormals[j,k] = rs.VectorCrossProduct(v3dTangents[j,k],(0,0,1))
    trees(p3dPto, v3dNormals, dblAngle)
    
def trees(Pts, Normals, Angle):
    
    
    
main()    