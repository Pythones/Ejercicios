#max_130520 Pythones@Manuel
#curvas de maxima pendiente

import rhinoscriptsyntax as rs
import math as mt

#User comunication module 
def imput(): 
    
    #Establecemos las variables de entrada
    cub = rs.GetObject("Selecciona la cubierta a estudiar", rs.filter.surface + rs.filter.polysurface)
    line = rs.GetObject("Selecciona una linea de referencia")
    numDivs = rs.GetInteger("Numero de puntos de muestreo",30)
    startpoint = rs.CurveStartPoint(line)
    endpoint = rs.CurveEndPoint(line)
    
    #Lista para las curvas de nivel
    contour = []
    contour = rs.AddSrfContourCrvs(cub,(startpoint, endpoint))
    
    #Proyectamos todas las curvas en el plano de la curva superior
    #Las almacenamos en una nueva lista
    ncurvasup = len(contour)-1
    curvasup = contour[ncurvasup]
    plproj = rs.CurvePlane(curvasup)
    xform = rs.XformPlanarProjection(plproj)
    contourProj = []
    contourProj = rs.TransformObjects(contour,xform,True )
    
    #Definimos los puntos de inicio
    pts = []
    pts = rs.DivideCurve(curvasup,numDivs)
    
    #iniciamos un contador para iterar por curvas proyectadas
    count = 1
    
    #llamamos a la iteracion
    iterate (pts,curvasup,contourProj,cub,count)
    
    
def iterate(points,curve,curveGroup,srf,intCount):
    
    #Controlamos como se mueve la iteracion sobre el grupo de curvas
    #En cada iteracion debe tomar otra de la lista
    intCount = intCount+1
    
    #Localizamos la siguiente curva y actualizamos el contador
    numCurves = len(curveGroup)
    ncurveGroup = numCurves-intCount
    newCurve = curveGroup[ncurveGroup]
    
    #De points obtenemos dos familias: su parametro + elevarlos en z
    pointsParam = []
    pointsUp = []
    #alimentamos sus listas
    for i in range (len(points)):
        pointsParam.append(rs.CurveClosestPoint(curve,points[i]))
        pointsUp.append(rs.PointAdd(points[i],(0,0,10)))
    
    #Vamos a obtener el vector perpendicular a la curva en un pto: crossdotproduct
    vcTan = []
    vcUp = []
    vcPerp = []
    auxPts = []
    auxLine = []
    line = []
    pointsInter = []
    pointsInterSimplify = []

    #Alimentamos listas y resolvemos
    for i in range (len(points)):
        vcTan.append(rs.CurveTangent(curve,pointsParam[i]))
        vcUp.append(rs.VectorCreate(pointsUp[i],points[i]))
        vcPerp.append(rs.VectorCrossProduct(vcTan[i],vcUp[i]))
        auxPts.append(rs.PointAdd(points[i],vcPerp[i]))
        auxLine.append(rs.AddLine(points[i],auxPts[i]))
        #CURVECURVE CACA, TARDA LA MISMA VIDA: USAR PLANECURVE
        pointsInter.append(rs.CurveCurveIntersection(auxLine[i],newCurve))
        pointsInterSimplify.append(pointsInter[i][0][1])
        line.append(rs.AddLine(points[i],pointsInterSimplify[i]))
        rs.DeleteObjects(auxLine[i])
    
    #Proyectamos el resultado y borramos lo auxiliar
    for i in range (len(points)):
        rs.ProjectCurveToSurface(line[i],srf,(0,0,1))
        rs.DeleteObjects(line[i])
        
    #Ajustamos la iteracion anadiendo un fin y borrando la proyeccion aux    
    if len(curveGroup)>intCount:
        iterate(pointsInterSimplify,newCurve,curveGroup,srf,intCount)
    else:
        for i in range (len(curveGroup)):
            rs.DeleteObjects(curveGroup[i])
        
    
    
imput()