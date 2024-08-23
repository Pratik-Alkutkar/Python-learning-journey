import sys 
import os 
import time 

def main(): 
    print("Parent Process Start") 
    print("Creating a new Process")
    x = os.fork() 
    if x == -1: 
        print("Creation of new process failed") 
        sys.exit(-1) 

    if x == 0: 
        while True: 
            print("Child Process:pid={}, ppid={}".format(os.getpid(), os.getppid()))
            time.sleep(1) 
    else: 
        while True: 
            print("Parent Process:pid={}, ppid={}".format(os.getpid(), os.getppid()))
            time.sleep(1) 

    sys.exit(0) 

main() 
