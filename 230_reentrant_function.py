import sys 
import time 
import _thread 
import random 

def thread_function(thread_id:int)->None: 
    i = 0 
    while i < 5:
        print("thread with id {}".format(thread_id))
        time.sleep(random.randint(1, 3))
        i = i + 1 
    print("thread with id {} exiting...".format(thread_id))

def main(): 
    for i in range(5): 
        _thread.start_new_thread(thread_function, (i, ))

    print("Main thread:created all threas:blocking now")    
    time.sleep(15)
    print("Main thread:all threads terminated:terminating application")

    sys.exit(0)

main() 

"""
Reentrant Function: 
    General Definition: 
        If more than one instance of function is inside the call then the function is re-entrant. 
    Simple Case: 
        Recursion: 

        def fact(n): 
            if n < 0: 
                raise ValueError
            if n == 0: 
                return (1)
            else: 
                return n * fact(n-1)

        rs = fact(5)

        fact(5)
            return 5 * fact(4)
                        return 4 * fact(3)
                                    return 3 * fact(2) 
                                                return  2 * fact(1) 
                                                            return  1 * fact(0)
                                                                    1 * 1 
                                                        2 * 1 
                                            3 * 2 * 1 
                                4 * 3 * 2 * 1 
                    5 * 4 * 3 * 2 * 1 
    Reentrany of kind 1: 
        When a function is re-entrant in one thread, it is known as a reentrancy of kind 1. 

        app code 
        app code 
        app code 
        EVENT -> OS -> suspend app code -> INVOKE EVENT HANDLER 
                                            run event handler 
                                            run event handler 
                                            run event handler 
                                            EVENT (RE-OCCUR-->RECUR) -> OS -> suspend (run event handler) -> INVOKE EVENT HANDLER
                                                                                                            run event handler 
                                                                                                            run event handler 
                                                                                                            run event handler 

    Reentrancy of kind 2: 
        When a single function is SIMULATANEOUSLY EXECUTED BY MORE THAN ONE THREAD OF EXECUTION.                                                                                                       

        Elite level: 
        1) Knowing 2 kind of re-entracies and 2 scenarios that give birth to them 
            theory explain 
        2) to demonstrate all three kind of re-entrancies using code 
        3) What is data concsistency? How consistenacy of shared data is in thread 
            when a function is REENTRANT. 
        4) How to update shared data safely (= without making it inconsistent)
            in each case of re-entrant function.
"""