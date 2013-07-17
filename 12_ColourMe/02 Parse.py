#intentos de leer txt
#130714 Pythones@Manu

import rhinoscriptsyntax as rs

def main():
    arch = []
    f = open("C:\ColourList.txt","r")
    for line in iter(f):
        arch.append(line)
    f.close()
    
    print arch
main()
