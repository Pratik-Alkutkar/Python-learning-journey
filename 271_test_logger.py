from logger import logger 
from time import sleep 

@logger 
def compute_1(a, b, c): 
    return a + b + c 

@logger 
def compute_2(a, b, *args, c=100, d=200, e, f, **kwargs): 
    print("Inside Master Function")

@logger 
def compute_3(a, b, c=100, d=200, **kwargs): 
    print("Inside compute 3")
    return True 

@logger
def compute_4(n): 
    if type(n) != int: 
        raise TypeError("n must be an integer")
    if n <= 0: 
        raise ValueError("n must be positive")
    print("Positive integer n:", n)

def main(): 

    compute_1(100, 200, 300)
    sleep(1) 
    compute_2(1, 2, *('a', 'b', 'c'), d=[4, 7, 9], e={100, 200}, f="Hello", u=1.1, w=2.2, z=3.3)
    sleep(2)
    compute_1(100, c=300, b=200)
    sleep(1)
    compute_3(a=500, b=600, d=-200, x='abc', y='pqr')
    sleep(2)
    compute_1(a=1.1, b=2.2, c=3.3)
    compute_3(101.4534, 564.32, c=235.25, d=57.235, k=[1000, 200, 300], s=('g', 'h', 'q'))
    sleep(3)
    try: 
        compute_4(100.100)
    except: 
        pass 
    sleep(1)
    try: 
        compute_4(-100)
    except: 
        pass 
    sleep(1) 
    try: 
        compute_4(500)
    except: 
        pass 
    
main()