import threading 
import time 

class cpaThread(threading.Thread): 
    def __init__(self, thread_id, data): 
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.data = data 
    # this function will be called by threading 
    # package once .start() method is called 
    # on cpaThread object 
    def run(self): 
        print("Child thread is running")
        i = 0 
        while i < 10: 
            print("Thread id={} Thread data={} doing work!".format(self.thread_id, self.data))
            time.sleep(1)
            i = i + 1 
        print('Child thread is exiting')

def main(): 
    print("main thread start")
    th1 = cpaThread(1, [200, 300])
    th1.start()
    print("main thread block until child thread exit")
    th1.join() 
    print("main thread exit")

main()