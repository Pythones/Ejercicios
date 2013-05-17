#Rewritten recursive action LISTS
#Imput: Point+Angle+scaleFactor+endLength

import rhinoscriptsyntax as rs
import math as mt


#User comunication
def Main():
    #List creation
    Pts1 = []
    Pts2 = []
    startLine = []
    #Feeding first list
    Pts1 = rs.GetObjects("Set points",rs.filter.point)
    if Pts1 is None: return
    #Feeding second list
    for i in range(len(Pts1)):
        Pts2.append(rs.PointAdd(Pts1[i],(0,10,0)))
        startLine.append(rs.AddLine(Pts1[i],Pts2[i]))
    dblAngle = rs.GetReal("Choose an angle",10)
    endLength = rs.GetReal("Dead length",5)
    scaleFactor = rs.GetReal("Scale Factor",0.9)
    
    Recursion (startLine,dblAngle,scaleFactor,endLength,endLength)
    
    
#Recursion Engine
def Recursion (Line,angle,scale,initialLength,deadLength):
    #calculamos por donde va ahora la longitud de la linea
    #mas tarde la compararemos con nuestra referencia
    for i in range(len(Line)):
        initialLength = rs.CurveLength(Line[i])
        #Puntos finales
        PtStart = rs.CurveStartPoint(Line[i])
        PtEnd = rs.CurveEndPoint(Line[i])
        #Vector
        vec0 = rs.VectorCreate(PtEnd,PtStart)
        vec1 = rs.VectorScale(vec0,scale)
        vec2 = rs.VectorRotate(vec1,angle,(0,0,1))
        vec3 = rs.VectorRotate(vec1,-angle,(0,0,1))
        #double Points
        Pta = rs.PointAdd(PtEnd,vec2)
        Ptb = rs.PointAdd(PtEnd,vec3)
        #Creating Line
        Linea = rs.AddLine(PtEnd,Pta)
        Lineb = rs.AddLine(PtEnd,Ptb)
        #Breaking Point
        if deadLength<initialLength:
            Recursion (Linea,angle,scale,initialLength,deadLength)
            Recursion (Lineb,angle,scale,initialLength,deadLength)
            
        
Main()
    
Main()