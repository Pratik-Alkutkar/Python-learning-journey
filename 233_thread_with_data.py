import sys 
import _thread 
import time 

def thread_entry(lst:list, s:str)->None: 
    print("Programmatically created thread")
    print("thread:printing data sent by the parent thread")
    for x in lst: 
        print("thread:lst:", x)
    for c in s: 
        print("thread:s:", c)
    
def main(): 
    print("Main thread of execution started by OS")
    _thread.start_new_thread(thread_entry, ([10, 20, 30], "Hello"))
    time.sleep(5)
    print("Main thread:terminating:Application:Terminating")

main()
