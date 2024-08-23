# globals() function can be used to access global symbol table 
# in any sc ope 

print(globals().keys())
p = 1.1 
q = 2.2 
r = 3.3 
print(globals().keys())

def func(): 
    print("In func")
    print("func:", globals().keys())
    def inner_func(): 
        print("In inner func")
        print("inner_func:", globals().keys())
    inner_func() 
func() 

class T: 
    a = 100 
    b = 200 
    print("In T:", globals().keys())

print(globals().keys())
