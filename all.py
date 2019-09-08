import time


def lcm(x,y):
    return (x*y)//gcd(x,y)


def gcd(x,y):
    if y==0:
        return x
    return gcd(y,x%y)

def greatestOfTwoNumber(x,y):
    if x>y:
        return x
    return y

def greatestOfThreeNumber(x,y,z):
    x=max(x,y)
    x=max(x,z)
    return x


def numberOfDigits(x):
    return len(str(x))

def sumOfDigits(x):
    if x==0:
        return x
    return int(x%10) + sumOfDigits(int(x/10))  
        
def sumOfNNumbers(x):
    sum=0
    for i in range(x):
        sum+=i
    return sum
 

def sumOfNNumbers(x):
    return x*(x+1)//2


def sumOfNumbersInRange(x,y):
    return ((y * (y + 1)) - (x * (x - 1))) // 2




def reverseNumber(n):
    rev = 0
    while(n != 0): 
        a = int(n) % 10
        rev = rev * 10 + a 
        n = int(n) // 10
    return rev


def factorial(x):
    if x==0:
        return 1
    if x<0:
        return -1
    return factorial(x-1)*x



def fib_to(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]


    
a=time.time()    
print("GCD or HCF of 2 Numbers "+str(gcd(98,56)))
b=time.time()
c=b-a
print("Time Taken "+str(c))
print("")



a=time.time() 
print("LCM OF 2 Numbers "+str(lcm(98,56)))
b=time.time()
c=b-a
print("Time Taken " + str(c))
print("")



a=time.time() 
print("Greatest OF 2 Numbers "+str(greatestOfTwoNumber(98,56)))
b=time.time()
c=b-a
print("Time Taken " + str(c))
print("")



a=time.time() 
print("Greatest OF 3 Numbers "+str(greatestOfThreeNumber(198,156,102)))
b=time.time()
c=b-a
print("Time Taken " + str(c))
print("")



a=time.time() 
print("Number OF Digits in Numbers "+str(numberOfDigits(98123)))
b=time.time()
c=b-a
print("Time Taken " + str(c))
print("")


a=time.time() 
print("Sum OF Digits in Numbers "+str(sumOfDigits(5)))
b=time.time()
c=b-a
print("Time Taken " + str(c))
print("")


a=time.time() 
print("Sum OF Natural Numbers "+str(sumOfNNumbers(5)))
b=time.time()
c=b-a
print("Time Taken " + str(c))
print("")




a=time.time() 
print("Sum OF Natural Numbers in Range"+str(sumOfNumbersInRange(1200,1500)))
b=time.time()
c=b-a
print("Time Taken " + str(c))
print("")



a=time.time() 
print("Reversed "+str(reverseNumber(12001)))
b=time.time()
c=b-a
print("Time Taken " + str(c))
print("")


a=time.time() 
print("Factorial  "+str(factorial(100)))
b=time.time()
c=b-a
print("Time Taken " + str(c))
print("")


a=time.time() 
print("Fibonnaci Series of N element  "+str(fib_to(100)))
b=time.time()
c=b-a
print("Time Taken " + str(c))
print("")









