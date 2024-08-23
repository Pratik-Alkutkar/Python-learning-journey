def f1(): 
    def f2(): 
        def f3(): 
            nonlocal N 
            N = 500 
        f3() 
    f2() 
f1()