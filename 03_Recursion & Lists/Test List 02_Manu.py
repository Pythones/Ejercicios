#list para todos_130210 Pythones@Manuel
#trying lists, divide diferent curves and write sth on each point

import rhinoscriptsyntax as rs

def main():
    #List declare
    objCrvs = []
    multiplePts = []
    muchasLines = []
    #feeding 1st list
    objCrvs = rs.GetObjects("Damelossss")
    if objCrvs is None: return
    #Defining variables
    intDvd = rs.GetInteger("en cuanto la dividimos?",10)
    #feeding 2nd list
    #for i in range(len(objCrvs)):
        #multiplePts.append(rs.DivideCurve(objCrvs[i],intDvd,True))
        #for j in range(len(multiplePts[i])):
            #rs.AddText("loco",multiplePts[i][j])
            
    Pointificacion(objCrvs,intDvd)
    

def Pointificacion(curves,divide):
    #List declare
    points = []
    #feeding 2nd list
    for i in range(len(curves)):
        points.append(rs.DivideCurve(curves[i],divide,True))
        for j in range(len(points[i])):
            rs.AddText("loco",points[i][j])
        
main()