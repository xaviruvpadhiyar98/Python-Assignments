##Balanced Parenthesis Check prints true or false based on Input



def BalancedParanthesis(str):
    balanced=0
    for x in str:
        if x=='(' in str or x=='[' in str or x=='{' in str :
            balanced+=1
        else:
            balanced-=1
    if balanced==0:
        print("True")
    else:
        print("False")
        
    
    

BalancedParanthesis('[[[]])](')