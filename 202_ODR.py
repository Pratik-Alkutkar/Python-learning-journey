# Theory: Every scope has its own symbol table. 
# A variable name can be defined only once in a given scope. 
# If a variable name is defined in other scope and attached to 
# some object, but the same variable name has not been used 
# in the current scope then you can create current scope 
# specific version of the variable name. 

N = 100     # N will be created in global scope 

def f(): 
    # f() being a function has its own symbol table 
    # N is not defined in f() yet though it is defined 
    # in other (=global) scope. 
    # According to ODR I have right to define every variable 
    # name exactly once in all scopes 
    # therefore, I can create 'N' which is local to f() 
    N = 500.500 
    print("f:N:", N) # local N of f() will be printed 
f() 
print("global:N:", N) # global N will be printed 

# One N is int and another N is float 
# It is a proof that there are two copies of N 
# belonging to 2 different symbol tables 
# and therefore, can have two different values 
# even of two different types! 

# One Definition Rules: also states that variable name can be defined 
# only once in any given scope. This is automatically guaranteed by 
# Python assignment statement algorithm 

# To create any varialbe or to DEFINE any variable in any scope 
# it must be used in LHS sense for the first time. 

# If you reuse the variable name on LHS then it is not considered 
# to be a defintion but a CASE OF RE-ASSIGNMENT. 

# Python will simply replace the object associated with variable 
# name with the current RHS object 

def f(): 
    N = 100 # N is being used on LHS for the first time 
            # therefore, this statement is definition N in scope of f() 

    print(N) 
    N = 500 # This is a resue of variable name N, that is N is being used on LHS 
            # for the second time. Therefore, according to assignment statement 
            # algorithm it is a case of re-assignment 
            # where in, address of int object 100 will be replaced by int object 500 
            # in local symbol table of f(). RC of int object 100 will be decremented by 1 
            # Garbage collector (GC) will be involed if it has fallen down to 0 
            # RC of int object 500 will be incremented by 1 
            # No second copy of N can be created in symbol table of f() 

            # There is easier way to understand this. 
            # Symbol tables are dictionaries and all variable names defined in the given scope 
            # are stored as keys in the symbol table and keys cannot be repeated in dictionary 
            # therefore, a variable name cannot appear twice in given scopes symbol table (= dict)
            # Thus, ODR is automatically followed in Python 

# non-trivial examples 

def f(): 
    # g is used on LHS for the first time in f() 
    # therefore, g and address of function object 
    # will be stored in local symbol table of f() 
    def g(): 
        print("Version 1")

    # g is reused on LHS in the scope of f() 
    # therefore, g will give up existing function object 
    # (version 1) and g will be attached with another 
    # function object (version 2)
    # two copies of g WILL NOT be created in scope of f() 
    # This makes us understand why function overloading is not supported by Python (only for C++ programmers)
    def g(): 
        print("Version 2")

def f(): 
    # g is used in LHS sense for the first time 
    # as g is used with def, g will bind with object of type function 
    # This is definition of g in scope of f() 
    def g(): 
        print("In func g")
    # g is resued in scope of f() 
    # therefore, it will not re-defined. 
    # In symbol table of f(), id of function object associated with g() 
    # will be replaced by id of int object 500 
    # RC of function object will be decremented by 1. If becomes zero, clear it with GC 
    # RC of int object 500 will be incremented by 1 
    g = 500 

# -------------------------------------

def f(): 
    # myType is used in LHS sense for the first time in the scope of f 
    # therefore, myType will be created in local symbol table of f() 
    # As myType is used with class statement, it will bind with object 
    # of class type 
    class myType: 
        print("In class myType")

    # existing type object will be replaced by new type object 

    class myType: 
        print("Second version of class ")


def f(): 
    class myType: 
        print("In class myType")

    # myType is a local variable of f(), pointing of object of class type 

    myType = 1.1 

    # myType will leave its association with type object 
    # and will bind itself with float object 1.1 

    # that is it is no longer a data type. 
    