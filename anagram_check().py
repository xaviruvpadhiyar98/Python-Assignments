#anagram string test without " "(spaces checking)
##anagram_check function !!
## anagram1 function



def removeFromList(a,b):
    for x in a:
            if x in b:
                a.remove(x)
                b.remove(x)
    

def anagram_check(str1,str2):
    
    a=[]
    b=[]
    for x in str1:
        if x!=' ':
            a.append(x)
    for x in str2:
        if x!=' ':
            b.append(x)
        
    for x in range(len(a)//2):
        removeFromList(a,b)
    
    print(a)
    print(b)
    if a==b:
        return True
    else:
        return False


def anagram1(s1,s2):
    s3=s1.replace(' ','').lower()
    s4=s2.replace(' ','').lower()
    return sorted(s3)==sorted(s4)


str1='cli nt eastwood'
str2='old west action'

print(anagram1(str1,str2))


