import sys 

def my_decorator(F): 
    def inner_function(p, q): 
        print("PREPROCESSING")
        ret = F(p, q)
        print("POSTPROCESSING")
        return ret 
    return inner_function

def my_add(x:int, y:int)->int: 
    print("my_add():start")
    if type(x) != int: 
        raise TypeError 
    if type(y) != int: 
        raise TypeError 
    print("my_add():leave")
    return x + y 

my_add = my_decorator(my_add)
#---------------------------------------------------------------------
def main(): 
    ret = my_add(100, 200)
    print("ret:", ret)

    ret = my_add(500, 600)
    print("ret:", ret)

    sys.exit(0)

main()


