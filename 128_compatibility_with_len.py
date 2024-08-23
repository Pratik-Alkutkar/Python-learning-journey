class ArrayInt: 
    def __init__(self, size:int): 
        if type(size) != int: 
            raise TypeError("Bad type for array size")
        if size < 0: 
            raise ValueError("Bad value for array size")
        self.L = [] 
        for i in range(size): 
            self.L.append(0)

    def get_length(self): 
        return len(self.L)
    
    def __len__(self): 
        return len(self.L)

    
A = ArrayInt(8)
n = A.get_length()
print("n:", n)

B = ArrayInt(10)
n = len(B)
print("n==len(B):", n)