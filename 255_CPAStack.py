"""
@Goal:This package implements a class CPAStack. 
@Author: Pratik 
"""

class CPAStack: 
    """
    This class implements a stack (LIFO type) using Python built in list 
    internally. 

    __init__(self): Constructor. Does not accept any initialization data 
    push(self, element:int): Pushes given element on stack 
    pop(self)->int: Removes and returns last pushed element. 
    top(self)->int: Returns last pushed element without removing it from stack 
    is_empty(self)->bool: True if stack is empty 
    clear(self)->Drop all elements from stack 
    """

    def __init__(self): 
        self.L = [] 

    def push(self, element:int)->None: 
        if type(element) != int: 
            raise TypeError("Data to be pushed must be of type int")
        self.L.append(element)

    def top(self)->int:
        if self.is_empty(): 
            raise ValueError("Cannot top from empty stack")
        return self.L[-1]

    def pop(self)->int: 
        if self.is_empty(): 
            raise ValueError("Cannot pop from empty stack")
        last_element = self.L[-1]
        del self.L[-1]
        return last_element 
    
    def is_empty(self)->bool: 
        return len(self.L) == 0 
    
    def clear(self): 
        self.L.clear() 

print("THIS WILL BE PRINTED FIRST")

if __name__ == '__main__': 
    print("UNIT TEST START")
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

    print("UNIT TEST END")