#1 
class CPA_int: 
    def __init__(self, init_n:int): 
        self.n = init_n 

    def __add__(self, other): 
        tmp_n = self.n + other.n
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self):
        return str(self.n)
    
n1 = CPA_int(20)
n2 = CPA_int(10)
n3 = n1 + n2 
print("type(n3):{}, n3:{}".format(type(n3), n3))

#2 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 
    
    def __add__(self, other): 
        tmp_n = self.n + other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self): 
        return str(self.n) 
    
n1 = CPA_int(20) 
n2 = CPA_int(10) 
n3 = n1 + n2 
print("n3:{}, type(n3):{}".format(n3, type(n3)))

# 3 

class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __add__(self, other): 
        tmp_n = self.n + other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self): 
        return str(self.n)
    
n1 = CPA_int(20)
n2 = CPA_int(10)
n3 = n1 + n2 
print("n3:{}, type(n3):type(n3)".format(n3, type(n3)))

# 4 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 
    def __add__(self, other): 
        tmp_n = self.n + other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj
    def __str__(self): 
        return str(self.n)
    
n1 = CPA_int(20)
n2 = CPA_int(10)
n3 = n1 + n2 
print("n3:{}, type(n3):{}".format(n3, type(n3)))

# 5 
class CPA_int: 
    def __init__(self, init_n):
        self.n = init_n 

    def __add__(self, other): 
        tmp_n = self.n + other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj

    def __str__(self): 
        return str(self.n)
    
n1 = CPA_int(20)
n2 = CPA_int(10)
n3 = n1 + n2 
print("n3:{}, type(n3):{}".format(n3, type(n3)))

#---------------------------------------------------------------

#1 
class CPA_int: 
    def __init__(self, init_n):
        self.n = init_n 
    
    def __sub__(self, other): 
        tmp_n = self.n - other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self): 
        return str(self.n)
    
n1 = CPA_int(20)
n2 = CPA_int(10)
rs = n1 - n2 
print(n1, n2, rs)

# 3 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 
    def __sub__(self, other): 
        tmp_n = self.n  - other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    def __str__(self): 
        return str(self.n)
n1 = CPA_int(20)
n2 = CPA_int(10)
rs = n1 - n2 
print(n1, n2, rs)

# 4 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __sub__(self, other): 
        tmp_n = self.n - other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self): 
        return str(self.n)
    
# 5 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __sub__(self, other): 
        tmp_n = self.n - other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self): 
        return str(self.n)
    
n1 = CPA_int(20)
n2 = CPA_int(10)
n3 = n1 - n2 
print(n1, n2, n3)

#---------------------------------------------------------------

#1 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __mul__(self, other): 
        tmp_n = self.n * other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self): 
        return str(self.n)
    
n1 = CPA_int(20)
n2 = CPA_int(5)
n3 = n1 * n2 
print(n1, n2, n3)

# 2 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __mul__(self, other): 
        tmp_n = self.n * other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self): 
        return str(self.n)
    
n1 = CPA_int(20)
n2 = CPA_int(5)
rs = n1 * n2 
print(n1, n2, rs)

# 3 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __mul__(self, other): 
        tmp_n = self.n * other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self): 
        return str(self.n)
    
n1 = CPA_int(10)
n2 = CPA_int(5)
n3 = n1 * n2 
print(n1, n2, n3)

# 4 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __mul__(self, other): 
        tmp_n =  self.n * other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self): 
        return str(self.n)
    
n1 = CPA_int(20)
n2 = CPA_int(5)
n3 = n1 * n2 
print(n1, n2, n3)

# 5 
class CPA_int: 
    def __init__(self, init_n):
        self.n = init_n 

    def __mul__(self, other): 
        tmp_n = self.n * other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self): 
        return str(self.n)

n1 = CPA_int(29)
n2 = CPA_int(5)
n3 = n1 * n2 
print(n1, n2, n3)

#---------------------------------------------------------------------

#1 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __floordiv__(self, other): 
        tmp_n = self.n // other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self): 
        return str(self.n)
    
n1 = CPA_int(20)
n2 = CPA_int(3)
q = n1//n2
print(n1, n2, q)

# 2 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __floordiv__(self, other): 
        tmp_n = self.n // other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self): 
        return str(self.n)
    
n1 = CPA_int(20)
n2 = CPA_int(3)
q = n1 // n2 
print(n1, n2, q)

# 3 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 
    
    def __floordiv__(self, other): 
        tmp_n = self.n // other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self): 
        return str(self.n)
    
n1 = CPA_int(20)
n2 = CPA_int(3)
q = n1 // n2 
print(n1, n2, q)

# 4 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __floordiv__(self, other): 
        tmp_n = self.n // other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self): 
        return str(self.n)
    
n1 = CPA_int(20)
n2 = CPA_int(3)
n3 = n1 // n2 
print(n1, n2, n3)

#5 
class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __floordiv__(self, other): 
        tmp_n = self.n // other.n 
        new_obj = CPA_int(tmp_n)
        return new_obj 
    
    def __str__(self): 
        return str(self.n)
    
n1 = CPA_int(20)
n2 = CPA_int(3)
q = n1 // n2 
print(n1, n2, q)