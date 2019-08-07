#Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.
#
#Write a python function which performs the run length encoding for a given String and returns the run length encoded String.
#
#Provide different String values and test your program.
#
#Sample Input         Expected Output
#AAAABBBBCCCCCCCC     4A4B8C
#AABCCA               2A1B2C1A






#PF-Assgn-30

def encode(message):
    encoding = ''
    prev_char = ''
    count = 1

    if not message: return ''

    for char in message:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding
    
    
    
    
    
#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)