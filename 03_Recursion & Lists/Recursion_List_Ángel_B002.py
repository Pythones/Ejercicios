import rhinoscriptsyntax as rs
import math as m

def tree(ptos,perp,dist):
    

def main():
    
    strCrv = rs.GetObjects("Select base curves",4)
    intDiv = rs.GetInteger("Number of divisions",5,2,15)
    dblDist = rs.GetReal("Initial branch length",1,0.1,10)
    tanCrv = []
    perpCrv = []
    
    dblPar = rs.DivideCurve(strCrv,intDiv,False,False)
    p3dDiv = rs.DivideCurve(strCrv,intDiv)
    for i in range(len(dblPar)):
        tanCrv.append(rs.CurveTangent(strCrv,dblPar[i]))
        perpCrv.append(rs.VectorCrossProduct(tanCrv[i],(0,0,-1)))
        #rs.AddPoint(rs.PointAdd(p3dDiv[i],perpCrv[i]*10))
        
    tree(p3dDiv,perpCrv,dblDist)
        
main()
    