#list para todos_130210 Pythones@Manuel
#trying lists, divide diferent curves and write "loco!" on each point

import rhinoscriptsyntax as rs

def main():
    #List declare
    objCrvs = []
    #feeding 1st list
    objCrvs = rs.GetObjects("Damelossss")
    if objCrvs is None: return
    #Defining variables
    intDvd = rs.GetInteger("en cuanto la dividimos?",10)
            
    Pointificacion(objCrvs,intDvd)
    
def Pointificacion(curves,divide):
    #List declare
    points = []
    coord = []
    #feeding 2nd list
    for i in range(len(curves)):
        points.append(rs.DivideCurve(curves[i],divide,True))
        for j in range(len(points[i])):
            #coord.append(rs.PointCoordinates(points[i][j]))
            rs.AddText("loco! ",points[i][j])
        
main()