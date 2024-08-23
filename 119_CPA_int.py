import sys 

class CPA_int: 
    def __init__(self, init_n:int): 
        if type(init_n) != int: 
            raise TypeError("Bad type")
        self.n = init_n 

    def __add__(self, other): 
        """
        note for understanding: 
        type(self) == CPA_int
        type(other) == CPA_int 

        type(self.n) == int (built in)
        type(other.n) == int (built in)
        type(n_sum) == int (built in)

        type(summation_object) == CPA_int
        """
        print("n1 + n2 support")
        n_sum = self.n + other.n
        summation_object = CPA_int(n_sum)
        return summation_object
    
    def __sub__(self, other): 
        """
        note for understanding: 
        type(self) == CPA_int 
        type(other) == CPA_int 
        type(self.n) == int (built in)
        type(other.n) == int (built in) 
        type(n_sub) == int (built in)
        type(subtraction_object) == CPA_int
        """
        print("n1 - n2 support")
        n_sub = self.n - other.n 
        subtraction_object = CPA_int(n_sub)
        return subtraction_object 

    def __mul__(self, other): 
        print("n1 * n2 support")
        n_mul = self.n * other.n 
        mul_object = CPA_int(n_mul)
        return mul_object 
    
    def __floordiv__(self, other): 
        print("n1 // n2 support")
        q = self.n // other.n 
        n_quo = CPA_int(q)
        return n_quo
    
    def __mod__(self, other): 
        print("n1 % n2 support")
        r = self.n % other.n 
        remainder_object = CPA_int(r)
        return remainder_object

    def __truediv__(self, other):
        """
        note for understanding 
        addition, subtraction, multiplication, 
        quotient and remainder of two CPA_int object 
        is expected to be another CPA_int object 
        But true divsion of two CPA_int is going to return 
        an object of type float. 
        """ 
        print("n1 / n2 support")
        return self.n / other.n

    def __pow__(self, other): 
        print("n1 ** n2 support")
        n_pow = self.n ** other.n 
        power_object = CPA_int(n_pow)
        return power_object 
    
    def __str__(self): 
        return str(self.n) 

    __repr__ = __str__

n1 = CPA_int(20)
n2 = CPA_int(7)

n_sum = n1 + n2 
n_sub = n1 - n2 
n_mul = n1 * n2 
n_quo = n1 // n2 
n_remainder = n1 % n2 
f = n1 / n2 
n_pow = n1 ** n2 

print("n1:", n1) # CPA_int.__str__(n1) -> str 
print("n2:", n2)
print("Addition:", n_sum)
print("Subtraction:", n_sub)
print("Multiplication:", n_mul)
print("Quotient:", n_quo)
print("Remainder:", n_remainder)
print("True or fractional division:", f)
print("Power:", n_pow)
