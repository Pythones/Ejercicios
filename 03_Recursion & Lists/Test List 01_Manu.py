#list para todos_130210 Pythones@Manuel
#trying lists

import rhinoscriptsyntax as rs

def main():
    multiplePts = []
    multiplePts = rs.GetObjects("Damelossss")
    if multiplePts is None: return
    engine(multiplePts)
    
    
def engine(points):
    for i in range(len(points)):
        rs.AddText("loco",points[i])
        
        
main()