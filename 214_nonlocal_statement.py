"""
case i): If one of the nested functions (inner function) wants to modify 
         enclosing functions (outer function's) local variable then 
         nonlocal statement must be used. 

def outer(): 
    N = 500 
    def inner(): 
        print(N) # Note that nonlocal statement is not required if 
                 # outer functions local variable is to be used on RHS 
                 # LEGB will take care of that  
    inner() 
outer()

Say the inner function wants to write a statement which will cause 
reassignment of N in outer function 

def outer(): 
    N = 500 
    def inner(): 
        N = 600     # This statement will not modify outer functions N 
                    # but will simply create a local N in inner functions 
                    # symbol table 
    inner() 
outer() 

def outer(): 
    N = 500 
    def inner(): 
        N = N + 1   # This will not only will not modify outer functions N but will also result 
                    # in UnboundLocalError 
    inner() 
outer() 

Soln : Declare N to be nonlocal in inner function by the following statement 
nonlocal N 
nonlocal is a keyword as well as the statement. 
It requires at least one variable name following it. 
More than one variable can be declared to be nonlocal 
Simply put them in comma separated list after the keyworld nonlocal 
nonlocal v 
nonlocal v1, v2, ..., vn 

nonlocal MUST BE USED inside def statement 
and logically it MUST BE USED inside the nested def statement 

def outer(): 
    N = 500 
    def inner(): 
        nonlocal N # This will direct Python interpreter to bind all 
                    # references to 'N' in inner function to outer 
                    # functions N 
                    # If there are more than one outer functions then 
                    # first function in inner to outer order having 
                    # N, will be chosen 
        N = 600     # outer functions N will be reassigned from 500 to 600 
    print(N) # 500 
    inner() 
    print(N) # 600 
outer() 
"""