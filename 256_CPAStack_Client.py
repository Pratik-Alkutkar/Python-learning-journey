"""
@Goal: To test CPAStack class in CPAStack package 
"""

from CPAStack import CPAStack 

def main(): 
    
    print("CLIENT START")
    S = CPAStack() 
    if S.is_empty(): 
        print("Stack is empty now")
    
    try: 
        n = S.pop() 
    except (ValueError, TypeError): 
        print("Cannot pop from empty stack")

    try: 
        n = S.top() 
    except (ValueError, TypeError): 
        print("Cannot top the empty stack")

    from random import randint 
    for i in range(5): 
        n = randint(1, 100)
        S.push(n)
        print("Pushed {} on stack".format(n))

    if not S.is_empty(): 
        print("Stack is not empty now")

    n = S.top() 
    print("Last pushed element:", n)

    while not S.is_empty(): 
        n = S.pop() 
        print("Poped element:", n)  
    print("CLIENT END")

main()