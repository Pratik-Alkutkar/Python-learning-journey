class array: 
    def __init__(self, N:int): 
        self.L = [0 for i in range(N)]

    def __setitem__(self, index, val): 
        self.L[index] = val 

    def __getitem__(self, index): 
        return self.L[index]
    
    def __str__(self): 
        return str(self.L) 
    
    def __len__(self): 
        return len(self.L)
    
    def __contains__(self, element): 
        return element in self.L 
    
    __repr__ = __str__ 

A = array(5)
print(A)
for i in range(len(A)):
    A[i] = (i+1) * 10 
print(A) 
for i in range(len(A)): 
    print("A[%d]:%d" % (i, A[i]))
print("len(A)=%d" % len(A))

print("20 in A:", 20 in A)
print("-200 in A:", -200 in A)

# v = A[i]
# v = A.__getitem__(i)
# v = array.__getitem__(A, i)

# A[i] = rhs 
# A.__setitem__(i, rhs)
# array.__setitem__(A, i, rhs)