def outer(): 
    N = 500 
    def inner(): 
        N = 600 
    print("Outer:N:", N)
    inner()
    print("Outer:N:", N)
outer()