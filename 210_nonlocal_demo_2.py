def outer(): 
    N = 500 
    def inner(): 
        nonlocal N # All references of N in inner function will be bound to 
                    # outer functions N 
        N = 600 
    print("Outer():Before call to inner():N:", N) # 500 
    inner() 
    print("Outer():After call to inner():N:", N) # 600 
outer() 