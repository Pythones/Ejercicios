# ColourMe_Manu developement Classes
# 130712 Pythones@Manu

import rhinoscriptsyntax as rs
import ColourMe as cm

def main():
    
    #asking for objects to colour
    objColour = rs.GetObjects("Select objects to colour")
    if not objColour:
        print 'At least one object is needed to run the script'
        return
    
    #asking for colour mode (1)  
    strColourSource = rs.GetString("select colour source","rgb",['rgb','txtfile_WIP','asefile_WIP'])
    if not strColourSource:
        print 'At least one colour source is needed to run the script'
        return
    
    #asking for colour distrution (2) - NOT IMPLEMENTED YET
    #intColourDist = rs.GetInteger("Groups number",1)
    #if not intColourDist:
        #print 'At least one group is needed to run the script'
        #return
    
    #asking for a colour mode (3) 
    strColourMode = rs.GetString("select colour mode","random",['random','predominant'])
    if not strColourMode:
        print 'At least one colour mode is needed to run the script'
        return
    
    #Inicializo una instancia de objeto a colorear y la almaceno en la lista
    coloured = []
    strColour = []
    
    #Preparamos la masa
    if strColourSource == "rgb":
        strColour.append((140,169,56))
        strColour.append((10,89,56))
        
    #Preparamos la masa
    if strColourSource == "txtfile":
        
        file = open("C:\ColourList1.txt","r")
        for line in file.readlines():
            str = [value for value in line.split()]
            strColour.append(str)
        file.close()
        
        #file = open('C:\ColourList.txt', 'r')
        #str = file.read()
        #strColour.append(str)
        #file.close()
        
    #Dependiendo del modo, pasamos de una opcion a otra
    if strColourMode == "random":
        for i in range (len(objColour)):
            coloured.append(cm.ColourMe(objColour[i]))
            #Llamo a la funcion ColourMe que calcula un deslizamiento
            coloured[i].randomColour(strColour)
            
    if strColourMode == "predominant":
        intUserPred = rs.GetInteger("Set predominant percent for the first colour in list",90,10,100)
        for i in range (len(objColour)):
            coloured.append(cm.ColourMe(objColour[i]))
            #Llamo a la funcion ColourMe que calcula un deslizamiento
            coloured[i].predominantColour(strColour,intUserPred)
    
    print len (strColour)
    print (strColour)
            
            
if( __name__ == '__main__' ):
    main()