import os 
import sys 

class ProcessCreationError(Exception): 
    pass 

class CalledProcessError(Exception): 
    pass 

def cpa_call(*cmdline): 
    pid = os.fork() 
    if pid == -1:
        raise ProcessCreationError("Failed to create a new process")
    if pid == 0: 
        os.execv(cmdline) 
        os.execvp(cmdline)
    else: 
        ret = os.wait() 
        return ret  
    
def cpa_check_call(*cmdline): 
    pid = os.fork() 
    if pid == -1:
        raise ProcessCreationError("Failed to create a new process")
    if pid == 0: 
        os.execv(cmdline) 
        os.execvp(cmdline)
    else: 
        ret = os.wait() 
        if ret != 0: 
            raise CalledProcessError("Command {} failed with exit code {}".format(cmdline, ret))
        return ret  