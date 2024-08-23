# do usual validation checks and follow python coding style 

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

L = [28, 2, 33, 45, 12, 3, 5, 1]
print("Before sort:L:", L)
insertions_sort(L)
print("After sort:L:", L)
