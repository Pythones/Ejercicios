import rhinoscriptsyntax as rs
import random as rd

def main():
    
    rgbValues = []
    lineProy = []
    
    #Open the file
    file = open("C:\ColourList.txt","r")
    #Read all the lines
    for line in file:
        rgbValues.append(line)
        split = line.split(",")
        s1 = int(split[0])
        s2 = int(split[1])
        s3 = int(split[2])
        lineProy.append(s1)
        lineProy.append(s2)
        lineProy.append(s3)


       
    valores = ('[(' + '), ('.join(rgbValues) + ')]')
    rcolour = rd.choice("abcdefghij")
    rcolour2 = rd.randint(1,3)
    if rcolour2 == 3:
        print "vale"
    else:
        print "no vale"

    print lineProy
    print line
    print split
    print rgbValues
    print valores
    print rcolour
    print rcolour2
    
main()