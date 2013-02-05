import rhinoscriptsyntax as rs
radio=6
centro= (10,0,0)
def CIRC(r,c):
    rs.AddCircle(c,r)
    if (r>0.01): 
        CIRC(r/2,rs.PointDivide(c,2))
        CIRC(r/2,rs.PointScale(c,2))
    else: return
CIRC(radio,centro)