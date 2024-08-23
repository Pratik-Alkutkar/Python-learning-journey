import sys 
import random 

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
    n1 = q-p+1
    n2 = r-q
    i, j, k, cnt = 0, 0, 0, 0 
    L1 = []
    L2 = [] 

    cnt = 0 
    while cnt < n1: 
        L1.append(L[p+cnt])
        cnt += 1 

    cnt = 0 
    while cnt < n2: 
        L2.append(L[q+1+cnt])
        cnt += 1 

    while True: 
        if L1[i] <= L2[j]: 
            L[p+k] = L1[i]
            i += 1 
            k += 1 
            if i == n1: 
                while j < n2: 
                    L[p+k] = L2[j]
                    j += 1
                    k += 1 
                break 
        else: 
            L[p+k] = L2[j]
            j += 1 
            k += 1 
            if j == n2: 
                while i < n1: 
                    L[p+k] = L1[i]
                    i += 1 
                    k += 1 
                break 

def merge_sort(L:list, p:int, r:int):
    assert type(L) == list, "TypeError"
    assert type(p) == int and type(r) == int, "TypeError"
    if p < r: 
        q = (p + r) // 2
        merge_sort(L, p, q)
        merge_sort(L, q+1, r)
        merge(L, p, q, r)
    
def main(argc:int, argv:list)->None: 
    if argc != 2: 
        print("UsageError:Correct Usage:{} number_of_elements".format(argv[0]))
        sys.exit(-1)
    
    try: 
        N = int(argv[1])
    except: 
        print("Bad format for integer")
        sys.exit(-1)
    
    if N <= 0: 
        print("Bad value for array size")
        sys.exit(-1)
    
    min_element = 0 
    max_element = 1000000
    L = [random.randint(min_element, max_element) for i in range(N)]
    print("Before sort:")
    for i in range(len(L)): 
        print("L[{}]:{}".format(i, L[i]))
    merge_sort(L, 0, len(L)-1)
    print("After sort:")
    for i in range(len(L)): 
        print("L[{}]:{}".format(i, L[i]))

main(len(sys.argv), sys.argv) 