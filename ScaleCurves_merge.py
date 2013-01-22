#Escalado incremental de curva con ajuste a area o longitud y creacion de
#pasos intermedios cada 5 iteraciones.
#Pythones 121218 @Angel & @Manuel

import rhinoscriptsyntax as rs #Importa los metodos de rhinoscript

#Import curve.
strCurve = rs.GetObject("Pick a curve", rs.filter.curve, True)

#Choose a scale algorithm.
strChoose = rs.GetString("Select the algorithm","Length",("Length","Area"))

def ChooseAlgorithm():
    if strChoose == "Length":
        curveScaleLength(strCurve)
    elif strChoose == "Area":
        curveScaleArea(strCurve)
    else: 
        print("Option doesn't available") 
        return
        
#Currelo de angelito
def curveScaleArea(strCurve):
    #print("Scale Area")
    if not rs.IsCurveClosed(strCurve):
        print("The curve is open, please close the curve before use this algorithm")
        return
    dblArea = rs.CurveArea(strCurve)
    dblTargetArea = rs.GetReal("Define target area. The actual area is "+str(dblArea[0]))
    #Find curve centroid
    dblScalePoint = rs.CurveAreaCentroid(strCurve)
    #Adding a counter to copy curves.
    intCount = 0
    #Choosing if scale up or down.
    while (dblArea[0] <= dblTargetArea):
        strCurve = rs.ScaleObject(strCurve,dblScalePoint[0],(1.01,1.01,1.01))
        dblArea = rs.CurveArea(strCurve)
        intCount = (intCount + 1)
        #print intCount
        if intCount >= 5:
            strNewCurve = rs.CopyObject(strCurve)
            intCount=0
    while (dblArea[0] >= dblTargetArea):
        strCurve = rs.ScaleObject(strCurve,dblScalePoint[0],(0.99,0.99,0.99))
        dblArea = rs.CurveArea(strCurve)
        intCount = (intCount + 1)
        if intCount >= 5:
            strNewCurve = rs.CopyObject(strCurve)
            intCount=0
    print "The new area is: ",dblArea[0]

#Currelo de manolito 
def curveScaleLength(strCurve):
    #print("muyperra")
    dblLength = rs.CurveLength(strCurve)
    strNewLength = rs.GetReal("Choose your new length. Your actual length is " +str(dblLength))
    dblCentroid = rs.CurveAreaCentroid(strCurve)
    
    intCount = 0
    while (dblLength>strNewLength):
        strCurve = rs.ScaleObject(strCurve,dblCentroid [0],(0.99,0.99,0.99))
        dblLength = rs.CurveLength(strCurve)
        intCount = (intCount+1)
        if (intCount >= 5):
            rs.CopyObject(strCurve)
            intCount = 0
            
        if strCurve is None:
            print "en algo la hemos liado"
            return
            
    while (dblLength<strNewLength):
        strCurve = rs.ScaleObject(strCurve,dblCentroid [0],(1.01,1.01,1.01))
        dblLength = rs.CurveLength(strCurve)
        intCount = (intCount+1)
        if (intCount >= 5):
            rs.CopyObject(strCurve)
            intCount = 0
        if strCurve is None:
            print "en algo la hemos liado"
            return
        
    print"el nuevo largor es:", rs.CurveLength(strCurve)

#rs.EnableRedraw(False)
ChooseAlgorithm()
#rs.EnableRedraw(True)