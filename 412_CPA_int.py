# 1 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __add__(self, other): 
        tmp_n = self.n + other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __sub__(self, other): 
        tmp_n = self.n - other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __mul__(self, other): 
        tmp_n = self.n * other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __floordiv__(self, other): 
        tmp_n = self.n // other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __truediv__(self, other): 
        return self.n / other.n 
    
    def __mod__(self, other): 
        tmp_n = self.n % other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __and__(self, other): 
        tmp_n = self.n & other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __or__(self, other): 
        tmp_n = self.n | other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __xor__(self, other): 
        tmp_n = self.n ^ other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __neg__(self): 
        tmp_n = -self.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __lshift__(self, k:int):
        tmp_n = self.n << k 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __rshift__(self, k:int): 
        tmp_n = self.n >> k 
        new_obj = CPA_int(tmp_n)
        return new_obj
    
    def __lt__(self, other): 
        return self.n < other.n 
    
    def __le__(self, other): 
        return self.n <= other.n 
    
    def __gt__(self, other): 
        return self.n > other.n 
    
    def __ge__(self, other):
        return self.n >= other.n 
    
    def __eq__(self, other): 
        return self.n == other.n 
    
    def __ne__(self, other): 
        return self.n != other.n 
    
    def __str__(self): 
        return str(self.n)
    
    __repr__ = __str__

n1 = CPA_int(20)
n2 = CPA_int(3)
rs1 = n1 + n2 
rs2 = n1 - n2 
rs3 = n1 * n2 
rs4 = n1 // n2 
rs5 = n1 / n2 
rs6 = n1 % n2 
rs7 = n1 & n2 
rs8 = n1 | n2 
rs9 = n1 ^ n2 
rs10 = -n1

b1 = n1 < n2 
b2 = n1 <= n2 
b3 = n1 > n2 
b4 = n1 >= n2 
b5 = n1 == n2 
b6 = n1 != n2 

# 2 
class CPA_int: 
    def __init__(self, init_n):
        self.n = init_n 

    def __add__(self, other): 
        tmp_n = self.n + other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __sub__(self, other): 
        tmp_n = self.n - other.n 
        new_obj = CPA_int(tmp_n) 
        return new_obj 
    
    def __mul__(self, other):
        tmp_n = self.n * other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __floordiv__(self, other): 
        tmp_n = self.n // other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __truediv__(self, other): 
        return self.n / other.n 
    
    def __mod__(self, other): 
        tmp_n = self.n % other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __and__(self, other): 
        tmp_n = self.n & other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __or__(self, other): 
        tmp_n = self.n | other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __xor__(self, other): 
        tmp_n = self.n ^ other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __not__(self): 
        tmp_n = ~self.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __neg__(self): 
        tmp_n = -self.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __lshift__(self, k:int): 
        tmp_n = self.n << k 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __rshift__(self, k:int): 
        tmp_n = self.n >> k 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __lt__(self, other): 
        return self.n < other.n 
    
    def __le__(self, other): 
        return self.n <= other.n 
    
    def __gt__(self, other): 
        return self.n < other.n

    def __ge__(self, other): 
        return self.n >= other.n 
    
    def __eq__(self, other): 
        return self.n == other.n 
    
    def __ne__(self, other): 
        return self.n != other.n 
    
    def __str__(self): 
        return str(self.n)
    
    __repr__ = __str__ 

n1 = CPA_int(20)
n2 = CPA_int(3)
rs1 = n1 + n2 
rs2 = n1 - n2 
rs3 = n1 * n2 
rs4 = n1 // n2 
rs5 = n1 % n2 
rs6 = n1 / n2 
rs7 = n1 & n2 
rs8 = n1 | n2 
rs9 = n1 ^ n2 
rs10 = ~n1 
rs11 = -n1 
rs12 = n1 << n2 
rs13 = n1 >> n2 
b1 = n1 < n2 
b2 = n1 <= n2 
b3 = n1 > n2 
b4 = n1 >= n2 
b5 = n1 == n2 
b6 = n1 != n2 

# 3 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __add__(self, other): 
        tmp_n = self.n + other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __sub__(self, other): 
        tmp_n = self.n - other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __mul__(self, other): 
        tmp_n = self.n * other.n 
        new_obj = CPA_int(tmp_n) 
        return new_obj 
    
    def __floordiv__(self, other): 
        tmp_n = self.n // other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __mod__(self, other): 
        tmp_n = self.n % other.n 
        new_obj = CPA_int(tmp_n) 
        return new_obj 
    
    def __truediv__(self, other): 
        return self.n / other.n 
    
    def __and__(self, other): 
        tmp_n = self.n & other.n 
        new_obj = CPA_int(tmp_n) 
        return new_obj 
    
    def __or__(self, other): 
        tmp_n = self.n | other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __xor__(self, other): 
        tmp_n = self.n ^ other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __not__(self):
        tmp_n = ~self.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __neg__(self): 
        tmp_n = -self.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __lshift__(self, k:int): 
        tmp_n = self.n << k 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __rshift__(self, k:int): 
        tmp_n = self.n >> k 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __lt__(self, other): 
        return self.n < other.n 
    
    def __le__(self, other): 
        return self.n <= other.n 
    
    def __ge__(self, other): 
        return self.n >= other.n 
    
    def __gt__(self, other): 
        return self.n > other.n 
    
    def __eq__(self, other): 
        return self.n == other.n 
    
    def __ne__(self, other): 
        return self.n != other.n 
    
    def __str__(self): 
        return str(self.n)
    
    __repr__ = __str__ 

n1 = CPA_int(20)
n2 = CPA_int(3) 
rs1 = n1 + n2 
rs2 = n1 - n2 
rs3 = n1 * n2 
rs4 = n1 // n2 
rs5 = n1 % n2 
rs6 = n1 / n2 
rs7 = n1 & n2 
rs8 = n1 | n2 
rs9 = n1 ^ n2 
rs10 = ~n1 
rs11= -n2 
rs12 = n1 << 2 
rs13 = n1 >> 4 

b1 = n1 < n2 
b2 = n1 <= n2 
b3 = n1 > n2 
b4 = n1 >= n2 
b5 = n1 == n2 
b6 = n1 != n2 
