import rhinoscriptsyntax as rs
import math as m

def main():
    
    strCrv = rs.GetObjects("Select base curves",4)
    intDiv = rs.GetInteger("Number of divisions",5,2,15)
    tanCrv = []
    perpCrv = []
    
    dblPar = rs.DivideCurve(strCrv,intDiv,False,False)
    p3dDiv = rs.DivideCurve(strCrv,intDiv)
    for i in range(len(dblPar)):
        tanCrv.append(rs.CurveTangent(strCrv,dblPar[i]))
        perpCrv.append(rs.VectorCrossProduct(tanCrv[i],(0,0,-1)))
        rs.AddPoint(rs.PointAdd(p3dDiv[i],perpCrv[i]*10))
        
main()
    