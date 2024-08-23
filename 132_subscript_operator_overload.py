class Array: 
    def __init__(self, size:int): 
        if type(size) != int: 
            raise TypeError("Bad type")
        if size < 0: 
            raise ValueError("Bad value")
        self.L = [] 
        for i in range(size): 
            self.L.append(0)

    def __setitem__(self, index, val): 
        """
        This method is called in response to 
        A[i] = value where A is object of class Array 
        A -> self 
        i -> index 
        value->val 
        """
        if type(index) != int: 
            raise TypeError("index must be int")
        if index < 0 or index >= len(self.L): 
            raise IndexError("index our of range")
        if type(val) != int: 
            raise TypeError("val must be integer")
        self.L[index] = val 

    def __getitem__(self, index): 
        """
        this value is called in response to 
        v = A[i] 
        where A is object of class Array
        A -> self 
        i -> index 
        """
        if type(index) != int: 
            raise TypeError("index must be int")
        if index < 0 or index >= len(self.L): 
            raise IndexError("index our of range")
        return self.L[index]
    
    def __str__(self): 
        """
        This method is called in response to 
        print(A) where A is object of class Array 
        A -> self
        """
        return str(self.L)
    
    def __len__(self): 
        """
        This method is called in response to 
        len(A) where A is object of class Array 
        A -> self
        """
        return len(self.L)
    
A = Array(8)
print("A:", A)
for i in range(len(A)): 
    A[i] = (i+1) * 1000 
print("A:", A)
for i in range(len(A)): 
    print("A[%d]:%d" % (i, A[i]))