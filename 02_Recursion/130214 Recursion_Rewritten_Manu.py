#Rewritten recursive action
#Imput: Point+Angle+scaleFactor+endLength

import rhinoscriptsyntax as rs
import math as mt


#User comunication
def Main():
    Pt1 = rs.GetPoint("Set a point")
    Pt2 = rs.PointAdd(Pt1,(0,10,0))
    startLine = rs.AddLine(Pt1,Pt2)
    #dblAngle = mt.radians(rs.GetReal("Choose an angle",110))
    dblAngle = rs.GetReal("Choose an angle",10)
    endLength = rs.GetReal("Dead length",5)
    scaleFactor = rs.GetReal("Scale Factor",0.9)
    
    return Recursion (startLine,dblAngle,scaleFactor,endLength,endLength)
    
    
#Recursion Engine
def Recursion (Line,angle,scale,initialLength,deadLength):
    #calculamos por donde va ahora la longitud de la linea
    #mas tarde la compararemos con nuestra referencia
    initialLength = rs.CurveLength(Line)
    #Puntos finales
    PtStart = rs.CurveStartPoint(Line)
    PtEnd = rs.CurveEndPoint(Line)
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