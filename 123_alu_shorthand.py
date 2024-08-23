class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __add__(self, other): 
        print("__add__")
        return CPA_int(self.n + other.n)
    
    def __iadd__(self, other): 
        print("__iadd__")
        self.n += other.n 
        return self 

    def __str__(self): 
        return str(self.n)
    

n1 = CPA_int(20) 
n2 = CPA_int(7)

n3 = n1 + n2 
print("n3:", n3)

n1 += n2  # n1 = n1 + n2 
print("n1:", n1)