import sys 

class Test: 
    def __init__(self, init_m: int, init_n: int): 
        if type(init_m) != int: 
            raise TypeError 
        if type(init_n) != int: 
            raise TypeError 
        self.m = init_m 
        self.n = init_n 

    def __getattribute__(self, attr_name: str): 
        if attr_name == '__dict__': 
            return object.__getattribute__(self, attr_name)
        elif attr_name == 'n': 
            return self.__dict__['n'] ** 2 
        else: 
            return self.__dict__[attr_name]
        
    def __setattr__(self, attr_name: str, rhs: int): 
        if type(rhs) != int: 
            raise TypeError 
        self.__dict__[attr_name] = rhs 

    def __delattr__(self, attr_name: str): 
        if attr_name == 'n': 
            raise AttributeError("Cannot remove attribute 'n' from object")
        else: 
            del self.__dict__[attr_name]

t = Test(10, 20)
print("t.m:{}, t.n:{}".format(t.m, t.n))
t.m = 15 
t.n = 25 
print("t.m:{}, t.n:{}".format(t.m, t.n))

print(t.__dict__)
del t.m 
print(t.__dict__)
try: 
    del t.n 
except: 
    exc_name, exc_data, _ = sys.exc_info() 
    print(exc_name, exc_data) 

