# Lower Triangular Matrix - diagonal (excluded)

L = [10, 20, 30, 40, 50]

print("While version")

i = 0 
while i < len(L): 
    j = 0 
    while j < i: 
        print("Index Pair:(%d,%d)" % (i, j))
        print("Element Pair:(%d,%d)" %(L[i], L[j]))
        print("*" * 30)
        j = j + 1 
    print("-" * 60)
    i = i + 1 

print("For version")
for i in range(len(L)): 
    for j in range(0, i): 
        print("Index Pair:(%d,%d)" % (i, j))
        print("Element Pair:(%d,%d)" %(L[i], L[j]))
        print("*" * 30)
    print("-" * 60)