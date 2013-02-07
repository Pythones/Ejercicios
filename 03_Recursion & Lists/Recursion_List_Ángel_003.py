# Recurssion tree over multiple curves (in near future)
# Actually: creates quills over the curves.
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
    intDiv = rs.GetInteger("Population per curve. Be careful with values greater than 5",5,1,50)
    dblStep = rs.GetReal("Initial path length",1,0.1,25)
    dblAngle = m.radians(rs.GetReal("Initial growing angle",60,5,90))
    
    
    #Loop used to create division point list.
    for i in range(len(strCurves)):
        #Creating parameters and divission points arrays
        dblParam.append(rs.DivideCurve(strCurves[i],intDiv,False,False))
        p3dPto.append(rs.DivideCurve(strCurves[i],intDiv))
    
    #Nested loops used to create normal vectors.
    for j in range(len(strCurves)):
        v3dTangents.append([]) #Appending an empty list everytime j changes.
        v3dNormals.append([])
        for k in range(intDiv): #Dado que ptos. de div. = segmentos + 1
            ###################################################################
            v3dTangents[j].append(rs.CurveTangent(strCurves[j],dblParam[j][k]))  
            ####################################################################
            #BUG: It works with open lines, not with closed ones.
            #"Div+1" works with open curves, but closed need "Div" ---> k loop.
            
            #Cross product with Z to calculate normal vectors to curves.
            v3dNormals[j].append(rs.VectorCrossProduct(v3dTangents[j][k],(0,0,-1)))
    trees(p3dPto, v3dNormals, dblAngle, intDiv)
    
def trees(Pts, Normals, Angle, Div):
    #Fancy way to declare several independant arrays in one time
    p3dPm, p3dP1, p3dP2 = ([] for k in range(3))
    # Loops para el acceso de los datos y la creacion de p3dPm.
    for i in range (len(Pts)):
        p3dPm.append([])
        for j in range(Div):
            p3dPm[i].append(rs.PointAdd(Pts[i][j],Normals[i][j]))
            rs.AddLine(Pts[i][j],p3dPm[i][j])
    
    
main()    