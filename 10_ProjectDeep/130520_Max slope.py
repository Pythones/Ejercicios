#max_130520 Pythones@Manuel
#curvas de maxima pendiente

import rhinoscriptsyntax as rs
import math as mt

#User comunication module 
def imput(): 
    
    #Establecemos las variables de entrada
    cub = rs.GetObject("Selecciona la cubierta a estudiar", rs.filter.surface + rs.filter.polysurface)
    line = rs.GetObject("Selecciona una linea de referencia")
    numpoints = rs.GetInteger("Numero de puntos de muestreo",30)
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
    
    planecurve (curvasup,numpoints,contourProj,cub)
    
    
def planecurve(curve,numDiv,curveGroup,srf):
    
    #Definimos los puntos de inicio
    points = []
    points = rs.DivideCurve(curve,numDiv)
    #obtenemos su parametro y elevamos los pt 3d en z
    paramPoints = []
    pointsUp = []
    #alimentamos sus listas
    for i in range (len(points)):
        paramPoints.append(rs.CurveClosestPoint(curve,points[i]))
        pointsUp.append(rs.PointAdd(points[i],(0,0,10)))
    
    #Vamos a obtener el vector perpendicular a la curva en un pto: crossdotproduct
    vcTan = []
    vcPer = []
    vcLine = []
    perPoints = []
    line = []
    line2 = []
    intersect = []
    #Localizamos la siguiente curva
    ncurveGroup = len(curveGroup)-2
    #Alimentamos listas y resolvemos
    for i in range (len(points)):
        vcTan.append(rs.CurveTangent(curve,paramPoints[i]))
        vcPer.append(rs.VectorCreate(pointsUp[i],points[i]))
        vcLine.append(rs.VectorCrossProduct(vcTan[i],vcPer[i]))
        perPoints.append(rs.PointAdd(points[i],vcLine[i]))
        line.append(rs.AddLine(points[i],perPoints[i]))
        #CURVECURVE CACA, TARDA LA MISMA VIDA: USAR PLANECURVE
        intersect.append(rs.CurveCurveIntersection(line[i],curveGroup[ncurveGroup]))
        line2.append(rs.AddLine(points[i],intersect[i][0][1]))
        rs.DeleteObjects(line[i])
        
    for i in range (len(points)):
        rs.ProjectCurveToSurface(line2[i],srf,(0,0,1))
        rs.DeleteObjects(line2[i])
    
    #comprobamos
    print (intersect[i][0][1])
    print len(intersect)
        
    
    
imput()