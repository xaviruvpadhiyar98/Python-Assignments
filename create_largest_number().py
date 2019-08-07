#Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers. 
#Note: Assume that all the numbers are two digit numbers.
#
#Also write the pytest test cases to test the program.
#
#Sample Input    Expected Output
#23,34,55        553423



def create_largest_number(number_list):
    maxstring=''
    
    for x in range(len(number_list)):
            
        maxnumber=max(number_list)
        number_list.remove(maxnumber)
        maxstring+=str(maxnumber)
        
    return int(maxstring)
    #remove pass and write your logic here

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)




