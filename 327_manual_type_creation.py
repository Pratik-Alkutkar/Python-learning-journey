"""
@goal: 

class Test: 
    def __init__(self, init_n): 
        self.n = init_n 
    def getn(self): 
        return self.n 
    def setn(self, newn): 
        self.n = newn 

# client 
t = Test(100)
n = t.getn()
print("n:", n)
t.setn(200)
n = t.getn()
print("n:", n)
"""

cls_name = 'Test'           # Class name in string format
cls_bases = (object, )      # Tuple containing immediate base classes 
# Body of class as a string object 
cls_body = """              
def __init__(self, init_n): 
    self.n = init_n 
def getn(self): 
    return self.n 
def setn(self, newn): 
    self.n = newn 
"""
# Empty dictionary, which will be later populated by 
# the symbol tables of class 
cls_dict = {} 

print("Before exec():cls_dict:", cls_dict)
exec(cls_body, globals(), cls_dict)
print("After exec():cls_dict:", cls_dict)

"""
Execution of header of class statement 
== 
Exection of its body
"""

"""
To create an object of class type using 'call operator' 
around class name 'type' we need three initialization 
parameters. 
1) class name : str 
2) Base classes tuple : tuple 
3) Class namespace (or symbol table of class) : dict
"""

Test = type(cls_name, cls_bases, cls_dict)

# client 
t = Test(100)
print("type(t):", type(t))
n = t.getn()
print("n:", n) # 100 
t.setn(200)
n = t.getn()
print("n:", n) # 200 