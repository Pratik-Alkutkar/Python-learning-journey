class B1: 
    def __init__(self): 
        print("In B1.__init__()")
        print("Return:B1.__init__()")

    """
    def func(self): 
        print("In B1.func()")
        print("Return:B1.func()")
    """

class B2: 
    def __init__(self): 
        print("In B2.__init__()")
        print("Return:B2.__init__()")

    """
    def func(self): 
        print("In B2.func()")
        print("Return:B2.func()")
    """
    
class D(B1, B2): 
    def __init__(self): 
        print("In D.__init__()")
        B1.__init__(self)
        B2.__init__(self)
        print("Return:D.__init__()")

    """
    def func(self): 
        print("In D.func()")
        print("Return:D.func()")
    """

def main(): 
    objD = D() 
    print("D.__mro__:", D.__mro__)
    objD.func()

main() 