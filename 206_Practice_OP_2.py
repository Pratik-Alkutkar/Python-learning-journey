# Program 3
def f(): 
    def g(): 
        print("g:N:", N)
    N = 100 
    g() 
f()

# Program 4 
def f(): 
    def g(): 
        print("g:N:", N)
    g() 
    N = 100 
f() 

# Program 5 
def f(): 
    N = 100 
    def g(): 
        print("g:N:", N)
    g() 
    del N 
f() 

# Program 6
def f(): 
    N = 100 
    def g(): 
        print("g:N:", N)
    del N 
    g()
f()