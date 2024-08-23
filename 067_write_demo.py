import sys
import os 

def main(): 

    s = "Hello,World"
    sb = s.encode()
    os.write(1, sb)
    sys.exit(0) 

main() 