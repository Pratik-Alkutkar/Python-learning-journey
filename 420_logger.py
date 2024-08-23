import time, sys, traceback

def logger(decorated_function_object): 

    def replacement_function(*args, **kwargs): 

        try: 
            log_handle = open("log.txt", "a")
            line = "-" * 80 
            print(line, decorated_function_object.__name__, file=log_handle)
            print("Time of call:", time.ctime(time.time()), file=log_handle)
            if len(args) > 0: 
                print("Nonkeyword arguments:", file=log_handle)
                for i in range(len(args)): 
                    print("args[{}]:{}\ttype(args[{}]:{}".format(i, args[i], i, type(args[i])), file=log_handle)
            if len(kwargs) > 0: 
                for (v_name, v_val) in kwargs.items(): 
                    print("{}:{}".format(v_name, v_val), file=log_handle)
            
            try: 
                ret = decorated_function_object(*args, **kwargs)
            except: 
                exc_name, exc_data, exc_tb = sys.exc_info()
                print(exc_name, exc_data, sep=':', file=log_handle)
                traceback.print_tb(exc_tb, file=log_handle)
                log_handle.close()
                sys.exit(-1)

            print("Return Value:{} Type of Return Value:{}".format(ret, type(ret)), file=log_handle)

            return (ret)

        except PermissionError: 
            print("Could not create/open a log file, terminating")
            sys.exit(-1)

    return replacement_function