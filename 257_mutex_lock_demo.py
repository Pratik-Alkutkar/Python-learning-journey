""""
@Goal: To demonstrate the guarding of critical section using the mutex lock 
@Author: Pratik 
@Commandline: 
# python mutex_lock_demo.py nr_threads log_file_path
"""

import sys 
import threading 

gnum = 0
log_file_path = None 

class cpaThread(threading.Thread): 
    mutex_lock_var = threading.Lock()

    def __init__(self, thread_id): 
        threading.Thread.__init__(self)
        self.thread_id = thread_id 
        
    def run(self): 
        """
        Common thread function for all  threads. 
        Note that cpaThread.run will be a re-entrant function
        """
        global gnum
        i = 0 
        while i < 5: 
            cpaThread.mutex_lock_var.acquire() 
            log_handle = open(log_file_path, "a")
            gnum += 1 
            print("Thread id:{}, gnum:{}".format(self.thread_id, gnum), file=log_handle, flush=True)
            log_handle.close() 
            cpaThread.mutex_lock_var.release() 
            i += 1 

def main(argc:int, argv:list)->None: 
    global log_file_path 

    if argc != 3: 
        print("UsageError:Correct Usage:{} {} {}".format(argv[0], "nr_threads", "log_file_path"))
        sys.exit(-1)

    try: 
        nr_threads = int(argv[1])
        if nr_threads < 2 or nr_threads > 25: 
            raise ValueError("2 <= nr_threads <= 25 required.")
        f_handle = open(argv[2], "w")
        f_handle.close() 
        log_file_path = argv[2]
    except: 
        exc_name, exc_data, _ = sys.exc_info() 
        print(exc_name, exc_data, sep=':')
        sys.exit(-1)

    thread_handle_list = [] 
    for i in range(nr_threads): 
        thread_handle_list.append(cpaThread(i+1))
    for thread in thread_handle_list: 
        thread.start()
    for thread in thread_handle_list: 
        thread.join()

    sys.exit(0)

main(len(sys.argv), sys.argv)
