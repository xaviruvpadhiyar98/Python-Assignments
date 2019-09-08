def rotate(l,n):
    return l[n:]+l[:n]

def nearestRoot(num):
    for x in range(num//2):
        if x**2 <= num and num > (x+1)**2:
            temp=x
    return temp+1


def mxn(list1):
    matrix=[]    
    n=nearestRoot(len(list1))
    while list1!=[]:        
        matrix.append(list1[:n])
        list1=list1[n:]
    return matrix

def matrixPrint(matrix):
    mat1=mxn(matrix)
    for index,x in enumerate(mat1):
        if index<3:
            for y in x:
                print(str(y) + " ", end='')
            print()
            
def diagonalsum(list1):
    n=nearestRoot(len(list1))
    n=n**2
    sum=list1[:n:2]
    mid=list1[len(list1[:n])//2]
    tot=0
    for x in sum:
        tot+=x
    return tot+mid        
    
    
list1=[1,2,3,4,5,6,7,8,9,10,11]

list2=list1[1:]
matrixPrint(list2)
n=diagonalsum(list1)
n1=diagonalsum(list2)










