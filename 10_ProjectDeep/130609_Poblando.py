# Review_Same script that Max slope but "functions style"
# 130609 Pythones@Manu

import rhinoscriptsyntax as rs
import time as t


def main():
    
    p3dDropProj = []
    
    #Pidiendo datos al usuario y anulandolo si alguno falta.
    strCurves = []
    strBaseSrf = rs.GetObject("Select the surface to calculate drop",rs.filter.surface)
    if not strBaseSrf:
        print 'At least one surface is needed to run the script'
        return
    #Pidiendo resto de parametros
    intIterations = rs.GetInteger("Iterations",10)
    dblStep = rs.GetReal("Step size", 0.1,0.01,100)
    strGradient = rs.GetString("Represent flowlines length?","Yes",('Yes','No'))
    #Counter for Flows
    Count = 0
    
    time0 = t.time()
    
    rs.EnableRedraw(False)
    Falls(strBaseSrf,p3dDropProj)
    Flows(strBaseSrf,dblStep,intIterations,p3dDropProj,Count)
    rs.EnableRedraw(True)
    
    time1 = t.time()
    print 'running time: ' + str(time1-time0) + 'sec.'
    
    
def Falls(strSfr1,p3dDropProj1):
   
    p3dDropProj0 = []
    
    # Get the number of rows
    rows = rs.GetInteger("Number of rows", 5, 2)
    if not rows: return
 
    # Get the number of columns
    cols = rs.GetInteger("Number of columns", 5, 2)
    if not cols: return
 
    # Get the domain of the surface
    u, v = rs.SurfaceDomain(strSfr1, 0), rs.SurfaceDomain(strSfr1, 1)
    if not u or not v: return
 
    # Turn off redrawing (faster)
    rs.EnableRedraw(False)
 
    # Add the points
    for i in range(rows):
        s = u[0] + ((u[1]-u[0])/(rows-1))*i
        for j in range(cols):
            t = v[0] + ((v[1]-v[0])/(cols-1))*j
            pt = rs.EvaluateSurface(strSfr1, s, t)
            p3dDropProj1.append(rs.AddPoint(pt)) # add the point
    
    # Turn on redrawing
    #rs.EnableRedraw(True)
    
    
def Flows(strSrf,step,iterations,p3dDropProj2,intCount):
    
    #New variable for setting a break point
    intCount = intCount+1
    
    #Setting lists    
    p3dDummy1 = []
    p3dUV = []
    v3dNormal = []
    v3dUni = []
    p3dDummy2 = []
    lineDummy = []
    lineProy = []
    p3dDropEnd = []
    p3dDrop = []
    lineProyTest = []
    
    #Tomamos los ptos proyectados y sacamos coordenadas
    for i in range (len(p3dDropProj2)):
        
        #obtenemos pto en srf #obtenemos su uv
        p3dDummy1.append(rs.coerce3dpoint(p3dDropProj2[i]))
        p3dUV.append(rs.SurfaceClosestPoint(strSrf,p3dDummy1[i]))
        
        #sacamos la normal en ese pto a la srf #hacemos unitario el vector #desplazamos el pto
        v3dNormal.append(rs.SurfaceNormal(strSrf,p3dUV[i]))
        v3dUni.append(rs.VectorUnitize(v3dNormal[i]))
        p3dDummy2.append(rs.PointAdd(p3dDummy1[i],v3dUni[i]))
        
        #anadimos linea #Proyectamos la linea sobre la superficie #borramos los pelos
        lineDummy.append(rs.AddLine(p3dDummy1[i],p3dDummy2[i]))
        lineProyTest.append(rs.ProjectCurveToSurface(lineDummy[i],strSrf,(0,0,-1)))
        rs.DeleteObjects(lineDummy[i])
        
        #Nueva lista eliminando los nones de la anterior (NEW! - USING FILTER)
        lineProy = filter(None,lineProyTest)
        
    for i in range (len(lineProy)):
        #Buscamos el pto final de las minicurvas para empezar a iterar
        p3dDropEnd.append(rs.CurveEndPoint(lineProy[i]))
        
    #set a Break Point
    if intCount<iterations:
        Flows(strSrf,step,iterations,p3dDropEnd,intCount)
        
        

main()







#bonus code
#import felizcumpleagnos as fc
#if Esther != None:
    #fc.sendGreetings (Esther,shout)
    
#MUCHAS FELICIDADESSSSSSSS!!!