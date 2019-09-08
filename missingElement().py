# finds the msiing elemnt from first to second arr


def MissingElement(a,b):

    for x in a:
        if x in b:
            b.remove(x)
            a.remove(x)
    for x in a:
        if x not in b:
            print(x)
            
    
    
    
a=[1,2,3,4,5,6,7]
b=[3,7,2,1,4,6]

MissingElement(a,b)