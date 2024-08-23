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
        exc_name, exc_data, exc_tb = sys.exc_info()
        print("EXCEPTION NAME:", exc_name)
        print("EXCEPTION DATA:", exc_data)
        print("EXCEPTION TRACEBACK")
        traceback.print_tb(exc_tb)

    print("EXCEPTION SUCCESSFULLY HANDLED...CONTINUING WITH CODE")
main()

"""
If you are not interested in tracebak 

exc_name, exc_data, _ = sys.exc_info()

traceback.print_tb(_)


"""