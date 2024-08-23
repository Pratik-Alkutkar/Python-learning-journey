"""
@Goal: To take a list of integers from user. 
Divide the list in all possible contiguous parts. (number of parts = 2)
Find max in each part.  
"""

import sys 
import random 

def get_list_of_integers(min_elements:int, max_elements:int)->list: 
    if type(min_elements) != int: 
        raise TypeError("bad type")
    if type(max_elements) != int: 
        raise TypeError("Value elements")
    if min_elements < 0 or max_elements <= 0: 
        raise ValueError("Bad range")
    if min_elements >= max_elements: 
        raise ValueError("Bad range")
    nr_elements = random.randint(min_elements, max_elements+1)
    L = [] 
    i = 0 
    while i < nr_elements: 
        L.append(int(input("Enter element at index %d:" % i)))
        i = i + 1 
    return L 

def partitioning_with_max(L:list)->None: 
    if type(L) != list: 
        raise TypeError("Bad type")

    i = 0 
    while i < len(L)-1:
        
        print("Part I index range:(%d,%d)" % (0, i))
        print("Part II: index range:(%d,%d)" % (i+1, len(L)-1))
        
        max_1 = L[0]
        j = 1 
        while j <= i: 
            if L[j] > max_1: 
                max_1 = L[j]
            j = j + 1

        max_2 = L[i+1]
        j = i + 2 
        while j < len(L): 
            if L[j] > max_2: 
                max_2 = L[j]
            j = j + 1

        print("Max in Part (%d,%d) = %d" % (0, i, max_1))
        print("Max in Part (%d,%d) = %d" % (i+1, len(L)-1, max_2))

        i = i + 1 

def main(): 
    min_expected_elements = 5 
    max_expected_elements = 15
    L = get_list_of_integers(min_expected_elements, max_expected_elements)
    partitioning_with_max(L)
    sys.exit(0)

main() 