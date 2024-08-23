import sys 
import threading 
import random 

# Server side 

class ThreadSafeStack: 
    mu_lock = threading.Lock() 
    
    def __init__(self, size:int): 
        if type(size) != int: 
            raise TypeError("Bad type for size")
        if size < 0: 
            raise ValueError("Bad size of stack")
        self.L = [None for x in range(size)] 
        self.stack_size = size 
        self.current_index = -1 

    def push(self, new_element: any) -> bool: 
        ThreadSafeStack.mu_lock.acquire() 
        if self.current_index + 1 == self.stack_size: 
            ThreadSafeStack.mu_lock.release()
            raise ValueError("Stack is full")
        self.current_index += 1 
        self.L[self.current_index] = new_element
        ThreadSafeStack.mu_lock.release() 
        return True 

    def top(self) -> any: 
        ThreadSafeStack.mu_lock.acquire()
        if self.current_index == -1: 
            ThreadSafeStack.mu_lock.release()
            raise ValueError("Stack is empty")
        tmp = self.L[self.current_index] 
        ThreadSafeStack.mu_lock.release()
        return tmp 

    def pop(self) -> any: 
        ThreadSafeStack.mu_lock.acquire()
        if self.current_index == -1: 
            ThreadSafeStack.mu_lock.release()
            raise ValueError("Stack is empty")
        tmp = self.L[self.current_index] 
        self.current_index -= 1
        ThreadSafeStack.mu_lock.release()
        return tmp 

    def is_empty(self) -> bool: 
        ThreadSafeStack.mu_lock.acquire()
        ret = (self.current_index == -1)
        ThreadSafeStack.mu_lock.release()
        return ret 

class TestThreadSafeStack(threading.Thread): 
    PUSH, POP, TOP, IS_EMPTY = range(0, 4)
    f_lock = threading.Lock()

    def __init__(self, thread_id: int, stack: ThreadSafeStack, nr_operations: int, f_handle): 
        if type(thread_id) != int: raise TypeError 
        if type(stack) != ThreadSafeStack: raise TypeError 
        if type(nr_operations) != int: raise TypeError 
        threading.Thread.__init__(self)
        self.thread_id = thread_id 
        self.nr_operations = nr_operations 
        self.stack = stack 
        self.f_handle = f_handle

    def run(self): 
        for i in range(self.nr_operations): 
            n = random.randint(1, 10000) % 4
            if n == TestThreadSafeStack.PUSH:
                try: 
                    new_element = random.randint(0, 1000)
                    ret = self.stack.push(new_element) 
                except: 
                    exc_name, exc_data, _ = sys.exc_info() 
                    TestThreadSafeStack.f_lock.acquire()
                    print(self.thread_id, "PUSH", exc_name, exc_data, sep=':', file=self.f_handle, flush=True)
                    TestThreadSafeStack.f_lock.release() 
                else: 
                    TestThreadSafeStack.f_lock.acquire()
                    print(self.thread_id, "PUSH", new_element, "SUCCESS", sep=':', file=self.f_handle) 
                    TestThreadSafeStack.f_lock.release() 
             
            elif n == TestThreadSafeStack.POP: 
                try: 
                    x = self.stack.pop()
                except: 
                    exc_name, exc_data, _ = sys.exc_info() 
                    TestThreadSafeStack.f_lock.acquire()
                    print(self.thread_id, "POP", exc_name, exc_data, sep=':', file=self.f_handle)
                    TestThreadSafeStack.f_lock.release() 
                else: 
                    TestThreadSafeStack.f_lock.acquire()
                    print(self.thread_id, "POP", x, "SUCCESS", sep=':', file=self.f_handle) 
                    TestThreadSafeStack.f_lock.release() 

            elif n == TestThreadSafeStack.TOP: 
                try: 
                    x = self.stack.top()
                except: 
                    exc_name, exc_data, _ = sys.exc_info() 
                    TestThreadSafeStack.f_lock.acquire()
                    print(self.thread_id, "TOP", exc_name, exc_data, sep=':', file=self.f_handle)
                    TestThreadSafeStack.f_lock.release() 
                else: 
                    TestThreadSafeStack.f_lock.acquire()
                    print(self.thread_id, "TOP", x, "SUCCESS", sep=':', file=self.f_handle) 
                    TestThreadSafeStack.f_lock.release() 

            elif n == TestThreadSafeStack.IS_EMPTY: 
                try: 
                    ret = self.stack.is_empty() 
                except: 
                    exc_name, exc_data, _ = sys.exc_info() 
                    TestThreadSafeStack.f_lock.acquire()
                    print(self.thread_id, "IS_EMPTY", exc_name, exc_data, sep=':', file=self.f_handle)
                    TestThreadSafeStack.f_lock.release() 
                else: 
                    TestThreadSafeStack.f_lock.acquire()
                    print(self.thread_id, "IS_EMPTY", ret, "SUCCESS", sep=':', file=self.f_handle) 
                    TestThreadSafeStack.f_lock.release() 

def main(argc, argv): 

    if argc != 4: 
        print("UsageError:%s nr_threads operations_per_thread log_file" % argv[0])
        sys.exit(-1)

    nr_threads = int(argv[1])
    assert nr_threads > 0, "Bad value for number of threads"
    operations_per_thread = int(argv[2])
    assert operations_per_thread > 0, "Bad value for number of operations"
    log_file = argv[3]

    tsf_stack = ThreadSafeStack(5)

    try: 
        log_file_handle = open(log_file, "w")
    except:
        exc_name, exc_data, _ = sys.exc_info()
        print(exc_name, exc_data, sep=':')
        sys.exit(-1)

    thread_handle_list = [] 
    for i in range(nr_threads): 
        thread_handle = TestThreadSafeStack(i+1, tsf_stack, operations_per_thread, log_file_handle)
        thread_handle_list.append(thread_handle)
    for thread in thread_handle_list: 
        thread.start() 
    for thread in thread_handle_list: 
        thread.join() 
    log_file_handle.close() 
    del tsf_stack 
    sys.exit(0)

main(len(sys.argv), sys.argv)
