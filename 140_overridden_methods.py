class Base:
    def f(self): 
        print("In Base.f()")

class D1(Base): 
    # overridden method -> extender 
    def f(self): 
        print("D1.f() logic start")
        Base.f(self)
        print("D1.f() furthter logic")
        print("D1.f() ends")

class D2(Base):
    # overridden method -> replacer  
    def f(self): 
        print("D2.f() logic")
        print("D2.f() logic ends")

d1 = D1() 
d2 = D2() 

d1.f() # D1.f is extender 
d2.f() # D2.f is a replacer 