import sys 
import re

def main(): 
    s = "SVG c@^e"
    """
    Syntax: dot --> . 
    a single dot matches with any character
    Match object: starts with c, ends with e and ANY TWO chars in between 
    """
    pattern = "c..e"
    L = re.findall(pattern, s)
    for word in L: 
        print(word)
    sys.exit(0)

main() 