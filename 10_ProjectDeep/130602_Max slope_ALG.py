import rhinoscriptsyntax as rs
import Raindrop as rd

def main():
    
    strBaseSrf = rs.GetObject("Select the surface to calculate drop",rs.filter.surface)
    strDrop = rs.GetObject("Select the drop point",rs.filter.point)
    
    Drop = Raindrop(strDrop)
    
    Drop.falls()
    
    
main()