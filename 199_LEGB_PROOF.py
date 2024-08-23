v = 10 # ten 
def f1(): 
    v = 100 # hundred 
    def f2(): 
        v = 1000 # thousand 
        def f3(): 
            v = 10000 # ten thousand 
            def f4(): 
                v = 100000 # one lac 
                print(v) 
            f4() 
        f3() 
    f2() 
f1() 
