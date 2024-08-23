"""
@author: Pratik Pramod Alkutkar
@goal: To write attribute management code using 
    i) __getattr__ (ii) __setattr__ (iii) __delattr__ 

    Name of attribute to be managed: 'n' 
    1) obj.n on RHS should return square of n 
    2) obj.n on LHS should reassign n 
    3) del obj.n should raise an exception that 'n' cannot be removed for object

    Rest of the attributes are not managed. Therefore, we will take additional 
    attribute 'm' in object to show that it has default behvaiour in all three cases. 
"""

import sys 

class Test: 
    def __init__(self, init_n: int, init_m: int): 
        if type(init_n) != int: 
            raise TypeError("Bad type for initial value of n")
        if type(init_m) != int:
            raise TypeError("Bad type for initial value of m")
        self.n = init_n # Test.__setattr__(self, 'n', init_n)
        self.m = init_m # Test._setattr__(self, 'm', init_m)

    def __getattr__(self, attr_name: str): 
        if attr_name == 'n': 
            return self.__dict__['_n'] ** 2
        else: 
            raise AttributeError("Object of Test has not attribute {}".format(attr_name)) 

    def __setattr__(self, attr_name: str, rhs: int): 
        if type(rhs) != int: 
            raise TypeError("Must reassign an integer")

        if attr_name == 'n': 
            self.__dict__['_n'] = rhs
        else: 
            self.__dict__[attr_name] = rhs
    
    def __delattr__(self, attr_name: str): 
        if attr_name == 'n': 
            raise AttributeError("Cannot remove attribute 'n'")
        else: 
            del self.__dict__[attr_name]


t = Test(7, 100)
print(t.__dict__)
t.x = 500
print(t.__dict__)
t.n = 11
print(t.__dict__)

print(t.m)
print(t.n)
try: 
    print(t.y)
except: 
    exc_name, exc_data, _ = sys.exc_info() 
    print(exc_name, exc_data)

print(t.__dict__) # {'_n':11, 'm':100, 'x':500}
del t.m 
print(t.__dict__) # {'_n':11, 'x':500}
del t.x 
print(t.__dict__) # {'_n':11}
try: 
    del t.n 
except: 
    exc_name, exc_data, _ = sys.exc_info() 
    print(exc_name, exc_data)
print(t.__dict__) # {'_n':11}

"""
print(t.n)
t.n = 11 
print(t.n)
try: 
    del t.n 
except: 
    exc_name, exc_data, _ = sys.exc_info() 
    print(exc_name, exc_data)
"""