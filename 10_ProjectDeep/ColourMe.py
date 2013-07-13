# ColourMe_Manu developement Classes
# 130712 Pythones@Manu

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random as rd

class ColourMe:
    
    def __init__(self,objColoured):
        self.objColoured = objColoured
        
    def getColour(self,strColour):
        
        objNewColour = self.objColoured
        #Fabricamos un rango aleatorio
        brake = rd.randint(0,len(strColour))
        #adjudicamos el color obtenido al objeto
        for i in range(0,brake):
            rs.ObjectColor(objNewColour,strColour[i])