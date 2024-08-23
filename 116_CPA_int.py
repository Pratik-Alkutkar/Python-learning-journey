class CPA_int: 
    def __init__(self, init_n:int): 
        if type(init_n) != int: 
            raise TypeError("Bad type of initializer")
        self.n = init_n 
    
    def __add__(self, other): 
        n_sum = self.n + other.n 
        sum_object = CPA_int(n_sum)
        return sum_object

n1 = CPA_int(10)
n2 = CPA_int(20)
n3 = n1 + n2 # n1+n2 == CPA_int.__add__(n1, n2)