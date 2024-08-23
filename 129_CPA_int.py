class CPA_int: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __add__(self, other): 
        """
        other-> CPA_int 
        other-> int
        """
        result_object = CPA_int(0)
        if type(other) == CPA_int: 
            result_object.n = self.n + other.n 
        elif type(other) == int: 
            result_object.n = self.n + other 
        else: 
            raise TypeError("second param must be CPA_int or int type")
        return result_object 

    def __iadd__(self, other): 
        self.n += other.n 
        return self 
    
    def __radd__(self, x:int):
        print("In __radd__()") 
        print("type(self):", type(self))
        print("type(x):", type(x))
        result_object = CPA_int(0)
        result_object.n = self.n + x 
        return result_object 

    def __str__(self): 
        return str(self.n)
    
def main(): 
    n1 = CPA_int(20)
    n2 = CPA_int(10) 
    n3 = n1 + n2    # CPA_int.__add__ 
    print("n3:", n3) # 30 
    n1 += n2        # CPA_int.__iadd__ 
    print("n1:", n1) # 30 

    m = CPA_int(40)
    print("m:", m)
    k = m + 30  # m:CPA_int, 30:int, k:CPA_int 
    print("k:", k)
    print("type(k):", type(k))
#-------------------------------------------------
    print("main():Doing 50 + m")
    y = 50 + m  # m + 50

main() 

"""
n1 + n2 
n1: CPA_int 
n2: CPA_int 

n1 += n2 

n1: CPA_int 
n2: CPA_int 

We have added support for adding two CPA_int objects. 

Now we will add a support to add CPA_int and int object. 

n1 = CPA_int(40)
n2 = 30 

n1: CPA_int (user defined class)
n2: int (built in class)

n1 + n2 
CPA_int + int 


"""