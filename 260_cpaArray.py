class cpaArray_iterator: 
    def __init__(self, G): 
        self.G = G 

    def __next__(self): 
        return self.G.__next__()

class cpaArray: 
    def __init__(self, size:int): 
        if type(size) != int: 
            raise TypeError 
        if size < 0: 
            raise ValueError 
        self.L = [0 for n in range(size)]

    def __setitem__(self, index_or_slice, rhs_element): 
        self.L[index_or_slice] = rhs_element 

    def __getitem__(self, index_or_slice): 
        if type(index_or_slice) == int: 
            return self.L[index_or_slice]
        tmpL = self.L[index_or_slice]
        A = cpaArray(0)
        A.L = tmpL 
        return A 
    
    def __iter__(self): 
        def get_generator(L:list): 
            for x in L: 
                yield x 
        return cpaArray_iterator(get_generator(self.L))
    
    def __len__(self): 
        return len(self.L)

    def __str__(self): 
        return str(self.L)
    
    __repr__ = __str__ 

def main(): 
    A = cpaArray(10)
    for i in range(len(A)): 
        A[i] = (i+1) * 100 
    print("A:", A) 
    for i in range(len(A)): 
        print("A[{}]:{}".format(i, A[i]))
    print("Iteration")
    for x in A: 
        print(x) 

main()
