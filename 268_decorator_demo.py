import sys 

def my_decorator(F): 
    def inner_function(p, q): 
        print("PREPROCESSING") # LOGIC 
        ret = F(p, q)
        print("POSTPROCESSING") # LOGIC 
        return ret 
    return inner_function

@my_decorator
def my_add(x, y): 
    print("my_add():start")
    if type(x) != int: 
        raise TypeError 
    if type(y) != int: 
        raise TypeError 
    print("my_add():leave")
    return x + y 

#---------------------------------------------------

def main(): 
    ret = my_add(100, 200)
    print("ret:", ret)

    ret = my_add(400, 500)
    print("ret:", ret)

    sys.exit(0)
    
main()

