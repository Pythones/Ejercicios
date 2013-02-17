import random as r

def randsign():
    a = r.randrange(0,2,1)*2-1
    return a
    
print randsign()