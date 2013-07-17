#intentos de leer txt
#130714 Pythones@Manu
#http://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/

import rhinoscriptsyntax as rs

def main():
    
    archivo = []
    
    #Open the file with read only permitouh
    file = ("C:\ColourList.txt")
    f = open(file)
    #Read the first line 
    line = f.readlines()
    archivo.append(line)
    
    #If the file is not empty keep reading line one at a time
    #till the file is empty
    while line:
        print line
        line = f.readline()
        archivo.append(line)
    f.close()
    
    print line
    print archivo
    
main()