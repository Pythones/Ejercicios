#Tuneando uno de los ejemplos de mcneel para la entrada de datos de recursion
#https://github.com/mcneel/rhinopython/blob/master/scripts/samples/advanced/CustomGetPoint.py
#Recursion para todos_130131 Pythones@Manuel

import Rhino
import System.Drawing.Color
import scriptcontext
import rhinoscriptsyntax as rs

def CustomLine():
    # Color to use when drawing dynamic lines
    line_color = System.Drawing.Color.FromArgb(255,0,0)
    
    rc, pt1 = Rhino.Input.RhinoGet.GetPoint("Start point", False)
    if( rc!=Rhino.Commands.Result.Success ): return

    # This is a function that is called whenever the GetPoint's DynamicDraw event occurs
    def GetPointDynamicDrawFunc( sender, args ):
        #draw a line from the first picked point to the current mouse point
        args.Display.DrawLine(pt1, args.CurrentPoint, line_color, 2)

    # Create an instance of a GetPoint class and add a delegate for the DynamicDraw event
    gp = Rhino.Input.Custom.GetPoint()
    gp.DynamicDraw += GetPointDynamicDrawFunc
    gp.Get()
    if( gp.CommandResult() == Rhino.Commands.Result.Success ):
        pt = gp.Point()
        line = Rhino.Geometry.Line(pt1,pt)
        scriptcontext.doc.Objects.AddLine(line)
        scriptcontext.doc.Views.Redraw()

CustomLine()