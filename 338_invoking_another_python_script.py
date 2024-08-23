import os 
import sys 

# python3 task.py -i -o dump.txt 

def main(): 
    # Please note that the task_path is not a 
    # standard executable path. Therefore, it must 
    # be an absolute path
    # However, python3 is an executable file in standard 
    # binary paths 
    task_path = "/home/pratik/automation/task.py"
    task_cmdline = ["python3", task_path, 
                    "-i", "-o", "dump.txt"]
    pid = os.fork() 
    if pid == -1: 
        print("Error in creating a new process")
        sys.exit(-1)
    
    if pid == 0: 
        os.execvp("python3", task_cmdline)
    else: 
        os.wait() 

    sys.exit(0)


main() 