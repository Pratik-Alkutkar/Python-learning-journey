L = [10, 20, 30, 40, 50]
# Pattern 1: Generate all pairs. 
# Every element in L must be paired 
# with every other element in L 

print("while version ")

i = 0 
while i < len(L): 
    j = 0 
    while j < len(L): 
        print("Index Pair:(%d,%d)" % (i, j))
        print("Element Pair:(%d, %d)" % (L[i], L[j]))
        print("*******")
        j = j + 1 
    print("-" * 60)
    i = i + 1 

print("for version")

for i in range(len(L)): 
    for j in range(len(L)): 
        print("Index Pair:(%d,%d)" % (i, j))
        print("Element Pair:(%d, %d)" % (L[i], L[j]))
        print("*" * 30)
    print("-" * 60)


