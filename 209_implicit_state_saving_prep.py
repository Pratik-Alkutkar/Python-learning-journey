def outer(): 
    N = 100 
    def inner(): 
        print("Inside inner():N:", N)
    return inner 

func = outer() 
print("global")
func()


def outer(): 
    N = 100 
    def inner():
        print("Inside inner():N:", N)
    inner() 
outer() 