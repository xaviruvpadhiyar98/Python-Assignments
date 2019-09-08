l=[1,3,2,2,1]
n=4
count=0
sum=0
l1=l
for x in l:
    for y in l1:
        if x+y == n:
            count+=1
            print(x,y)
            l1.remove(y)
            l1.remove(x)
print(count)
            


    
    