# Program 1 

N = 100 
def f(): 
    print("1:f:N:", N)
    N = 200 
    print("2:f:N:", N)
f() 

# Program 2 
N = 100 
def f(): 
    print("1:f:N:", N)
    N = N + 1 
    print("2:f:N:", N)
f()

# Program 3 
def f(): 
    def g(): 
        print("1:g:N:", N)
    N = 100 
    g() 
f() 
#----------------------------------

def f(): 
    N = 100 
    def g(): 
        print(N)
    g() 
f() 