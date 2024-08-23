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
    
    def __iadd__(self, other): 
        print("n1 += n2 support")
        self.n += other.n 
        return self 
    
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
    
    def __isub__(self, other): 
        print("n1 -= n2 support")
        self.n -= other.n 
        return self 

    def __mul__(self, other): 
        print("n1 * n2 support")
        n_mul = self.n * other.n 
        mul_object = CPA_int(n_mul)
        return mul_object 
    
    def __imul__(self, other): 
        print("n1 *= n2 support")
        self.n *= other.n 
        return self 
    
    def __floordiv__(self, other): 
        print("n1 // n2 support")
        q = self.n // other.n 
        n_quo = CPA_int(q)
        return n_quo
    
    def __ifloordiv__(self, other): 
        print("n1 //= n2 support")
        self.n //= other.n 
        return self 
    
    def __mod__(self, other): 
        print("n1 % n2 support")
        r = self.n % other.n 
        remainder_object = CPA_int(r)
        return remainder_object

    def __imod__(self, other): 
        print("n1 %= n2 support")
        self.n %= other.n 
        return self 

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
    
    def __itruediv__(self, other): 
        print("n1 /= n2 support")
        return self.n / other.n 

    def __pow__(self, other): 
        print("n1 ** n2 support")
        n_pow = self.n ** other.n 
        power_object = CPA_int(n_pow)
        return power_object 
    
    def __ipow__(self, other): 
        print("n1 **= n2 support")
        self.n **= other.n 
        return self 

    def __lshift__(self, other): 
        print("n1 << n2 support")
        return CPA_int(self.n << other.n)
    
    def __ilshift__(self, other): 
        print("n1 <<= n2 support")
        self.n <<= other.n 
        return self 
    
    def __rshift__(self, other): 
        print("n1 >> n2 support")
        return CPA_int(self.n >> other.n)
    
    def __irshift__(self, other): 
        print("n1 >>= n2 support")
        self.n >>= other.n 
        return self 
    
    def __and__(self, other): 
        print("n1 & n2 support")
        return CPA_int(self.n & other.n)
    
    def __iand__(self, other): 
        print("n1 &= n2 support")
        self.n &= other.n 
        return self 

    def __or__(self, other): 
        print("n1 | n2 support")
        return CPA_int(self.n | other.n)
    
    def __ior__(self, other): 
        print("n1 |= n2 support")
        self.n |= other.n 
        return self 

    def __xor__(self, other): 
        print("n1 ^ n2 support")
        return CPA_int(self.n ^ other.n)
    
    def __ixor__(self, other): 
        print("n1 ^= n2 support")
        self.n ^= other.n 
        return self 

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

n1 = CPA_int(100)
n2 = CPA_int(104)
bit_and = n1 & n2 
bit_or = n1 | n2 
bit_xor = n1 ^ n2 

print("bit_and:", bit_and)
print("bit_or:", bit_or)
print("bit_xor:", bit_xor)

n1 = CPA_int(20)
n2 = CPA_int(7)
n1 += n2    # CPA_int.__iadd__(n1, n2) self==n1, other.n2 
            # Under CPA_int.__iadd__ 
            # self.n += other.n     n1.n += n2.n 
            # retrn self            return n1  
print("n1:", n1)

n1 = CPA_int(20)
n2 = CPA_int(7)
n1 -= n2 
print("n1:", n1)

n1 = CPA_int(20)
n2 = CPA_int(7)
n1 *= n2 
print("n1:", n1)

n1 = CPA_int(20)
n2 = CPA_int(7)
n1 //= n2 
print("n1:", n1)

n1 = CPA_int(20)
n2 = CPA_int(7)
n1 %= n2 
print("n1:", n1)

n1 = CPA_int(20)
n2 = CPA_int(7)
n1 /=n2 
print("n1:", n1)

n1 = CPA_int(20)
n2 = CPA_int(7)
n1 <<= n2 
print("n1:", n1)

n1 = CPA_int(20)
n2 = CPA_int(7)
n1 >>= n2 
print("n1:", n1)

n1 = CPA_int(20)
n2 = CPA_int(7)
n1 &= n2 
print("n1:", n1)

n1 = CPA_int(20)
n2 = CPA_int(7)
n1 |= n2 
print("n1:", n1)

n1 = CPA_int(20)
n2 = CPA_int(7)
n1 ^= n2 
print("n1:", n1)