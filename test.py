import timeit

def UniqueChar(s):
    print(s)
    c=0
    for x in s:
        if s.count(x) > 1:
            c=1
        else:
            c=0
    if c==0:           
        print("Unique")
    else:
        print("Not Unique")
    
    
UniqueChar('abcde')
a=timeit.timeit(1)
print(a)