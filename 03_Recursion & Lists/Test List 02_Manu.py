#list para todos_130210 Pythones@Manuel
#trying lists, divide diferent curves and write sth on each point

import rhinoscriptsyntax as rs

def main():
    #List declare
    objCrvs = []
    multiplePts = []
    #feeding list
    objCrvs = rs.GetObjects("Damelossss")
    if objCrvs is None: return
    intDvd = rs.GetReal("en cuanto la dividimos?",10)
    
    multiplePts = rs.DivideCurve(objCrvs,intDvd,True)
    #for i in range(len(objCrvs)):
        #multiplePts = rs.DivideCurve(objCrvs[i],intDvd,True)
    
    engine(objCrvs,multiplePts)
    
    
def engine(curves,points):
    for i in range(len(points)):
        rs.AddText("loco",points[i])
        
        
main()