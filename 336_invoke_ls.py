import sys 
import os 

def main(): 
    cmdline_of_ls = ['ls', '-l', '/'] 
    relative_path_name = 'ls' 
    pid = os.fork() 
    if pid == 0: 
        os.execvp(relative_path_name, cmdline_of_ls) 
    else: 
        os.wait() 
    sys.exit(0) 
main()
