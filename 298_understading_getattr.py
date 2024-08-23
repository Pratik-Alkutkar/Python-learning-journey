import sys 
class B: 
    p = 500 

class C(B): 
    def __init__(self): 
        self.x = 1.1 
        self.y = 2.2 
        self.z = 3.3 

    m = 10 
    n = 20 

objC = C() 

print(objC.x)
print(objC.y)
print(objC.z)
print(objC.m)
print(objC.n)
print(objC.p)

try: 
    print(objC.q)
except: 
    exc_name, exc_data, _ = sys.exc_info() 
    print(exc_name, exc_data)

print("lets retry!")

import sys 
class B: 
    p = 500 

class C(B): 
    def __init__(self): 
        self.x = 1.1 
        self.y = 2.2 
        self.z = 3.3 

    def __getattr__(self, attr_name:str): 
        print("attr_name:", attr_name)
        print("type(attr_name):", type(attr_name))
        return True 

    m = 10 
    n = 20 

objC = C() 

print(objC.x)
print(objC.y)
print(objC.z)
print(objC.m)
print(objC.n)
print(objC.p)

print(objC.q)