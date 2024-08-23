"""
@goal: 
To implement meta-class and to verify the hook position 
of meta-class as learnt in theory. 
"""

class MyMeta(type): 
    def __new__(cls, cls_name, cls_bases, cls_dict): 
        print("start of metaclass hook")
        print("cls_name:", cls_name)
        print("Base classes names:")
        for c in cls_bases: 
            print(c.__name__)
        print("Class attributes:")
        for name in cls_dict: 
            print(name)
        print("end of metaclass hook")
        return type.__new__(cls, cls_name, cls_bases, cls_dict)
    
class B1: pass 
class B2: pass 

class D(B1, B2, metaclass=MyMeta): 
    a = 10 
    s = "Hello"
    def __init__(self, init_n): 
        self.n = init_n 
    def getn(self): 
        return self.n 
    def setn(self, new_n): 
        self.n = new_n

print("type(D):",type(D)) # class __main__.MyMeta 
