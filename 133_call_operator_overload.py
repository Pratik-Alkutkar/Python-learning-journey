class Test: 
    pass 

print("type(Test):", type(Test)) # <class 'type'> 
t = Test() 
print("type(t):", type(t)) # <class '__main__.Test'>
try: 
    t() # TypeError: 'Test' object is not callable 
except TypeError as e: 
    print(e)

"""
Principle: If programmer wants to make object compatible with 
call operator, then its class must define a function named
__call__ 
"""

class MyClass: 
    def __init__(self): 
        print("In MyClass.__init__")
    def __call__(self): 
        print("In MyClass.__call__, will return bool")
        return True 
    
m = MyClass() # In MyClass.__init__ 
ret = m() # MyClass.__call__(m) 
print("ret:", ret)