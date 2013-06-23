# Raindrop_Manu developement Classes
# 130622 Pythones@Manu

import rhinoscriptsyntax as rs
import RaindropManu as rd

def main():
    
    #Pidiendo datos al usuario y anulandolo si alguno falta.
    strBaseSrf = rs.GetObject("Select the surface to calculate drop",rs.filter.surface)
    if not strBaseSrf:
        print 'At least one surface is needed to run the script'
        return
    strDrop = rs.GetObjects("Select points ON surface",rs.filter.point)
    if not strDrop:
        print 'At least one point ON surface is needed to run the script'
        return
    intIterations = rs.GetInteger("Iterations",100)
    
    #Inicializo una instancia de gota y la almaceno en la lista drops
    dropCoord = []
    drops = []
        
    for i in range (len(strDrop)):
        dropCoord.append(rs.PointCoordinates(strDrop[i]))
        drops.append(rd.Raindrop_Manu(dropCoord[i]))
    
    #Itero para una gota concreta utilizando el maximo suministrado por el usuario
    for i in range(len(drops)):
        for k in range(intIterations):
            #Llamo a la funcion flow que calcula un deslizamiento
            drops[i].flow(strBaseSrf)
            
            
if( __name__ == '__main__' ):
    main()