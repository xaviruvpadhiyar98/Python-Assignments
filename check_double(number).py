#Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.
#
#The number and its double should have exactly the same number of digits.
#Both the numbers should have the same digits ,but in different order.
#Otherwise it should return False.
#
#Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.





#PF-Assgn-38

def check_double(number):
    b=2*number
    c=1
    if len(str(number))==len(str(b)):
        for x in str(number):
          if x not in str(b):
              c=0
        if c==0:
            return False    
        else:
            return True
    else:
        return False        
print(check_double(125874))