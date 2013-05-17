#Lineweight_130513 Pythones@Manuel
#proyectar sobre plano identificando espesores

import rhinoscriptsyntax as rs
import math as mt

def main():
    #Definimos el plano de proyeccion
    rs.Prompt("El plano de proyeccion es el YZ")
    PlProy = rs.WorldYZPlane()
    rs.AddPlaneSurface(PlProy,30,30)
    
    #Definimos el plano de corte
    PlCortea = rs.WorldYZPlane()
    Neworigin = rs.GetPoint("Origen del plano de corte")
    PlCorteb = rs.MovePlane(PlCortea,Neworigin)
    rs.AddPlaneSurface(PlCorteb,30,30)
    
    #Anadimos texto
    rs.AddTextDot("Plano de Proyeccion",Neworigin)
    rs.AddTextDot("Plano de Corte",(0,0,0))
    
    #Calculamos la distancia entre el plano del proyeccion y el de corte
    length = rs.DistanceToPlane(PlProy,Neworigin)
    
    #Definimos los elementos sobre los que trabajaremos
    #List declare
    edge = []
    interpoints = []
    PlBase = rs.WorldXYPlane()
    Cosaproyectada = rs.GetObject("Dame algo que proyectar")
    edge = rs.DuplicateEdgeCurves(Cosaproyectada)
    for i in range(len(edge)):
        interpoints.append(rs.LinePlaneIntersection(edge[i],PlBase))
            
    diferenciando(objCrvs,PlProy,length,interpoints)
    
def diferenciando(curves,plane,dist,points):
    #List declare
    distances = []
    
    #feeding distances list
    for i in range(len(points)):
        distances.append(rs.DistanceToPlane(plane,points[i]))
        
    #evaluamos distancias
    for i in range(len(distances)):
        if distances[i] > dist:
            rs.AddText("fuera",curves [i])
        else:
            rs.AddText("dentro",curves [i])
    
    print distances
        
main()