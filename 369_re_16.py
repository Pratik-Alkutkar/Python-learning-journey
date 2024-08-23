import sys 
import re 

def main(): 
    s = "SVG ceo -> pratik"
    pattern = '\S'
    ret = re.findall(pattern, s)
    print("ret:", ret)
    sys.exit(0) 

main()