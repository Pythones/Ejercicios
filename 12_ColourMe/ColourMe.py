# ColourMe_Manu developement Classes
# 130712 Pythones@Manu

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random as rd

class ColourMe:
    
    def __init__(self,objColoured):
        self.objColoured = objColoured
        
    def randomColour(self,strColour):
        
        objNewColour = self.objColoured
        #Fabricamos un rango aleatorio
        rcolour = rd.randint(0,len(strColour)-1)
        #adjudicamos el color obtenido al objeto
        rs.ObjectColor(objNewColour,strColour[rcolour])
            
    def predominantColour(self,strColour):
                
        objNewColour = self.objColoured
        #Fabricamos un rango aleatorio
        rcolour = rd.randint(1,10)
        if rcolour == "1":
            #adjudicamos el color obtenido al objeto
            rs.ObjectColor(objNewColour,strColour[1])
        else:
            rs.ObjectColor(objNewColour,strColour[0])