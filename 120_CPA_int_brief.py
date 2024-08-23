class CPA_int: 
    def __init__(self, init_n:int): 
        if type(init_n) != int: 
            raise TypeError("Bad type for initial data")
        self.n = init_n 

    def __add__(self, other): 
        """
        support for CPA_int_object_1 + CPA_int_object_2
        """
        return CPA_int(self.n + other.n)
    
    def __sub__(self, other): 
        """
        Support for CPA_int_object_1 + CPA_int_object_2
        """
        return CPA_int(self.n - other.n)