import os
import sys 

def main(): 
    print("My Pid = {}".format(os.getpid())) 
    print("My Parent Process ID = {}".format(os.getppid())) 

    x = os.fork() 

    print(os.getpid(), "This will be executed TWO TIMES") 

    sys.exit(0) 

main() 

"""
1) How to invoke another program through Python script? 
2) How to invoke another Python script through your Python script? 
3) How to invoke another program/another Python script through your 
    Python script and redict(catch) its output as a string/byte string? 
4) How to do it using low level functions? 
5) How to do it using a subprocess package? 
"""

