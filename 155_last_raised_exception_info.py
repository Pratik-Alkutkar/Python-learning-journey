import sys 
import random 
import traceback 

def h(): 
    n = random.randint(1, 3) 
    if n == 1: 
        raise NameError("Undefined Name")
    elif n == 2: 
        raise TypeError("Bad type")
    elif n == 3: 
        raise ValueError("Bad value")
    
def g(): 
    h() 

def f(): 
    g() 

def main():
    try:  
        f() 
    except: 
        T = sys.exc_info()
        print("EXCEPTION NAME:")
        print(T[0])

        print("EXCEPTION DATA:")
        print(T[1])

        print("TRACEBACK INFO:")
        traceback.print_tb(T[2])

    print("EXCEPTION SUCCESSFULLY HANDLED...CONTINUING WITH CODE")
main()

