def outer(): 
    m = 100 
    n = 200
    print("outer():locals():", locals()) 
    def inner(): 
        print("In inner()")
        print("inner():locals():", locals())
        print(n)
    inner() 
outer() 