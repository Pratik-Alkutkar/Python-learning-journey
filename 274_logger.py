"""
@Author: Pratik Pramod Alkutkar  
@Date: 24/05/2023 
@Goal: To implement a decorator logger which when applied to a decorated function, 
will log every call to that function. Information saved in each log is as follows: 
1) Name of function 
2) Time of call. 
3) All parameters seggregating nonkeyword and keyword params from each other 
    Value and type of each parameter is printed 
4) Return type along with type 
5) If decorated function terminates due to uncaught exception then 
    exception name, error data and traceback will be logged. 
"""

import sys 
import time
import traceback 

def logger(log_file_path):
    
    def true_decorator(logged_function_object): 

        curr_log_file_path = log_file_path
        
        def inner_function(*args, **kwargs): 
            try: 
                # PREPROCESSING STRATEGY -> START
                log_handle = open(curr_log_file_path, "a") 
                print('-' * 80, logged_function_object.__name__, file=log_handle)
                print("Time of call:", time.ctime(time.time()), file=log_handle) 
                print("Nonkeyword arguments:", file=log_handle)
                for i in range(len(args)): 
                    print("args[{}]:{} | type(args[{}]):{}".format(i, args[i], i, type(args[i])), 
                            file=log_handle)
                print("Keyword arguments:", file=log_handle)
                for (arg_name, arg_val) in kwargs.items(): 
                    print("Argument Name:{}, Argument Value:{}, Type of Argument Value:{}".format(
                        arg_name, arg_val, type(arg_val)), file=log_handle)
                # PREPROCESSING STRATEGY -> END 

                # DECORATED FUNCTION OBJECT -> CALL -> START 
                try: 
                    ret = logged_function_object(*args, **kwargs) 
                except: 
                    exc_name, exc_data, exc_tb = sys.exc_info() 
                    print(exc_name, exc_data, sep=':', file=log_handle)
                    traceback.print_tb(exc_tb, file=log_handle)
                    log_handle.close() 
                    raise 
                # DECORATED FUNCTION OBJECT -> CALL -> END 

                # POSTPROCESSING STRATEGY -> START 
                print("ret:", ret, "type(ret):", type(ret), file=log_handle)
                # POSTPROCESSING STRATEGY -> END 
                log_handle.close() 
                # RETURN VALUE OF DECORATED FUNCTION TO CALLER 
                return ret 
            
            except FileNotFoundError: 
                print("Invalid path for log file")
                sys.exit(-1)
            
            except PermissionError: 
                print("Permission denied while creating log file")
                sys.exit(-1)

            except: 
                exc_name, exc_data, _ = sys.exc_info() 
                print(exc_name, exc_data, sep=':') 

        return inner_function 
    
    return true_decorator