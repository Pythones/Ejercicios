################
# 
#
################

# Import modules
import rhinoscriptsyntax as rs
import random as rd
import math as m

def main():
    #Parameters.
    strPt0 = rs.GetPoint("Set system origin")
    dblLength = m.radians(rs.GetReal("Set initial length",1,0.01,15.0))
    dblalpha0 = m.radians(rs.GetReal("Set alpha angle limit0 (in degrees)",45.0,30.0,150.0))
    dblalpha1 = m.radians(rs.GetReal("Set alpha angle limit1 (in degrees)",45.0,30.0,150.0))
    dblbetha0 = m.radians(rs.GetReal("Set betha angle limit0 (in degrees)",45.0,30.0,150.0))
    dblbetha1 = m.radians(rs.GetReal("Set betha angle limit1 (in degrees)",45.0,30.0,150.0))
    
    dblalpha = rd.uniform(dblalpha0,dlbalpha1)
    
    
    
def recursion():
    
