def merge(L:list, p:int, q:int, r:int)->None: 
    """
    @L: Input list
    @p, @q, @r: Indices satisfying the following properties: 
    P1) 0 <= p <= q < r 
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

    # L1 = L[p:q+1]
    cnt = 0 
    while cnt < n1: 
        L1.append(L[p+cnt])
        cnt += 1 

    # L2 = L[q+1:r+1]
    cnt = 0 
    while cnt < n2: 
        L2.append(L[q+1+cnt])
        cnt += 1 

    print("L1:{}, L2:{}".format(L1, L2))

def main(): 
    L = [-1, 45, 67, 10, 20, 30, 40, 50, 5, 15, 25, 45, 47, 55, -56, 76] 
    p = L.index(10)
    q = L.index(50)
    r = L.index(55)
    merge(L, p, q, r)

main() 

"""
Let n1 and n2 be integers such that n1 < n2
We have to count total number of integers between n1 and n2. 
But the question arises whether or not to include n1 and n2 themselves. 

This gives rise to four combinations: 

1) include both n1 and n2: denoted by : [n1, n2] : closed interval
    n2 - n1 + 1 
2) include n1 and exclude n2: denoted by : [n1, n2) : semi open / semi closed interval 
    n2 - n1 
3) exclude n1 and incluide n2: denoted by : (n1, n2] : semi open / semi closed 
    n2 - n1 
4) Exclude both n1 and n2: denoted by : (n1, n2) : open interval 
    n2 - n1 - 1  
"""