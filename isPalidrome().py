#Write a recursive function, is_palindrome() to find out whether a string is a palindrome or not. The function should return true, if it is a palindrome. Else it should return false. 
#
#Note- Perform case insensitive operations wherever necessary.
#
#Also write the pytest test cases to test the program.
#
#



#PF-Assgn-40
def is_palindrome(word):
    rev=word[::-1]
    if rev==word:
        return True
    else:
        return False
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")