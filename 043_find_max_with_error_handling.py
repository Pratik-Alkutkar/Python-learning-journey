'''
@Author: Pratik Pramod Alkutkar
@Date: 11th Jan 23 
@Goal: To demonstrate: 
        detection of error by function definition writer 
'''

def find_max(L:list)->int: 
    if len(L) == 0: 
        print("ERROR:List is empty")
        return None 
    
    for x in L: 
        if type(x) != int: 
            print("ERROR:List contains non-integer data")
            return None 

    m = L[0]
    i=1 
    while i < len(L): 
        if L[i] > m: 
            m = L[i]
        i = i + 1 
    return m 

L1 = [] 
ret = find_max(L1)
print("ret:", ret)

L2 = [10, 20, 30, "Hello", 40, 4.34]
ret = find_max(L2)
print("ret:", ret)