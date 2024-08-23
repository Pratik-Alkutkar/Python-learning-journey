import sys 
import random 

def create_stack(): 
    return [] 

def push(stack:list, element:int)->None: 
    if type(stack) != list or type(element) != int: 
        raise TypeError 
    stack.append(element)

def top(stack:list)->int:
    if type(stack) != list: 
        raise TypeError 
    if len(stack) == 0: 
        raise ValueError("Cannot top from empty stack")
    return stack[-1]

def pop(stack:list)->int: 
    if type(stack) != list: 
        raise TypeError 
    if len(stack) == 0: 
        raise ValueError("Cannot top from empty stack")
    last_element = stack[-1]
    del stack[-1]
    return last_element

def is_empty(stack:list)->bool: 
    if type(stack) != list: 
        raise TypeError 
    return len(stack) == 0 

def clear(stack:list)->None: 
    if type(stack) != list: 
        raise TypeError 
    stack.clear() 

def main(): 
    S = create_stack() 
    
    if is_empty(S): 
        print("Stack is empty just after its creation")
    
    try: 
        n = pop(S)
    except (TypeError, ValueError): 
        print("Cannot pop the empty stack")

    try: 
        n = top(S)
    except (TypeError, ValueError): 
        print("Cannot top the empty stack")

    for i in range(5): 
        n = random.randint(1, 100)
        print("Pushing {} on stack".format(n))
        push(S, n)
        print("Pushed {} successfully".format(n))
    
    if not is_empty(S): 
        print("Stack is not empty now")

    n = top(S) 
    print("Last pushed element:", n)

    while is_empty(S) != True: 
        n = pop(S) 
        print("Poped element:", n)
    
    sys.exit(0) 

main()