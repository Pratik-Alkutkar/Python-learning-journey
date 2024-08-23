class B1: 
    def func(self): 
        print("In B1.func()")

class B2: 
    def func(self): 
        print("In B2.func()")

class D(B1, B2): 
    def func(self): 
        print("In D.func()")

print("B1.__mro__:", B1.__mro__)
print("B2.__mro__:", B2.__mro__)
print("D.__mro__:", D.__mro__)


class B1: pass 
class B2: pass 
class D(B1, B2): pass 

print("D.__mro__:", D.__mro__)