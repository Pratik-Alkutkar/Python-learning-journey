import os 
import sys 
import time 

def main(): 
    pid = os.fork() 
    if pid == -1: 
        print("Creation of new process failed") 
        sys.exit(-1) 

    if pid == 0: 
        # Logic of the child process 
        for i in range(5): 
            print("Child:Doing work") 
            time.sleep(1) 
    else: 
        # Logic of the parent process 
        print("Parent:Just created a new child") 
        print("Parent:I will block until the child terminates") 
        os.wait() 
        print("Parent:The child has terminated, I will now contnue") 

    sys.exit(0) 

main() 
