import sys
from typing import Any 

class B: 
    p = 500 

class C: 
    def __init__(self): 
        self.x=1.1
        self.y=2.2 
        self.z=3.3 
    
    m = 10 
    n = 20 

    def __getattribute__(self, attr_name: str) -> Any:
        print("attr_name:", attr_name)
        print("type(attr_name):", type(attr_name))
        return True 
    
def main(): 
    objC = C() 
    print(objC.x)
    print(objC.y)
    print(objC.z)
    print(objC.m) 
    print(objC.n)
    print(objC.p) 
    print(objC.q)

main()