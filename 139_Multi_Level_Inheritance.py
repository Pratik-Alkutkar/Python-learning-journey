class B1: 
    def __init__(self): 
        print("In B1.__init__()")
        print("Returning from B1.__init__()")

    def f1(self): 
        print("In B1.f1()")
        print("Returning from B1.f1()")

    def f2(self): 
        print("In B1.f2()")
        print("Returning from B1.f2()")

class B2(B1): 
    def __init__(self): 
        print("In B2.__init__()")
        B1.__init__(self)
        print("Returning from B2.__init__()")
    
    def g1(self): 
        print("In B2.g1()")
        print("Returning from B2.g1()")

    def g2(self): 
        print("In B2.g2()")
        print("Returning from B2.g2()")

# Multi-level inheritance 
class D(B2): 
    def __init__(self): 
        print("In D.__init__()")
        B2.__init__(self)
        print("Returning from D.__init__()")

    def h1(self): 
        print("In D.h1()")
        print("Returning from D.h1()")

    def h2(self): 
        print("In D.h2()")
        print("Returning from D.h2()")

def main(): 
    print("Creating object of type D")
    objD = D() # D constructor -> B2 constructor -> B1 constructor 
    objD.h1() 
    objD.h2() 
    objD.g1() 
    objD.g2() 
    objD.f1() 
    objD.f2()

main()


# Employee <---- Manager <---- HR_Manager 