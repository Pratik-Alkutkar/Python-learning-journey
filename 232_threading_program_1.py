import sys 
import _thread 
import time 

def f3(): 
    print("Thread 1 function 3")
    time.sleep(1)

def f2(): 
    print("Thread 1 function 2")
    time.sleep(2)
    f3()

def f1(): 
    print("Thread 1 entry point function")
    time.sleep(1)
    f2()

def g3(): 
    print("Thread 2 function 3")
    time.sleep(2)

def g2(): 
    print("Thread 2 function 2")
    time.sleep(1)
    g3() 

def g1(): 
    print("Thread 2 entry point function")
    time.sleep(1)
    g2()

def main(): 
    print("Main thread of execution started by the OS")
    
    print("Main thread:Creating Thread 1")
    _thread.start_new_thread(f1, ())
    print("Main thread:Starting thread 2")
    _thread.start_new_thread(g1, ())

    i = 0 
    while i < 15: 
        print("Main thread : blocking for other threads to terminate")
        time.sleep(1)
        i = i + 1 
    print("Main thread:exiting:application:exiting")

    sys.exit(0) 

main()