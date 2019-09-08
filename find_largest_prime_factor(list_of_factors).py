#A 10-substring of a number is a substring of its digits that sum up to 10.
#
#For example, the 10-substrings of the number 3523014 are:
#3523014, 3523014, 3523014, 3523014
#
#Write a python function, find_ten_substring(num_str) which accepts a string and returns the list of 10-substrings of that string.
#
#Handle the possible errors in the code written inside the function.
#
#Sample Input    Expected Output
#'3523014'   ['5230', '23014', '523', '352']





def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))
    
print(is_prime(12,13//2))    