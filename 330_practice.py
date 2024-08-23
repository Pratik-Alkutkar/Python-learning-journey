"""
class Test: 
    a = 10 
    L = [100, 200, 300]
    s = "Hello"
    def __init__(self, init_m, init_n): 
        self.m = init_m 
        self.n = init_n 
    def getn(self): 
        return self.n 
    def getm(self): 
        return self.m 
    def setn(self, n): 
        self.n = n 
    def setm(self, m): 
        self.m = m 

# expected symbol table 
{
    'a': 10, 
    'L': [100, 200, 300], 
    's': "Hello", 
    '__init__': <function object>, 
    'getn': <funcrtion object>, 
    'getm': <function object>, 
    'setn': <function object>, 
    'setm': <function object>
}
"""

cls_body = """
a = 10 
L = [100, 200, 300]
s = "Hello"
def __init__(self, init_m, init_n): 
    self.m = init_m 
    self.n = init_n 
def getn(self): 
    return self.n 
def getm(self): 
    return self.m 
def setn(self, n): 
    self.n = n 
def setm(self, m): 
    self.m = m 
"""

cls_dict = {} 
print("Befor exec():cls_dict:", cls_dict)
exec(cls_body, globals(), cls_dict)
print("After exec():cls_dict:", cls_dict)