import os 
import sys 

def parent_logic(): 
    pass 

def child_logic(): 
    pass 

def main(): 
    x = os.fork() 
    if x == -1: 
        print("Process creating failed. exiting...") 
        sys.exit(-1) 

    if x == 0: 
        child_logic() 
    else: 
        parent_logic()

    common_logic() # will be executed twice 

    sys.exit(0) # both processes (parent & child) will be termined by this 

main() 

