class Base: 
    def __init__(self): 
        print("In Base.__init__()")
        print("Returning from Base.__init__()")

    # Inheriter method: This method will not be 
    # implemented in derived class and yet will be 
    # callable on derived object 
    def f(self): 
        print("In Base.f()")
        print("Returning from Base.f()")

    # This method will be overrideen by derived class 
    # i.e. will be reimplemented by derived class. 
    # While re-implmenting its own version Derived.g() 
    # will call Base.g() thus extending the logic of Base.g()
    def g(self): 
        print("In Base.g()")
        print("Returning from Base.g()")

    # This method will be overrideen by derived class 
    # i.e. will be reimplemented by derived class 
    # while reimplementing its version, derived class 
    # will totally new definition without any reference to 
    # Base version of function f 
    def h(self): 
        print("In Base.h()")
        print("Returning from Base.h()")

class Derived(Base): 
    def __init__(self): 
        print("In Derived.__init__()")
        Base.__init__(self)
        print("Returning from Derived.__init__()")

    # Derived.g() -> overridden method for extender purpose 
    def g(self): 
        print("In Derived.g()")
        Base.g(self)
        print("Returning from Derived.g()")

    # Derived.h() -> overridden method for replacor purpose 
    def h(self): 
        print("In Derived.h()")
        print("Returning from Derived.h()")

    # Derived class specific function 
    # Derived Class = Base class + extra behaviour 
    # methods such as k() capture the notion of 
    # extra behaviour 
    def k(self): 
        print("In Derived.k()")
        print("Returning from Derived.k()")

def main(): 
    D = Derived() 
    print("Calling inheriter D.f()")
    D.f() # Calling Inheriter. 
    print("Calling extender D.g()")
    D.g() # Calling extender.
    print("Calling replacer D.h()")
    D.h() # Calling replacer. 
    print("Calling derived speicific function D.k()")
    D.k() # Calling derived specific method 

main() 