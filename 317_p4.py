"""
Assume that a function denotes its return type by function annotation syntax. 
e.g. 

def test_func(a:int, b:int)->int: 
    # some logic 

How will you make sure that every call to test_func() in future returns an integer? 
If any particular call to test_func() does not return an integer, then flag an error. 

Afterwards solve this problem GENRALLY. (meaning that return value of a function 
could be anything.)

Technique: Decorator: Decorate a function and put a validity chec 
in post processing fragment. 
"""

def return_type_checker(F): 
    def inner_function(*args, **kwargs): 
        ret = F(*args, **kwargs)
        print("Return type checking of:{}".format(F.__name__))
        if 'return' not in F.__annotations__.keys(): 
            print("The function does not specify any particular return type")
        else: 
            if type(ret) != F.__annotations__['return']: 
                print("Function claims to return {} but returns {}".format(
                    F.__annotations__['return'].__name__, 
                    type(ret).__name__
                ))
        return ret 
    return inner_function

@return_type_checker  
def test_func_1(a:int, b:int)->int: 
    assert type(a) == int and type(b) == int, "TypeError"
    return a + b 

@return_type_checker        
def test_func_2(a:int, b:int)->int: 
    assert type(a) == int and type(b) == int, "TypeError"
    return (a + b)/2.0

@return_type_checker 
def test_func_3(a, b): 
    return a + b 

ret = test_func_1(100, 200)
ret = test_func_2(5, 8)
ret = test_func_3(5, 8) 
