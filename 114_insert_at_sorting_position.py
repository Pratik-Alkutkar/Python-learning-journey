"""
@Goal: 
A non-empty list of integers is given whose 
all but last elements are sorted. 

Write a code to fully sort the list
"""

L = [10, 20, 30, 40, 50 ,60, 70, 80, 25]

"""
L is a non-empty list of integers whose all 
elements are sorted except the last one. 

Goal: To bring L in sorted order. 
YOU ARE NOT ALLOWED TO CREATE ANY TEMPORARY LIST
YOU ARE NOT ALLOWED TO USE BUILT IN FUNCTION SORT
"""

"""
HINT: 
    Assign last element to tmp variable. 
    Travel the list from second last element 
    to the first element in the reverse order. 

    If the current element is greater than the last 
    element (stored in tmp variable) then shift the current 
    element to the next position and continue with loop. 

    If the current element is less than or equal to 
    the last element (accessible through tmp variable)
    then STOP and write tmp element to the next index (than 
    that of current)

    If you fall out of valid index range then 
    assign tmp to 0 index. 
"""

def insert_at_sorting_pos(L:list)->list: 
    """
    input: L: Non-empty list of integers whose all 
    but last element are sorted. 
    output: Sorted list 
    """
    key = L[-1] 
    j = len(L)-2
    while j > -1 and L[j] > key: 
        L[j+1] = L[j] 
        j = j - 1
    L[j+1] = key 
    return L 

def main(): 
    L = [10, 20, 30, 40, 50, 60, 70, 25]
    print("Before:L:", L)
    L = insert_at_sorting_pos(L)
    print("After L:", L)

    L = [10, 20, 30, 40, 50, 60, 70, 5]
    print("Before:L:", L)
    L = insert_at_sorting_pos(L)
    print("After L:", L)

main()