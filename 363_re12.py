import sys 
import re 

def main(): 
    s1 = "SVG"
    s2 = "Programming is at the SVG"
    pattern = r'\bSVG'
    ret1 = re.findall(pattern, s1)
    ret2 = re.findall(pattern, s2)
    print("first:", ret1)
    print("second:", ret2)
    sys.exit(0) 

main() 