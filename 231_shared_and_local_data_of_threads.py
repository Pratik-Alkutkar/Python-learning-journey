import sys 
import _thread 
import time 

gnum = 0 

def thread_func(thread_id:int)->None: 
    global gnum 
    print("Thread {} start".format(thread_id))
    i = 0   # thread entry point function 
            # all functions that are called from it 
            # local variables -> PER THREAD : ONE COPY 
            # global variables -> SHARED AMONGST ALL THREADS 
    while i < 5: 
        gnum += 1 
        i += 1 
        print("Thread with ID:{}:gnum={}:i={}".format(thread_id, gnum, i))
    print("Thread {} end".format(thread_id))

def main(): 
    _thread.start_new_thread(thread_func, (1, ))
    _thread.start_new_thread(thread_func, (2, ))
    time.sleep(5)

    sys.exit(0)

main()