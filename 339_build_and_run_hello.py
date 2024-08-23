import sys 
import subprocess 

def main(): 
    cc_cmdline = ['cl.exe', 'hello.c']
    ret = subprocess.call(cc_cmdline)
    print("CC Return:", ret)
    hello_cmdline = ['hello.exe']
    ret = subprocess.call(hello_cmdline)
    sys.exit(0)

main() 