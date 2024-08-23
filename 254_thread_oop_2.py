import threading 
import time 
import sys 
import random 

gnum = 0 

class cpaThread(threading.Thread): 
    def __init__(self, thread_id): 
        threading.Thread.__init__(self)
        self.thread_id = thread_id 

    def run(self):
        global gnum 
        l_num = 0 
        while True: 
            l_num += 1 
     
            gnum += 1 
            print("thread_id={}, gnum={}, l_num={}".format(self.thread_id, gnum, l_num))

            time.sleep(random.randint(1, 4))

def main(): 
    th1 = cpaThread(1)
    th2 = cpaThread(2)
    th1.start() 
    th2.start() 
    th1.join() 
    th2.join() 
    sys.exit(0) 

main()