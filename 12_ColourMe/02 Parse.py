#intentos de leer txt
#130714 Pythones@Manu

import rhinoscriptsyntax as rs

def main():
    
    f = open("C:/rgb.txt")
    for line in iter(f):
        print line
    f.close()
    
    print line