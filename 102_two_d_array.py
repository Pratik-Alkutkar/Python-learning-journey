import sys 

def prn_all_evens(L:list):
    """
    approach: 
        Let (i, j) be any valid pair of indices 
        in two D array. 

        if L[i][j] % 2 == 0: 
            print(L[i][j], "is an even number")        
    """

    for i in range(len(L)): 
        for j in range(len(L[i])): 
            if L[i][j] % 2 == 0: 
                print(i, j, L[i][j], 'is an even number')

def main():

    L = [

        [10, 20, 30, 40, 50], 
        [-34, 12, 65, 11, 21], 
        [14, 51, 22, -32, -44], 
        [11, 23, -11, -25, 38], 
        [41, 28, 47, 35, -17]
    ]

    for i in range(len(L)): 
        for j in range(len(L[i])): 
            print(i, j, L[i][j])

    print("Printing all evens")
    prn_all_evens(L)

    sys.exit(0)

main()