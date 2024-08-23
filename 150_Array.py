class Array: 
    def __init__(self, size:int): 
        if type(size) != int: 
            raise TypeError("Bad type for size")
        if size < 0: 
            raise ValueError("Bad value for size")
        self.L = [] 
        for x in range(size): 
            self.L.append(0)
        self.log_file_name = "exception.log" 
        f_handle = open(self.log_file_name, "w")
        f_handle.close() 
    
    def __getitem__(self, index): 
        try: 
            return self.L[index]
        except: 
            f_handle = open(self.log_file_name, "a")
            print("Exception occurred in __getitem__", file=f_handle)
            f_handle.close() 
            raise 
    
    def __setitem__(self, index, val): 
        self.L[index] = val 

    def __str__(self):
        return str(self.L)
    
def main(): 
    A = Array(5)
    print(A[0]) # A[0] == A.__getitem__(0) == Array.__getitem__(A, 0)
    print(A[1])
    print(A[2])
    print(A[3])
    print(A[4])
    print(A[8])

main()