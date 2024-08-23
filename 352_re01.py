import sys 
import re 

def main():
    s = "SVG"
    pattern = "[b-f]"
    L = re.findall(pattern, s)
    print(L)
    sys.exit(0) 

main()  

