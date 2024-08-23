# Pattern 7: All pairs exception diagonal 

L = [10, 20, 30, 40, 50]

i = 0 
while i < len(L): 
    j = 0 
    while j < len(L): 
        if i != j: 
            print("Index Pair:(%d,%d)" % (i, j))
            print("Element Pair:(%d, %d)" % (L[i], L[j]))
            print("*******")
        j = j + 1 
    print("-" * 60)
    i = i + 1 

print("for version")

for i in range(len(L)): 
    for j in range(len(L)): 
        if i != j: 
            print("Index Pair:(%d,%d)" % (i, j))
            print("Element Pair:(%d, %d)" % (L[i], L[j]))
            print("*" * 30)
    print("-" * 60)