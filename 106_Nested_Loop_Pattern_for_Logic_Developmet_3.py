# Upper triangular matrix - Diagonal 

L = [10, 20, 30, 40, 50]

print("While version")

i = 0 
while i < len(L): 
    j = i + 1 
    while j < len(L): 
        print("Index Pair:(%d,%d)" % (i, j))
        print("Element Pair:(%d,%d)" % (L[i], L[j]))
        j = j + 1 
        print("*" * 30)
    print("-" * 60)
    i = i + 1

print("For version")

for i in range(len(L)): 
    for j in range(i+1, len(L)): 
        print("Index Pair:(%d,%d)" % (i, j))
        print("Element Pair:(%d,%d)" % (L[i], L[j]))
        print("*" * 30)
    print("-" * 60)
        
