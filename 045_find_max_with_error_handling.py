'''
@author: Pratik Pramod Alkutkar
@date: 12th Jan 23 
@goal: To demonstrate: 
        detection of error by function definition writer 
'''

import sys 

def find_max(L:list)->int: 
    if type(L) != list: 
        raise TypeError("Input must be list")

    if len(L) == 0: 
        raise ValueError("Empty list is given")
       
    for x in L: 
        if type(x) != int: 
            raise TypeError("List contains non-integer data")
           
    m = L[0]
    i=1 
    while i < len(L): 
        if L[i] > m: 
            m = L[i]
        i = i + 1 
    return m 

L1 = [] 

try: 
    ret = find_max(L1)
    print("ret:", ret)
except TypeError as e: 
    print(e) 
except ValueError as e: 
    print(e) 
except: 

L2 = [10, 20, 30, "Hello", 40, 4.34]   
try: 
    ret = find_max(L2)
    print("ret:", ret)
except TypeError as e: 
    print(e) 
except ValueError as e: 
    print(e) 

print("my life continues")
