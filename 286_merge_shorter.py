def merge(L:list, p:int, q:int, r:int)->None: 
    """
    @L: Input list
    @p, @q, @r: Indices satisfying the following properties: 
    P1) 0 <= p <= q < r < len(L)
    P2) L[p...q] (pythonwise: L[p:q+1]) and 
        L[q+1...r] (pythonwise: L[q+1:r+1]) are SORTED 
    @output: L[p...r] (pythonwise) L[p...r+1] is SORTED 

    Mathematically: subarray 1: range: 
    [p, q] 
    Length = q - p + 1

    subarray 2: (q, r]      
    Length = r - q
    """
    L1, L2 = L[p:q+1],  L[q+1:r+1]
    i,j,k=0,0,0 
    while True: 
        if L1[i] <= L2[j]: 
            L[p+k] = L1[i] 
            i += 1
            k += 1 
            if i == len(L1): 
                L[p+k : r+1] = L2[j : ]
                break 
        else: 
            L[p+k] = L2[j]
            j += 1 
            k += 1 
            if j == len(L2): 
                L[p+k : r+1] = L1[i : ]
                break  

def main(): 
    L = [-1, 45, 67, 10, 20, 30, 40, 50, 5, 15, 25, 45, 47, 55, -56, 76] 
    p = L.index(10)
    q = L.index(50)
    r = L.index(55)
    print("Before Merge:", L)
    merge(L, p, q, r)
    print("After Merge:", L)

main() 