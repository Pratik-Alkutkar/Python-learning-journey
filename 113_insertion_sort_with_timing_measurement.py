import sys, random, time 

def insertions_sort(L): 
    k = 1 
    while k < len(L): 
        key = L[k]
        j = k - 1 
        while j > -1 and L[j] > key: 
            L[j+1] = L[j]
            j = j - 1 
        L[j+1] = key 
        k = k + 1 

def main(argc, argv): 
    if argc != 2: 
        print("Usage Error: %s number_of_elements" % argv[0])
        sys.exit(-1)

    N = int(argv[1])
    if N <= 0: 
        print("Number of elements must be positive")
        sys.exit(-1)


    # L = [random.randint(0, 10000000) for i in range(N)]

    L = []   
    for i in range(N): 
        num = random.randint(0, 100000000)
        L.append(num)

    start_time = time.time() 
    insertions_sort(L)
    end_time = time.time() 
    delta = end_time - start_time 
    print("insertion sort for input size %d took %f seconds" % (N, delta))


main(len(sys.argv), sys.argv)
