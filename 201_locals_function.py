# locals(): Returns the symbol table of the scope from which it is called 
# Theory: Every scope has its own symbol table. 
# There is a global symbol table which is created when Python interpreter 
# is started to execute .py file 
# Every def statement and every class has its own local symbol table. 

print(locals().keys())          # prints global symbol table 
p = 1.1 
q = 2.2 
r = 3.3 
print(locals().keys())          # prints global symbol table 

def func(): 
    print("In func")
    m = 100 
    def inner_func(): 
        print("In inner_func")
        n = 500 
        print(locals().keys())  # prints symbol table of inner_func() 
    inner_func() 
    print(locals().keys())      # prints symbol table of func() 
func() 
print(locals().keys())          # prints global symbol table 