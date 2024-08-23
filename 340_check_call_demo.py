import sys 
import subprocess 

def main(): 
    cc_cmdline = ['cl.exe', 'hello.c']
    try: 
        subprocess.check_call(cc_cmdline)
    except subprocess.CalledProcessError as e: 
        print("cl.exe hello.c has failed")
        print(e)
        sys.exit(-1) 

    hello_cmdline = ['hello.exe']
    try: 
        subprocess.check_call(hello_cmdline)
    except subprocess.CalledProcessError as e: 
        print("hello.exe has failed")
        print(e)
        sys.exit(-1) 

    sys.exit(0)

main() 