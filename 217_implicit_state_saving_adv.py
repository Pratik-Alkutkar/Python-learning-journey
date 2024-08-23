def outer(): 
    N = 100 
    M = 200 
    print("outer():locals():", locals())
    def inner(): 
        print("Inner:locals():", locals())
        print("inner():N:", N)
    inner() 
    N = 1.1 
    print("outer():locals():", locals())
    inner() 
outer()