def f1(): 
    N = 500 
    def f2(): 
        N = "Hello"
        def f3(): 
            x = 100 
            def f4():
                nonlocal N # which N? 
                N = 1.1 
            f4() 
        print("f2():Before call to f3():N:", N)  # "Hello"
        f3()
        print("f2():After call to f3():N:", N)  # 1.1 
    print("f1():Before call to f2():N:", N) # 500
    f2() 
    print("f1():After call to f2():N:", N) # 500 
f1()  