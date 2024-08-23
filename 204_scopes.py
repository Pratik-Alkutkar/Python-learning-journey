gn = 10                         # global 
def f1():                       # global 
    n1 = 100                    # local wrt f1() 
    print("In f1")              # local wrt f1() 
    def f2():                   # local wrt f1() 
        n2 = 1000               # local wrt f2(), enclosing of f1() 
        print("In f2")          # local wrt f2(), enclosing of f1()
        def f3():               # local wrt f2(), enclosing of f1()
            n3 = 10000          # local wrt f3(), enclosing of f1(), enclosing of f2()
            print("In f3")      # local wrt f3(), enclosing of f1(), enclosing of f2() 
        f3()                    # local wrt f2(), enclosing of f1()
        print(n2)               # local wrt f2(), enclosing of f1() 
    f2()                        # local wrt f1()
    print(n1)                   # local wrt f1()
print(gn)                       # global
f1()                            # global