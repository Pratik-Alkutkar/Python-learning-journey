"""
Interview Question:
    
Let L be a list of integers.
Modify L as follows:
    1) All even numbers must be prefix by 'E'
    2) All odd numbers must be prefixed by 'O'

L = [10, 15, 25, 30, 40, 50]

L = ['E', 10, 'O', 15, 'O', 25, 'E', 30, 'E', 40, 'E', 50]
"""

import sys

def main():
    L = [10, 15, 25, 30, 40, 50]
    print("BEFORE:", L)
    i = 0
    while i < len(L):
        c = None
        if L[i] % 2 == 0:
            c = 'E'
        else:
            c = 'O'
        L.insert(i, c)
        i = i + 2
    print("AFTER:", L)
    sys.exit(0)

main() 