def outer(): 
    m = 100 
    n = 200
    print("outer():locals():", locals()) 
    def inner(): 
        print("In inner()")
        print("inner():locals():", locals())
        print(n)
        print(m)
    inner() 
    return inner 
func = outer() 
print("global scope")
func()

