# Calculates drainage lines over a surface.
# 130604 Pythones@Angel

import rhinoscriptsyntax as rs
import Raindrop as rd
import time as t
import System.Drawing as sd

def main():
    
    #Pidiendo datos al usuario y anulandolo si alguno falta.
    strCurves = []
    strBaseSrf = rs.GetObject("Select the surface to calculate drop",rs.filter.surface)
    if not strBaseSrf:
        print 'At least one surface is needed to run the script'
        return
    strDrop = rs.GetObjects("Select the drop point",rs.filter.point)
    if not strDrop:
        print 'At least one point is needed to run the script'
        return
    intIterations = rs.GetInteger("Iterations",1000)
    strGradient = rs.GetString("Represent flowlines length?","Yes",('Yes','No'))
    
    drops = []
    
    # Inicializo una instancia de gota y la almaceno en la lista drops
    # y establezco una marca temporal time0
    time0 = t.time()
    for i in range(0,len(strDrop)):

        # Compruebo que los puntos son proyectables sobre la superficie
        # y los almaceno si lo son.
        # Esto no seria necesario si rs.ProjectPointToSurface funcionara bien.
        
        p3dTest = rs.ShootRay(strBaseSrf,strDrop[i],(0,0,-1))
        if p3dTest != None:
            drop = rs.PointCoordinates(strDrop[i])
            drops.append(rd.Raindrop(drop))
        
    # Paro el redibujo de la vista para acelerar el proceso de dibujo
    rs.EnableRedraw(False)
    
    # Itero a lo largo de drops para llamar a las funciones de cada instancia
    # simbolizada por la variable droptest.
    
    flowlines = []
    for droptest in drops:
        
        # La funcion falls proyecta los puntos sobre la superficie.
        droptest.falls(strBaseSrf)
        
        # Se inicializa la variable strCurves cada vez que se empieza el loop
        # para una nueva gota. En esta lista se almacenan los trozos de las lineas
        # de caida.
        strCurves = []
        
        # Itero para una gota concreta utilizando el maximo suministrado por le usuario.
        for k in range(intIterations):
            
            # Llamo a la funcion flow que calcula un deslizamiento y devuelve la
            # linea de deslizamiento o None en caso de no poder calcularse. 
            # Guardo la linea en strCurves.
            strLine = droptest.flow(strBaseSrf)
            
            # Para almacenar la linea compruebo que se haya trazado y que su
            # longitud sea mayor a un limite preestablecido. Caso contrario,
            # se cancela el loop.
            if strLine != None and rs.CurveLength(strLine) > 0.01:
                strCurves.append(strLine)
            else:
                break            

        # Uno todas las lineas almacenadas y las borro en caso de que haya mas
        # de una almacenada en la lista.
        if len(strCurves)>1:
            strJCurves = rs.JoinCurves(strCurves,True)
            flowlines.append(strJCurves)
        elif len(strCurves)==1:
            flowlines.append(strCurves)
    
    if strGradient == 'Yes':
        dblColours = CalcColour(flowlines)
        # print dblColours
        for i in range(len(flowlines)):
            rs.ObjectColor(flowlines[i],sd.Color.FromArgb(255,int(dblColours[i]),0))
    
    # Cuando termino con todas las gotas, reestablezco la vista, calculo la marca
    # temporal 2 y la imprimo en pantalla.
    rs.EnableRedraw(True)
    time1 = t.time()
    print 'running time: ' + str(time1-time0)
    
    
    
# Calcula un color degradado de amarillo a rojo segun longitud
# de una curva.
def CalcColour(strCurves):
    dblLen = []
    for crv in strCurves:
         #print crv
         #if rs.IsCurve(crv):
         dblLen.append(rs.CurveLength(crv))
         #elif rs.IsLine(crv):
         #dblLen.append(rs.Distance(crv.From,crv.To))
    
    for i in range(len(dblLen)):
        #print max(dblLen)
        dblLen[i] = dblLen[i]/max(dblLen)
        #print len
        dblLen[i] = dblLen[i]*255
        #print len
        
    return dblLen


if( __name__ == '__main__' ):
    main()