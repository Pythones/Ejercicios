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
    strColourSource = rs.GetString("select colour source","rgb",['rgb','txtfile','asefile'])
    if not strColourSource:
        print 'At least one colour source is needed to run the script'
        return
    
    #asking for colour distrution (2)
    intColourDist = rs.GetInteger("Groups number",1)
    if not intColourDist:
        print 'At least one group is needed to run the script'
        return
    
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
        #file = open('C:\ColourList.txt', 'r')
        #str = file.read()
        #strColour.append(str)
        #file.close()
        #f = open('C:\Users\Administrador\AppData\Local\Apps\2.0\R7HE8EDP.ZHO\9XXQA0AY.BQ3\gith..tion_317444273a93ac29_0001.0000_08490aa4380d2e54\psf\Home\Documents\GitHub\Ejercicios\10_ProjectDeep\ColourList.txt', 'r')
        #strColour = f.read()
        #print strColour
        strColour.append((140,169,56))
        strColour.append((10,89,56))
                
    #Dependiendo del modo, pasamos de una opcion a otra
    if strColourMode == "random":
        for i in range (len(objColour)):
            coloured.append(cm.ColourMe(objColour[i]))
            #Llamo a la funcion ColourMe que calcula un deslizamiento
            coloured[i].randomColour(strColour)
            
    if strColourMode == "predominant":
        for i in range (len(objColour)):
            coloured.append(cm.ColourMe(objColour[i]))
            #Llamo a la funcion ColourMe que calcula un deslizamiento
            coloured[i].predominantColour(strColour)
    
    print len (strColour)
    print (strColour)
            
            
if( __name__ == '__main__' ):
    main()