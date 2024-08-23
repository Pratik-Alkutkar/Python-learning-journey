"""
To overload every binary operator for following: 
Let * be a binary operator. 

result = operand_1 * operand_2 
operand_1 *= operand_2 

result = operand_1 + x  # x is object of some other type 
result = x + operand_1 

CPA_int + CPA_int
CPA_int += CPA_int 
CPA_int + int 
int + CPA_int 
"""

class CPA_int: 
    def __init__(self, init_n): 
        if type(init_n) != int: 
            raise TypeError("Bad type for initialisation data")
        self.n = init_n 

    def __str__(self): 
        return str(self.n)
    
    __repr__ = __str__

    def __add__(self, other): 
        """
        CPA_int + CPA_int 
        CPA_int + int 
        """
        print("__add__")
        result_object = CPA_int(0)
        if type(other) == CPA_int: 
            result_object.n = self.n + other.n 
        elif type(other) == int: 
            result_object.n = self.n + other 
        else: 
            raise TypeError("Bad operand type")
        return result_object 
    
    def __iadd__(self, other): 
        """
            CPA_int += CPA_int
        """
        print("__iadd__")
        self.n += other.n 
        return self 
    
    def __radd__(self, other): 
        """
        int + CPA_int 
        """
        print("__radd__")
        if type(other) != int: 
            raise TypeError("Bad type for operand")
        result_object = CPA_int(0)
        result_object.n = self.n + other 
        return result_object 
    
def main(): 
    n1 = CPA_int(20)
    n2 = CPA_int(7)
    print("n1:", n1)
    print("n2:", n2)
    
    n3 = n1 + n2 # __add__
    n1 += n2 # __iadd__
    n4 = n2 + 30 # __add__ 
    n5 = 500 + n2 # __radd__
    print("n3==n1+n2:", n3)
    print("n1:after n1+=n2:", n1)
    print("n4:(CPA_int + int)", n4)
    print("n5(int + CPA_int):", n5)

main()