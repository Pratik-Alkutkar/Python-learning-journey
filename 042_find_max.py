'''
@Author: Pratik Pramod Alkutkar
@Date: 11th Jan 23 
@Goal: To demonstrate: 
        unhandled exception due to error by caller 
'''

def find_max(L:list) -> int: 
    m = L[0]
    i=1 
    while i < len(L): 
        if L[i] > m: 
            m = L[i]
        i = i + 1 
    return m 

L1 = [10, 20, 30, 40, 50]
m1 = find_max(L1)
print("Max in L1 is", m1)

L2=[]
m2 = find_max(L2)