# 1) Inner functions 
# 2) Sibling functions of L and E 

# example of rule 1 

def f(): 
    print(n) 
    def g(): 
        n = 500 
    g() 
f() 

# examples of rule 2 
# 1 
def f(): 
    print(n) 

def g(): 
    n = 500 

# 3 

def f(): 
    def g1(): 
        n = 500 

    def g2(): 
        print(n)

# 4 

def f(): 
    def g1(): 
        def h1(): 
            n = 6000 
        def h2(): 
            print(n)

    def g2(): 
        n = "Hello"

def k(): 
    n = 1.1