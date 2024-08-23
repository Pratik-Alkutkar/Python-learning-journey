'''
@author:    Pratik Pramod Alkutkar
@date:      2nd Feb 2023 
@goal:      To create our own version of range and slice 
            with positive step count
'''

import sys 

def cpa_range(s:str, i:int, j:int)->str: 
    '''
    cpa_range(s:str, i:int, j:int)
    @s: string object that will undergo the range operation 
    @i: starting index 
    @j: ending index 
    @output: a new string object containing characters from 
             i to j-1 if i < j 
             empty string if i >= j 
    '''

    if type(s) != str or type(i) != int or type(j) != int: 
        raise TypeError("s must be a string and i and j must be integers")

    s_result = ''
    if i < 0 or i >= len(s): 
        return s_result

    if j >= len(s): 
        j = len(s)

    '''
    if i >= j: 
        return s_result
    '''
    index = i 
    while index < j: 
        s_result = s_result + s[index]
        index = index + 1 
    return s_result

def cpa_slice(s:str, i:int, j:int, k:int)->str: 
    '''
    cpa_slice(s:str, i:int, j:int)
    @s: string object that will undergo the slice operation 
    @i: starting index 
    @j: ending index 
    @k: step count
    @output: 
        Assuming k > 0
        a new string object containing every kth character 
        from i to j-1 if i < j 

        an empty string if i >= j
    '''
    if k == 0: 
        raise ValueError("Step cannot be 0")
    if k < 0: 
        print("Negative step count is not supported by cpa_slice()")
    s_result = '' 
    '''
    if i >= j: 
        return s_result
    '''
    index = i 
    while index < j: 
        s_result = s_result + s[index]
        index = index + k 
    return (s_result)

def main(): 
    print("range testing")
    s = input("Enter a string:")
    if len(s) == 0: 
        print("Nonempty string is expected")
        sys.exit(-1)
    i = int(input("Enter starting index i for range:"))
    j = int(input("Enter ending index j for range:"))
    s_result = cpa_range(s, i, j)
    print("s_result:", s_result)

main()

