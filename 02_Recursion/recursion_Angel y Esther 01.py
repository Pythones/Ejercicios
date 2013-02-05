import rhinoscriptsyntax as rs
radio=6
centro= (10,10,10)
def CIRC(r,c):
    rs.AddCircle(c,r)
    if (r>0.1): CIRC(r/2,rs.PointDivide(c,2))
    else: return
CIRC(radio,centro)