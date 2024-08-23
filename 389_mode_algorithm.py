import math 
math.inf

def cpa_mode(X)->any: 
    if '__iter__' not in dir(type(X)): 
        print("Input must be an interable object")
        return None 
    D = {}
    for elem in X: 
        n = D.setdefault(elem, 0)
        D[elem] += 1
    [key, val] = [None, -math.inf] 
    for (k, v) in D.items(): 
        if v > val: 
            [key, val] = [k, v]
    print(D)
    return key 

lst = [1.1, 3.4, 7.8, 6.5, 2.3, 9.9, 3.4, 1.1, 1.1, 7.8, 3.4, 3.4, 11.32, 3.4]
md = cpa_mode(lst)
print(md)