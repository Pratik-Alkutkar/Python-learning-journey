def f(): 
    L = [] 
    print("In f():id(L):", id(L))
    return L 

ret_1 = f() 
print("ret_1:{}, id(ret_1):{}".format(ret_1, id(ret_1)))
ret_2 = f() 
print("ret_2:{}, id(ret_2):{}".format(ret_2, id(ret_2)))
ret_3 = f() 
print("ret_3:{}, id(ret_3):{}".format(ret_3, id(ret_3)))

#--------------------------------------------------------------

def outer(): 
    def inner(): 
        print("Inside inner function")
    print("Inside outer():id(inner):", id(inner))
    return inner 

X1 = outer() 
print("global:id(X1):", id(X1))

X2 = outer() 
print("global:id(X2):", id(X2))

X3 = outer() 
print("global:id(X3):", id(X3))

X1() # Inside inner function
X2() # Inside inner function
X3() # Inside inner function

